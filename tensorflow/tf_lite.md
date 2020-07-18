## TensorFlow Lite

使用 TensorFlow 训练好的模型，模型太大、运行效率比较低，不能直接在移动端部署，需要通过相应工具进行转换成适合边缘设备的格式. 本节以 android 为例，简单介绍如何在 android 应用中部署转化后的模型.

### 模型转换

- 转换工具有两种：命令行工具和 Python API

- 转换后的原模型为 FlatBuffers 格式。 FlatBuffers 原来主要应用于游戏场景，是谷歌为了高性能场景创建的序列化库，相比 Protocol Buffer 有更高的性能和更小的大小等优势，更适合于边缘设备部署

- 转换方式有两种：Float 格式和 Quantized 格式


```
usage: tflite_convert [-h] --output_file OUTPUT_FILE
                      (--saved_model_dir SAVED_MODEL_DIR | --keras_model_file KERAS_MODEL_FILE)
  --output_file OUTPUT_FILE
                        Full filepath of the output file.
  --saved_model_dir SAVED_MODEL_DIR
                        Full path of the directory containing the SavedModel.
  --keras_model_file KERAS_MODEL_FILE
                        Full filepath of HDF5 file containing tf.Keras model.

# SavedModel
tflite_convert --saved_model_dir=saved/1 --output_file=mnist_savedmodel.tflite
# keras save
tflite_convert --keras_model_file=mnist_cnn.h5 --output_file=mnist_sequential.tflite
```

### Android 部署
https://tf.wiki/zh_hans/deployment/lite.html

- 配置 build.gradle

- 配置 app/build.gradle

- 添加 tflite 文件到 assets 文件夹

- 加载模型

- 运行输入

- 运行输出

- 运行及结果处理

## tf.js

https://tf.wiki/zh_hans/deployment/javascript.html
