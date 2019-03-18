#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-18 09:03
@Author  : red
@Site    : 
@File    : split_util.py
@Software: PyCharm
"""
import jieba_fast as jieba
import codecs

# 开启并行分词模式，参数为并行进程数
jieba.enable_parallel(4)


def get_stop_word():
    with codecs.open('../stop_words/stop_word_chinese_1.txt', 'r', encoding='utf8') as f1:
        data1 = f1.read()

    with codecs.open('../stop_words/stop_word_chinese_1.txt', 'r', encoding='utf8') as f2:
        data2 = f2.read()
    f_stop_list = (data1 + data2).split('\n')
    return f_stop_list
