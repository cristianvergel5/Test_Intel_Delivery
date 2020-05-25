#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import math, time
from Locators import *

class intelDelivery():

    def __init__(self, time_to_wait=5):
        self.web_link = "http://localhost:3000/"

        self.driver = webdriver.Firefox(
            executable_path="./geckodriver.exe"
        )
        self.driver.implicitly_wait(time_to_wait)
        self.login_state = False
        self.username = None
        

    def singIn(self, username, password):
        if not self.login_state:
            self.driver.get(self.web_link)
            username_box = self.driver.find_element(*InteldeliveryLoginPage.username_box)
            password_box = self.driver.find_element(*InteldeliveryLoginPage.password_box)
            self.username = username

            username_box.send_keys(self.username)
            password_box.send_keys(password)
            self.driver.find_element(*InteldeliveryLoginPage.sign_in_btn).click()
            time.sleep(1)

            if self.driver.current_url == "http://localhost:3000/manage":
                self.login_state = True
            else:
                self.login_state = False
            return self.login_state
            time.sleep(3)
            self.driver.close()
        
    def signOut(self):
        if self.login_state:
            self.driver.find_element(*InteldeliveryManagePage.menu_link).click()
            time.sleep(1)
            self.driver.find_element(*InteldeliveryManagePage.sign_out_btn).click()
            time.sleep(1)
            self.login_state = False
            return True
        return False
    
    def cancelDelivery(self):
        if self.login_state:
            self.driver.find_element(*InteldeliveryManagePage.cancel_btn).click()
            time.sleep(1)
            self.driver.find_element(*InteldeliveryManagePage.cancel_btn_confirm).click()
            

            if "CANCELADO" not in self.driver.page_source: 
                return True

        return False
    
    def PaymentDelivery(self):
        if self.login_state:
            self.driver.find_element(*IntelDeliveryPaymentPage.payment_btn).click()
            time.sleep(2)
            self.driver.find_element(*IntelDeliveryPaymentPage.payment_next_btn).click()
            time.sleep(2)
            name_card = self.driver.find_element(*IntelDeliveryPaymentPage.first_name_card)
            last_name_card = self.driver.find_element(*IntelDeliveryPaymentPage.last_name_card)
            payment_number_card = self.driver.find_element(*IntelDeliveryPaymentPage.number_card)
            payment_date_card = self.driver.find_element(*IntelDeliveryPaymentPage.expiration_date_card)
            payment_cvv_card = self.driver.find_element(*IntelDeliveryPaymentPage.cvv_card)

            name_card.send_keys(*infoCard.firstname)
            last_name_card.send_keys(*infoCard.lastname)
            payment_number_card.send_keys(*infoCard.number_card)
            payment_date_card.send_keys(*infoCard.date_card)
            payment_cvv_card.send_keys(*infoCard.cvv)
            time.sleep(2)
            
            self.driver.find_element(*IntelDeliveryPaymentPage.card_next_btn).click()
            time.sleep(2)
            self.driver.find_element(*IntelDeliveryPaymentPage.take_order).click()
            if "gracias por tu orden" in self.driver.page_source:
                return True           
            return True
        return False
    
    def addOrder(self):
        if self.login_state:
            self.driver.find_element(*InteldeliveryAddOrder.add_order_btn).click()
            time.sleep(2)

            address = self.driver.find_element(*InteldeliveryAddOrder.address1)
            city = self.driver.find_element(*InteldeliveryAddOrder.city)
            region = self.driver.find_element(*InteldeliveryAddOrder.region)
            postal_code = self.driver.find_element(*InteldeliveryAddOrder.postal_code)
            

            address.send_keys(*infoNewOrder.address)
            city.send_keys(*infoNewOrder.city)
            region.send_keys(*infoNewOrder.region)
            postal_code.send_keys(*infoNewOrder.postal_code)
            time.sleep(2)

            self.driver.find_element(*InteldeliveryAddOrder.registrer_btn).click()
            if "su pedido ha sido creado exitosamente!" in self.driver.page_source:
                return True
        return False

    def orderDate(self):
        if self.login_state:
            self.driver.find_element(*InteldeliveryOrderDate.date_picker_btn_one).send_keys(Keys.RETURN)
            self.driver.find_element(*InteldeliveryOrderDate.date_picker_btn_two).send_keys(Keys.RETURN)
            
            date_one = self.driver.find_element(*InteldeliveryOrderDate.date_picker_btn_one)
            date_two = self.driver.find_element(*InteldeliveryOrderDate.date_picker_btn_two)
            
            date_one.send_keys(*InteldeliveryOrderDate.date_one)
            date_two.send_keys(*InteldeliveryOrderDate.date_two)
            
            if "No hay domicilios que entregar." in self.driver.page_source:
                return True
        return False

def main():
    intelDeliveryPage = intelDelivery()
    print("IntelDeliveryLogin: :", intelDeliveryPage.signIn('cristianvergel', 'cristianvergel'))
    print("IntelDeliverySignOut: ", intelDeliveryPage.signOut())
    print("IntelDeliveryCancel: ", intelDeliveryPage.cancelDelivery())
    print("IntelDeliveryPayment: ", intelDeliveryPage.PaymentDelivery())
    print("IntelDeliveryDate: ", intelDeliveryPage.orderDate())

    

if __name__ == "__main__":
    main()