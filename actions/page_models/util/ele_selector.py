#!/uer/bin/python
# -*- coding: utf-8 -*-
"""
element selector base class
author: Flint LIU
email: fliu@brandscreen.com
"""

__version__ = "0.1"
__all__ = ["elementSelector"]

from .object_models import *

class elementSelector(object):
    """
element selector base class
"""
    def __init__(self,ele_name,elements_info,window):
        self.ele_name = ele_name
        self.elements_info = elements_info
        self.window = window
        self.path_flow = []
        
    def get_ele_info(self,_ele_name):
        ele_info = self.elements_info.get(_ele_name)
        root_ele = ele_info[0]
        s_method = ele_info[1]
        arg_ele = ele_info[2]
        ele_type = ele_info[3]
        return root_ele,s_method,arg_ele,ele_type
    
    def element_selector(self,_driver):
        if len(self.path_flow) == 1:
            return _driver
        else:
            self.path_flow.pop(-1)
            s_method = self.get_ele_info(self.path_flow[-1])[1]
            arg_ele = self.get_ele_info(self.path_flow[-1])[2]
            if s_method == "id":
                _driver = _driver.find_element_by_id(arg_ele)
            elif s_method == "ids":
                _driver = _driver.find_elements_by_id(arg_ele)
            elif s_method == "xpath":
                _driver = _driver.find_element_by_xpath(arg_ele)
            elif s_method == "name":
                _driver = _driver.find_element_by_name(arg_ele)
            elif s_method == "className":
                _driver = _driver.find_element_by_class_name(arg_ele)
            elif s_method == "tagName":
                _driver = _driver.find_element_by_tag_name(arg_ele)
            elif s_method == "tagNames":
                _driver = _driver.find_elements_by_tag_name(arg_ele)
            elif s_method == "linkText":
                _driver = _driver.find_element_by_link_text(arg_ele)
            elif s_method == "linkPartialText":
                _driver = _driver.find_element_by_partial_link_text(arg_ele)
            elif s_method == "css":
                _driver = _driver.find_element_by_css_selector(arg_ele)
            return self.element_selector(_driver)
    
    def path_builder(self,_root_ele):
        self.path_flow.append(_root_ele)
        if self.path_flow[-1] == "window":
            return None
        else:
            _root_ele = self.get_ele_info(_root_ele)[0]
            return self.path_builder(_root_ele)
    
    def get_element(self):
        self.path_builder(self.ele_name)
        element = self.element_selector(self.window)
        ele_type = self.get_ele_info(self.ele_name)[3]
        if ele_type != "" and objects.OBJECT_MAP.has_key(ele_type):
            return objects.OBJECT_MAP[ele_type](element)
        else:
            return element

if __name__ == "__main__":
    elements_info = {"aaa":["window","a2","a3",""],"bbb":["aaa","b2","b3",""],"ccc":["bbb","c2","c3",""]}
    es = elementSelector("ccc",elements_info,"window")
    print es.get_element()
