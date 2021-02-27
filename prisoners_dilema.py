#  -*- coding: utf-8 -*-
'''
P8
Derek Nguyen
Created: 2019-04-03
Modified: 2019-04-03
Due: 2019-04-03
'''

# %% codecell
import numpy as np

def nguyen_derek_p9_2020(history, score):
    '''
    Prisoner's Dilemma function that returns either hawk, 'h' or dove 'd'
    Strategy: Attempy to play cooperatively by playing 'd', if falling behind, play 'h'. Otherwise play 'd'. On the final round two rounds, play 'h' to get the lead.
    Parameters:
    history, list of two character strings recording the history of the entire match
    score, two element tuple containing the current scores
    '''
    if history is None: # Begin by attempting cooperation
        return 'd'
    elif score[0] < score[1]: # Hawk when behind to gain points
        return 'h'
    elif len(history) == 198: # Hawk in the end to prevent opponent from gaining points
        return 'h'
    elif len(history) == 199:
        return 'h'
    else: # Play cooperatively if ahead
        return 'd'
