###############################################################################
###    HW0
###
###    Function definitions have been declared for you. Fill in the function
###    definitions with your solution.
###
###############################################################################

# Reverse String
#
# Given a string, print the reverse.
#
# Ex INPUT:
# "Hello World"
#
# Output:
# "dlroW olleH"
#
def reverse_string(my_str):
    # Your solution goes here
    return my_str[::-1]

# Odd Even
#
# Given a string, print "odd" if there are an odd number of characters and "even" if there are an even number of characters
#
# Ex INPUT:
# "Hello World"
#
# Ex OUTPUT:
# "odd"
#
def oddEven(my_str):
    if len(my_str) % 2==0:
        print "even"
    else:
        print "odd"

# Sign Flipper
#
# Input:
#   ary: An array of ints with arbitrary length
#
# Output:
#   Flip the signs of all the integers in the array and return that
#   resulting array.
#
# Example:
#   >>> sign_flipper([1, -2, 3])
#    [-1, 2, -3]
#
def sign_flipper(arr):
    return map(lambda x: x*-1, arr)

# Intersect Sum
#
# Input:
#   ary1: Array of ints with arbitrary length
#   ary2: Array of ints with arbitrary length
#
# Output:
#   Return the sum of integers that are in both the first array and the
#   second array. (Count each unique integer only once for the sum)
#
# Example:
#   >>> intersect_sum([1, 2, 3, 3, 4], [3, 4, 5, 6])
#    7
#
def intersect_sum(ary1, ary2):
    counted = set()
    inter_sum = 0
    for num in ary1:
        if not(num in counted):
            inter_sum += num
            counted.add(num)
    for num in ary2:
        if not(num in counted):
            inter_sum += num
            counted.add(num)
    return inter_sum
    # set1 = set(ary1)
    # set2 = set(ary2)
    # return sum(set1.intersection(set2))

# Given a Dictionary with the type of fruit as the key
# and the number of that type of fruit as its value, return the
# number of bananas as a String. Ex. "5 Bananas"
# We do not care about gramatical correctness. When there is 1 banana, please
# return '1 Bananas'.
# If bananas could not be found, return the String "No Bananas"
# Examples:
# >>> num_bananas({'apples': 4, 'bananas': 10, 'kiwis': 9})
# '10 Bananas'
# >>> num_bananas({'oranges': 10, 'apples': 2})
# 'No Bananas'
# >>> num_bananas({'bananas': 1, 'watermelons': 10})
# '1 Bananas'
#
def num_bananas(fruit_basket):
    return str(fruit_basket['bananas']) + " Bananas"

# Given a string, return whether it has repeating letters or not.
# If the word is repeating, return the max number or repeating letters.
# Otherwise, return 0.
# Examples:
# >>> repeating('potato')
# 2
# >>> repeating('abcdefgh')
# 0
# >>> repeating('aabbccddeeffff')
# 4
#
def repeating(str):
    letter_dict = {}
    repeating = False
    max_val = 0
    for char in str:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            cur_val = letter_dict[char]
            cur_val += 1
            letter_dict[char] = cur_val
            repeating = True
            if cur_val > max_val:
                max_val = cur_val
    if repeating:
        return max_val
    return 0

import sys
# Given an integer N, print a triangle that is height N.
#
# Ex INPUT:
# 4
#
# Ex OUTPUT:
#     *
#    **
#   ***
#  ****
#
def triangle(input):
    for row in xrange(input):
        sys.stdout.write(' '*(input - row - 1))
        sys.stdout.write('*'*(row + 1))
        sys.stdout.write('\n')


# Given an integer N, print the Fibonacci series up to its Nth term.
#
# Ex INPUT:
# 8
#
# Ex OUTPUT:
# 1,1,2,3,5,8,13,21
#
def fibonacci(input):
    first = 1
    second = 1
    if input <= 0:
        return 0
    if input == 1:
        return first
    if input == 2:
        return second
    for i in xrange(input - 3):
        cur = first + second
        first = second
        second = cur
    return first + second
    # if input == 1:
    #     return 1
    # if input == 2:
    #     return 1
    # return fibonacci(input-1) + fibonacci(input-2)


# Given a 2d array, flatten the array.
#
# Ex INPUT:
# [[1],[2,3],[4,5,6],[7,8,9,10]]
#
# Ex OUTPUT:
# [1,2,3,4,5,6,7,8,9,10]
#
def flatten(input):
    return [num for sub_arr in input for num in sub_arr]


# Given a 2d NxN matrix, traverse the structure in a spiral and return an array
# representing the traversed values in order.
#
# Ex INPUT:
# [[a,b,c,d,e],
#  [f,g,h,i,j],
#  [k,l,m,n,o],
#  [p,q,r,s,t],
#  [u,v,w,x,y]]
#
# Ex OUTPUT:
# [a,b,c,d,e,j,o,t,y,x,w,v,u,p,k,f,g,h,i,n,s,r,q,l,m]
def spiralMatrix(input):
    return [letter for sub_arr in [input[i][::(-1)**i] for i in xrange(len(input))] for letter in sub_arr]

"""
Given a string in a way formatted below, find the number of <name>'s
friend's friend who are not friends with <name>.

Format:
graph is given in a newline formatted string. The first word is a person's name,
and the following names are friends of that person.

Sample 1:
missing_friends('james', '''
                         james jack jill
                         jack jill james
                         jill jack james
                         ''')

This means that we need to find the number of James' friends' friends, that are
also not friends with James.

James is friends with Jack and Jill, and both Jack and Jill
have friends that are friends with James, that means we
should return 0. (James -> Jack -> Jill -> James and James -> Jill -> Jack -> James)

Sample 2:
missing_friends('james', '''
                         james jack
                         jack james jill bob
                         jill jack bob
                         bob jill jack
                         ''')
James is friends with Jack, and Jack is friends with Jill, Bob, and James. However,
Jill and Bob are not friends with James, so we return 2
(2 friends of friends that are not friends with James.)

Sample 3:
missing_friends('james', '''
                         james jack
                         jack james jill
                         jill jack
                         ''')

James is friends with Jack, who are friends with James and Jill. However,
Jill is not friends with James, so we return 1 (1 friends of friends that are not friends with James.)

"""
def missing_friends(name, graph):
    graph_arr = map(lambda x: x.split(str=' '), graph.split(str="\n"))
    friends_set = set([arr[1:] for arr in graph_arr if arr[0] == name])
    friends_of_friends = [arr[1:] for arr in graph_arr if arr[0] in friends_set]
    friends_of_friends_flat = [person for arr in friends_of_friends for person in arr if not(person in friends_set)]
    return len(set(friends_of_friends_flat))

# Test HW#0
# print reverse_string("")
# print reverse_string("hello")
# oddEven("Hello World")
# oddEven("Four")
# print sign_flipper([1,3,4,5,6])
# print intersect_sum([1, 2, 3, 3, 4], [3, 4, 5, 6])
# print num_bananas({'apples': 4, 'bananas': 10, 'kiwis': 9})
# print repeating('potato')
# print repeating('abcdefgh')
# print repeating('aabbccddeeffff')
# triangle(4)
# print fibonacci(8)
# print flatten([[1],[2,3],[4,5,6],[7,8,9,10]])
# spiral_arr = [['a','b','c','d','e'], ['f','g','h','i','j'], ['k','l','m','n','o'], ['p','q','r','s','t'], ['u','v','w','x','y']]
# print spiralMatrix(spiral_arr)