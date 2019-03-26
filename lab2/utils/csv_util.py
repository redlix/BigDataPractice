#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-25 08:55
@Author  : red
@Site    : 
@File    : csv_util.py
@Software: PyCharm
"""
import csv


def write_heads_csv(file_path, heads, data, delimiter):
	with open(file_path, 'w', newline='', encoding='utf-8') as w:
		writer = csv.writer(w, delimiter=delimiter)

		# 先写入columns_name
		writer.writerow(heads)
		# 写入多行用writerows
		writer.writerows(data)


def write_csv(file_path, data, delimiter):
	with open(file_path, 'w', newline='', encoding='utf-8') as w:
		writer = csv.writer(w, delimiter=delimiter)
		# 写入多行用writerows
		writer.writerows(data)


def append_heads_csv(file_path, data, delimiter):
	with open(file_path, 'a+', newline='', encoding='utf-8') as w:
		writer = csv.writer(w, delimiter=delimiter)

		# 写入多行用writerows
		writer.writerows(data)
