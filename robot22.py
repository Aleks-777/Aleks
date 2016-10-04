#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    l=0
    o = 0
    q=0
    while not wall_is_beneath() or not wall_is_on_the_right() and not wall_is_beneath():
        while not wall_is_on_the_right():
            o = o + 1
            fill_cell()
            move_right()
        fill_cell()
        for i in range (1,o+1):
            move_left()
        if not wall_is_beneath():
            move_down()
        o = 0
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        fill_cell()
        l = l+1
    for q in range (1,l+1):
        move_left()

if __name__ == '__main__':
    run_tasks()