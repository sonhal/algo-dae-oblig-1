import argparse

from exercise_1.exercise_1 import Exercise1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trie create and search')
    parser.add_argument('in_file', type=str, help="File to build Trie and keys to search for")
    parser.add_argument('out_file', type=str, help='output file name')

    args = parser.parse_args()
    Exercise1(args.in_file).write_to_output(args.out_file)
