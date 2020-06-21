#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n log n)


c) O(n)

## Exercise II
Parameters: n = number of stories, num = number of eggs
Egg is broken if n > f floors, not broken if n < f floors

Complexity: 0(log n)

The most effecient way to solve the problem is to use binary search. By testing the midpoint of a moving range 0 - num, we can optmize the time and number of eggs it takes to figure out the answer.
