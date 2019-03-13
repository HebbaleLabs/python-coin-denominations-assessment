import unittest
from parameterized import parameterized
from coin_denominations import coin_denominations

class CoinDenominationsTest(unittest.TestCase):

  @parameterized.expand([
    ('dispense a single coin',[1,5,10], 10, 1),
    ('dispense a single coin',[1,5,10], 5, 1),
    ('dispense a single coin',[1,5,10], 1, 1),
    ('dispense more than one coin',[1,5,10], 6, 2),
    ('dispense more than one coin',[1,5,10], 15, 2),
    ('dispense more than one coin',[1,5,10], 11, 2),
    ('dispense all unique coins',[1,5,10], 16, 3),
    ('dispense all unique coins',[1,2,5,10], 18, 4),
    ('dispense all unique coins',[1,10,25], 36, 3),
    ('dispense all unique coins',[5,10], 15, 2)
  ])
  def test_dispense(self, name, denominations, amount, expected_no_of_coins):
    no_of_coins = coin_denominations(denominations, amount)
    message = 'For input denominations: {0} and amount: {1}, expected value = {2}, and actual value = {3}'.format(denominations, amount, expected_no_of_coins, no_of_coins)
    self.assertEqual(expected_no_of_coins, no_of_coins, message)

  @parameterized.expand([
    ('dispense least coins',[1,3,4], 6, 2),
    ('dispense least coins',[1,5,7], 11, 3),
    ('dispense least coins',[1,2,5,7], 10, 2)
  ])
  def test_greedy_dispensing(self, name, denominations, amount, expected_no_of_coins):
    no_of_coins = coin_denominations(denominations, amount)
    message = 'For input denominations: {0} and amount: {1}, expected value = {2}, and actual value = {3}'.format(denominations, amount, expected_no_of_coins, no_of_coins)
    self.assertEqual(expected_no_of_coins, no_of_coins, message)

  @parameterized.expand([
    ('dispense no coins',[5,10], 1, 0),
    ('dispense no coins',[5,10], 4, 0),
    ('dispense no coins',[10,25], 7, 0)
  ])
  def test_dispense_no_coins(self, name, denominations, amount, expected_no_of_coins):
    no_of_coins = coin_denominations(denominations, amount)
    message = 'For input denominations: {0} and amount: {1}, expected value = {2}, and actual value = {3}'.format(denominations, amount, expected_no_of_coins, no_of_coins)
    self.assertEqual(expected_no_of_coins, no_of_coins, message)