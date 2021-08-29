

from collections import deque
from sys import getsizeof


def greet():
    print("Hi there")
    print("Welcome Abroad!")


greet()


def greet(firstName, lastName):
    print(f"Hi {firstName} {lastName}")
    print("Welcome Abroad")


greet('Shaikat', 'Barua')
greet('Thor', 'Odinson')


def get_greet(name):
    return f"Hi {name}"


message = get_greet('Alpha')
file = open('content.txt', 'w')
file.write(message)


def increment(number, by):
    return number+by


print(increment(5, by=2))


def print_Function(number):
    for x in range(number):
        print(x+1)


print_Function(10)


def defaultArg(number, by=1):
    return number+by


incbyOne = defaultArg(5)
print(incbyOne)


def defaultArg(number, by=2):
    return number+by


incbyTwo = defaultArg(5)
print(incbyTwo)


def numbers(*n):
    return n


print(numbers(2, 3, 4, 5))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 5, 7, 10))


def save_user(**user):
    return user


shaikat = save_user(id=1, name="Shaikat", age=23)

print(shaikat)
print(shaikat['age'])
print(shaikat['id'])
print(shaikat['name'])


def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(addition(2, 3, 5, 8))


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


fizz_buzz(15)
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(7)


letters = ['a', 'b', 'c']
matrix = [[1, 2], [2, 3], [3, 4]]
zeros = [0]*5
combined = zeros + matrix

print(letters)
print(matrix)
print(combined)
print(zeros)


numbers = list(range(20))
char = list('Hello JavaScript')
print(numbers)
print(char)
print(len(numbers))
print(len(char))

numbers = list(range(5))
print(numbers)

for i in numbers:
    print(i+1)
print(numbers)

print(numbers)


for i in range(5):
    print(i+1)

letters = ['a', 'b,', 'c', 'd']
print(letters[0])
print(letters[-1])
print(letters[-4])
print(letters[0:3])
print(letters[0:])
print(letters[:3])
print(letters[:])
print(letters[::])
numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

numbers = [1, 2, 3]
first, second, third = numbers
print(first)
print(second)
print(third)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one, two, *other = numbers
print(one)
print(two)
print(other)

numbers = [1, 2, 2, 2, 4, 4, 4, 9]
first, *other, last = numbers
print(first)
print(last)
print(other)

letters = ['a', 'b', 'c', 'd']

for letter in enumerate(letters):
    print(letter[0], letter[1])

for index, letter in enumerate(letters):
    print(index, letter)


empty = []
for number in list(range(20)):
    empty.append(number+1)


print(empty)

letters = ['a', 'b', 'c', 'd']
letters.append("d")
letters.pop()
letters.insert(0, 'x')
letters.pop(0)
letters.remove('b')
del letters[0:2]
letters.clear()
print(letters)
letters = ['a', 'b', 'c', 'd']
print(letters.index("c"))

if "e" in letters:
    print(letters.index("e"))

print(letters.count("e"))


empty = []

for x in range(5):
    n = int(input())
    empty.append(n)
print(empty)

empty.sort(reverse=True)
print(empty)

maximum = empty[0]
for num in empty:
    if(num < empty[0]):
        maximum = num
        break
print(maximum)

numbers = [3, 5, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers = [3, 5, 2, 8, 6]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

if __name__ == '__main__':
    n = int(input())
    empty = []
    for x in range(n):
        num = int(input())
        empty.append(num)

    empty.sort(reverse=True)

    def runner(empty):
        maximum = empty[0]
        for x in empty:
            if(x < empty[0]):
                return x

    print(runner(empty))


items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

for index in items:
    print(index[0], index[1])
    print(index[1], index[0])


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


items.sort(key=lambda item: item[1])
print(items)

items = [
    ("Product1", 10), ("Product2", 9), ("Product3", 12)
]
price = []

for item, p_price in items:
    price.append(p_price)


print(price)

x = map(lambda item: item[1], items)

for item in x:
    print(item)


prices = list(map(lambda item: item[1], items))

print(prices)


x = filter(lambda item: item[1] >= 10, items)
print(x)
x = list(filter(lambda item: item[1] >= 10, items))
print(x)


prices1 = list(map(lambda item: item[0], items))
print(prices1)
prices1 = list(map(lambda item: item[1], items))
print(prices1)
prices2 = [item[1]for item in items]
print(prices2)


list1 = [1, 2, 3]
list2 = [10, 20, 30]

numbers = list(zip(list1, list2))
print(numbers)

alphabet_numbers = list(zip("abc", list1, list2))
print(alphabet_numbers)

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)


if not browsing_session:
    print("Fuck!")
browsing_session.pop()
browsing_session.pop()
browsing_session.pop()
if not browsing_session:
    print("Fuck!")


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

queue.popleft()
queue.popleft()
queue.popleft()

print(queue)


point = (1, 2)
print(type(point))

point1 = (1, 3)
point2 = (5, 7)
print(point1+point2)

print(point1*3)

arr = tuple([1, 2])
print(arr)
sentence = tuple("Hello World")
print(sentence)

point = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(point[2:6])
point = (1, 2, 3, 4)
x, y, *other = point
print(other)
if 10 in point:
    print("exists")
else:
    print("Doesn't")


point = (1, 2, 3, 4, 10)
x, y, *other = point
print(other)
if 10 in point:
    print("exists")
else:
    print("Doesn't")


numbers = [1, 1, 2, 2, 3, 4]
unique = set(numbers)
# print(unique)
second = {1, 5, 2, 7, 3}
second.add(9)
print("Second:", second)
unique.add(8)
print("Unique:", unique)

# union (|)
print(unique | second)

# intersection(&)
print(unique & second)

# unique - second(-)
print(unique - second)

# Either in Unique and Second but not both(^)
print(unique ^ second)


point = {"x": 1, "y": 2}
print(point)

point = dict(x=10, y=20)

print(point.get("a"))
print(point.get("x"))
del point["y"]
print(point)
point = dict(z=50, y=20, a=50, b=40, c=100)
point["x"] = 25
print(point)

for alphabets in point:
    print(alphabets)
for alphabets in point.items():
    print(alphabets)

for key, value in point.items():
    print(key, "=", value)


for key in point:
    print(key, point[key])


print(point.values())

values = {}
for x in range(5):
    values[x] = x*2

print(values)

values2 = {x: x*3 for x in range(5)}

print(values2)

values = (x*2 for x in range(500000))


values1 = [x*2 for x in range(500000)]


print(getsizeof(values))
print(getsizeof(values1))


numbers = [1, 2, 3]
print(*numbers)

values = list(range(9))
print(values)
values = [*range(9)]
print(values)
values = [*range(9), *"Hello"]
print(values)
first = [1, 2, 4]
second = [9, 16, 25]

values = [*first, "a", *second, *"hello!"]

print(values)
first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second, "z": 1}
print(combined)


sentence = "This is a common interview question"
newl = sentence.lower()
print(newl)
newLnoSpace = newl.replace(" ", "")
print(newLnoSpace)
newLnoSpaceSet = set(newLnoSpace)
print(newLnoSpaceSet)
for i in newLnoSpaceSet:
    print(newLnoSpace.count(i), " = ", i)
