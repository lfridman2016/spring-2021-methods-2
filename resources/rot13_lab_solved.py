#==================================================
# Problem 0

# Write a function, encode_table(), that should print out
# each letter from a-z, along with its UTF-8 value, use one line per character.
# Each line should look like this:
#     a: 97
# The function does not need to return anything.

def encode_table():
    i = ord('a')
    while i <= ord('z'):
        print(chr(i) + ': ' + str(i))
        i+= 1

print(('=' * 10) + "Problem 0" + ('=' * 10))
encode_table()
# End Problem 0
#==================================================

#==================================================
# Problem 1

# There is a cipher (https://en.wikipedia.org/wiki/Cipher) called rot13
# The following shows how to "encrypt" something in rot13:

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# n o p q r s t u v w x y z a b c d e f g h i j k l m

# 'hello' in rot13 becomes 'uryyb'

# Look at the Unicode values from encode_table()
# what can you tell about a letter and its rot13 equivalent?
# print your answer as a string below

print(('=' * 10) + "Problem 1" + ('=' * 10))
answer = ''
print(answer)


# End Problem 1
#==================================================

#==================================================
# Problem 2

# Write a function that takes a single character string
# as a parameter and returns its rot13 equivalent.
# If the character is not a lower case letter,
# return the original character.
# for example rot13char("b") would return "o"

def rot13char(c):
    if c >= 'a' and c <= 'z':
        utfc = ord(c) - ord('a')
        utfc+= 13
        utfc%= 26
        utfc+= ord('a')
        c = chr(utfc)
    return c

print(('=' * 10) + "Problem 2" + ('=' * 10))
print( 'b: ' + rot13char('b') )
print( 'q: ' + rot13char('q') )
print( '?: ' + rot13char('?') )

# End Problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that prints out all the characters
# from 'a' to 'z' along with their rot13 equivalents.
# Like problem 0, each letter should be on its own line.
# A line of this string might look like:
#       h -> u

def rot13_table():
    c = 'a'
    while c <= 'z':
        print(c + ' -> ' + rot13char(c))
        c = chr(ord(c) + 1)


print(('=' * 10) + "Problem 3" + ('=' * 10))
rot13_table()

# End Problem 3
#==================================================

#==================================================
# Problem 4
# Write a function that will take a string consisting of
# lowercase letters only and will return its rot13 equivalent.

# For example, rot13("skywalker") would return "fxljnyxre"

def rot13(s):
    news = ''
    i = 0
    while i < len(s):
        news+= rot13char(s[i])
        i+= 1
    return news

print(('=' * 10) + "Problem 4" + ('=' * 10))
tester = 'skywalker'
rotted = rot13(tester)
print( tester + ' -> ' + rotted )

# What happens when you call rot13 on a string that was created by rot13?
# print your answer as a string below
answer = 'Running rot13 twice results in the original string.'
print(answer)

# End Problem 4
#==================================================

#==================================================
# Problem 5

# Go back to problem 2, modify the function such
# that it now works with both upper and lower case letters.

def rot13char_anycase(c):
    offset = 0
    if c >= 'a' and c <= 'z':
        offset = ord('a')
    elif c >= 'A' and c <= 'Z':
        offset = ord('A')
    else:
        return c    
    utfc = ord(c) - offset
    utfc+= 13
    utfc%= 26
    utfc+= offset
    return chr(utfc)



# Test your function here
print(('=' * 10) + "Problem 5" + ('=' * 10))
print( 'b: ' + rot13char_anycase('b') )
print( 'q: ' + rot13char_anycase('q') )
print( 'B: ' + rot13char_anycase('B') )
print( 'Q: ' + rot13char_anycase('Q') )
print( '?: ' + rot13char_anycase('?') )


# End Problem 5
#==================================================

#==================================================
# Problem 6

# Go back to problem 4, modify the function such
# that it can take a string with any characters in it,
# but will only modify letters, leaving spaces, numbers
# and punctuation unchanged.
#
# Hint: If you've gotten to this point, most of the
# work has already been done.

def rot13_full(s):
    news = ''
    i = 0
    while i < len(s):
        news+= rot13char_anycase(s[i])
        i+= 1
    return news

# Test your function here
print(('=' * 10) + "Problem 6" + ('=' * 10))
tester = 'Red 5 standing by!'
rotted = rot13_full(tester)
print( tester + ' -> ' + rotted )
print( rotted + ' -> ' + rot13_full(rotted) )
# End Problem 6
#==================================================
