# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0801

Scott Elmore
11/11/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/RRaAywKhts8
"""
import os
import random


class SimplePlotGenerator:
    '''Returns a plot to the user when generate is called. Can be registered with a view.'''

    def __init__(self, view=None):
        'constructor can take a view object'
        self.view = view

    def registerView(self, view):
        'register view for I/O'
        self.view = view

    def sendForView(self, display_str, expect_return=False):
        'determines if view exists, if so send a display_str and whether or not to return input'
        if self.view is not None:
            return self.view.display(display_str, expect_return)
        else:
            # use simple I/O without a view
            if expect_return:
                return eval(input(display_str))
            else:
                print(display_str)

    def generate(self):
        'simple plot message is Something happens'
        self.sendForView("Something happens\n")


class RandomPlotGenerator(SimplePlotGenerator):
    '''Extend SimplePlotGenerator, returns a more advanced plot using files within the directory'''

    def generate(self):
        'generate a plot by randomly selecting words from the 7 files'
        plot_str = '{}, a {} {}, must {} the {} {}, {}.\n'.format(self.__getWord('names'), self.__getWord('adjectives'),
                                                                  self.__getWord('profesions'), self.__getWord(
                                                                      'verbs'), self.__getWord('adjectives_evil'),
                                                                  self.__getWord('villian_job'), self.__getWord('villains'))
        self.sendForView(plot_str)

    def __getWord(self, file_suffix):
        'get words by reading from file to a list, then randomly selecting a word from list'
        with open(os.path.join(os.getcwd(), 'plot_' + file_suffix + '.txt')) as infile:
            content = infile.readlines()

        # strip lines to remove whitespace
        content = [x.strip() for x in content]
        return content[random.randint(0, len(content)-1)]


class InteractivePlotGenerator(SimplePlotGenerator):
    '''Extend SimplePlotGenerator, returns a more advanced plot by querying user for inputs'''

    def generate(self):
        'generate a plot by querying user to select between 5 random words from the 7 files'
        plot_str = '{}, a {} {}, must {} the {} {}, {}.\n'.format(self.queryUser('names'), self.queryUser('adjectives'),
                                                                  self.queryUser('profesions'), self.queryUser(
                                                                      'verbs'), self.queryUser('adjectives_evil'),
                                                                  self.queryUser('villian_job'), self.queryUser('villains'))
        self.sendForView(plot_str)

    def queryUser(self, file_suffix):
        'get the list of 5 words and then ask user to select which word to use'
        words = self.__getWords(file_suffix)

        # continue to iterate until given an appropriate selection
        while(True):
            for i, word in enumerate(words):
                self.sendForView('{}: {}'.format((i + 1), word))

            # pass True into sendForView as a response is requested
            selection = self.sendForView(
                'Select which ' + file_suffix + ' you want with the appropriate number.', True)
            if 1 <= selection <= 5:
                return words[selection - 1]
            else:
                # wrong input, continue to loop
                self.sendForView('Must select between 1 and 5.\n')

    def __getWords(self, file_suffix):
        'get words by reading from file to a list, then randomly selecting 5 words from list'
        with open(os.path.join(os.getcwd(), 'plot_' + file_suffix + '.txt')) as infile:
            content = infile.readlines()
        # strip lines to remove whitespace
        content = [x.strip() for x in content]
        words = []
        for x in range(5):
            words.append(content[random.randint(0, len(content)-1)])
        return words


def Main():
    '''Give Examples'''

    pg = SimplePlotGenerator()
    pg.generate()

    pg = RandomPlotGenerator()
    pg.generate()

    pg = InteractivePlotGenerator()
    pg.generate()


if __name__ == "__main__":
    Main()
