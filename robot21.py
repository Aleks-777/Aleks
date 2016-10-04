#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    for i in range (1,14):
        for j in range (1,i+1):
            fill_cell()
            move_right()
        for h in range (1,i+1):
            move_left()
        move_down()




if __name__ == '__main__':
    run_tasks()