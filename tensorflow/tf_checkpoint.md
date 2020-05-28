## save, restore and tensorboard

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
