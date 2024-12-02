from aoc_helper import AdventOfCode
import pandas as pd
import numpy as np

def main():
    result1, result2 = 0, 0

    aoc = AdventOfCode(year=2024, day=1)
    input_data = aoc.get_input()
    input_data = input_data.split("\n")
    
    df = pd.DataFrame(input_data)
    df = df[0].str.split(' ', n=1, expand=True)
    df = df.astype(int).transform(np.sort)
    for i in zip(df[0], df[1]):
        result1 += abs(i[0] - i[1])
    print(f"Part 1 answer: {result1}")
    
    numbers = df[0].values
    df[2] = list(map(lambda x: df[1].value_counts().get(x, 0), numbers))
    for i in zip(df[0], df[2]):
        result2 += i[0] * i[1]
    print(f"Part 2 answer: {result2}")

if __name__ == "__main__":
    main()