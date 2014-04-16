#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Base page modle class
author: Flint Liu
email: flintliu@hotmail.com
"""

from .util.ele_selector import elementSelector

class page(object):
	def __init__(self):
		self._driver = None
		self._url = None
		self._title = None
		self._element_list = None

	@property
	def driver(self):
		return self._driver

	@driver.setter
	def driver(self, dr):
		self._driver = dr

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, ur):
		self._url = ur

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, ti):
		self._title = ti

	@property
	def element_list(self):
		return self.element_list

	@element_list.setter
	def element_list(self, el):
		self._element_list = el

	def is_loaded(self):
		return self._driver.title == self._title

	def open(self):
		self._driver.get(self._url)

	def _elements(self):
		raise NotImplementedError("Need to create get_elements.")

	def get_element(self, en):
		es = elementSelector(en, self._element_list, self.driver)
		return es.get_element()