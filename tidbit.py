#!/usr/bin/env python

from __future__ import print_function

import notify2
import wikipedia
import random
import time
import textwrap
from os.path import expanduser

configpath = expanduser('~') + '/.tidbit_categories'

def get_random_category():
    categories = load_category_file()
    if categories[-1] == '':
        categories = categories[:-1]

    if len(categories) is 0:
        print('There are no registered categories.')
        print_usage()
        quit()
    return categories[random.randint(0, len(categories) - 1)]

def get_fact():
    category = get_random_category()
    titles = wikipedia.category_members(category, cmlimit=1000)
    title = titles[random.randint(0, len(titles) - 1)]

    return ('Tidbit: ' + category, title + '\n\n' + textwrap.fill(wikipedia.summary(title, sentences=2), 60))

def notification():
    notify2.init('tidbit')
    title, text = get_fact()
    notif = notify2.Notification(title, text)
    notif.set_timeout(notify2.EXPIRES_NEVER) # so you can actually read it
    notif.show()

def tty_print():
    title, text = get_fact()
    print(title + '\n' + text)

def print_usage():
    print('usage: tidbit [help | <<<add | remove> <category>> | <background> <interval>>')

def print_help():
    help_text = ('''\ntidbit - shintoo 2018'''
    '''\n\ntidbit creates a desktop notification displaying the first two sentences from'''
    '''\nthe summary section of a Wikipedia page belonging to one of the categories\nlisted'''
    ''' in ~/.tidbit_categories'''
    '''\n\n  tidbit\t\t\tdisplay one tidbit notification'''
    '''\n  tidbit add <category>\t\tadd <category> to list of categories'''
    '''\n  tidbit remove <category>\tremove <categor> from list of categories'''
    '''\n  tidbit list\t\t\tlist all categories'''
    '''\n  tidbit background <interval>\tdisplay one tidbit notification every\n\t\t\t\t<interval> seconds'''
    '''\n  tidbit fact\t\t\tdo not send any notification, instead print to tty'''
    '''\n  tidbit help\t\t\tprint this help''')

    print(help_text)

def load_category_file():
    try:
        with open(configpath) as category_file:
            content = category_file.read()
    except IOError:
        print('There are no registered categories.')
        print_usage()
        quit()

    return content.split('\n')

def add_category(category):
    with open(configpath, 'a+') as category_file:
        category_file.write(category + '\n')

def remove_category(category):
    categories = load_category_file()
    categories.remove(category)
    with  open(configpath, 'w') as category_file:
        category_file.write('\n'.join(categories))

def list_categories():
    map(print, load_category_file())

def run_in_background(interval):
    while True:
        notification()
        time.sleep(interval)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        notification()

    elif len(sys.argv) == 3:
        if sys.argv[1] == 'remove':
            remove_category(sys.argv[2])

        elif sys.argv[1] == 'add':
            add_category(sys.argv[2])

        elif sys.argv[1] == 'background':
            run_in_background(int(sys.argv[2]))

        else:
            print_usage()

    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            list_categories()
        elif sys.argv[1] == 'fact':
            tty_print()
        elif sys.argv[1] == 'help':
            print_help()
        
        else:
            print_usage()

    else:
        print_help()
