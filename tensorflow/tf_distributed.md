## TensorFlow 分布式训练

### 单机多卡训练： MirroredStrategy

`strategy = tf.distribute.MirroredStrategy()`

MirroredStrategy 的步骤如下：

- 训练开始前，该策略在所有 N 个计算设备上均各复制一份完整的模型；

- 每次训练传入一个批次的数据时，将数据分成 N 份，分别传入 N 个计算设备（即数据并行）；

- N 个计算设备使用本地变量（镜像变量）分别计算自己所获得的部分数据的梯度；

- 使用分布式计算的 All-reduce 操作，在计算设备间高效交换梯度数据并进行求和，使得最终每个设备都有了所有设备的梯度之和；

- 使用梯度求和的结果更新本地变量（镜像变量）；

- 当所有设备均更新本地变量后，进行下一轮训练（即该并行策略是同步的）。

- 默认情况下，TensorFlow 中的 MirroredStrategy 策略使用 NVIDIA NCCL 进行 All-reduce 操作。

### 多机训练： MultiWorkerMirroredStrategy

```
os.environ['TF_CONFIG'] = json.dumps({
    'cluster': {
        'worker': ["localhost:20000", "localhost:20001"]
    },
    'task': {'type': 'worker', 'index': 0}
})
```

### TPU

```
tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)
strategy = tf.distribute.experimental.TPUStrategy(tpu)
```
