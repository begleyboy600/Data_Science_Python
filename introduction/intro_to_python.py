# Basic Calculations
x = 10
y = 3
z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)
z = x // y
print(z)
z = x % y
print(z)
z = pow(x, 3)
print(z)
z = 10 ** 4
print(z)

###Ranges
x = range(10)  # 0,1,2 …, 9
print(x)
x = range(2, 10, 3)  # 2, 5, 8
print(x)

###Selection - If Statement
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
print(message)

if z > 1000:
    print("yippee")

# Loops
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")

for x in range(10, 20, 2):
    if x % 3 == 0:
        print(x)

for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break  # quit the loop entirely
    print(x)

# Lists
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)  # equals 3
list_length2 = len(list_of_lists)  # equals 3

list_sum = sum(integer_list)  # equals 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]  # equals 0, lists are 0-indexed
one = x[1]  # equals 1
nine = x[-1]  # equals 9, 'Pythonic' for last element
eight = x[-2]  # equals 8, 'Pythonic' for next-to-last element

x[0] = -1  # now x is [-1, 1, 2, 3, ..., 9]

print(list_of_lists[1][1])

first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]
print(x)
y = x
print(y)
y[0] = -10
print(y)
print(x)

x = [1, 2, 3]
x.extend([4, 5, 6])  # x is now [1, 2, 3, 4, 5, 6]
x = [1, 2, 3]
y = x + [4, 5, 6]  # y is [1, 2, 3, 4, 5, 6]; x is unchanged

z = [i * 2 for i in y]
z = [i * 2 for i in y if i > 3]

# Tuples
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3  # my_list is now [1, 3]

print(my_tuple[0])


# my_tuple[0]=10 #immutable


# Functions
def func1(x, y):
    return x * y, x / y


z, t = func1(10, 3)


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)  # sp is (5, 6)
s, p = sum_and_product(5, 10)  # s is 15, p is 50

# Functions on list
z = [1, 2, 3, 4]


def addList(listIn):
    total = 0
    for val in listIn:
        total += val
    return total


print(addList(z))

# Dictionaries
details = {"firstName": "Kev", "surname": "McDaid"}

print(details["surname"])

for (k, v) in details.items():
    print(k)
    print(v)

tweet = {"user": "joelgrus", "text": "Data Science is Awesome",
         "retweet_count": 100, "hashtags": ["#data", "#science",
                                            "#datascience", "#awesome", "#yolo"]}

print(tweet["hashtags"][1])

from collections import defaultdict

grades = defaultdict(int)  # int() produces 0
print(grades["Kevin"])







