from selenium import webdriver
import time
import form_inputs

web = webdriver.Chrome()

web.get('https://docs.google.com/forms/d/e/1FAIpQLSdPPCxfAiTxcGDNWx_LziLpCwq4Jb0mbw5SjmPHNoOEP2T5HQ/viewform')

time.sleep(2)

def fill_out_text_module(module):
    web.find_element_by_xpath(form_inputs.text_xpaths[module]).send_keys(form_inputs.inputs[module])

def click_button_modules():
    for i in range(1,6):
        web.find_element_by_xpath(form_inputs.button_xpaths[i]).click()