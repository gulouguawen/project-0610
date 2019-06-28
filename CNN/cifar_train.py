import tensorflow as tf
import input_data
import cifar_inference
import os
import numpy as np

BATCH_SIZE = 100
REGULARAZTION_RATE = 0.0001
LEARNING_RATE_BASE = 0.0009
LEARNING_RATE_DECAY = 0.99
REGULARAZTION_RATE = 0.0001
TRAINING_STEPS = 10
MOVING_AVERAGE_DECAY = 0.99

MODEL_SAVE_PATH = "models"
MODEL_NAME = "model.ckpt"


def train(images, labels, test_iamges, test_labels):
    x = tf.placeholder("float32", shape=[None, 3072])
    y = tf.placeholder("float32", shape=[None, 10])

    regularization = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

    output_labels = cifar_inference.inference(x, regularization)

    global_step = tf.Variable(0, trainable=False)
    variable_average = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variable_averages_op = variable_average.apply(tf.trainable_variables())
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=output_labels)
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection("losses"))
    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.arg_max(y, 1), tf.arg_max(output_labels, 1)), "float"))

    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,
                                               global_step,
                                               50000 // BATCH_SIZE,
                                               LEARNING_RATE_DECAY)
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name="train")

    saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        loop_time = 50000 // BATCH_SIZE if 50000 % BATCH_SIZE == 0 else 50000 // BATCH_SIZE + 1
        try:
            for i in range(TRAINING_STEPS):
                if coord.should_stop():
                    break
                loss_value = 0.0
                for t in range(loop_time):
                    start = t * BATCH_SIZE % 50000
                    end = min(start + BATCH_SIZE, 50000)
                    _, loss_value, step = sess.run([train_op, loss, global_step],
                                                   feed_dict={x: images[start:end], y: labels[start:end]})
                acc = sess.run(accuracy, feed_dict={x: test_iamges, y: test_labels})
                print("经过 %d 轮训练, 整体损失为： %g， 准确率为：%g." % (i + 1, loss_value, acc))
                if acc > 0.7:
                    saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)
        except tf.errors.OutOfRangeError:
            print("Done training--epoch limit reached.")
        finally:
            coord.request_stop()
    coord.join(threads)


def main(argv=None):
    (images, labels), (
        t_images, t_labels) = input_data.load_data()  # input_data.distorted_inputs("../data/cifar/", 128)
    images = np.reshape(images, (50000, 3072))
    t_images = np.reshape(t_images, (10000, 3072))
    tmp = []
    tmp_t = []
    for i in range(0, 50000):
        data = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.int)
        data[labels[i]] = 1
        tmp.append(data)
        del data
    del labels
    for i in range(0, 10000):
        data = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.int)
        data[t_labels[i]] = 1
        tmp_t.append(data)
        del data
    del t_labels
    train(images, np.array(tmp), t_images, tmp_t)


if __name__ == "__main__":
    tf.app.run()
