# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

def getLocInfo(locater):
    try:
        key, value = locater.split(">")
    except:
        print("配置文件格式错误")

    if key == "id":
        return By.ID, value
    if key == "class":
        return By.CLASS_NAME, value
    if key == "xpath":
        return By.XPATH, value


def test():
    print("ggggggggggggggggggggg")