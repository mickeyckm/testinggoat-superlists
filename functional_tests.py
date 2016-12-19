from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
    firefox_path='/Users/mickey/Downloads/firefox45/Firefox.app/Contents/MacOS/firefox-bin'
))

browser.get('http://localhost:8000')

assert 'Django' in browser.title