from asyncio import sleep

import driver
from Base.SeleniumBase import SeleniumMethod

class Login(SeleniumMethod):
    def __init__(self):
        super().__init__()
        self.driver = driver.wd

    def login(self):
        self.is_visible('id', 'loginEdit-el').send_keys('Supervisor')
        self.is_visible('id', 'passwordEdit-el').send_keys('Supervisor')
        self.is_visible('id', 't-comp17-textEl').click()



