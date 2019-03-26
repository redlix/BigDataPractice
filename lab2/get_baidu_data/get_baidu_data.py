#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-25 09:00
@Author  : red
@Site    : 
@File    : get_baidu_data.py
@Software: PyCharm
"""
import requests
import json
import time
from utils import csv_util


def get_json():
	r = requests.get('https://jiaotong.baidu.com/trafficindex/city/list')
	return r.text


def analysis_json():
	response = get_json()
	lst = json.loads(response)
	if lst['status'] == 0:
		return lst['data']['list']
	else:
		return False


def integration():
	heads = ['time', 'citycode', 'cityname', 'index', 'last_index', 'index_level', 'speed', 'city_coords',
			 'provincecode', 'provincename', 'weekRate']
	lst = analysis_json()
	result = []
	if lst:
		for element in lst:
			tmp = []
			for h in heads:
				tmp.append(element.get(h))
			result.append(tmp)
		return heads, result
	else:
		print('get response error!')
		pass


if __name__ == '__main__':
	i = 0
	while True:
		print("[{}]-start get {} data".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), i))
		heads, result = integration()
		csv_util.write_heads_csv('../resource/baidu_map' + str(i) + '.csv', heads, result, '~')
		print("[{}]-save {} data finally!".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), i))
		time.sleep(60 * 5)
		i += 1
