import notify2
import wikipedia
import random
from os.path import expanduser

configpath = expanduser('~') + '/.tidbit_categories'

def get_random_category():
    categories = load_category_file()
    if len(categories) is 0:
        print 'There are no registered categories.'
        print_help()
        quit()
    return categories[random.randint(0, len(categories) - 1)]

def get_fact():
    titles = wikipedia.category_members(category=get_random_category(), cmlimit=200)
    title = titles[random.randint(0, len(titles) - 1)]
    return (title, wikipedia.summary(title, sentences=2))

def notification():
    notify2.init('tidbit')
    title, text = get_fact()
    notif = notify2.Notification(title, text)
    notif.show()

def print_help(name):
    print('usage: ' + name + '[<add | remove> <category>]')

def load_category_file():
    with open(configpath) as category_file:
        content = category_file.read()
    return content.split('\n')

def add_category(category):
    with open(configpath, 'a') as category_file:
        category_file.write(category + '\n')

def remove_category(category):
    categories = load_category_file()
    categories.remove(category)
    with  open(configpath, 'w') as category_file:
        category_file.write('\n'.join(categories))

if __name__ == '__main__':
    import sys

    if len(sys.argv) is 1:
        notification()
    elif len(sys.argv) is 3:
        if sys.argv[1] is 'remove':
            remove_category(sys.argv[2])
        elif sys.argv[1] is 'add':
            add_category(sys.argv[2])
    else:
        print_help(argv[0])
