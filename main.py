#!/usr/bin/env python

import sys, os
#sys.path.append('/modules')

import modules.attendance_module
import modules.add_students_module
import modules.view_attendance_module


menu_actions  = {}

def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Take Attendance"
    print "2. Add into students database"
    print "3. View current attendance"
    print "4. Convert images to pickle"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

def take_attendance():
    modules.attendance_module.am()
    menu_actions['main_menu']()
    return


def add_students():
    modules.add_students_module.asm()
    menu_actions['main_menu']()
    return

def view_attendance():
    modules.view_attendance_module.vam()
    menu_actions['main_menu']()
    return

def img_to_pickle():
    modules.img_to_pickle_module.itp()
    return


def exit():
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': take_attendance,
    '2': add_students,
    '3': view_attendance,
    '4': img_to_pickle,
    '0': exit,
}

if __name__ == "__main__":
    main_menu()
