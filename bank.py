
balance = 0
def deposit(amount):
    global balance
    balance+=amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance-=amount
    else:
        print("No sufficient funds available")

def get_balance():
    return balance

"""
Problems with the above approach
1. uses global state
2. only supports one user and impossible to scales
3. no separation of concersn
4. no security
5. easy to break accidentally
6. cannot model real banking behaviour
"""