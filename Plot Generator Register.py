# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0802

Scott Elmore
11/11/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/OtjmrGKmu8M
"""
# import the appropriate Plot Generator classes
from DSC430_A0801 import InteractivePlotGenerator
from DSC430_A0801 import RandomPlotGenerator
from DSC430_A0801 import SimplePlotGenerator


class PlotViewer():
    '''viewer class that registers a plot generator model and displays output and receives input according
    to its connected view'''

    # set a variable confirming that this view will indeed use standard_IO unless told otherwise
    standard_IO = True

    def __init__(self, model=None):
        'initialize with a model optional'
        self.model = model

    def registerPlotGenerator(self, model):
        'register a plot generator by passing in a model'
        self.model = model
        # must register this view within the model
        self.model.registerView(self)

    def generate(self):
        'generate a plot by calling on the registered model'
        if self.model is not None:
            self.model.generate()
        else:
            # raise exception when no model registered
            raise Exception('Plot generator not registered')

    def display(self, display_str, expect_return=False):
        'how the view will decide to display output and receive input'
        # to emphasize that this I/O comes from the view
        print('***FROM VIEW***')

        # either print or input depending on if method expects return
        if self.standard_IO:
            if expect_return:
                return eval(input(display_str))
            else:
                print(display_str)


def Main():
    '''Give Examples'''
    pv = PlotViewer()
    pv.registerPlotGenerator(SimplePlotGenerator())
    pv.generate()

    pv.registerPlotGenerator(RandomPlotGenerator())
    pv.generate()

    pv.registerPlotGenerator(InteractivePlotGenerator())
    pv.generate()


if __name__ == "__main__":
    Main()
