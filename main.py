import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import imaplib, email
from imap_tools import MailBox
from email.header import Header, decode_header, make_header
import os
from os import path
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random
try:
    class Main():
        def __init__(self, fname, lname, email, email_pass, passworld, day, month, year, sex, ua):
            self.fname = fname
            self.lname = lname
            self.email = email
            self.email_pass = email_pass
            self.passworld = passworld
            self.day = day
            self.month = month
            self.year = year
            self.sex = sex
            self.ua = ua
            self.driver_set()
            self.create_accaunt()
            self.verf()
    
        def driver_set(self): 
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('user-agent=' + self.ua)
            #self.options.add_argument('--proxy-server=http://' + self.proxy)
            self.driver = webdriver.Chrome(executable_path = "C:\development\soft\prg_fb\chromedriver.exe", chrome_options=self.options)
            self.driver.implicitly_wait(5)
            self.driver.minimize_window()
        
    
        def create_accaunt(self):
            self.driver.get("https://ru-ru.facebook.com/")
            self.btn_new_akk = self.driver.find_elements_by_xpath("//a[text()='Создать аккаунт']")
            for elem in self.btn_new_akk:
                elem.click()
            sleep(2)
            self.btn_f = self.driver.find_elements_by_name("firstname")
            for elem in self.btn_f:
                elem.send_keys(self.fname)
            sleep(1)
            self.btn_l = self.driver.find_elements_by_name("lastname")
            for elem in self.btn_l:
                elem.send_keys(self.lname)
            sleep(1)
            self.btn_email = self.driver.find_elements_by_name("reg_email__")
            for elem in self.btn_email:
                elem.send_keys(self.email)
            sleep(1)
            self.btn_email_conf = self.driver.find_elements_by_name("reg_email_confirmation__")
            for elem in self.btn_email_conf:
                elem.send_keys(self.email)
            self.btn_pas = self.driver.find_elements_by_name("reg_passwd__")
            for elem in self.btn_pas:
                elem.send_keys(self.passworld)
            sleep(1)
            self.select_one = self.driver.find_elements_by_name("birthday_day")
            for el in self.select_one:
                days_input = Select(el)
                days_input.select_by_value(str(random.randint(20, 29)))
            self.select_two = self.driver.find_elements_by_name("birthday_month")
            for el in self.select_two:
                month_input = Select(el)
                month_input.select_by_visible_text(random.choice(["янв", "фев", "апр", "май", "авг", "сен"]))
            sleep(1)
            self.select_three = self.driver.find_elements_by_name("birthday_year")
            for el in self.select_three:
                year_input = Select(el)
                year_input.select_by_value(str(random.randint(1960, 2000)))
            sleep(1)
            if self.sex == "Муж":
                self.btn_men = self.driver.find_elements_by_xpath('//label[text()="Мужчина"]')
                for elem in self.btn_men:
                    elem.click()
            elif self.sex == "Жен":
                self.btn_woman = self.driver.find_elements_by_xpath('//label[text()="Женщина"]')
                for elem in self.btn_woman:
                    elem.click()
            elif self.sex == "Другое":
                self.btn_unisex = self.driver.find_elements_by_xpath('//label[text()="Другое"]')
                for elem in self.btn_unisex:
                    elem.click()
            sleep(1)
            self.btn_registr = self.driver.find_elements_by_name("websubmit")
            for elem in self.btn_registr:
                elem.click()
            sleep(3)
            self.virt_url = self.driver.current_url
        def verf(self):
            mess = []
            mess2 = []
            user = self.email
            passw = self.email_pass
            imap_url = 'imap.gmail.com'
            with MailBox(imap_url).login(user, passw, 'INBOX') as mailbox:
                for msg in mailbox.fetch(limit=1, reverse=False):
                    for i in msg.subject:
                        mess.append(i)
    
            for j in mess:
                if j.startswith("0") or j.startswith("1") or j.startswith("2") or  j.startswith("3") or j.startswith("4") or j.startswith("5") or j.startswith("6") or j.startswith("7") or j.startswith("8") or j.startswith("9"):
                    mess2.append(j)
            werf = "".join(mess2)
            sleep(3)

            self.driver.get(self.virt_url)
            self.driver.find_element_by_name("n").send_keys(werf)
            self.driver.find_element_by_name("reset_action").click()
    

            self.driver.quit()
except IndexError:
    pass






    