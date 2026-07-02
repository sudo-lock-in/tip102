def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))



def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])


# print(sum_stones([5, 10]))

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))



def count_suits_iterative(suits):
    count = 0
    for suit in set(suits):
        count += 1
    return count 

def count_suits_recursive(suits):
    seen = []
    def count(suits, seen):
        if not suits:
            return 0
        if suits[0] not in seen:
            seen.append(suits[0])
            return 1 + count(suits[1:], seen)
        else:
            return count(suits[1:], seen)
    return count(suits, seen)

# codepath's solution:
# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     first = suits[0]
#     rest_unique_count = count_suits_recursive(suits[1:])
#     if first in suits[1:]:
#         return rest_unique_count
#     else:
#         return 1 + rest_unique_count

# seen = []
# print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))







# Groot grows according to a pattern similar to the Fibonacci sequence.
# Given n, find the height of Groot after n months using a recursive method.

# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

# print(fibonacci_growth(5))
# print(fibonacci_growth(8))



# The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the result of 4 raised to the nth power to determine their training level.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

#case n > 0
#case n < 0


# derek's code: 
def power_of_four(n):
    if n == 0:
        return 1
    if n > 0:
        return power_of_four(n - 1) * 4
    if n < 0:
        return power_of_four(n + 1) / 4
# Example Usage:

# print(power_of_four(2))
# print(power_of_four(-2))
# Example Output:

# 16
# Example 1 Explanation: 4 to the 2nd power (4 * 4) is 16. 
# .0625
# Example 2 Explanation: 4 to the power of -2 is 1/(4 * 4), which is 0.0625.


# bradshaw solved this without slicing so i wanted to try something like that
# for space complexity
def strongest_avenger(strengths):
    length = len(strengths)
    index = 0
    maxi = strengths[index]
    def find_max(strengths, length, index, maxi):
        if index == length:
            return maxi
        if strengths[index] > maxi:
            maxi = strengths[index]
        return find_max(strengths, length, index + 1, maxi)
    return find_max(strengths, length, index, maxi)
# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))

# problem set 2

def get_village_class_iterative(population):
    return len(str(population))

def get_village_class_recursive(population):
    if not population:
        return 0
    return 1 + get_village_class_recursive(str(population)[1:])

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))