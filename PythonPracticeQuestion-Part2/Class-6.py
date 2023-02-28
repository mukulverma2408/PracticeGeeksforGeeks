#How to Change a Dictionary Into a Class?

class Dict2class():
    def __init__(self, my_dict):

        for key in my_dict:
            setattr(self, key, my_dict[key])

if __name__ == "__main__":
    my_dict = {"Name": "Geeks",
               "Rank": "1223",
               "Subject": "Python"}

    result = Dict2class(my_dict)
    print(type(result))
