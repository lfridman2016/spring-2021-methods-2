# This is a python library that we will use to generate random numbers
import random

#==================================================
# Problem 0

# random.randrange( limit ) is a python function that returns a
# random integer in the range [0, limit)

# Write a function that will create and return a list of size n that
# is filled with random integers in the range [0, limit)

def rand_list(n, limit):
    g = []
    i = 0
    while i < n:
        g.append(random.randrange(limit))
        i+=1     
    return g

# When printed, a and b should have different values.
print(('=' * 10) + "Problem 0" + ('=' * 10))
a = rand_list(10, 10)
b = rand_list(10, 10)
print(len(a), a)
print(len(b), b)

# End Problem 0
#==================================================


#==================================================
# Problem 1
# Write a function that takes a list of non-negative integer
# values and returns a string of a bar graph representation of the list.
# The length of each bar should be the same as the value at that index.
# That means if g[0] = 9, then the first bar should have a length of 9.

def bar_graph(g):
    s = ''
    i = 0
    for e in g:
        s+= str(i) + ': '
        s+= '=' * e + '\n'
        i+= 1
    return s

# The code below should have this output:
# 0: =========
# 1: =====
# 2: =====
# 3: ===
# 4: =
# 5: =====
# 6: =========
# 7: =====
# 8: =======
# 9: ========
print(('=' * 10) + "Problem 1" + ('=' * 10))
test = [9, 5, 5, 3, 1, 5, 9, 5, 7, 8]
print(bar_graph(test))

# This should print out the bar graph for your random
# lists from Problem 0
print(bar_graph(a))
print(bar_graph(b))

# End Problem 1
#==================================================


#==================================================
# Problem 2

# Write a function that returns the average of the
# values in a list. You may assume that the argument
# provided is a list that only contains numbers.

def list_avg( g ):
    avg = 0
    for e in g:
        avg+= e
    avg = avg/len(g)
    return avg

print(('=' * 10) + "Problem 2" + ('=' * 10))
# This should print 5.7
print( list_avg(test) )

# This should print out the averages of your random
# lists from Problem 0
print( list_avg(a) )
print( list_avg(b) )

# End problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that returns the number of times
# the value n appears in list g.

def count(n, g):
    c = 0
    for e in g:
        if n == e:
            c+= 1
    return c

print(('=' * 10) + "Problem 3" + ('=' * 10))
# This should print 4
print( count(5, test) )

# End Problem 3
#==================================================


#==================================================
# Problem 4

# Write a function that returns the mode (most frequently
# appearing value) of a given list.
# It should only return a single value, even if there are
# multiple modes, just return one of them.


def find_mode(g):
    guess = 0
    guess_count = 0
    for e in g:
        c = count(e, g)
        if c > guess_count:
            guess = e
            guess_count = c
    return guess

print(('=' * 10) + "Problem 4" + ('=' * 10))
# Should print 5
print( find_mode(test) )

print( find_mode(a) )
print( find_mode(b) )

#==================================================
# Problem 5

# Write a function that keeps track of the frequencies of values
# from a list containing only integers.
# For example, if the provided list only contained 0s and 1s,
# and there were 8 0s and 23 1s, then the fucntion should
# return this list: [8, 23]
# It is important to understand that each index in the new
# list represents a value from the parameter list. So the new
# list needs to be as large as the biggest value in the parameter.
def list_counts(g, max_value):
    #This will create a new list with a size of max_value filled with 0s
    counts = [0] * max_value
    i = 0
    while i < len(counts):
        c = count(i, g)
        counts[i] = c
        i+= 1
    return counts

print(('=' * 10) + "Problem 5" + ('=' * 10))
# Should print
# [0, 1, 0, 1, 0, 4, 0, 1, 1, 2]
test_counts = list_counts( test, 10 )
print( test_counts )

print( list_counts(a, 10) )
print( list_counts(b, 10) )

# create a new list of 10 random values in the range [0, 5)
# print that list
# YOUR CODE HERE
c = rand_list(10, 5)
print(c)

# create a list that correctly counts all the values in
# the new list you just made.
# print that list
# YOUR CODE HERE
c_counts = list_counts(c, 5)
print(c_counts)
# End Problem 5
#==================================================

#==================================================
# Problem 6
# If you use bar_graph on a list with sufficiently large
# values, you'll have a problem with the bars taking up
# more than one line.

# Write a new bar_graph function that will draw a scaled bar
# graph. It should take an argument for the scale factor,
# such that 1 piece of a bar represents 1 quantity equal
# to the scale factor.

def bar_graph_scaled(g, scale_factor):
    s = ''
    i = 0
    for e in g:
        s+= str(i) + ': '
        s+= '=' * (e // scale_factor)
        s+= '\n'
        i+= 1
    return s

print(('=' * 10) + "Problem 6" + ('=' * 10))
# Should print:
# 0: =====
# 1: ======
# 2: =
scale_test = [500, 670, 125]
print(bar_graph_scaled(scale_test, 100))

# now let's try it on a list with very large values
big_list = rand_list(10, 1000)
print( bar_graph_scaled(big_list, 25))

# End Problem 6
#==================================================


#==================================================
# Problem 7

# random.randrange() distributes numbers evenly, meaning
# that every possible random value has an equal chance
# of being returned.

# How could you test how evenly random.randrange()
# distributes the results?
# print out your answer as a string
print(('=' * 10) + "Problem 7" + ('=' * 10))
answer = 'Make a large lists with a limited range of values, like 1000 elements in the range [0,10). Then, generate the counts of all the values, the counts should be close to equal.'
print(answer)
# Write code below that performs the test you described.
# YOUR ANSWER BELOW
big_list = rand_list(10000, 10)
big_counts = list_counts(big_list, 10)
print(big_counts)
print( bar_graph_scaled(big_counts, 25))



# End Problem 7
#==================================================

