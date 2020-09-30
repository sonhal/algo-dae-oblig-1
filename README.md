# Algorithms: Design and Efficiency
## Oblig 1
### Exercise 1: Trie
Run the program
```bash
python3 -m exercise_1 [-h] in_file out_file

Trie create and search

positional arguments:
  in_file     File to build Trie and keys to search for
  out_file    output file name

optional arguments:
  -h, --help  show this help message and exit
```

### Exercise 2: Dynamic Programming

**a)**
The values in the individual cells in the table U indicates if the value j at cell(i, j) is solvable for the value j, 
where i indexes a value in the collection T and j indexes a value in the range [0, S].

**Formula:**
n = number of values in collection T
U = a table n x s
S = sum to be solved
    
U[n-1, S-1] is the cell that contains True or False if the value is solvable
U[i, j] = U[i - 1, j] if T[i] > S else U[i, j] = U[i - 1, j] or U[i-1, j - T[i]]

The algorithm must be correct finding if a the value is solvable because the value T[i] is larger than S it cannot be part
of the collection and the algorithm defers to the result from smaller values in T. If T[i] is smaller than S we check if the T[i]
can be composed with a solution from a lower value T[i-1, j - T[i]] for the value j that would compose with T[i] to S.

The answer will occur in the final cell in row indexed by K's index in the range [0, S]. The cell can be represented as 
such: solution = cell(n-1, K-1)

Run the program
```bash

```