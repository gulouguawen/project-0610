
import tensorflow as tf


def get_weight(shape, std=0.1, regularization=None):
    weights = tf.get_variable("weights", shape, initializer=tf.truncated_normal_initializer(stddev=std))
    if regularization:
        tf.add_to_collection("losses", regularization(weights))
    return weights


def get_biases(shape):
    biases = tf.get_variable("biases",
                             shape,
                             initializer=tf.constant_initializer(0))
    return biases


def convolution(x, w, strides):

    return tf.nn.conv2d(x, w, strides=strides, padding="SAME")


def pooling(input, ksize, strides):

    return tf.nn.max_pool(input, ksize, strides=strides, padding="VALID")


def avg_pooling(input, ksize, strides):

    return tf.nn.avg_pool(input, ksize, strides=strides, padding='VALID')


def full_connection_nn(input_tensor, input_size, output_size, regularization=None):

    weights = get_weight([input_size, output_size], 0.1, regularization)
    biases = get_biases(shape=[output_size])
    result = tf.nn.bias_add(tf.matmul(input_tensor, weights), biases)
    return result


def inference(input_tensor, regularization):

    input_tensor = tf.reshape(input_tensor, shape=[-1, 32, 32, 3])

    with tf.variable_scope("conv1"):
        w_conv1 = get_weight([5, 5, 3, 32], 0.0001, regularization)
        b_conv1 = get_biases([32])
        conv1 = tf.nn.selu(convolution(input_tensor, w_conv1, strides=[1, 1, 1, 1]) + b_conv1)
        max_pool = pooling(conv1, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1])

    with tf.variable_scope("conv2"):
        w_conv2 = get_weight(shape=[5, 5, 32, 32], std=0.01, regularization=regularization)
        b_conv2 = get_biases(shape=[32])
        conv2 = tf.nn.selu(convolution(max_pool, w_conv2, strides=[1, 1, 1, 1]) + b_conv2)
        max_pool2 = pooling(conv2, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1])

    with tf.variable_scope("conv3"):
        w_conv3 = get_weight([3, 3, 32, 64], 0.01, regularization=regularization)
        b_conv3 = get_biases(shape=[64])
        conv3 = tf.nn.selu(convolution(max_pool2, w_conv3, [1, 1, 1, 1]) + b_conv3)
        max_pool3 = pooling(conv3, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1])

    with tf.variable_scope("fc1"):
        max_pool3 = tf.reshape(max_pool3, [-1, 576])
        fc1 = full_connection_nn(max_pool3, 576, 10,
                                 regularization=regularization)
        fc1 = tf.nn.relu(fc1)
        return fc1
