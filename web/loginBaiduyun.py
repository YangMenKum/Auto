# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def login(driver,username,password):
    orgin_url = ['https://pan.baidu.com/']
    driver.get(orgin_url[0])
    time.sleep(10)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(3)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(username)
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(password)
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(5)
def extract(driver,srcurl,srcpwd):
    driver.get(srcurl)
    try:
        time.sleep(5)
        getpwd = driver.find_element_by_id("eqqo3Jx")
        getpwd.send_keys(srcpwd)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        # 全选
        time.sleep(10)
        try:
            selectall = driver.find_element_by_class_name("zbyDdwb")
            selectall.click()
        except NoSuchElementException:
            file_name = "no_zbyDdwb.png"
            # driver.save_screenshot(file_name)
            driver.get_screenshot_as_file(file_name)
            pass
        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(5)
        # AA 保存路径
        selectdir = driver.find_element_by_xpath("//span[@node-path='/AA']")
        selectdir.click()
        enter = driver.find_element_by_link_text("确定")
        enter.click()
        time.sleep(2)
    except NoSuchElementException:
        file_name = "no_such_element.png"
        # driver.save_screenshot(file_name)
        driver.get_screenshot_as_file(file_name)
        pass
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver, "你的云盘账号", "密码")
    srcurl="https://pan.baidu.com/s/1S6CL1cgRWcoxH8IZZB5kYQ"
    srcpwd="pmq0"
    extract(driver,srcurl,srcpwd)
