print("enter amount: ")
amount=int(input())
if (amount <= 1000):
    net_amount=amount*95/100
    print(net_amount)
elif(amount in range(4000-5001)):
    net_amount=amount*10/100
    print(net_amount)
        
