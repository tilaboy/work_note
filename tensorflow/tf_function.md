## tf.function ：图执行模式

### @tf.function 修饰符

将模型转换为高效的 TensorFlow 图模型, 就能轻松将模型以图执行模式运行


```
model = CNN()
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

@tf.function
def train_one_step(X, y):
    with tf.GradientTape() as tape:
        y_pred = model(X)
        loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=y, y_pred=y_pred)
        loss = tf.reduce_mean(loss)
        # 注意这里使用了TensorFlow内置的tf.print()。@tf.function不支持Python内置的print方法
        tf.print("loss", loss)
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))

for batch_index in range(num_batches):
    X, y = data_loader.get_batch(batch_size)
    train_one_step(X, y)
```

### tf.function 内在机制

- 在即时执行模式关闭的环境下，函数内的代码依次运行。也就是说，每个 tf. 方法都只是定义了计算节点，而并没有进行任何实质的计算。这与 TensorFlow 1.X 的图执行模式是一致的；

- 使用 AutoGraph 将函数中的 Python 控制流语句转换成 TensorFlow 计算图中的对应节点（比如说 while 和 for 语句转换为 tf.while ， if 语句转换为 tf.cond 等等；

- 基于上面的两步，建立函数内代码的计算图表示（为了保证图的计算顺序，图中还会自动加入一些 tf.control_dependencies 节点）；

- 运行一次这个计算图；

- 基于函数的名字和输入的函数参数的类型生成一个哈希值，并将建立的计算图缓存到一个哈希表中。

在被 @tf.function 修饰的函数之后再次被调用的时候，根据函数名和输入的函数参数的类型计算哈希值，检查哈希表中是否已经有了对应计算图的缓存。如果是，则直接使用已缓存的计算图，否则重新按上述步骤建立计算图。

note:
如果想要直接获得 tf.function 所生成的计算图以进行进一步处理和调试，可以使用被修饰函数的 get_concrete_function 方法。该方法接受的参数与被修饰函数相同。

```
graph = train_one_step.get_concrete_function(X, y)
```

### AutoGraph：将 Python 控制流转换为 TensorFlow 计算图

原函数中的 Python 控制流
`if...else...`
被转换为了
`x = ag__.if_stmt(cond, if_true, if_false, get_state, set_state)`
这种计算图式的写法。

AutoGraph 起到了类似编译器的作用，能够帮助我们通过更加自然的 Python 控制流轻松地构建带有条件 / 循环的计算图，而无需手动使用 TensorFlow 的 API 进行构建。

## tf.TensorArray ：TensorFlow 动态数组

一种支持计算图特性的 TensorFlow 动态数组


其声明的方式为：

arr = tf.TensorArray(dtype, size, dynamic_size=False) ：声明一个大小为 size ，类型为 dtype 的 TensorArray arr 。如果将 dynamic_size 参数设置为 True ，则该数组会自动增长空间。

其读取和写入的方法为：

write(index, value) ：将 value 写入数组的第 index 个位置；

read(index) ：读取数组的第 index 个值；

除此以外，TensorArray 还包括 stack() 、 unstack() 等常用操作

```
@tf.function
def array_write_and_read():
    arr = tf.TensorArray(dtype=tf.float32, size=3)
    arr = arr.write(0, tf.constant(0.0))
    arr = arr.write(1, tf.constant(1.0))
    arr = arr.write(2, tf.constant(2.0))
    arr_0 = arr.read(0)
    arr_1 = arr.read(1)
    arr_2 = arr.read(2)
    return arr_0, arr_1, arr_2

a, b, c = array_write_and_read()
print(a, b, c)
```
