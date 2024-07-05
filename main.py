from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.imagecaptcha import *

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

login_url = 'https://highschool.kh.edu.tw/Login.action?schNo=563401D' #高雄高商校務行政系統專屬網址
driver.get(login_url)


#等待載入並點擊"確定"關閉公告

announcement_ok_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'btnOK'))
)
announcement_ok_button.click()


#等待帳號和密碼輸入框加載

username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'loginId'))
)
password_field = driver.find_element(By.ID, 'password')


#輸入帳號密碼

username_field.send_keys('id')  #輸入帳號
password_field.send_keys('pwd')  #輸入密碼


#下載驗證碼圖片

captcha_image = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'validatePic'))
)
captcha_image.screenshot('captcha.png')


#使用Anti-Captcha破解驗證碼

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key('key')  #輸入Anti-Captcha API Key

captcha_text = solver.solve_and_return_solution('captcha.png')
if captcha_text == 0:
    print("CAPTCHA 解出驗證碼錯誤:", solver.error_code)
else:
    print("CAPTCHA 解出驗證碼:", captcha_text)


#輸入驗證碼

captcha_field = driver.find_element(By.ID, 'validateCode')
captcha_field.send_keys(captcha_text)


#點擊登入按鈕

login_button = driver.find_element(By.ID, 'login')
login_button.click()


#等待左側菜單加載

left_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'LeftPane'))
)


#點擊"學生線上"

student_online_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="sysMenu-學生線上"]/a'))
)
student_online_menu.click()


#點擊"04彈性學習"

flexible_learning_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="sysMenu-學生線上-04彈性學習"]/a'))
)
flexible_learning_menu.click()


#點擊"彈性學習線上選課"

online_course_selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@name="AB113S" and text()="彈性學習線上選課"]'))
)
online_course_selection.click()

print("已成功點擊 '彈性學習線上選課'")


#點擊"二升三彈性選課"

class_selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//td[@title="二升三彈性選課"]'))
)
class_selection.click()

print("已成功點擊 '二升三彈性選課'")


#點及課程

class_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, 'xpath'))  #輸入要選取的課程的XPATH
)
class_button.click()

print("已成功點擊課程")


#點擊"儲存"

add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/table[3]/tbody/tr[2]/td/input'))
)
add_button.click()

print("儲存成功")

#保持瀏覽器開啟狀態
input("按下 Enter 鍵以結束程式，但保持瀏覽器開啟...")
