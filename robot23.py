#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    i=0
    move_right()
    while not wall_is_on_the_right():
        if not wall_is_above():
            i=1
            while not wall_is_above():
                move_up()
                fill_cell()
        if i==1:
            while not wall_is_beneath():
                move_down()
        move_right()
    if not wall_is_above():
            i=1
            while not wall_is_above():
                move_up()
                fill_cell()
    if i==1:
        while not wall_is_beneath():
            move_down()
    while wall_is_beneath():
        move_left()



if __name__ == '__main__':
    run_tasks()