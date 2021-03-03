def fibonacci(n):
    result = [0, 1]
    n1, n2 = 0, 1
    while n + 1 > len(result):
        n1, n2 = n2, n1 + n2
        result.append(n2)

    return result

print(fibonacci(10))

#Task
#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    even_num = []
    odd_num = []
    for num in integers:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    return int(* even_num if len(even_num) < len(odd_num) else odd_num)

print(find_outlier(([160, 3, 1719, 19, 11, 13, -21,1719,3,11,13,7,23])))

#Task
#Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
# which leads to [1,2,3,1,2,3].

def delete_nth(order,max_e):
    result = []
    for num in order:
        if result.count(num) < max_e:
            result.append(num)
    return result

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))


#Task
# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.
#
# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?
#
# Example:
# With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].
#
# The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.
#
# The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].
#
# The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language.
#
# With C++, C, Rust, Swift, Go, Kotlin, Dart return -1.
#
# Examples:
# ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163
#
# xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)
#
# ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

import random as r
def choose_best_sum(t, k, ls):
    while True:
        num_list = []
        rand_num = r.sample(range(0,len(ls)),k)
        for km in range(k):
            num_list.append(ls[rand_num[km]])
        if sum(num_list) == t:
            result = num_list
            break

    return result

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs))


import itertools

def choose_best_sum(t,k,ls):
    routes = list(itertools.combinations(ls,k))
    sum_km = [sum(km) for km in routes]
    sum_km2 = [km for km in sum_km if km <= t]
    if sum_km2 == []:
        return None
    else:
        return max(sum_km2)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430, 8, xs))