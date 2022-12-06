#!/usr/bin/env python

import sys
import json

from q1 import get_data
from q1 import average_price
from q1 import model
from q1 import plot
from q1 import create_ranks
from q1 import rank_plot
from q1 import price_row
from q1 import price
from q1 import locate

def main(targets):
    if 'all' in targets:
        print("I put raw data in google drive!")
        
    if 'test' in targets:
        #with open('test/test.json') as fh:
            #df = get_data(fh)  
        print('1111111')
        df = get_data('test/test.json')
        average_price(df)
        model(df)
        plot(df)
        gender_ranks = create_ranks(df,'gender')
        race_ranks = create_ranks(df,'ethnicity')
        rank_plot(gender_ranks)
        rank_plot(race_ranks)
    

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
    
