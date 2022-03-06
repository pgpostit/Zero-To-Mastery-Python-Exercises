#Use the generator to make a fibonacci function
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b += temp

while True:
    try:
        n = int(input('Tell the fibonacci generator range: '))
        break
    except:
        print('Try a number')


for x in fib(n):
    print(x)