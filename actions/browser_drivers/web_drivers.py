from selenium import webdriver

def get_browser(browser_name):
    if browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "chrome":
    	return webdriver.Chrome()
    elif browser_name == "opera":
    	return webdriver.Opera()
    elif browser_name == "andriod":
    	pass
    elif browser_name == "ios":
    	pass
    else:
    	return None