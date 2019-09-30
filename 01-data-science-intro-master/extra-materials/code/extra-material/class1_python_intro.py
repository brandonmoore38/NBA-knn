### PYTHON OBJECT MODEL


# ASSIGNMENT

x = "python"               # Create an object
y = x                      # Assign a new name to the string object "python"                     
id(x)                      # X and Y both point to the same object
id(y)

# x is the name assigned to an str object with a value of "python"
# that is why we get a NameError for a misspelled name.
X                           #NameError: name 'X' is not defined



# BASIC DATA TYPES

type(x)             # check the type: str (not declared explicitly)
type(5.0)           # float
type('five')        # int
type(True)          # bool

# Why does type matter - it defines behavior
2 + 2               # int are added together
'python' + 'class'  # strings are concatenated
'2' + 2             # TypeError: cannot concatenate 'str' and 'int' objects
2 + '2'             # TypeError: unsupported operand type(s) for +: 'int' and 'str'

tweet = "my shampoo and conditioner never run out at the \
         same time #firstworldproblems"

#Use http://pythontutor.com/visualize.html#mode=edit to see function step by step
def remove_hashtag(input_tweet):
    """return a tweet without its hashtag"""
    new_tweet = input_tweet.split('#')
    return new_tweet[0]

remove_hashtag(tweet)
remove_hashtag(52)      #AttributeError: type int does not have split attribute



# ATTRIBUTES AND BUILT-IN FUNCTIONS

#What does it mean to be a string?
word = "python"

word.capitalize()       # Return a copy of the string with only its first character capitalized
capitalize(word)        # NameError
len(word)               # Return the number of items of a sequence or collection
word.len()              # AttributeError
#capitalize is a string attribute; len in a built-in function


#create a capitalize function
def capitalize(input_word):
    return input_word.capitalize()

capitalize(word)        # Now capitalize works as both a method and function

dir()                   # Return the list of names in the current local scope
del capitalize          # Delete the function capitalize
dir()                   # Function capitalize is no longer in the local scope

dir(word)               # Return a list of valid attributes for the object
dir(str)
help(str.capitalize)    # str.capitalize Docstring and Type

word_with_spaces = '   python   '   # create a word with excess spaces
word_with_spaces == word            # False
# we can use dir(str) to find string operations - strip removes excess spaces
word_with_spaces.strip() == word    # True

# What does it mean to be an int
num1 = 1                
type(num1)              # type: int
num1 + 2

dir(num1)               # Return a list of int attributes
x.__add__(4)            # add two ints using a magic method
?int.__add__            # x.__add__(y) <==> x+y

import this             # The Zen of Python



# MUTABILITY & IMMUTABILITY

num1 = 1
num2 = num1         # num1 & num2 are names for the same object
id(num1)            # with matching ids
id(num2)

num2 = 3            # num2 points to a different object because ints are immuatable    
num1                # num1 still refers to 1 


nums1 = [1, 2, 3]
nums2 = nums1       # nums1 and nums2 are names for the same list object
nums2.append(4)     # nums2 changes the original object because lists are mutable
nums1               # the nums1 list also changed 

# Type defines if an object is mutable
nums_list = [1, 2, 3]
first_num = nums_list[0]
type(nums_list)
type(first_num)

for num in nums_list:
    num *= 10
    print num
print nums



# ITERATION

my_list = ['a', 'b', 'c', 'd']
# index:    0    1    2    3

i = 0
while i < len(my_list):
    v = my_list[i]
    print v
    i += 1

# or over python range
for i in range(len(my_list)):
    v = my_list[i]
    print v


# pythonic code
for i in my_list:
    print i


my_list = ['c', None, 'o', 'd', 'e']
# index     0    1     2    3    4

for letter in my_list:                  # iterator can take any name
    if letter == 'c':
        print 'entered condition'
    print letter


for letter in my_list:                  
    if letter == 'c':
        break                           # break ends the entire for loop
    print letter


for letter in my_list:                  # iterator can take any name
    if letter == 'c':
        continue                        # continue ends the current iteration
    print letter


# pythonic with index  
for ind, val in enumerate(my_list):     # provides both the index and value      
    print ind, val
    


# TUPLE UNPACKING
tuple_list = [(1,2,3), (4,5,6)]
for a, b, c in tuple_list:
    print a, b, c


# ZIP
names = ["Eiffel Tower", "Empire State Building", "Sears Tower"]
heights = [324, 381, 442]

for name, height in zip(names, heights):
    print name, height


# FORMATTING
for name, height in zip(names, heights):
    print "The {0} is {1} meters".format(name, height)

# format allows you to use repeat the same item  and takes functions as arguments  
"{0}: The {0} is {1} meters and is a {2}.".format(names[0], heights[0], names[0].split()[0])

# Not Pythonic
for name, height in zip(names, heights):
    print "The " + name + " is " + str(height)


# CASTING


# FUNCTIONS

# Function scope
building = "Eiffel Tower"
print dir()                         # view the global scope

def get_building_type(building):
    print building                  # print passed in parameter
    building  = 'a'                 # rename building in function scope
    print building                  # print altered parameter
    print dir()                     # view the local scope
    
get_building_type(building)
building                            # global scope remains unchanged
                                    # because assignment never copies data and
                                    # strings are immutable


building_list = ["Eiffel Tower", "Empire State Building", "Sears Tower"]

def alter_building_list(b_list):
    b_list.append("Burj Khalifa")   # add item to building list
    print b_list                    # print local list
     
alter_building_list(building_list)
building_list                       # print global list, which also has the 
                                    # new item because list are mutable



# Function arguments
def get_distance(rate, time):       # standard function
    return rate * time
    
get_distance(10, 60)                # positional arguments
get_distance(rate=10, time=60)      # named arguments
get_distance(time=60, rate=10)      # names allow you to change argument position


def get_distance(rate, time=60):    # default argument
    return rate * time

get_distance(10, 60)                # call function as usual
get_distance(10)                    # call function without named argument


def get_distance(rate=10, time):    # SyntaxError
    return rate * time              # non-default arg follows default arg


def get_distance(rate, time *args): # variable length arguments
    for pit_stop in args:
        print pit_stop
        time -= pit_stop            # do not include time for pit stops
    return rate * time

get_distance(10, 60, 5, 10)         # cannot use named arguments



def get_distance(rate, time, **kwargs): # varialbe length named arguments
    for pit_stop in kwargs:
        print pit_stop
        print kwargs[pit_stop]
        time -= kwargs[pit_stop]
    return rate * time

get_distance(rate=10,
             time=60,
             pit_stop1=5,
             pit_stop2=10)          # call function with names
