#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.00000001)
def task_2_4():
    move_right()
    for p in range (1,6):
        for i in range (1,11):
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
            if i!=10:
                move_right(n=3)
                move_up()
        move_left (n=37)
        if p!=5:
            move_down (n=3)
        if p==5:
            move_left()
            move_up()


if __name__ == '__main__':
    run_tasks()