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
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
```

  - Dataset.map():
```
dataset = dataset.map(map_func=rot90, num_parallel_calls=nr_cpus)
# or
dataset = dataset.map(map_func=rot90, num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

- tf.data.Dataset 是一个 Python 的可迭代对象，因此可以使用 For 循环迭代获取数据, 也可以使用 iter() 显式创建一个 Python 迭代器并使用 next() 获取下一个元素

```
dataset = tf.data.Dataset.from_tensor_slices((A, B, C, ...))
for a, b, c, ... in dataset:
    xxxx

it = iter(dataset)
a_0, b_0, c_0, ... = next(it)
a_1, b_1, c_1, ... = next(it)
```

Keras 支持使用 tf.data.Dataset 直接作为输入。当调用 tf.keras.Model 的 fit() 和 evaluate() 方法时，可以将参数中的输入数据 x 指定为一个元素格式为 (输入数据, 标签数据) 的 Dataset ，并忽略掉参数中的标签数据 y
```
model.fit(x=train_data, y=train_label, epochs=num_epochs, batch_size=batch_size)
# =>
model.fit(train_data, epochs=num_epochs)
```

## TFRecord ：TensorFlow 数据集存储格式

### 数据集整理为 TFRecord
  - 读取该数据元素到内存；
  - 将该元素转换为 tf.train.Example 对象（每一个 tf.train.Example 由若干个 tf.train.Feature 的字典组成，因此需要先建立 Feature 的字典）；
  - 将该 tf.train.Example 对象序列化为字符串，并通过一个预先定义的 tf.io.TFRecordWriter 写入 TFRecord 文件

tf.train.Feature形式如下:
```
[
    {   # example 1 (tf.train.Example)
        'feature_1': tf.train.Feature,
        ...
        'feature_k': tf.train.Feature
    },
    ...
    {   # example N (tf.train.Example)
        'feature_1': tf.train.Feature,
        ...
        'feature_k': tf.train.Feature
    }
]
```

```
with tf.io.TFRecordWriter(tfrecord_file) as writer:
    for filename, label in zip(train_filenames, train_labels):
        image = open(filename, 'rb').read()
        feature = {
            'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),  
            'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
        }
        example = tf.train.Example(features=tf.train.Features(feature=feature))
        writer.write(example.SerializeToString())

```

### tf.train.Feature 支持三种数据格式：

- tf.train.BytesList ：字符串或原始 Byte 文件（如图片），通过 bytes_list 参数传入一个由字符串数组初始化的 tf.train.BytesList 对象；

- tf.train.FloatList ：浮点数，通过 float_list 参数传入一个由浮点数数组初始化的 tf.train.FloatList 对象；

- tf.train.Int64List ：整数，通过 int64_list 参数传入一个由整数数组初始化的 tf.train.Int64List 对象。




### 读取 TFRecord 数据
  - 通过 tf.data.TFRecordDataset 读入原始的 TFRecord 文件（此时文件中的 tf.train.Example 对象尚未被反序列化），获得一个 tf.data.Dataset 数据集对象
  - 通过 Dataset.map 方法，对该数据集对象中的每一个序列化的 tf.train.Example 字符串执行 tf.io.parse_single_example 函数，从而实现反序列化


```
raw_dataset = tf.data.TFRecordDataset(tfrecord_file)    # 读取 TFRecord 文件

feature_description = { # 定义Feature结构，告诉解码器每个Feature的类型是什么
    'image': tf.io.FixedLenFeature([], tf.string),
    'label': tf.io.FixedLenFeature([], tf.int64),
}

def _parse_example(example_string): # 将 TFRecord 文件中的每一个序列化的 tf.train.Example 解码
    feature_dict = tf.io.parse_single_example(example_string, feature_description)
    feature_dict['image'] = tf.io.decode_jpeg(feature_dict['image'])    # 解码JPEG图片
    return feature_dict['image'], feature_dict['label']

dataset = raw_dataset.map(_parse_example)
```

feature_description 类似于一个数据集的 “描述文件”，通过一个由键值对组成的字典，告知 tf.io.parse_single_example 函数每个 tf.train.Example 数据项有哪些 Feature，以及这些 Feature 的类型、形状等属性。 tf.io.FixedLenFeature 的三个输入参数 shape 、 dtype 和 default_value （可省略）为每个 Feature 的形状、类型和默认值。这里我们的数据项都是单个的数值或者字符串，所以 shape 为空数组
