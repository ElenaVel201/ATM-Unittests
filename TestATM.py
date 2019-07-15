import unittest
from ATM import *


class TestBank(unittest.TestCase):
   def setUp(self):
       self.terminal = InternetBank()
       self.terminal.enter_pin_code(333)

   def test_top_up(self):
       my_money = self.terminal.top_up_money(5000)
       self.assertEqual(my_money, 10000)

   def test_correct_pin_code(self):
       self.assertTrue(self.terminal.enter_pin_code(333))

   def test_attempts_failed(self):
       incorrect_attempt_1 = self.terminal.enter_pin_code(222)
       incorrect_attempt_2 = self.terminal.enter_pin_code(222)
       incorrect_attempt_3 = self.terminal.enter_pin_code(222)
       self.assertEqual(self.terminal.attempts, 0)
       self.assertTrue(self.terminal.user_can_get_money)

   def test_my_money_boundaries_negative(self):
       # this test should be down
       minus_sum = self.terminal.top_up_money(-1)
       self.assertEqual(minus_sum, 5000)

   def test_withdraw_money(self):
       money = self.terminal.withdraw_money(2500)
       self.assertEqual(self.terminal.balance, 2500)

   def test_withdraw_money_incorrect(self):
       money = self.terminal.withdraw_money(5001)
       self.assertEqual(self.terminal.balance, 5000)

   def test_withdraw_money_zero(self):
       money = self.terminal.withdraw_money(0)
       self.assertEqual(self.terminal.balance, 5000)

   def test_withdraw_money_negative(self):
       money = self.terminal.withdraw_money(-1)
       self.assertEqual(self.terminal.balance, 5000)

    def test_attempts_failed_exception(self):
        incorrect_attempt_1 = self.terminal.enter_pin_code(222)
        incorrect_attempt_2 = self.terminal.enter_pin_code(222)
        incorrect_attempt_3 = self.terminal.enter_pin_code(222)
        self.assertRaises(Exception)

   def test_withdraw_money_exception(self):
       money = self.terminal.withdraw_money(5001)
       self.assertRaises(Exception)

    def test_check_balance_exception(self):
        user_not_authorized = self.terminal.enter_pin_code(111)
        self.assertRaises(Exception)
