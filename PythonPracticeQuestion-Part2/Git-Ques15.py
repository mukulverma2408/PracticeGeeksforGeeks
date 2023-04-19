#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
#D 100
#W 200

def UserInput():
    trans = {}
    while True:
        ip = input("Enter the transactions or just press enter if no new transacation")
        if not ip:
            break
        val = ip.split(" ")
        trans[val[0]] = int(val[1])
    print(trans)

UserInput()