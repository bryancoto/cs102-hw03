import sys
from statistics import mean
import csv

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")
    with open(input_file_path) as f:
        finder =csv.reader(f, delimiter=',')
        for line in finder:
            newlist = []
            for i in line:
                newlist.append(float(i))
            print(mean(newlist))






if __name__ == "__main__":
    main()
