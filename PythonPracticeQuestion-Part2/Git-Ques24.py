#Write a function to compute 5/0 and use try/except to catch the exceptions.

def RaiseException():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("Denominator is zero, not a valid operation")
    finally:
        print("In finally block for  cleanup")

RaiseException()