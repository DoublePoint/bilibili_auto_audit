from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import schedule
from datetime import datetime
from twilio.rest import Client

account_sid = 'ACe9c8bb26b96eabb15afd73a566b82eb5'
auth_token = 'c584157e41dc795a8304edee40770803'
client = Client(account_sid, auth_token)

class bilibili(object):
    def __init__(self,username,pwd,start_page=2,max_page=999,key_word=''):
        self.__username = username
        self.__pwd = pwd
        self.__total = 0
        self.__start_page = start_page
        self.__current_page = 0
        self.__max_page = max_page
        self.__key_word = key_word
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bilibili.com/")

    def run(self):
        # 1.开始登录
        self.__login()
        schedule.clear()
        # 创建一个按3秒间隔执行任务
        schedule.every(3*60*24).seconds.do(self.__audit)
        while True:
            schedule.run_pending()
        # 5.退出模拟浏览器
        # self.driver.quit()  # 一定要退出!不退出会有残留进程!
    def __audit(self):
        # 1.1 跳转到搜索页面
        self.driver.get("https://search.bilibili.com/all?keyword=" + self.__key_word)
        time.sleep(5)

        # 2.从start_page页开始
        self.__step_page()

        # 3. 开始点赞当前页
        self.__dizan_current_page()

        # 4. 跳转到下一页点赞
        try:
            while self.__current_page < self.__max_page:
                nextPage = self.driver.find_element(By.XPATH, '//button[text()="下一页"]')
                nextPage.click()
                time.sleep(5)
                self.__dizan_current_page()
                self.__current_page += 1
        except:
            print("所有页面完成")

        client.messages.create(
            from_='+19382533388',
            body='所有页面完成自动评论',
            to='+8617686026701'
        )
    def __login(self):
        # 1进入登录页面
        print("开始进入登录页面")  # 打印页面的标题
        showLoginBtn = self.driver.find_element(By.XPATH, '//div[contains(@class,"header-login-entry")]/..')
        showLoginBtn.click()
        time.sleep(1)
        # 2输入账号
        print("开始输入登录账号")  # 打印页面的标题
        unipt = self.driver.find_element(By.XPATH, '//input[@placeholder="请输入账号"]')
        unipt.click()
        unipt.send_keys(self.__username)
        # 3输入账号
        print("开始输入密码")  # 打印页面的标题
        pwdipt = self.driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]')
        pwdipt.click()
        pwdipt.send_keys(self.__pwd)

        # 4点击登录按钮
        print("开始点击登录按钮")
        loginBtn = self.driver.find_element(By.XPATH, '//div[contains(@class,"btn_primary")]')
        loginBtn.click()

        # 5判断是否成功
        login_success = True
        for i in range(10):
            login_success = self.__is_login_seccess()
            if not login_success:
                time.sleep(3)
                print("登录出现异常，3秒后重试")
        if not login_success:
            print("登录失败")
        else:
            print("登录成功")

    def __step_page(self):
        for i in range(self.__start_page):
            nextPage = self.driver.find_element(By.XPATH, '//button[text()="下一页"]')
            nextPage.click()
            time.sleep(5)
    def __dizan_current_page(self):
        videoList = self.driver.find_elements(By.XPATH, '//div[contains(@class,"bili-video-card__wrap")]/a')
        for i in range(len(videoList)):
            self.__total += 1

            try:
                video = self.driver.find_elements(By.XPATH, '//div[contains(@class,"bili-video-card__wrap")]/a')[i]
                self.driver.get(video.get_attribute("href"))
                time.sleep(5)
                textarea = self.driver.find_element(By.XPATH, '//textarea')
                textarea.click()
                textarea.send_keys("互关")
                send_btn = self.driver.find_element(By.XPATH, '//div[contains(@class,"reply-box-send")]')
                send_btn.click()
                time.sleep(2)
                self.driver.back()
                print(str(self.__total) + '条记录成功')
            except:
                print(str(self.__total) + '条记录失败')

    def __is_login_seccess(self):
        try:
            btn = self.driver.find_element(By.XPATH, '//div[contains(@class,"header-login-entry")]/..')
            return False
        except:
            return True

if __name__ == '__main__':
    bilibili = bilibili(username='17686026701',pwd='203105800liulei',max_page=2,start_page=0,key_word="互关互赞")
    bilibili.run()
