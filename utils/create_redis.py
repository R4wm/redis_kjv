#!/usr/bin/env python
###################################################################################
# Synopsis: Create a redis db with bible verses for a quick backend web db engine #
# Authors:  Raymond W. Mintz                                                      #
# Date:     20180906                                                              #
# Email:    raymondmintz11@gmail.com                                              #
# Notes:                                                                          #
###################################################################################

###########
# Imports #
###########
import os
import sys
import redis

<<<<<<< HEAD:utils/create_redis.py
###########
# Globals #
###########
TEXT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'data',
    'bible.txt')

R = redis.Redis(host='localhost', port=6379)

##########
# sanity #
##########
def sanity():
    if not os.path.exists(TEXT):
        print('Cant fine {}'.format(TEXT))
        sys.exit(1)

=======

###########
# Globals #
###########
TEXT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "bible.txt")
R = redis.Redis(host='localhost', port=6379)


##########
# sanity #
##########
def sanity():
    if not os.path.exists(TEXT):
        print('Cant find {}'.format(TEXT))
        sys.exit(1)

>>>>>>> cleanup:create_redis.py

####################
# if_numbered_book #
####################
def if_numbered_book(a_func):
    def run_func(**kwargs):
        try:
            int(kwargs['a_verse_list'][0])
            kwargs['a_verse_list'][0] += kwargs['a_verse_list'].pop(1)

        except ValueError:
            pass

        a_func(**kwargs)

    return run_func


#######################
# push_verse_to_redis #
#######################
@if_numbered_book
def push_verse_to_redis(a_verse_list=None):
    '''
    An a_verse_list broken up like:
    [0] The Book (or) the number of book
    [1] Chapter
    [2] Verse
    [3] Text

    Returns: void
    '''
    redis_key = []

    # Book
    redis_key.append(broken_line[0] + ':')

    # Chapter and verse
    redis_key.append(broken_line[1])
    redis_key = ''.join(redis_key)

    # Push Book:Chapter:Verse Text
    R.set(redis_key, ' '.join(broken_line[2:]))

    return broken_line
<<<<<<< HEAD:utils/create_redis.py
=======

>>>>>>> cleanup:create_redis.py

if __name__ == '__main__':
    sanity()
    for i_line in open(TEXT).readlines():
        broken_line = i_line.split()
        push_verse_to_redis(a_verse_list=broken_line)
