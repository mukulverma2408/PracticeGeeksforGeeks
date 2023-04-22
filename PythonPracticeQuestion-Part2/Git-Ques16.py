#Define a class with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.

class generator():
    def num_gen(self, num):
        num = [x for x in range(0, int(num))]
        print(num)

obj = generator()
obj.num_gen(10)


