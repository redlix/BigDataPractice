#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-18 09:16
@Author  : red
@Site    : 
@File    : main.py
@Software: PyCharm
"""
from utils import docx_util, file_util
from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i, item in enumerate(seq):
        tally[item].append(i)
    return ((key, locs) for key, locs in tally.items()
            if len(locs) > 1)


if __name__ == '__main__':
    file_list = file_util.get_file_list('/Users/red/Desktop/temp/study/firstgrade/bigdatapractice/lab1/operation-exper',
                                        [])

    content_list = []
    for file_path in file_list:
        content_list.append(docx_util.get_content(file_path))
    print("------result------")
    for dup in sorted(list_duplicates(content_list)):
        for itm in dup[1]:
            print(file_list[itm])
        print('------------')
