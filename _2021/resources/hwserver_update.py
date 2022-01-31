from urllib.request import urlopen
import sys
import pprint
from fabric import Connection, Config
import getpass
import time

YEAR = '/21'
BASE_DIR = '/usr/local/www/bert/teacherdb/spring2021/'

def get_assignment_html(url):
    page = urlopen(url)
    html = page.read().decode('utf-8')

    # get title
    start_pos = html.find('<title>') + len('<title>')
    end_pos = html.find(' | ')
    title = html[start_pos : end_pos]

    #extract body from html
    start_pos = html.find('<body>')
    end_pos = html.find('</body>')
    body = html[start_pos : end_pos]

    return (title, body)

def get_due_string(body, prefix):
    start_pos = body.find( prefix ) + len(prefix)
    #move start_pos past the day
    start_pos = body.find(' ', start_pos) + 1
    end_pos = body.find('</h4>', start_pos)


    time_string = body[start_pos:end_pos]
    year_spot = time_string.find(' ')
    time_string = time_string[:year_spot] + YEAR + time_string[year_spot:]
    spot = time_string.rfind(' ')
    if 'am' in time_string:
        time_string = time_string[:spot] + 'a'
    elif 'pm' in time_string:
        time_string = time_string[:spot] + 'p'

    return time_string

def get_name_string(body):
    name_prefix = 'name: '
    start_pos = body.find(name_prefix) + len(name_prefix)
    end_pos = body.find('</h4>', start_pos)
    return body[start_pos:end_pos]


def connect_to_bert(pw, command, auth=False):
    config = Config(overrides={'sudo': {'password': pw}})
    c = Connection(host = 'bert.stuy.edu', user = "teacher", connect_kwargs={"password":pw}, config=config)
    if auth:
        output = c.sudo(command, hide=True)
    else:
        output = c.run(command, hide=True)
    #print(output)
    output = output.stdout
    c.close()
    return output

def get_next_anum(atype, period, pw):
    f = f'{BASE_DIR}{period}'
    afile = connect_to_bert(pw, f'cat {f}')

    start_pos = afile.rfind('assignment,' + atype)
    end_pos = afile.find(',', start_pos + len('assignment,'))
    anum = afile[start_pos:end_pos]
    anum = int(anum[-2:])
    anum+=1
    return f'{anum:02}'

def get_update_strings(url, course, atype, pw):
    update_strings = {}
    name_due_string = ''
    if atype == 'cw':
        name_due_string = url
    else:
        title, body = get_assignment_html(url)
        due_string = get_due_string(body, course[0])
        name_string = get_name_string(body)
        name_due_string = f'{name_string},{due_string}'
    for class_file in course[1]:
        anum = get_next_anum(atype, class_file, pw)
        update_strings[class_file] = f'assignment,{atype}{anum},{name_due_string},,,'
    return update_strings

def publish_updates(update_strings, pw):
    for uf in update_strings:
        command = f'sed -i "$ a {update_strings[uf]}" {BASE_DIR}{uf}'
        connect_to_bert(pw, command, auth=True)
        #print(command)

courses = {
    'intro45': ['(period 4/5): ',
                ['p4d.csv', 'p5d.csv']],
    'intro9': ['(period 9): ',
               ['p9d.csv']]
}

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("usage: python hwserver_update.py -u COURSE [cw|w|l] [URL|NAME,M/D/YY H:MMap")
        exit()
    if sys.argv[1] == '-u':
        course = courses[sys.argv[2]]
        atype = sys.argv[3]
        pw = getpass.getpass(prompt = 'bert pw: ')
        assignments = get_update_strings(sys.argv[4], course, atype, pw)
        pprint.pprint(assignments)

        ans = input('Puiblish this assignment (y/N): ')
        if (ans == 'y' or  ans == 'Y'):
            publish_updates(assignments, pw)
    else:
        print("usage: python hwserver_update.py -u COURSE [cw|w|l] [URL|NAME,M/D/YY H:MMap")
