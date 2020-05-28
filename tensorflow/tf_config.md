## tf.config：GPU 的使用与分配

### 指定当前程序使用的 GPU

- 通过 tf.config.list_physical_devices ，我们可以获得当前主机上某种特定运算设备类型（如 GPU 或 CPU ）的列表

```
gpus = tf.config.list_physical_devices(device_type='GPU')
cpus = tf.config.list_physical_devices(device_type='CPU')
```

- 通过 tf.config.set_visible_devices ，可以设置当前程序可见的设备范围

```
gpus = tf.config.list_physical_devices(device_type='GPU')
tf.config.set_visible_devices(devices=gpus[0:2], device_type='GPU')
```

- 使用环境变量 CUDA_VISIBLE_DEVICES 也可以控制程序所使用的 GPU。

假设发现四卡的机器上显卡 0,1 使用中，显卡 2,3 空闲，Linux 终端输入:

`export CUDA_VISIBLE_DEVICES=2,3`
或在代码中加入 `os.environ['CUDA_VISIBLE_DEVICES'] = "2,3"`


### 显存使用策略

- 可以通过 `tf.config.experimental.set_memory_growth` 将 GPU 的显存使用策略设置为 “仅在需要时申请显存空间”

```
gpus = tf.config.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(device=gpu, enable=True)
```

- 限制消耗固定大小的显存

```
gpus = tf.config.list_physical_devices(device_type='GPU')
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=1024)])
```
