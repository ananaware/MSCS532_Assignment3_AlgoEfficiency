# MSCS-532 Assignment 3: Algorithm Efficiency and Scalability

## Course Information
- Course: MSCS-532 – Algorithms and Data Structures
- Term: Spring 2026
- Assignment: Understanding Algorithm Efficiency and Scalability

---

## Overview
This project analyzes and compares the efficiency and scalability of two algorithms:

1. **Randomized Quicksort vs Deterministic Quicksort**
2. **Hash Table with Chaining**

Both theoretical analysis and empirical evaluation are performed to understand algorithm behavior under different input conditions, following concepts from *Introduction to Algorithms* by Cormen et al. (2022).

---

## Project Structure

MSCS532_Assignment3_AlgoEfficiency
├── src
│ ├── quicksort.py
│ ├── benchmark.py
│ └── hash_table.py
├── data
├── report
├── README.md
├── requirements.txt


---

## Part 1: Quicksort Algorithms

### Implementations
- **Randomized Quicksort**: Selects pivot uniformly at random.
- **Deterministic Quicksort**: Always selects the first element as pivot.

Both implementations sort arrays in-place and handle edge cases such as empty arrays, sorted arrays, reverse-sorted arrays, and repeated elements.

### How to Run Correctness Check
```bash
python3 src/quicksort.py
```
This command verifies correctness by sorting multiple test arrays using both algorithms.

### Empirical Benchmarking

The benchmarking script compares both algorithms on:

Random arrays

Sorted arrays

Reverse-sorted arrays

Arrays with repeated elements

Input sizes tested:

1000

3000

5000

To run benchmarks:
```bash
python3 src/benchmark.py
```
The output reports execution times and highlights cases where recursion depth is exceeded, demonstrating worst-case behavior.

### Part 2: Hash Table with Chaining
Implementation Details

Collision resolution using chaining

Supports:

Insert

Search

Delete

Uses a universal-style hash function

Tracks load factor (α = n / m)

How to Run Hash Table Demo
```bash
python3 src/hash_table.py
```
### This demonstrates:

Insert operations

Successful and unsuccessful searches

Deletion of keys

Load factor changes

### Key Observations

Randomized Quicksort exhibits expected 
𝑂(𝑛log⁡ 𝑛)performance on most inputs.

Deterministic Quicksort degrades to 
𝑂(𝑛2)on sorted and reverse-sorted inputs.

Hash tables with chaining provide expected 
𝑂(1+𝛼)performance for insert, search, and delete operations when the load factor is controlled.

### References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
Introduction to Algorithms (4th ed.). MIT Press.
ISBN: 9780262046305

---


