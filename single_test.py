from selenium import webdriver
from single import single

driver = webdriver.Firefox()
code = '1234'

single(driver,code)
