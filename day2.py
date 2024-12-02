from aoc_helper import AdventOfCode
import pandas as pd
import numpy as np

def main():
    result1, result2 = 0, 0

    aoc = AdventOfCode(year=2024, day=2)
    input_data = aoc.get_input()
    input_data = input_data.split("\n")
    df = pd.DataFrame(input_data)
    #print(df)
    df = df[0].str.split(' ', expand=True)
    df = df.fillna(0).astype(int)
    
    x = lambda y: [z > 0 for z in y]
    a = lambda b: [c < 0 for c in b]
    g = lambda h: [abs(j) < 4 for j in h]

    for report in df.values:
        report_data = np.array(list(int(x) for x in report if x != 0))
        diff_data = np.diff(report_data)
        print(f"{report_data=}")
        print(f"  {diff_data=}")
        print(all(g(diff_data)))
        if all(g(diff_data)) and not (all(x(diff_data)) == all(a(diff_data))):
            result1 += 1
    print(f"Part 1 answer: {result1}")

if __name__ == "__main__":
    main()
