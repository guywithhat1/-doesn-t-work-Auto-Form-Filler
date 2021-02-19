from selenium import webdriver
import time
import form_inputs

web = webdriver.Chrome()

web.get('https://docs.google.com/forms/d/e/1FAIpQLSdPPCxfAiTxcGDNWx_LziLpCwq4Jb0mbw5SjmPHNoOEP2T5HQ/viewform')

time.sleep(2)

def fill_out_module(module, text=None):
    element = web.find_element_by_xpath(form_inputs.xpaths[module])

    element.send_keys(form_inputs.inputs[module])
