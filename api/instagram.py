from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import json
import pandas as pd


def extract_insta_data(user_id="id", user_passwd="passwd", wish_num=10,
                       login_option="facebook",
                        keyword="키친마이야르",
                       instagram_id_name="username", instagram_pw_name="password",
                       instagram_login_btn=".sqdOP.L3NKy.y3zKF     ",
                       facebook_login_page_css=".sqdOP.L3NKy.y3zKF     ",
                       facebook_login_page_css2=".sqdOP.yWX7d.y3zKF     ",
                       facebook_id_form_name="email",
                       facebook_pw_form_name="pass",
                       facebook_login_btn_name="login"):
    driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

    print(f"login start - option {login_option}")

    login_url = "https://www.instagram.com/accounts/login/"
    driver.get(login_url)
    time.sleep(10)

    is_login_success = False

    if login_option == "instagram":
        try:
            instagram_id_form = driver.find_element_by_name(instagram_id_name)
            instagram_id_form.send_keys(user_id)
            time.sleep(5)

            instagram_pw_form = driver.find_element_by_name(instagram_pw_name)
            instagram_pw_form.send_keys(user_passwd)
            time.sleep(7)

            login_ok_button = driver.find_element_by_css_selector(instagram_login_btn)
            login_ok_button.click()
            is_login_success = True
        except:
            print("instagram login fail")
            is_login_success = False

        time.sleep(10)
    elif login_option == "facebook":
        is_facebook_btn_click = False
        try:
            print("try click facebook login button 1")
            facebook_login_btn = driver.find_element_by_css_selector(facebook_login_page_css)
            time.sleep(5)
            facebook_login_btn.click()
            is_facebook_btn_click = True
            is_login_success = True
        except:
            print("click facebook login button 1 fail")
            is_facebook_btn_click = False
            is_login_success = False

        time.sleep(10)

        if not is_facebook_btn_click:
            print("try click facebook login button 2")
            try:
                facebook_login_btn = driver.find_element_by_css_selector(facebook_login_page_css2)
                time.sleep(5)
                facebook_login_btn.click()
                is_facebook_btn_click = True
                is_login_success = True
            except:
                print("click facebook login button 2 fail")
                is_login_success = False

        time.sleep(10)

        if is_facebook_btn_click:
            id_input_form = driver.find_element_by_name(facebook_id_form_name)
            time.sleep(5)
            id_input_form.send_keys(user_id)

            time.sleep(7)

            pw_input_form = driver.find_element_by_name(facebook_pw_form_name)
            time.sleep(5)
            pw_input_form.send_keys(user_passwd)

            time.sleep(7)

            login_btn = driver.find_element_by_name(facebook_login_btn_name)
            time.sleep(5)
            login_btn.click()
        time.sleep(10)

    if is_login_success:
        print(f"login {login_option} success")
        print(f"Start {keyword} Extract")


extract_insta_data(user_id="id", user_passwd="pwd", wish_num=3,
                   login_option="facebook",  # facebook or instagram
                    keyword="키친마이야르",
                   instagram_id_name="username", instagram_pw_name="password",
                   instagram_login_btn=".sqdOP.L3NKy.y3zKF     ",
                   facebook_login_page_css=".sqdOP.L3NKy.y3zKF     ",
                   facebook_login_page_css2=".sqdOP.yWX7d.y3zKF     ",
                   facebook_id_form_name="email",
                   facebook_pw_form_name="pass",
                   facebook_login_btn_name="login")
