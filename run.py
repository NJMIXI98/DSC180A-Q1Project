#!/usr/bin/env python

import sys
import json

from etl import get_data
from etl import average_price
from etl import model

def main(targets):
    df = get_data(targets)
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
    
