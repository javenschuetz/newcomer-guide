import sys
import os

import menus

name = ""

def main():
	name = intro()
	main_menu = menus.Menu(name)
	main_menu.first_load()


def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('****************************************')
    print('Welcome to a guide to learning Coding!!!')
    print('****************************************')

    name = input("\nPlease enter your name: ")
    print('Welcome, {}!\n\n'.format(name))
    return name


if __name__ == "__main__":
	main()
