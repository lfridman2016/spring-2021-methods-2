#==================================================
# Problem 0
pop_file = open('nyc_pop.csv')
text = pop_file.read()
text = text.strip()
print(text)

print('==================================================')

#==================================================
# Problem 1
def get_headers(s):
    g = s.split('\n')
    return g[0].split(',')

# Should print
# ['Year', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
pop_headers = get_headers(text)
print(pop_headers)

print('==================================================')

#==================================================
# Problem 2
def get_data(s):
    lines = s.split('\n')
    lines.pop(0)
    data = []
    for line in lines:
        data.append(line.split(','))
    return data

# Should print:
# [['1790', '33131', '4549', '6159', '1781', '3827', '49447'], ['1800', '60515', '5740', '6642', '1755', '4563', '79215'],
# There will be more sublists after that.
pop_data = get_data(text)
print(pop_data)

print('==================================================')

#==================================================
# Problem 3
def number_convert(data):
    for row in data:
        i = 0
        while i < len(row):
            row[i] = float(row[i])
            i+= 1

# Should print
# [[1790.0, 33131.0, 4549.0, 6159.0, 1781.0, 3827.0, 49447.0], [1800.0, 60515.0, 5740.0, 6642.0, 1755.0, 4563.0, 79215.0],
# There will be more sublists after that.
number_convert(pop_data)
print (pop_data)

print('==================================================')

#==================================================
# Problem 4
def row_total(row_key, data):
    total = 0
    for row in data:
        if row[0] == row_key:
            for value in  row[1:]:
                total+= value
    return total

# Should print 49447.0
print( row_total(1790, pop_data) )

# How many people lived in NYC in 1880?
print( row_total(1880, pop_data) )

print('==================================================')

#==================================================
# Problem 5
def get_column(key, headers, data):
    position = headers.index(key)
    column = []
    for row in data:
        column.append( row[position] )
    return column

# Should print
# [1781.0, 1755.0, 2267.0, 2782.0, 3023.0, 5346.0, 8032.0, 23593.0, 37393.0, 51980.0,
# With more data after that
bronx_pops = get_column('Bronx', pop_headers, pop_data)
print(bronx_pops)

print('==================================================')

#==================================================
# Problem 6
#a) How many people lived in NYC in 2010?
p_2010 =  row_total(2010, pop_data)
print(p_2010)

#b) How many people lived in Brooklyn in 1970?
years = get_column('Year', pop_headers, pop_data)
bk_pops = get_column('Brooklyn', pop_headers, pop_data)
print( bk_pops[ years.index(1970)] )

#c) What was the change in total population from 1900 to 2000?
new = row_total(2000, pop_data)
old = row_total(1900, pop_data)
print( new - old )
#d) What percentage of the total NYC population did Queens account for in 2010?
q_pop = get_column('Queens', pop_headers, pop_data)
q2010 = q_pop[ years.index(2010) ]
print( q2010 / p_2010 )
