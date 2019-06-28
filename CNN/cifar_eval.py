#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Project：project-0610
# @Author：shiyao
# @Email：13207690135@163.com
# @Time：2019-06-21 09:27:19
# @IDE：PyCharm
# @Project Name：project-0610
# @File Name：cifar_eval.py

import tensorflow as tf
import cifar_inference
import cifar_train
import input_data
import numpy as np

IS_MODEL_INIT = False
SESS = None


def evaluate(images):
    with tf.Graph().as_default() as g:
        x = tf.placeholder("float32", shape=[None, 3072], name="x-input")
        validate_feed = {x: images}
        regularization = tf.contrib.layers.l2_regularizer(cifar_train.REGULARAZTION_RATE)
        output_labels = tf.nn.softmax(cifar_inference.inference(x, regularization))

        variable_average = tf.train.ExponentialMovingAverage(cifar_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_average.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)
        global SESS
        global IS_MODEL_INIT
        if not IS_MODEL_INIT:
            SESS = tf.Session()
            ckpt = tf.train.get_checkpoint_state(cifar_train.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(SESS, ckpt.model_checkpoint_path)
            IS_MODEL_INIT = True
        try:
            predicted = SESS.run(tf.argmax(output_labels, 1), feed_dict=validate_feed)
            return predicted
        finally:
            SESS.close()
