def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        print('True')
    else:
        print('False')


def divisible_by_ten(num):
    ans = (num % 10)
    if ans == 0:
        print(num, " is divisible by 10.")
    else:
        print(num, " is not divisible by 10.")


large_power(10, 2)
divisible_by_ten(23)
