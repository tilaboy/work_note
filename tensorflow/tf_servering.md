## TensorFlow Serving

### TensorFlow Serving installation:

可以使用 apt-get 或 Docker 安装。在生产环境中，推荐 使用 Docker 部署 TensorFlow Serving

#### SavedModel 格式的模型:

```
tensorflow_model_server \
    --rest_api_port=端口号（如8501） \
    --model_name=模型名 \
    --model_base_path="SavedModel格式模型的文件夹绝对地址（不含版本号）"
```

#### Keras Sequential 模式模型:

由于 Sequential 模式的输入和输出都很固定，因此这种类型的模型很容易部署，无需其他额外操作

```
tensorflow_model_server \
    --rest_api_port=8501 \
    --model_name=MLP \
    --model_base_path="/home/.../.../saved"  # 文件夹绝对地址根据自身情况填写，无需加入版本号
```

#### 自定义 Keras 模型:

- 需要导出到 SavedModel 格式的方法（比如 call ）

- 不仅需要使用 @tf.function 修饰，还要在修饰时指定 input_signature 参数，以显式说明输入的形状

```
class MLP(tf.keras.Model):
    ...
    @tf.function(input_signature=[tf.TensorSpec([None, 28, 28, 1], tf.float32)])
    def call(self, inputs):
```

- 在将模型使用 tf.saved_model.save 导出时，需要通过 signature 参数提供待导出的函数的签名（Signature）

```
tf.saved_model.save(model, "saved_with_signature/1", signatures={"call": model.call})
```

由于自定义的模型类里可能有多个方法都需要导出，因此，需要告诉 TensorFlow Serving 每个方法在被客户端调用时分别叫做什么名字。例如，如果我们希望客户端在调用模型时使用 call 这一签名来调用 model.call 方法时，我们可以在导出时传入 signature 参数，以 dict 的键值对形式告知导出的方法对应的签名

- after this, we can deploy them as normal:

```
tensorflow_model_server \
    --rest_api_port=8501 \
    --model_name=MLP \
    --model_base_path="/home/.../.../saved_with_signature"
```

### 客户端调用

支持以 gRPC 和 RESTful API 调用以 TensorFlow Serving 部署的模型

#### RESTful API

RESTful API 以标准的 HTTP POST 方法进行交互，请求和回复均为 JSON 对象

```
{
    "signature_name": "需要调用的函数签名（Sequential模式不需要）",
    "instances": 输入数据
}
```

回复为：

```
{
    "predictions": 返回值
}
```

#### examples:

```
data = json.dumps({
    "instances": data_loader.test_data[0:3].tolist()
    })
headers = {"content-type": "application/json"}
json_response = requests.post(
    'http://localhost:8501/v1/models/MLP:predict',
    data=data, headers=headers)
```

自定义的 Keras 模型，在发送的数据中加入 signature_name 键值即可，即将上面代码的 data 建立过程改为

```
data = json.dumps({
    "signature_name": "call",
    "instances": data_loader.test_data[0:10].tolist()
    })
```
