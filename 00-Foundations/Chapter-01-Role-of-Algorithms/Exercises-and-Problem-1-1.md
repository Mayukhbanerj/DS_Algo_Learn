# Chapter 1 — Exercises and Problem 1-1

These are original worked study responses based on CLRS, Fourth Edition, Chapter 1. They are not quotations or an official solutions manual.

## Exercises 1.1

### 1.1-1 — Real-world examples
- **Sorting:** an online store orders product records by price. The key is price; the product description and inventory data are satellite data that must move with the key.
- **Shortest distance:** a navigation system models roads as a weighted graph and finds a minimum-distance route between a source and destination.

### 1.1-2 — Measuring efficiency
Speed is not the only resource. Depending on the system, relevant measures include memory, communication bandwidth, energy, storage, I/O, reliability, and operating cost. The important measure is determined by the application and its constraints.

### 1.1-3 — Data structure strengths and limitations
Example: a hash table.
- Strength: expected constant-time search, insertion, and deletion under suitable hashing and load-factor assumptions.
- Limitations: collisions, no inherent sorted order, resizing/reorganization costs, and potentially linear worst-case operations in common implementations.
A structure should be selected according to the operations and guarantees the application needs.

### 1.1-4 — Shortest path versus traveling salesperson
Both are graph optimization problems, but their outputs differ:
- Shortest path: a minimum-cost path between a specified pair of vertices.
- Traveling salesperson: a minimum-cost tour that visits every specified city and returns to the start.
The traveling-salesperson problem has a much harder general optimization structure.

### 1.1-5 — Exact versus approximate solutions
An exact solution is appropriate when the specification requires a provably optimal answer and the instance is small enough to solve. An approximation may be appropriate for a very large routing or scheduling instance when a solution with a stated quality guarantee is more useful than waiting too long for an exact optimum.

### 1.1-6 — Offline and online
A workforce schedule can be **offline** if all shifts, requests, and constraints are known before decisions are made. It is **online** if new absences or staffing requests arrive over time and decisions must be made without knowing future arrivals.

## Exercises 1.2

### 1.2-1 — Application-level algorithms
A route-planning application uses algorithms to represent the road network, search addresses, find routes (for example, shortest paths), choose among alternatives, and render/interpolate map information. The graphical interface and network are not substitutes for the algorithms that compute the route.

### 1.2-2 — Comparing 8n² and 64n lg n
Insertion sort wins under the stated step-count models when:
[
8n^2 < 64nlg n.
]
For positive (n), divide by (8n):
[
n < 8lg n.
]
Checking the integer boundary gives:
- (n=43): (43 < 8lg 43 approx 43.48), true.
- (n=44): (44 < 8lg 44 approx 43.73), false.
The positive integer range in which insertion sort wins is therefore:
[
oxed{2le nle 43}
]
(The comparison is between the stated mathematical models, not a benchmark claim.)

### 1.2-3 — Comparing 100n² and 2ⁿ
We seek the smallest positive integer (n) for which:
[
100n^2 < 2^n.
]
At (n=14): (100(14)^2=19{,}600), while (2^{14}=16{,}384), so the inequality is false.
At (n=15): (100(15)^2=22{,}500), while (2^{15}=32{,}768), so it is true.
Checking the preceding integer establishes minimality:
[
oxed{n=15}
]

---

## Problem 1-1 — Comparison of running times

The problem asks for the largest input size (n) that can be processed in time (t), when the running time is (f(n)) microseconds. Convert each time budget to microseconds, then solve (f(n)le t). The table's seven time budgets use the standard textbook convention: 30 days per month, 365 days per year, and 100 years per century.

### Time budgets

| Budget | Microseconds |
|---|---:|
| 1 second | (10^6) |
| 1 minute | (60\times10^6) |
| 1 hour | (3.6\times10^9) |
| 1 day | (8.64\times10^{10}) |
| 1 month (30 days) | (2.592\times10^{12}) |
| 1 year (365 days) | (3.1536\times10^{13}) |
| 1 century (100 years) | (3.1536\times10^{15}) |

### Inverting each running-time function

- (f(n)=\lg n): (\lg n\le t\Rightarrow n\le 2^t). The maximum is (2^t).
- (f(n)=\sqrt n): (\sqrt n\le t\Rightarrow n\le t^2). The maximum is (t^2).
- (f(n)=n): maximum (n=t).
- (f(n)=n\lg n): solve numerically for the largest integer satisfying (n\lg n\le t); check that integer and its successor.
- (f(n)=n^2): maximum (\lfloor\sqrt t\rfloor).
- (f(n)=n^3): maximum (\lfloor\sqrt[3]t\rfloor).
- (f(n)=2^n): maximum (\lfloor\lg t\rfloor).
- (f(n)=n!\): choose the largest integer whose factorial does not exceed (t).

### Complete results

For the (n\lg n) column, values are the largest integer solutions, found numerically and checked against the next integer. All other columns use the exact inverse formula and integer floor where needed.

| (f(n)) | 1 second | 1 minute | 1 hour | 1 day | 1 month | 1 year | 1 century |
|---|---:|---:|---:|---:|---:|---:|---:|
| (\lg n) | (2^{1,000,000}) | (2^{60,000,000}) | (2^{3,600,000,000}) | (2^{86,400,000,000}) | (2^{2,592,000,000,000}) | (2^{31,536,000,000,000}) | (2^{3,153,600,000,000,000}) |
| (\sqrt n) | (10^{12}) | (3.6\times10^{15}) | (1.296\times10^{19}) | (7.46496\times10^{21}) | (6.718464\times10^{24}) | (9.94519296\times10^{26}) | (9.94519296\times10^{30}) |
| (n) | (10^6) | (6\times10^7) | (3.6\times10^9) | (8.64\times10^{10}) | (2.592\times10^{12}) | (3.1536\times10^{13}) | (3.1536\times10^{15}) |
| (n\lg n) | 62,746 | 2,801,417 | 133,378,058 | 2,755,147,513 | 71,870,856,404 | 797,633,893,349 | 68,610,956,750,570 |
| (n^2) | 1,000 | 7,745 | 60,000 | 293,938 | 1,609,968 | 5,615,692 | 56,156,922 |
| (n^3) | 100 | 391 | 1,532 | 4,420 | 13,736 | 31,593 | 146,645 |
| (2^n) | 19 | 25 | 31 | 36 | 41 | 44 | 51 |
| (n!\) | 9 | 11 | 12 | 13 | 15 | 16 | 17 |

**How to read very large entries:** the (\lg n) and (\sqrt n) rows are intentionally expressed as powers or scientific notation. For example, with a one-second budget and (f(n)=\lg n), the largest input is (2^{1,000,000}), not one million.

### Verification notes
- For (n\lg n), the listed values are integer roots of (n\log_2 n\le t); the next integer violates the inequality.
- For (2^n), use the floor of (\log_2 t).
- For (n!\), check both the listed factorial and the next factorial.
- The result assumes the textbook time-unit convention above. A different month/year convention changes those columns.

