# CS251A Homework 3

## Experiment Results
The experiment results are contained in the 3 directories. The `freq_tests` directory contains the main results obtained by running the benchmarks using the different cache replacement policies. We varied the clock frequency and associativity using the parameters outlined in the homework.

The other two directories contain the results of additional tests that were performed. In `assoc_tests` we varied the associativity (range 4-16) and replacement policy, but kept all other parameters constant. In `policy_tests` we varied the cache replacement policy and kept all other parameters constant.

## Scripts
The scripts `assoc.py`, `freq.py`, and `policy.py` were used to run all of the experiments. The `parse_stats.py` file was used to parse results from each experiment's `stats.txt` file into an easy-to-read CSV file.
