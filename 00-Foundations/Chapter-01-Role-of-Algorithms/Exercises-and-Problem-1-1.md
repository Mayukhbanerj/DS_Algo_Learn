# Chapter 1 — Exercises and Problem 1-1

These are original study explanations, not an official solutions manual.

## Exercises 1.1

### 1.1-1
- Sorting example: order a store's products by price.
- Shortest-distance example: find a minimum-distance route between two locations on a road network.

### 1.1-2
Beyond speed, consider memory, energy, I/O, network bandwidth, storage, reliability, and operating cost.

### 1.1-3
A hash table offers expected constant-time lookup under suitable assumptions. Limitations include collisions, lack of inherent sorted order, resizing, and possible linear worst-case operations.

### 1.1-4
Both shortest path and traveling salesperson optimize routes in a graph. Shortest path connects a specified pair of vertices; traveling salesperson seeks a minimum-cost tour visiting every specified city and returning to the start.

### 1.1-5
An exact solution may be required for a small safety-constrained optimization task. A near-optimal solution may be sufficient for a very large delivery-routing workload where a provably optimal answer is too costly to compute.

### 1.1-6
A workforce scheduler can operate offline when all shifts and requests are known in advance, or online when new absences and staffing requests arrive during the day.

## Exercises 1.2

### 1.2-1
A navigation application needs algorithms for graph modeling, shortest paths, route selection, address search, and map rendering.

### 1.2-2
Given insertion sort time (8n^2) and merge sort time (64n\lg n), insertion sort wins when:

[
8n^2 < 64n\lg n
]

For positive (n):

[
n < 8\lg n
]

The integer values satisfying this are (2\le n\le43).

### 1.2-3
Find the smallest positive integer (n) such that:

[
100n^2 < 2^n
]

At (n=14): (19{,}600 > 16{,}384).  
At (n=15): (22{,}500 < 32{,}768).

Answer: (n=15).

---

## Problem 1-1 — Comparison of running times

The problem asks for the largest input size (n) that fits in a time budget (t), when the running time is (f(n)) microseconds.

Convert every time budget to microseconds first:

- 1 second = (10^6) microseconds
- 1 minute = (60\times10^6) microseconds
- 1 hour = (3.6\times10^9) microseconds
- 1 day = (8.64\times10^{10}) microseconds
- 1 month (30 days) = (2.592\times10^{12}) microseconds
- 1 year (365 days) = (3.1536\times10^{13}) microseconds
- 1 century (100 years) = (3.1536\times10^{15}) microseconds

For each row, find the largest integer (n) satisfying (f(n)\le t).

### Inversion methods

| Function | Method |
|---|---|
| (lg n) | (n\le2^t) |
| (sqrt n) | (n\le t^2) |
| (n) | (n\le t) |
| (n\lg n) | Solve numerically, then verify adjacent integers |
| (n^2) | (n\le\lfloor\sqrt t\rfloor) |
| (n^3) | (n\le\lfloor\sqrt[3]t\rfloor) |
| (2^n) | (n\le\lfloor\lg t\rfloor) |
| (n!) | Find the largest factorial not exceeding (t) |

### Selected check values

| Function | 1 second | 1 minute | 1 hour | 1 day |
|---|---:|---:|---:|---:|
| (n\lg n) | 62,746 | 2,800,000 (approx.) | 133,000,000 (approx.) | 2,760,000,000 (approx.) |
| (n^2) | 1,000 | 7,745 | 60,000 | 293,938 |
| (n^3) | 100 | 391 | 1,532 | 4,420 |
| (2^n) | 19 | 25 | 31 | 36 |
| (n!) | 9 | 11 | 12 | 13 |

For (n\lg n), these are approximate numerical inversions. The exact integer should be checked by substituting it and the next integer into (n\lg n\le t).

**Caution:** The month/year/century values depend on the convention used for their length. For a formal submission, use the time-unit convention stated by the instructor or textbook and verify every row directly. The full table should be independently audited rather than inferred from rounded values.
