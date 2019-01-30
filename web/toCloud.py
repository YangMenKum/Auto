# -*- coding: UTF-8 -*-
import xlrd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
# 登录云盘
def login(driver,username,password):
    orgin_url = ['https://pan.baidu.com/']
    driver.get(orgin_url[0])
    time.sleep(5)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(10)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(username)
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(password)
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    #此处有可能会有验证码，可以sleep一会儿手动输入验证码
    #time.sleep(20)
    elem_submit.click()
    time.sleep(10)
# 将加密分享的文件保存到自己云盘的目录下[AA]
def extract(driver,srcurl,srcpwd):
    driver.get(srcurl)
    try:
        #输入密码的input的id已经被修改了
        getpwd = driver.find_element_by_id("eqqo3Jx")
        getpwd.send_keys(srcpwd)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        time.sleep(15)
		# 目前有两种情况
		# 一：分享文件是一压缩包
		# 二：分享的是一路径
        try:
            # 全选（情况二）
            selectall = driver.find_element_by_class_name("zbyDdwb")
            selectall.click()
        except NoSuchElementException:
            file_name = "no_zbyDdwb.png"
            driver.save_screenshot(file_name)
            driver.get_screenshot_as_file(file_name)
            pass
        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(10)
        # AA 保存路径
        selectdir = driver.find_element_by_xpath("//span[@node-path='/AA']")
        selectdir.click()
        enter = driver.find_element_by_link_text("确定")
        enter.click()
        time.sleep(5)
    except NoSuchElementException:
        file_name = "no_such_element.png"
        driver.get_screenshot_as_file(file_name)
        pass
# 从Excel中读取分享链接和提取密码（默认第一列是链接、第二列是提取密码）
def read_excel(path):
    workbook = xlrd.open_workbook(path)
    sheet0=workbook.sheet_by_index(0);
    listUrl=[]
    listpwd=[]
    rownum=sheet0.nrows
    for index in range(rownum):
        listUrl.append(sheet0.cell(index,0).value.encode('utf-8'))
        listpwd.append(sheet0.cell(index,1).value.encode('utf-8'))
    return listUrl,listpwd
# 调用执行
def doWork():
    path=r'C:\filetmp\demo4q.xlsx'
    listUrl,listpwd= read_excel(path)
    driver = webdriver.Chrome()
    login(driver,"你的云盘账号","密码")
    for index in range(len(listUrl)):
        srcurl=listUrl[index]
        srcpwd=listpwd[index]
        extract(driver,srcurl,srcpwd)
    driver.quit()
if __name__ == '__main__':
    doWork()