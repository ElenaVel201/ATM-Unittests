from Exceptions import *


class InternetBank(object):
    balance = 5000
    attempts = 3
    user_can_get_money = False

    def top_up_money(self, my_money):
        return self.balance + my_money

    def enter_pin_code(self, pin_code):
        correct_pin_code = 333
        if self.attempts == 0:
            raise AttemptsOver

        if pin_code != correct_pin_code:
            self.attempts = self.attempts - 1

        if correct_pin_code == pin_code:
            self.user_can_get_money = True
            return True

    def withdraw_money(self, wanted_money):
        if self.user_can_get_money:
            if wanted_money <= self.balance:
                self.balance = self.balance - wanted_money
                return wanted_money
            else:
                raise NotEnoughMoney

    def check_balance(self):
        # if pin code is correct, user_can_get_money is true and we can show balance
        if self.user_can_get_money == True:
            return self.balance
        else:
            raise UserNotAuthorized
            
