from selenium import webdriver
import unittest
driver = webdriver.Firefox(executable_path=r'/Users/elmaanshikder/Downloads/geckodriver')

#Jeff is looking for a blog written by Elmaan 
driver.get('http://127.0.0.1:8000')

#He notices that the title is is the name of the person he is looking for
assert 'Elmaan Blog' in driver.title , "instead title is " + driver.title

#he is done with the internet for today
driver.quit()