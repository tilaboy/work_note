## save and load:

### TensorFlow SavedModel: complete model information

- 与 Checkpoint 不同，SavedModel 包含了一个 TensorFlow 程序的完整信息： 不仅包含参数的权值，还包含计算的流程, 即计算图

```
tf.saved_model.save(model, "保存的目标文件夹名称")
model = tf.saved_model.load("保存的目标文件夹名称")
y_pred = model(data_loader.test_data)
```

- 当模型导出为 SavedModel 文件时，无需建立模型的源代码即可再次运行模型，这使得 SavedModel 尤其适用于模型的分享和部署。TensorFlow Serving（服务器端部署模型）、TensorFlow Lite（移动端部署模型）以及 TensorFlow.js 都会用到这一格式。

- SavedModel 基于计算图，所以对于使用继承 tf.keras.Model 类建立的 Keras 模型，其需要导出到 SavedModel 格式的方法（比如 call ）都需要使用 @tf.function 修饰

```
class MLP(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.flatten = tf.keras.layers.Flatten()
        self.dense1 = tf.keras.layers.Dense(units=100, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)

    @tf.function
    def call(self, inputs):         # [batch_size, 28, 28, 1]
        x = self.flatten(inputs)    # [batch_size, 784]
        x = self.dense1(x)          # [batch_size, 100]
        x = self.dense2(x)          # [batch_size, 10]
        output = tf.nn.softmax(x)
        return output

model = MLP()

y_pred = model.call(data_loader.test_data)
```

### Keras Sequential save 方法


- HDF5 格式， keras 训练后的模型，其中已经包含了训练后的模型结构和权重等信息
```
model.save('mnist_cnn.h5')
keras.models.load_model("mnist_cnn.h5")
```
