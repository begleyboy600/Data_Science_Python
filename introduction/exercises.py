print("-- PART 1 --")
# PART 1
print("-- Q1 --")
# Q1
x = 5
y = 10
z = y - x
print(z)

print("-- Q2 --")
# Q2
x = 5
y = 3
z = y * x
print(z)

print("-- Q3 --")
# Q3
x = 30
y = 4
z = x / y
print(z)

print("-- Q4 --")
# Q4
x = 30
y = 4
z = x // y
print(z)

print("-- Q5 --")
# Q5
x = 18
y = 12
z = 18 % 12
print(z)

print("-- Q6 --")
# Q6
x = 0
for x in range(10, 21):
    print("x = ", x)

print("-- Q7 --")
# Q7
x = 0
for x in range(10, 51):
    if x % 3 == 0:
        print("x = ", x)

print("-- PART 2 --")
# PART 2
print("-- Q1 --")
# Q1
num = 5
def fun1(num):
    return 5 ** 2


z = fun1(num)
print(z)

print("-- Q2 --")
# Q2
num = 3
num2 = 7

def add_2_then_multiply(num, num2):
    x = num + num2
    return x * 2


z = add_2_then_multiply(num, num2)
print(z)

print("-- PART 3 --")
# PART 3
print("-- Q1 --")
# Q1
numbers_list = [3, 7, 8, 9]
print(numbers_list)

print("-- Q2 --")
# Q2
print("method 1: ")
numbers_list.extend([10])
print(numbers_list)

print("method 2: ")
# numbers_list = numbers_list + [10]
# print(numbers_list)

print("method 3: ")
# numbers_list.append(10)
# print(numbers_list)

print("-- Q3 --")
# Q3
new_number_list = numbers_list.copy()
print(new_number_list)

print("-- Q5 --")
# Q5
number_list_with_plus_ten = [i + 10 for i in new_number_list]
print(number_list_with_plus_ten)

print("-- Q6 --")
# Q6
multilist = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [13, 14, 15, 16, 17]]
print(multilist)

print("-- PART 4 --")
# PART 4
print("-- Q1 --")
# Q1
countries = {"Ireland": 5123536, "France": 67390000, "Italy": 59550000, "Romania": 19290000, "England": 55980000}
print(countries)

print("-- Q2 --")
# Q2
countries["Spain"] = 47350000
print(countries)

print("-- Q3 --")
# Q3
country = "Romania"
try:
    def get_population(country):
        population_get = countries.get(country)
        return population_get

    population = get_population(country)
    print(population)

except KeyError:
    print(country, "is an invalid key, please try a different key")






