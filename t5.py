from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
import pytesseract
from selenium.webdriver.chrome.options import Options
import datetime
import myweb

#点击坐标
def click_clocxy(dr,x,y,left_click=True):
    if left_click:
        ActionChains(dr).move_by_offset(x,y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x,y).context_click().perform()
    ActionChains(dr).move_by_offset(-x,-y).perform()

 

def str2sec1(x):
    s=x.split(' ')
    s=s[1].split('已学')
    return s[1]

browser = webdriver.Chrome()
browser.get("chrome://settings/content/flash")
browser.maximize_window()
click_clocxy(browser,1107,178)

browser.get("https://www.sxgbxx.gov.cn/")

#登陆
browser.find_element_by_link_text('登录').click()
browser.implicitly_wait(5)
browser.maximize_window()
username='u0179407'
password='u0179407'
myweb.denglu(username,password,browser)

#打开学习
lis=browser.find_elements_by_class_name('tzc_zt_b1')
lis[5].click()

browser.find_element_by_link_text('立即学习').click()
k=0
starts=browser.find_elements_by_class_name('lh-reply-btn')
for j in range(0,len(starts)):
    if j!=0:
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        starts=browser.find_elements_by_class_name('lh-reply-btn')
    starts[j].click()
    browser.switch_to_window(browser.window_handles[1])
    baifen=browser.find_elements_by_class_name('play-icon-box')
    for i in range(0,len(baifen)):
        if i!=0:
        #     browser.close()
        #     browser.switch_to_window(browser.window_handles[0])
            baifen=browser.find_elements_by_class_name('play-icon-box')
        print(baifen[i].text)
        t=myweb.Mystr(baifen[i].text)
        t=t.strtotimes()
        print(t)
        s=str2sec1(baifen[i].text)
        print(s)
        if s=='100%':
            continue
        else:
            baifen[i].click()
            # time.sleep(10)
            fls=browser.find_elements_by_class_name('c-p-wrap')            
            rs=fls[i].text
            rs=rs.replace('\n','')
            print(rs)
            if rs.find('分')!=-1 and rs.find('秒')!=-1:                
                if k==0:
                    click_clocxy(browser,636,390)
                    if input('flash可以开始按任意键')!=None:   
                        # click_clocxy(browser,636,390)
                        k=1
                else:
                    # time.sleep(5)
                    time.sleep(5)
            else:
                time.sleep(20)
                browser.back()
                continue
        click_clocxy(browser,636,390)
        aa=int(s.strip('%'))
        print(aa)
        if aa>50:
            time.sleep(5)
            click_clocxy(browser,405,687)
            time.sleep(5)
            click_clocxy(browser,605,687)
            time.sleep(t/2)
        else:
            time.sleep(t)
        # print("完成")
        #1time.sleep(5)
        browser.back()
        # browser.close()
        # browser.switch_to_window(browser.window_handles[0])
        # starts=browser.find_elements_by_class_name('lh-reply-btn')
        # starts[j].click()
        # browser.switch_to_window(browser.window_handles[1])

 
    # starts=browser.find_elements_by_class_name('lh-reply-btn')






