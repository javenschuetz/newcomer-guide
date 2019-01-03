import os
import sys
import json
import webbrowser

from flower import draw_flower

class Menu:
    """A class to create and navigate through a menu

    Attributes:
        user_name (str): user's name
        options (dictionary): contains the menus, links, and text to display
        current (array): array representing location within the menu options object
    """
    def __init__(self, name='stranger'):
        """Creates a Menu object

        Args:
            name (str): the name of the person using these menus
        """
        self.user_name = name
        self.current = ['main']
        with open('menu_options.json') as options_file:
            self.options = json.loads(options_file.read())

    def first_load(self):
        """Prints instructions and loads the main menu"""
        print("instructions:")
        print(self.options['main']['instructions']['text'])
        self.load(['main'])

    def load(self, page_path, text='OPTIONAL'):
        """ This loads a menu page

        Args:
            page_path (array): array representing the property of the options
            object to load. Eg, to load foo['bar']['baz'] the array would
            contain ['foo', 'bar', 'baz']

        Returns:
            If the page contains menu items, it returns an array of items.
            If the page is a link, run, or text, it will simply print the text,
                load the link or run the executable
        """
        page = self.get_page_dictionary(page_path)
        keys = list(page.keys())
        if keys.count('text') > 0:
            self.load(self.current, page['text'])
        elif keys.count('link') > 0:
            webbrowser.open(page['link'])
            self.load(self.current)
        elif keys.count('run') > 0:
            # currently draw_flower is the only 'run' command
            draw_flower()
            self.load(self.current)
        else:
            self.current = page_path
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.options['help']['text'])
            print('\nyou are at: {}'.format(page_path))
            print('****************************************************')
            for key in keys:
                if key != 'secret':
                    print(key)
            if text != 'OPTIONAL':
                print('\n{}'.format(text))
            selection, err = self.get_selection(keys)
            self.load(selection, err)

    def get_page_dictionary(self, page_path):
        """Retrieve page dictionary given a path array

        Args:
            page_path (array): array representing path to the menu

        Returns:
            returns dictionary containing menu at that location
        """
        page_path = page_path[::-1]
        page_dic = self.options[page_path.pop()]
        while len(page_path) > 0:
            page_dic = page_dic[page_path.pop()]
        page_path = page_path[::-1]
        return page_dic

    def get_selection(self, keys):
        """Request and collect user input. If valid, load that page. If not,
        load previous page
        """
        selection = input('\n\nHello {}! Please type the option you would like to select: '
            .format(self.user_name));
        text = 'OPTIONAL'

        current = list(self.current)
        if selection == 'exit' or selection == 'quit' or selection == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('goodbye!')
            exit()
        elif selection == 'back' or selection == 'b':
            if len(current) > 1:
                current.pop()
        elif keys.count(selection) == 0:
            orig_selection = selection
            for key in keys:
                if key.find(selection) != -1:
                    selection = key
            if orig_selection == selection:
                text = 'Option not found!'
            else:
                current.append(selection)
        else:
            current.append(selection)

        return current, text
