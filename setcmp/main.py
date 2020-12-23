#!/usr/bin/env python

# Copyright (c) 2020 Pierre Wacrenier

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sys import stdin, stderr
from argparse import ArgumentParser, RawTextHelpFormatter


operation_help = """
Operation to perform on the two given sets.
- and : return the intersection of the two sets, e.g. {1,2} and {1,3} => {1}
- or : return the difference of the two sets, with elements in left but not right, e.g. {1,2} or {1,3} => {2}
- xor : return the difference of the two sets, with elements in either left or right but not both, e.g. {1,2} or {1,3} => {2,3}
- all : return a combination of both sets, e.g. {1,2} or {1,3} => {1,2,3}
"""


def abort(msg):
    print(msg, file=stderr)
    exit(-1)

def print_set(collection):
    for item in collection:
        print(item)

def setfile(filename):
    if filename == '-':
            return frozenset(stdin.read().split("\n"))
    else:
        try:
            with open(filename, 'r') as handle:
                return frozenset(handle.read().split("\n"))
        except FileNotFoundError as err:
            abort(str(err))

def main():
    parser = ArgumentParser(description='Perform set operation on list of items', formatter_class=RawTextHelpFormatter)
    parser.add_argument('left', help='Base csv file containing one item per line', type=setfile)
    parser.add_argument('op', help=operation_help, choices=('and', 'or', 'xor', 'all'), metavar='op')
    parser.add_argument('right', help='Other csv file containing one item per line', type=setfile)

    args = parser.parse_args()
    op = args.operation

    if op == 'and':
        result = args.left & args.right
        print_set(result)
    if op == 'or':
        result = args.left - args.right
        print_set(result)
    if op == 'xor':
        result = args.left ^ args.right
        print_set(result)
    if op == 'all':
        result = args.left | args.right
        print_set(result)

if __name__ == "__main__":
    main()
