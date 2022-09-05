def fizzBuzz(n: int):
    re = []
    for i in range(n):
        re.append(str(i + 1))
        three = (i + 1) % 3
        five = (i + 1) % 5
        if not three and not five:
            re[i] = 'FizzBuzz'
        elif not three:
            re[i] = 'Fizz'
        elif not five:
            re[i] = 'Buzz'
    return re


if __name__ == "__main__":
    n = 30
    result = fizzBuzz(n)
    print(result)