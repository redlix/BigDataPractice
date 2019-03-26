#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-18 08:32
@Author  : red
@Site    : 
@File    : docx_util.py
@Software: PyCharm
"""
import docx


def get_content(file_path):
    document = docx.Document(file_path)
    text = ''
    for element in document.paragraphs:
        text += element.text
    print(text)
    return text


if __name__ == '__main__':
    path = '/Users/red/Desktop/temp/study/firstgrade/bigdatapractice/lab1/operation-exper/20183192_明珠/01-计算机的诞生和发展.docx'
    get_content(path)
