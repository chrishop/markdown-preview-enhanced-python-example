#!/usr/bin/env python3

import sys

import altair as alt
import pandas as pd


# This is the function where you write your code to produce the visualisation
# This function MUST return a string of vega-lite json
def visualisation() -> str:
    source = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    return alt.Chart(source).mark_bar().encode(
        x='a',
        y='b'
    )


# DON'T touch this, unless you know what you're doing
def main():
    if len(sys.argv) != 2:
        print("There should be exactly 1 argument after the command")
        print("(which should be the file name)")
        return 0
    
    output_filename = sys.argv[1]
    
    with open(output_filename, 'w+') as f:
        f.write(visualisation().to_json())

if __name__ == '__main__':
    main()