"""

Questions:
1. What is howManyEven() doing? What is the output for howManyEven(9)?
    A. It turns (-) numbers to (+). Then it counts how many even numbers there are between the input number and 0 (inclusive)
        The output for howManyEven(9) is 5
2. What does isOdd(3) return? Why?
    A. This would return True, because 3 % 2 is 1, which is not 0, which would return True.
3. Recall the factorial code from the previous lab. Rewrite the corrected factorial code using our new -=, +=, *=, /= (etc) operators.
    A. See Below
4. How can we rewrite n = int(¾) using // to make the output look the same?
    A. n = 3 // 4
"""


# input: a number
# output: the number of even numbers between that number and 0 (including 0 and the number)
def howManyEven(num):
    count = 0
    if num < 0:
        num *= -1
    while (num >= 0):
        if isEven(num):
            count += 1
        num -= 1
    return count


# input: a number
# output: true/false depending on whether the number is even or not
def isEven(num):
    return num % 2 == 0


# input: a number
# output: true/false depending on whether the number is odd or not
def isOdd(num):
    return num % 2 != 0


def noChange(cents):
    # student code here
    if (cents % 100) == 0:
        print('Hoorah')
        return (cents // 100)
    else:
        print('Keep the Change!')
        return (cents // 100)


# input: num–an int of some kind
# output: the positive factorial of num
def oldFactorial(num):
    total = 1
    if num < 0:
        num = num * (-1)
    while (num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num = num - 1
    return total


def newFactorial(num):
    total = 1
    if num < 0:
        num *= -1
    while (num == num):
        if num <= 0:
            break
        else:
            total *= num
            num -= - 1
    return total

print("TESTING", noChange(100))
print("TESTING", noChange(225))

print("TESTING", noChange(700))
print("TESTING", noChange(599))

def main():
    print(howManyEven(4))
    print(howManyEven(9))
    print(isOdd(12))
    print(isEven(12))


if __name__ == "__main__":
    main()
