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
        a= average_price(df)
        print(a)
        b= model(df)
        print(b)
        c= plot(df)
        print(c)
        gender_ranks = create_ranks(df,'gender')
        race_ranks = create_ranks(df,'ethnicity')
        fig = interaction_plot(x=df['ethnicity'], trace=df['gender'], response=df['price_mean'], 
                               colors=['#d17a22', '#4c061d'])
        plt.show()
        gender_ranks.T.plot()
        plt.xlabel('Ranking')
        plt.ylabel('Average Price')
        race_ranks.T.plot()
        plt.xlabel('Ranking')
        plt.ylabel('Average Price')
      

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
    
