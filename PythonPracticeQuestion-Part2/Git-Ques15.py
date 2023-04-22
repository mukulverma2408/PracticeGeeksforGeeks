#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
#D 100
#W 200

def UserInput():
    trans = []
    while True:
        ip = input("Enter the transactions or just press enter if no new transacation ")
        if not ip:
            break
        op, amt = ip.split(" ")
        if op == 'D':
            trans.append(int(amt))
        elif op == 'W':
            trans.append(int(amt)*-1)
    print(trans)
    print("The final a mount in account is {0} ".format(sum(trans)))

UserInput()