from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8100')

assert 'Django' in browser.title
