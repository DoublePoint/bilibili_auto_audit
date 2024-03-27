from selenium import webdriver
import time

from selenium.webdriver.common.by import By

total = 0
current_page = 0;
def is_login_seccess():
    try:
        btn = driver.find_element(By.XPATH, '//div[contains(@class,"header-login-entry")]/..')
        return False
    except:
        return True

def dizan_current_page():
    videoList = driver.find_elements(By.XPATH, '//div[contains(@class,"bili-video-card__wrap")]/a')
    for i in range(len(videoList)):
        video = driver.find_elements(By.XPATH, '//div[contains(@class,"bili-video-card__wrap")]/a')[i]
        driver.get(video.get_attribute("href"))
        time.sleep(2)
        textarea = driver.find_element(By.XPATH, '//textarea')
        textarea.click()
        textarea.send_keys("互赞")
        send_btn = driver.find_element(By.XPATH, '//div[@class="reply-box-send"]')
        send_btn.click()
        time.sleep(2)
        print(++total + '条记录已经点赞')


driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")

print("开始进入登录页面")  # 打印页面的标题
showLoginBtn = driver.find_element(By.XPATH, '//div[contains(@class,"header-login-entry")]/..')
print(showLoginBtn)
showLoginBtn.click()
time.sleep(1)
# 输入账号
print("开始输入登录账号")  # 打印页面的标题
unipt = driver.find_element(By.XPATH, '//input[@placeholder="请输入账号"]')
unipt.click()
unipt.send_keys("15153560513")
# 输入账号
print("开始输入密码")  # 打印页面的标题
pwdipt = driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]')
pwdipt.click()
pwdipt.send_keys("203105800")

# 点击登录
print("开始点击登录按钮")
loginBtn = driver.find_element(By.XPATH, '//div[contains(@class,"btn_primary")]')
loginBtn.click()

login_success = True
for i in range(10):
    login_success = is_login_seccess()
    if not login_success:
        time.sleep(3)
        print("登录出现异常，3秒后重试")

if not login_success:
    print("登录失败")
else:
    print("登录成功")

driver.get("https://search.bilibili.com/all?keyword=%E4%BA%92%E5%85%B3")
dizan_current_page()
try:
    if(++current_page<10):
        nextPage = driver.find_element(By.XPATH, '//button[text()="下一页"]')
        time.sleep(5)
        dizan_current_page()
except:
    print("所有页面完成")

# print(videoList)

time.sleep(10)
# 退出模拟浏览器
driver.quit()  # 一定要退出!不退出会有残留进程!
