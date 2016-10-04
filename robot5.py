#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():

    while wall_is_beneath ():
        move_right()
    while wall_is_on_the_right ():
        move_up()
    while wall_is_on_the_left ():
        move_down()


if __name__ == '__main__':
    run_tasks()