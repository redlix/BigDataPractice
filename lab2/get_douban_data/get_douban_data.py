#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-26 10:24
@Author  : red
@Site    : 
@File    : get_douban_data.py
@Software: PyCharm
"""
from utils import csv_util
import requests
import json

file_path = '/home/workspace/python/bigdatapractice/lab2/resource/douban_games.csv'


def get_json(num):
	r = requests.get('https://www.douban.com/j/ilmen/game/search?genres=1&platforms=&q=&sort=rating&more=' + str(num))
	return r.text


def integration_data(page):
	# platforms, genres, rating, title, url, star, review{content, author}, n_ratings, cover, id
	res = get_json(page + 1)
	json_rst = json.loads(res)
	result = []
	for element in json_rst.get('games'):
		tmp = []
		tmp.append(element.get('id'))
		tmp.append(element.get('platforms'))
		tmp.append(element.get('genres'))
		tmp.append(element.get('rating'))
		tmp.append(element.get('title'))
		tmp.append(element.get('url'))
		tmp.append(element.get('star'))
		tmp.append(element.get('review').get('content'))
		tmp.append(element.get('review').get('author'))
		tmp.append(element.get('n_ratings'))
		tmp.append(element.get('cover'))

		result.append(tmp)
	return result


def write_file(num):
	heads = ['id', 'platforms', 'genres', 'rating', 'title', 'url', 'star', 'content', 'author', 'n_ratings', 'cover']
	csv_util.write_heads_csv(file_path, heads, integration_data(num), '|')


def append_file(num):
	csv_util.append_heads_csv(file_path, integration_data(num), '|')


if __name__ == '__main__':
	for i in range(10):
		if not i:
			write_file(i)
		else:
			append_file(i)
