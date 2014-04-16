#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Actions of common object
author: Flint Liu
email: fliu@brandscreen.com
"""
import time

class optionSelecter(object):
	def __init__(self, selecter):
		self.selecter = selecter
		self.all_options = None

	def get_all_options(self):
		self.all_options = self.selecter.find_elements_by_tag_name("option")

	def select_the_first(self):
		self.get_all_options()
		self.all_options[1].click()

	def select_the_last(self):
		self.get_all_options()
		self.all_options[-1].click()

	def select_empty(self):
		self.get_all_options()
		self.all_options[0].click()

	def select_by_value(self, value):
		self.get_all_options()
		for o in self.all_options:
			if o.get_attribute("value") == value:
				o.click()
				break

	def select_by_text(self, text):
		self.get_all_options()
		for o in self.all_options:
			if o.text == text:
				o.click()
				break

class labelInput(object):
	def __init__(self, label):
		self.label = label

	def set_keys(self, value):
		self.label.send_keys(value)
		self.label.send_keys("\n")

class optionTable(object):
	def __init__(self, table):
		self.table = table

	def get_table_contents(self):
	    tbody = self.table.find_element_by_tag_name("tbody")
	    contents = tbody.find_elements_by_tag_name("tr")
	    return contents[0:-1], contents[-1]

	def select_option(self, name, action):
		_, option_list = self.get_table_contents()
		for o in option_list:
			on = o.find_element_by_tag_name("td")
			if on.text == name:
				clickAct = on.find_element_by_link_partial_text("actions")
				clickAct.click()

	def change_seleted_option(self):
		pass

class inputTab(object):
	def __init__(self, tab):
		self.tab = tab

	def set_value(self, value):
		while not self.tab.is_displayed():
			time.sleep(0.1)
		self.tab.send_keys(value)

	def clean_value(self):
		self.tab.clear()

class button(object):
	def __init__(self, button):
		self.button = button

	def click(self):
		self.button.click()

class radioSet(object):
	def __init__(self, radios):
		self.radios = radios

	def select_one(self, value):
		self.radios[value].click()

class dateWidget(object):
	def __init__(self, dateWidget):
		self.widget = dateWidget

	def select_month(self, month):
		month_select = optionSelecter(self.widget.find_element_by_class_name("ui-datepicker-month"))
		month_select.select_by_text(month)

	def select_year(self, year):
		year_select = optionSelecter(self.widget.find_element_by_class_name("ui-datepicker-year"))
		year_select.select_by_text(year)

	def next_month(self):
		next_button = button(self.widget.find_element_by_link_text("Next"))
		next_button.click()

OBJECT_MAP = {"optSelecter": optionSelecter,\
              "labelInput": labelInput,\
              "optTable": optionTable,\
              "inputTab": inputTab,\
              "button": button,\
              "radioSet": radioSet,\
              "dateWidget": dateWidget}