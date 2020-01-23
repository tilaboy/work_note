## bert models:

  bert as service: https://github.com/hanxiao/bert-as-service

### smaller bert models:

  albert: https://github.com/brightmart/albert_zh



## tf estimate/dataset

### dataset
https://developers.googleblog.com/2017/09/introducing-tensorflow-datasets.html

The return value must be a two-element tuple organized as follows: :

The first element must be a dict in which each input feature is a key, and then a list of values for the training batch.
The second element is a list of labels for the training batch.

```
def input_fn():
    ...<code>...
    return ({ 'SepalLength':[values], ..<etc>.., 'PetalWidth':[values] },
            [IrisFlowerType])
```

The tf.data API introduces two new abstractions

https://developers.googleblog.com/2017/11/introducing-tensorflow-feature-columns.html

### feature columns:
  - tf.numeric_column()

```
tf.feature_column.numeric_column(key="SepalLength",dtype=tf.float64)
tf.feature_column.numeric_column(key="MyMatrix",shape=[10,5])
```

  - Bucketized Column

The categorization splits a single input number into a four-element vector. Therefore, the model now can learn four individual weights rather than just one. Four weights creates a richer model than one. More importantly, bucketizing enables the model to clearly distinguish between different year categories since only one of the elements is set (1) and the other three elements are cleared 0. So, bucketing provides the model with additional important information that it can use to learn.

#### A numeric column for the raw input.
numeric_feature_column = tf.feature_column.numeric_column("Year")

#### Bucketize the numeric column on the years 1960, 1980, and 2000
bucketized_feature_column = tf.feature_column.bucketized_column(
    source_column = numeric_feature_column,
    boundaries = [1960, 1980, 2000])

  - Categorical identity columns
```
  identity_feature_column = tf.feature_column.categorical_column_with_identity(
      key='feature_name_from_input_fn',
      num_buckets=4) # Values [0, 4)
```

  - Categorical vocabulary column
    - from list
```
vocabulary_feature_column =
    tf.feature_column.categorical_column_with_vocabulary_list(
        key="feature_name_from_input_fn",
        vocabulary_list=["kitchenware", "electronics", "sports"])
```

  - from file

```
vocabulary_feature_column =
    tf.feature_column.categorical_column_with_vocabulary_file(
        key="feature_name_from_input_fn",
        vocabulary_file="product_class.txt",
        vocabulary_size=3)
```
- hash buckets: means different categories might end up in the same hash value, but result normally fine

```
tf.feature_column.categorical_column_with_hash_bucket(
  key = "feature_name_from_input_fn",
  hash_buckets_size = 100) # The number of categories
```

- crossed_column: mutliple features combined, e.g. latitude and longitude

- indicator column
`indicator_column = tf.feature_column.indicator_column(categorical_column)`


- embedding column  
```
embedding_column = tf.feature_column.embedding_column(
  categorical_column=categorical_column,
  dimension=dimension_of_embedding_vector)
```

## Text classification example

http://ruder.io/text-classification-tensorflow-estimators/

```
def parser(x, length, y):
    features = {"x": x, "len": length}
    return features, y

def train_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((x_train, x_len_train, y_train))
    dataset = dataset.shuffle(buffer_size=len(x_train_variable))
    dataset = dataset.batch(100)
    dataset = dataset.map(parser)
    dataset = dataset.repeat()
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()

def eval_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((x_test, x_len_test, y_test))
    dataset = dataset.batch(100)
    dataset = dataset.map(parser)
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()

def train_and_evaluate(classifier):
    classifier.train(input_fn=train_input_fn, steps=25000)
    eval_results = classifier.evaluate(input_fn=eval_input_fn)
    predictions = np.array([p['logistic'][0] for p in classifier.predict(input_fn=eval_input_fn)])
    tf.reset_default_graph()
    # Add a PR summary in addition to the summaries that the classifier writes
    pr = summary_lib.pr_curve('precision_recall', predictions=predictions, labels=y_test.astype(bool), num_thresholds=21)
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(os.path.join(classifier.model_dir, 'eval'), sess.graph)
        writer.add_summary(sess.run(pr), global_step=0)
        writer.close()
train_and_evaluate(classifier)
```

pretrained embeddings
```
params = {'embedding_initializer': tf.random_uniform_initializer(-1.0, 1.0)}

def my_initializer(shape=None, dtype=tf.float32, partition_info=None):
    assert dtype is tf.float32
    return embedding_matrix

params = {'embedding_initializer': my_initializer}

cnn_pretrained_classifier = tf.estimator.Estimator(
    model_fn=cnn_model_fn,
    model_dir=os.path.join(model_dir, 'cnn_pretrained'),
    params=params)

train_and_evaluate(cnn_pretrained_classifier)
```

CNN model:
```
head = tf.contrib.estimator.binary_classification_head()

def cnn_model_fn(features, labels, mode, params):    
    input_layer = tf.contrib.layers.embed_sequence(
        features['x'], vocab_size, embedding_size,
        initializer=params['embedding_initializer'])

    training = mode == tf.estimator.ModeKeys.TRAIN
    dropout_emb = tf.layers.dropout(inputs=input_layer,
                                    rate=0.2,
                                    training=training)

    conv = tf.layers.conv1d(
        inputs=dropout_emb,
        filters=32,
        kernel_size=3,
        padding="same",
        activation=tf.nn.relu)

    # Global Max Pooling
    pool = tf.reduce_max(input_tensor=conv, axis=1)

    hidden = tf.layers.dense(inputs=pool, units=250, activation=tf.nn.relu)

    dropout_hidden = tf.layers.dropout(inputs=hidden,
                                       rate=0.2,
                                       training=training)

    logits = tf.layers.dense(inputs=dropout_hidden, units=1)

    # This will be None when predicting
    if labels is not None:
        labels = tf.reshape(labels, [-1, 1])


    optimizer = tf.train.AdamOptimizer()

    def _train_op_fn(loss):
        return optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())

    return head.create_estimator_spec(
        features=features,
        labels=labels,
        mode=mode,
        logits=logits,
        train_op_fn=_train_op_fn)
```

lstm model:
```
head = tf.contrib.estimator.binary_classification_head()

def lstm_model_fn(features, labels, mode):    
    # [batch_size x sentence_size x embedding_size]
    inputs = tf.contrib.layers.embed_sequence(
        features['x'], vocab_size, embedding_size,
        initializer=tf.random_uniform_initializer(-1.0, 1.0))

    # create an LSTM cell of size 100
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(100)

    # create the complete LSTM
    _, final_states = tf.nn.dynamic_rnn(
        lstm_cell, inputs, sequence_length=features['len'], dtype=tf.float32)

    # get the final hidden states of dimensionality [batch_size x sentence_size]
    outputs = final_states.h

    logits = tf.layers.dense(inputs=outputs, units=1)

    # This will be None when predicting
    if labels is not None:
        labels = tf.reshape(labels, [-1, 1])

    optimizer = tf.train.AdamOptimizer()

    def _train_op_fn(loss):
        return optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())

    return head.create_estimator_spec(
        features=features,
        labels=labels,
        mode=mode,
        logits=logits,
        train_op_fn=_train_op_fn)
```
