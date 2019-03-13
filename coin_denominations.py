
def coin_denominations(denominations, amount):
  #
  # IMPORTANT:
  # 1. Write your solution in this function
  # 2. Do not make changes to the function signature
  # 3. Use the 'pip-install' command in the IDE, to install any requirements. This takes a few seconds.
  # 4. Use the 'run' command in the IDE, to run the main method. You can also invoke the main method from the terminal.
  # 5. Use the 'run-tests' command in the IDE, to run unit tests. The 'pip-install' command must be run before this.
  return None


def main():
  denominations = [1, 5, 10]
  amount = 121
  no_of_coins = coin_denominations(denominations, amount)
  message = 'Given coins of denominations {0}, no of coins used to create change for amount {1} is {2}\n'.format(
    denominations, amount, no_of_coins)
  print(message)


if __name__ == '__main__':
  main()
