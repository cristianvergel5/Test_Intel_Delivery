from selenium.webdriver.common.by import By

class InteldeliveryLoginPage(object):
    username_box = (By.CSS_SELECTOR, '#username_email')
    password_box = (By.CSS_SELECTOR, '#password')
    sign_in_btn = (By.CSS_SELECTOR, '#signInBtn > span.MuiButton-label')

class InteldeliveryManagePage(object):
    menu_link = (By.CSS_SELECTOR, '#root > div.makeStyles-root-357 > header > div > button > span.MuiIconButton-label > svg > path')
    sign_out_btn = (By.CSS_SELECTOR, 'body > div.MuiDrawer-root.MuiDrawer-modal > div.MuiPaper-root.MuiDrawer-paper.MuiDrawer-paperAnchorLeft.MuiPaper-elevation16 > div > ul:nth-child(3) > a > div.MuiListItemIcon-root')
    cancel_btn = (By.CSS_SELECTOR, 'div.MuiPaper-root:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')
    cancel_btn_confirm = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]/span[1]')

class IntelDeliveryPaymentPage(object):
    payment_btn = (By.CSS_SELECTOR, '#pagarBtn > span.MuiIconButton-label > svg')
    payment_next_btn = (By.CSS_SELECTOR, '#continuarBtn > span.MuiButton-label')
    card_next_btn = (By.CSS_SELECTOR, '#continuarBtn > span.MuiButton-label')
    take_order = (By.CSS_SELECTOR, '#continuarBtn > span.MuiButton-label')
    first_name_card = (By.CSS_SELECTOR, '#firstName')
    last_name_card = (By.CSS_SELECTOR, '#lastName')
    number_card = (By.CSS_SELECTOR, '#cardNumber')
    expiration_date_card = (By.CSS_SELECTOR, '#expDate')
    cvv_card = (By.CSS_SELECTOR, '#cvv')

class InteldeliveryAddOrder(object):
    add_order_btn = (By.CSS_SELECTOR, '#create_delovery_btn > span.MuiIconButton-label > svg')
    registrer_btn = (By.CSS_SELECTOR, '#registrer_btn > span.MuiButton-label')
    accept_btn = (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button/span[1]')
    address1 = (By.CSS_SELECTOR, '#address1')
    city = (By.CSS_SELECTOR, '#city')
    region = (By.CSS_SELECTOR, '#region')
    postal_code = (By.CSS_SELECTOR, '#postal_code')

class InteldeliveryOrderDate(object):
    date_picker_btn_one = (By.CSS_SELECTOR, '#datePicker1')
    date_picker_btn_two = (By.CSS_SELECTOR, '#datePicker2')
    date_one = '2019-01-15'
    date_two = '2020-01-15'

class infoCard(object):
    firstname = 'Cristian'
    lastname = 'Vergel'
    number_card = '7894564456362'
    date_card = '04/24'
    cvv = '078'

class infoNewOrder(object):
    address = 'Calle 35 #74-94'
    city = 'Santa Marta'
    region = 'Magdalena'
    postal_code = '470003'


    