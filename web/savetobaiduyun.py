import readExcel
from selenium import webdriver
import loginBaiduyun
def doWork():
    path=r'C:\filetmp\demo4q.xlsx'
    listUrl,listpwd= readExcel.read_excel(path)
    driver = webdriver.Chrome()
    loginBaiduyun.login(driver,"你的云盘账号","密码")
    for index in range(len(listUrl)):
        srcurl=listUrl[index]
        srcpwd=listpwd[index]
        loginBaiduyun.extract(driver,srcurl,srcpwd)
    driver.quit()
if __name__ == '__main__':
    doWork()
