#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-18 08:25
@Author  : red
@Site    : 
@File    : file_util.py
@Software: PyCharm
"""
import os


def get_file_list(dir_path, file_list):
    if os.path.isfile(dir_path) and str.split(str.split(dir_path, '/')[-1], '.')[-1] == 'docx':
        file_list.append(dir_path)
    elif os.path.isdir(dir_path):
        for s in os.listdir(dir_path):
            new_dir = os.path.join(dir_path, s)
            get_file_list(new_dir, file_list)
    return file_list


if __name__ == '__main__':
    print(get_file_list('/Users/red/Desktop/temp/study/firstgrade/bigdatapractice/lab1/operation-exper', []))
