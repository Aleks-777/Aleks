#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down()
    for i in range (1,6):
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right(n=2)
        fill_cell()
        if i!=5:
            move_right(n=3)
            move_up()
    move_left(n=2)
    move_up()

if __name__ == '__main__':
    run_tasks()