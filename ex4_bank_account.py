# Exercise 4: Bank account simulator
# ==========
#
# Take as input an initial bank account balance (e.g., `1000`). Next, accept
# inputs consisting of either expenses (e.g., `-13.99`) or revenues (e.g., `20`)
# until the user introduces `exit`. After each input, in case the balance is
# about to go negative, print an error message (e.g., `Operation not permitted:
# insufficient funds.`). Otherwise, print the new balance value.

balance = float(input("Initial balance: "))

while True:
    action = input("Action: ")
    if action == 'exit':
        break
    action = float(action)
    if balance + action >= 0:
        balance += action
        print("New balance: {}".format(balance))
    else:
        print("Operation not permitted: insufficient funds.")
