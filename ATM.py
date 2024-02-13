#CASH DISPENSER APP (ATM)

BeratAccount={
    "name" : "Berat Yetis",
    "accountNumber":"32132123",
    "balance" : 3000,
    "additionalBalance": 2000
}

AliAccount={
    "name" : "Ali Veli",
    "accountNumber":"32155568",
    "balance" : 2000,
    "additionalBalance": 1000
}

def withdrawal(account,amount):
    print(f"Hello {account['name']}")
    
    if (account['balance'] >= amount):
        account['balance'] -= amount
        print("You can get your money...")
        checkBalance(account)
    else:
        total = account['balance'] + account['additionalBalance']    
        
        if total >= amount:
            additional = input("Do you want to use your additional balance (y/n) ?")
            
            if additional == 'y':
                additionalBalanceUsage = amount-account['balance']
                account['balance'] = 0
                account['additionalBalance'] -= additionalBalanceUsage
                print("You can get your money...")
                checkBalance(account)
            else:
                print(f"There is a balance of {account['balance']} in your account number {account['accountNumber']}. ") 
        else:
            print("Insufficient funds!!!")
            checkBalance(account)           


def checkBalance(account):
    print(f"There are {account['balance']}$ in your account number {account['accountNumber']}. Also Your additional balance is {account['additionalBalance']}$ ")



withdrawal(BeratAccount,3000)
print("-------------------------------------------------------------------------------------------")
withdrawal(BeratAccount,2000)
