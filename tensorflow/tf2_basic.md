# TF 101

## variables:

`zero_vector = tf.zeros(shape=(2), dtype=tf.int32)`

TensorFlow 的大多数 API 函数会根据输入的值自动推断张量中元素的类型（一般默认为 tf.float32 ）。也可以通过 dtype 参数。

```
A = tf.constant([[1., 2.], [3., 4.]])
print(A.shape)      # 输出(2, 2)，即矩阵的长和宽均为2
print(A.dtype)      # 输出<dtype: 'float32'>
print(A.numpy())    # 输出[[1. 2.]
                    #      [3. 4.]]
```

张量的 numpy() 方法是将张量的值转换为一个 NumPy 数组。

## gradient computation

```
optimizer = tf.keras.optimizers.SGD(learning_rate=5e-4)
X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L = tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
w_grad, b_grad = tape.gradient(L, [w, b])        # 计算L(w, b)关于w, b的偏导数
optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
```

with tf.GradientTape上下文环境中计算步骤都会被自动记录。比如在上面的示例中，计算步骤 y = tf.square(x) 即被自动记录。离开上下文环境后，记录将停止，但记录器 tape 依然可用，因此可以通过 y_grad = tape.gradient(y, x) 求张量 y 对变量 x 的导数。


## Model
### 模型的构建： tf.keras.Model 和 tf.keras.layers

Define your own model, and call with `y_pred = model(X)`

1. linear model

```
class MyLinear(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense = tf.keras.layers.Dense(
            units=1,
            activation=None,
            kernel_initializer=tf.zeros_initializer(),
            bias_initializer=tf.zeros_initializer()
        )

    def call(self, input):
        output = self.dense(input)
        return output
```

2. MLP model

```
class MLP(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.flatten = tf.keras.layers.Flatten()    # Flatten层将除第一维（batch_size）以外的维度展平
        self.dense1 = tf.keras.layers.Dense(units=100, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)

    def call(self, inputs):         # [batch_size, 28, 28, 1]
        x = self.flatten(inputs)    # [batch_size, 784]
        x = self.dense1(x)          # [batch_size, 100]
        x = self.dense2(x)          # [batch_size, 10]
        output = tf.nn.softmax(x)
        return output
```

### 模型的损失函数： tf.keras.losses

tf.keras.losses.categorical_crossentropy V.S.
tf.keras.losses.sparse_categorical_crossentropy:
with sparse, 真实的标签值 y_true 可以直接传入 int 类型的标签类别




### 模型的优化器： tf.keras.optimizer

### 模型的评估： tf.keras.metrics

tf.keras.metrics.SparseCategoricalAccuracy 评估器:

```
sparse_categorical_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
num_batches = int(data_loader.num_test_data // batch_size)
for batch_index in range(num_batches):
    start_index, end_index = batch_index * batch_size, (batch_index + 1) * batch_size
    y_pred = model.predict(data_loader.test_data[start_index: end_index])
    sparse_categorical_accuracy.update_state(y_true=data_loader.test_label[start_index: end_index], y_pred=y_pred)
print("test accuracy: %f" % sparse_categorical_accuracy.result())
```

### CNN

使用 Keras 中预定义的经典卷积神经网络结构:

tf.keras.applications 中有一些预定义好的经典卷积神经网络结构，如 VGG16 、 VGG19 、 ResNet 、 MobileNet 等。我们可以直接调用这些经典的卷积神经网络结构（甚至载入预训练的参数），而无需手动定义网络结构。

`model = tf.keras.applications.MobileNetV2()`

每个网络结构具有自己特定的详细参数设置，一些共通的常用参数如下：

input_shape ：输入张量的形状（不含第一维的 Batch），大多默认为 224 × 224 × 3 。一般而言，模型对输入张量的大小有下限，长和宽至少为 32 × 32 或 75 × 75 ；

include_top ：在网络的最后是否包含全连接层，默认为 True ；

weights ：预训练权值，默认为 'imagenet' ，即为当前模型载入在 ImageNet 数据集上预训练的权值。如需随机初始化变量可设为 None ；

classes ：分类数，默认为 1000。修改该参数需要 include_top 参数为 True 且 weights 参数为 None 。

```
dataset = tfds.load("tf_flowers", split=tfds.Split.TRAIN, as_supervised=True)
dataset = dataset.map(lambda img, label: (tf.image.resize(img, (224, 224)) / 255.0, label)).shuffle(1024).batch(batch_size)
model = tf.keras.applications.MobileNetV2(weights=None, classes=5)
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
for e in range(num_epoch):
    for images, labels in dataset:
        with tf.GradientTape() as tape:
            labels_pred = model(images, training=True)
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=labels, y_pred=labels_pred)
            loss = tf.reduce_mean(loss)
            print("loss %f" % loss.numpy())
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.trainable_variables))
    print(labels_pred)
```

## Keras pipeline:

```
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(100, activation=tf.nn.relu),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Softmax()
])
```

```
inputs = tf.keras.Input(shape=(28, 28, 1))
x = tf.keras.layers.Flatten()(inputs)
x = tf.keras.layers.Dense(units=100, activation=tf.nn.relu)(x)
x = tf.keras.layers.Dense(units=10)(x)
outputs = tf.keras.layers.Softmax()(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

Model's functions:

```
model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.sparse_categorical_crossentropy,
        metrics=[tf.keras.metrics.sparse_categorical_accuracy]
    )

model.fit(data_loader.train_data, data_loader.train_label, epochs=num_epochs, batch_size=batch_size)

```

## self defined layers:

```
class LinearLayer(tf.keras.layers.Layer):
    def __init__(self, units):
        super().__init__()
        self.units = units

    def build(self, input_shape):     # 这里 input_shape 是第一次运行call()时参数inputs的形状
        self.w = self.add_variable(name='w',
            shape=[input_shape[-1], self.units], initializer=tf.zeros_initializer())
        self.b = self.add_variable(name='b',
            shape=[self.units], initializer=tf.zeros_initializer())

    def call(self, inputs):
        y_pred = tf.matmul(inputs, self.w) + self.b
        return y_pred


class LinearModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.layer = LinearLayer(units=1)

    def call(self, inputs):
        output = self.layer(inputs)
        return output
```

## self defined loss function:

重写 call 方法即可
```
class MeanSquaredError(tf.keras.losses.Loss):
    def call(self, y_true, y_pred):
        return tf.reduce_mean(tf.square(y_pred - y_true))
```

## self defined metrics

并重写 __init__ 、 update_state 和 result 三个方法

```
class SparseCategoricalAccuracy(tf.keras.metrics.Metric):
    def __init__(self):
        super().__init__()
        self.total = self.add_weight(name='total', dtype=tf.int32, initializer=tf.zeros_initializer())
        self.count = self.add_weight(name='count', dtype=tf.int32, initializer=tf.zeros_initializer())

    def update_state(self, y_true, y_pred, sample_weight=None):
        values = tf.cast(tf.equal(y_true, tf.argmax(y_pred, axis=-1, output_type=tf.int32)), tf.int32)
        self.total.assign_add(tf.shape(y_true)[0])
        self.count.assign_add(tf.reduce_sum(values))

    def result(self):
        return self.count / self.total
```

## save and restore

- Checkpoint 只保存模型的参数，不保存模型的计算过程

- tf.train.Checkpoint() 接受的初始化参数是一个 `**kwargs` 具体而言，是一系列的键值对，键名可以随意取，值为需要保存的对象。例如，如果我们希望保存一个继承 tf.keras.Model 的模型实例 model 和一个继承 tf.train.Optimizer 的优化器 optimizer

```
checkpoint = tf.train.Checkpoint(myAwesomeModel=model, myAwesomeOptimizer=optimizer)
checkpoint.save(save_path_with_prefix)
```

- 在 save 目录下: checkpoint 、 model.ckpt-1.index 、 model.ckpt-1.data-00000-of-00001 的三个文件，这些文件就记录了变量信息。

- checkpoint.save() 方法可以运行多次，每运行一次都会得到一个.index 文件和.data 文件，序号依次累加

```
model_to_be_restored = MyModel()
# 键名保持为“myAwesomeModel”
checkpoint = tf.train.Checkpoint(myAwesomeModel=model_to_be_restored)
checkpoint.restore(save_path_with_prefix_and_index)
```

- CheckpointManager can be used to 保留最后的几个 Checkpoint, 并使用 batch 的编号作为 Checkpoint 的文件编号

```
checkpoint = tf.train.Checkpoint(myAwesomeModel=model)
manager = tf.train.CheckpointManager(checkpoint, directory='./save', max_to_keep=3)
....
if batch_index % 100 == 0:
    path = manager.save(checkpoint_number=batch_index)
    print("model saved to %s" % path)
```

## TensorBoard

- 每运行一次 tf.summary.scalar() ，记录器就会向记录文件中写入一条记录

```
summary_writer = tf.summary.create_file_writer('./tensorboard')
with summary_writer.as_default():
    tf.summary.scalar("loss", loss, step=batch_index)
    tf.summary.scalar("MyScalar", my_scalar, step=batch_index)
```

- trace model training processs:

TensorBoard 中选择 “Profile”，以时间轴的方式查看各操作的耗时情况

```
tf.summary.trace_on(profiler=True)
with summary_writer.as_default():
    tf.summary.trace_export(name="model_trace", step=0, profiler_outdir=log_dir)
```


## tf.data

- tf.data 的核心是 tf.data.Dataset 类，提供了对数据集的高层封装。

- tf.data.Dataset 由一系列的可迭代访问的元素（element）组成，每个元素包含一个或多个张量。比如说，对于一个由图像组成的数据集，每个元素可以是一个形状为 长×宽×通道数 的图片张量，也可以是由图片张量和图片标签张量组成的元组（Tuple）

```
X = tf.constant([2013, 2014, 2015, 2016, 2017])
Y = tf.constant([12000, 14000, 15000, 16500, 17500])

# 也可以使用NumPy数组，效果相同
# X = np.array([2013, 2014, 2015, 2016, 2017])
# Y = np.array([12000, 14000, 15000, 16500, 17500])

# 当提供多个张量作为输入时，张量的第 0 维大小必须相同
dataset = tf.data.Dataset.from_tensor_slices((X, Y))
```

- 对于特别巨大而无法完整载入内存的数据集，我们可以先将数据集处理为 TFRecord 格式，然后使用 tf.data.TFRocrdDataset() 进行载入

- tf.data.Dataset 类为我们提供了多种数据集预处理方法:
  - Dataset.map(f) ：对数据集中的每个元素应用函数 f ，得到一个新的数据集
  - Dataset.shuffle(buffer_size) ：将数据集打乱(设定一个固定大小的缓冲区（Buffer），取出前 buffer_size 个元素放入，并从缓冲区中随机采样，采样后的数据用后续数据替换)
  - Dataset.batch(batch_size) ：将数据集分成批次，即对每 batch_size 个元素，使用 tf.stack() 在第 0 维合并，成为一个元素
  - Dataset.repeat(): 重复数据集的元素
  - Dataset.reduce(): 与 Map 相对的聚合操作
  - Dataset.take(): 截取数据集中的前若干个元素


- buffer_size in shuffle:
  - 设定一个固定大小为 buffer_size 的缓冲区（Buffer）；
  - 初始化时，取出数据集中的前 buffer_size 个元素放入缓冲区；
  - 每次需要从数据集中取元素时，即从缓冲区中随机采样一个元素并取出，然后从后续的元素中取出一个放回到之前被取出的位置，以维持缓冲区的大小。
  - 当 buffer_size 设置为 1 时，其实等价于没有进行任何打散
  - 当数据集的标签顺序分布极为不均匀（例如二元分类时数据集前 N 个的标签为 0，后 N 个的标签为 1）时, 需要设置较大的缓冲区


- tf.data 并行化策略

  - Dataset.prefetch(): 预取出若干个元素, 使得在 GPU 训练的同时 CPU 可以准备数据
```
mnist_dataset = mnist_dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
```

  - Dataset.map():
```
mnist_dataset = mnist_dataset.map(map_func=rot90, num_parallel_calls=nr_cpus)
```
