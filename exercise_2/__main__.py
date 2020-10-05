import argparse

from exercise_2.exercise_2 import Exercise2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sum of Selections')
    parser.add_argument('in_file', type=str, help="Input file with problem instances")
    parser.add_argument('out_file', type=str, help='output file name')
    parser.add_argument('--memoized', '-m', help='use memoized strategy', action='store_true')

    args = parser.parse_args()
    if args.memoized:
        Exercise2.memoized(args.in_file).write_to_file(args.out_file)
    else:
        Exercise2.dynamic(args.in_file).write_to_file(args.out_file)
