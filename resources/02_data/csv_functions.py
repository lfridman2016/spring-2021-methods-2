# Two functions to assist with reading in csv files.
# These do not manipulate data in any way.
# If you know that the data provided is numeric, you may want to
# convert the values from strings using int() or float()


# Takes a csv file and creates a list of lists.
# Each sub-list is a single row of the file.
def csv_to_lists(filename):
    f = open(filename)
    text = f.read().strip() #strip removes extra whitespace before and after
    #separate each line of the file
    lines = text.split('\n')

    #create the list of lists
    data = []
    for line in lines:
        line = line.strip()
        line = line.split(',')
        data.append(line)
    return data

# Takes a csv file and creates a list of dictionaries.
# Assumes the first row contains the headers.
def csv_to_dicts(filename):
    f = open(filename)
    text = f.read().strip()
    lines = text.split('\n')

    # pop(0) removes and returns the row at position 0
    headers = lines.pop(0).strip().split(',')

    data = []
    for line in lines:
        line = line.strip().split(',')

        row_dict = {}
        for i in range(len(headers)):
            header = headers[i]
            row_dict[header] = line[i]
        data.append(row_dict)
    return data

# testing
pop_lists = csv_to_lists('nyc_pop.csv')
pop_dicts = csv_to_dicts('nyc_pop.csv')
#print(pop_lists)
#print(pop_dicts)

# the pprint module prints out lists and dictionaries in an easier to read format.
import pprint
pprint.pprint(pop_lists)
pprint.pprint(pop_dicts)
