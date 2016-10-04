#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    o=1
    move_right()
    for i in range (1,12):
        for j in range (1,27):
            if o%2==0:
                fill_cell()
                move_left()
            else:
                fill_cell()
                move_right()
        fill_cell()
        o=o+1
        move_down()



if __name__ == '__main__':
    run_tasks()