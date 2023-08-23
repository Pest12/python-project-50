#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa: F841
    diff = generate_diff('file1.json', 'file2.json')
    print(diff)


if __name__ == '__main__':
    main()
