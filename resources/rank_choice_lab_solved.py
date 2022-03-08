from matplotlib import pyplot as plt
from pprint import pprint


# This will read in the necessary data
# make sure avengers.csv is in the same directory
# as this python file.
# You can get the file here: https://raw.githubusercontent.com/mks22-dw/python/main/avengers.csv

# avengers.csv represents the results of ranked choice voting
# on who should be the leader of the Avengers.

# Each line in the file represents a single ballot.
# The names in each line represent the ranked choices
# separated by commas.
# The first name listed is the top choice, second name, second
# choice, etc.

text = open('avengers.csv').read().strip()
print(text)



#==================================================
print(('=' * 10) + "Problem 0" + ('=' * 10))

# See above for a description of that data that should be
# in text.
# Write a function that will take a string of csv data and
# return a list of lists.
# Each sublist should represent a single line, with the
# values separated by commas.

# For example, the first two elements in this list given
# the avengers data should be:
#    [['Captain America', 'Falcon', 'Black Widow', 'Iron Man', 'Thor'],
#     ['Black Widow', 'Thor', 'Falcon', 'Captain America', 'Iron Man'],

def make_lists(s):
    data = []
    lines = s.split('\n')
    lines.pop(0)
    for line in lines:
        data.append(line.split(','))
    return data

choices = make_lists(text)
# only printing out the first 5 to keep from overloading
# the Thonny shell with data.
pprint(choices[:5])

#==================================================
print(('=' * 10) + "Problem 1" + ('=' * 10))

# In order to do ranked choice voting, we
# need to count votes for candidates, focusing on
# the specific rank in a given ballot.

# This function should take a list of lists, like
# what make_lists returns as input.

# It should create and return a dictionary where the
# keys are the names on the ballots, and the values
# are the number of people that voted for that name
# in the given rank.

# Assume that rank 0 means top choice, rank 1 means second, etc

def isolate_choice(data, rank):
    single_choice = {}
    for entry in data:
        if entry == []:
            continue
        choice = entry[rank]
        if choice in single_choice:
            single_choice[choice]+= 1
        else:
            single_choice[choice] = 1
    return single_choice

choice0 = isolate_choice(choices, 0)
# This should print:
# {'Black Widow': 35,
#  'Captain America': 14,
#  'Falcon': 25,
#  'Iron Man': 9,
#  'Thor': 17}
pprint(choice0)

# find and print the choices for the last rank
choice4 = isolate_choice(choices, 4)
pprint(choice4)
    
#==================================================
print(('=' * 10) + "Problem 2" + ('=' * 10))

# We can create bar graphs to look at the voting data.

# This function should take a dictionary like the one returned
# in problem 1, and generate a bar graph where the x axis constains
# the names of the candidates, and the y axis is their vote count.

# Use the second parameter as the title for the graph
def choice_bar(choice_data, title):
    values = list(choice_data.values())
    labels = list(choice_data.keys())
    plt.bar(labels, values)
    plt.title(title)
    plt.show()

choice_bar(choice0, "top choices")
choice_bar(choice4, "bottom choices")


#==================================================
print(('=' * 10) + "Problem 3" + ('=' * 10))

# In ranked choice voting, percentages are important.
# We can make pie charts to visualize this.

# This function should take a dictionary like the one returned
# in problem 1, and generate a pie chart where each wedge
# represents a specific candidate. The wedges should contain
# the vote percentage.

# For information on pie charts, go here: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

def choice_pie(choice_data, title):
    values = list(choice_data.values())
    labels = list(choice_data.keys())
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title(title)
    plt.show()

choice_pie(choice0, "top choices")


#==================================================
print(('=' * 10) + "Problem 4" + ('=' * 10))

# Charts are helpful, but to automate ranked choice voting
# we need to calculate the percentages ourselves.

# This function should take a dictionary like the one returned
# in problem 1 and modify it so the values are no longer vote counts,
# but percentages of the total vote

def add_pcts(choice_data):
    values = list(choice_data.values())
    total = sum(values)
    
    for option in choice_data:
        value = choice_data[option]
        choice_data[option] = value/total*100

add_pcts(choice0)
# This should print:
# {'Black Widow': 35.0,
#  'Captain America': 14.000000000000002,
#  'Falcon': 25.0,
#  'Iron Man': 9.0,
#  'Thor': 17.0}
pprint(choice0)


#==================================================
print(('=' * 10) + "Problem 5" + ('=' * 10))

# When voting, we need to know who got the most votes.

# This function should take a dictionary like one that
# has been modified by add_pcts, and return a dictionary
# with keys 'name', and 'pct', containing the name and
# perect vote of the top candidate.
def get_top_choice(choice_data):
    top = {'name':'', 'pct': 0}
    for choice in choice_data:
        pct = choice_data[choice]
        if pct > top['pct']:
            top['name'] = choice
            top['pct'] = pct
    return top

top_choice = get_top_choice(choice0)
# should print:
# winner: {'name': 'Black Widow', 'pct': 35.0}
print("winner:", top_choice)

# For ranked choice voting, it is also important to find
# the candidate with the fewest votes.

# This function should take a dictionary like one that
# has been modified by add_pcts, and return a dictionary
# with keys 'name', and 'pct', containing the name and
# perect vote of the bottom candidate.
def get_bottom_choice(choice_data):
    bottom = {'name':'', 'pct': 100}
    for choice in choice_data:
        pct = choice_data[choice]
        if pct < bottom['pct']:
            bottom['name'] = choice
            bottom['pct'] = pct
    return bottom

bottom_choice = get_bottom_choice(choice0)
# should print:
# last place: {'name': 'Iron Man', 'pct': 9.0}
print('last place:', bottom_choice)


#==================================================
print(('=' * 10) + "Problem 6" + ('=' * 10))

# In ranked choice voting, we need to be able to
# remove all votes for the last place candidate.

# This function should create a new list that is
# almost identical to the one generated by make_lists
# (problem 0), except it will not contain any values
# equal to the option parameter.

# For example, if Iron Man were given as option, then
# this function would create a new ballot list of
# lists, without any votes for Iron Man, but leaving
# everything else, and not changing the order.
def remove_option(data, option):
    new_data = []
    for ballot in data:
        new_ballot = []
        for choice in ballot:
            if choice != option:
                new_ballot.append(choice)
        new_data.append(new_ballot)
    return new_data

choices = remove_option(choices, bottom_choice['name'])
# The printed list should not contain Iron Man
pprint(choices[:5])

#==================================================
print(('=' * 10) + "Problem 7" + ('=' * 10))

# In problem 6, we removed Iron Man, let's see
# how things changes.

# First, recalcualte the the top choice votes.
choice0 = isolate_choice(choices, 0)
pprint(choice0)

# Now display a bar and pie graphs of the new results.
choice_bar(choice0, "top choices")
choice_pie(choice0, "top choice")

# Calculate predentages for the new results
add_pcts(choice0)
pprint(choice0)

#==================================================
print(('=' * 10) + "Problem 8" + ('=' * 10))

# First off, lets reset the data since it has been
# modified for prior tests.
text = open('avengers.csv').read().strip()
choices = make_lists(text)

# Now, let's automate the ranked choice voting
# process.

# This function should:
    # get the choices for rank 0
    # display a bar graph of them: include the number of removed candidates in the title
    # display a pie chart of them: include the number of removed candidates in the title
    # calculate the percentages
    # find the top choice
    # find the bottom choice
    # print out the bottom choice
    # remove the bottom choice
    # repeat all these steps until the top choice has over 50% of the vote
    # At the end, return the top choice winner


def ranked_choice_voting(data):
    
    top_choice = {'name': '', 'pct':0}
    round = 0
    
    while top_choice['pct'] <= 50:
        choice0 = isolate_choice(data, 0)
        #choice_bar(choice0, f'choices round {round}')
        choice_pie(choice0, f'choices round {round}')
        
        add_pcts(choice0)
        top_choice = get_top_choice(choice0)
        bottom_choice = get_bottom_choice(choice0)
        data = remove_option(data, bottom_choice['name'])
        
        print('removing:', bottom_choice['name'])
        round+= 1
    return top_choice

winner = ranked_choice_voting(choices)
pprint(winner)

