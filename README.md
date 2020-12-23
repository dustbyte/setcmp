# Setcmp

Perform set operation on list of items

## Installation

```
$ python setup.py install
```

## Usage

```
usage: setcmp [-h] left op right

Perform set operation on list of items.

positional arguments:
  left        Base csv file containing one item per line. A single dash is stdin.
  op
              Operation to perform on the two given sets.
              - int : return the intersection of the two sets,
                  e.g. {1,2} and {1,3} => {1}
              - diff : return the difference of the two sets, with elements in left but not right,
                  e.g. {1,2} or {1,3} => {2}
              - symdiff : return the difference of the two sets, with elements
                  in either left or right but not both, e.g. {1,2} or {1,3} => {2,3}
              - union : return a combination of both sets, e.g. {1,2} or {1,3} => {1,2,3}
  right       Other csv file containing one item per line. A single dash is stdin.

optional arguments:
  -h, --help  show this help message and exit
```

## Examples

```
$ cat file1
1
2
$ cat file2
1
3
$ setcmp file1 int file2
1
$ setcmp file1 diff file2
2
$ setcmp file1 symdiff file2
3
2
$ setcmp file1 union file2
1
3
2
```

## Contact

Send email to Pierre Wacrenier - pierre@wacrenier.me
