# CLRS Study Progress

**Primary source:** CLRS, Fourth Edition (2022)  
**Working language:** Python  
**Target branch:** `main`

## Completion audit — 21 November 2026

Chapters 1–7 are complete study packages. Each chapter has been checked against the uploaded PDF, this conversation's requirements and prior decisions, and the committed GitHub files.

| Chapter | Coverage | Status |
|---|---|---|
| 1 — The Role of Algorithms in Computing | Sections 1.1–1.2, Exercises 1.1-1–1.2-3, Problem 1-1 | **Complete** |
| 2 — Getting Started | Sections 2.1–2.3, pseudocode conventions, Exercises 2.1-1–2.3-8, Problems 2-1–2-4 | **Complete** |
| 3 — Characterizing Running Times | Sections 3.1–3.3, Exercises 3.1-1–3.3-9, Problems 3-1–3-7 | **Complete** |
| 4 — Divide-and-Conquer | Sections 4.1–4.7, Exercises 4.1-1–4.7-6, Problems 4-1–4-7 | **Complete** |
| 5 — Probabilistic Analysis and Randomized Algorithms | Sections 5.1–5.4, Exercises 5.1-1–5.4-8, Problems 5-1–5-2 | **Complete** |
| 6 — Heapsort | Sections 6.1–6.5, Exercises 6.1-1–6.5-11, Problems 6-1–6-3 | **Complete** |
| 7 — Quicksort | Sections 7.1–7.4, Exercises 7.1-1–7.4-6, Problems 7-1–7-7 | **Complete** |
| 8 — Sorting in Linear Time | Sections 8.1–8.4, Exercises 8.1-1–8.4-6, Problems 8-1–8-7 | **Complete** |
| 9 — Medians and Order Statistics | Sections 9.1–9.3, Exercises 9.1-1–9.3-10, Problems 9-1–9-6 | **Complete** |
| 10 — Elementary Data Structures | Sections 10.1–10.3, Exercises 10.1-1–10.3-6, Problems 10-1–10-3 | **Complete** |
| 11 — Hash Tables | Sections 11.1–11.5, Exercises 11.1-1–11.5-3, Problems 11-1–11-4 | **Complete** |
| 12 — Binary Search Trees | Sections 12.1–12.3, Exercises 12.1-1–12.3-7, Problems 12-1–12-4 | **Complete** |
| 13 — Red-Black Trees | Sections 13.1–13.4, Exercises 13.1-1–13.4-9, Problems 13-1–13-3 | **Complete** |
| 14 — Dynamic Programming | Sections 14.1–14.5, Exercises 14.1-1–14.5-4, Problems 14-1–14-12 | **Complete** |

## Chapter 1

- [x] Section 1.1: algorithms, problem specifications and instances, correctness, applications, data structures, techniques, NP-completeness, approximation, parallel and online models
- [x] Section 1.2: efficiency, insertion-sort/merge-sort comparison, hardware example, algorithms as technology, machine learning and data science
- [x] Exercises 1.1-1 through 1.1-6 and 1.2-1 through 1.2-3
- [x] Problem 1-1: all eight functions and seven time budgets
- [x] Numerical thresholds and inverse formulas independently checked
- [x] Mathematical notation and chapter-note summary audited

Files:
- [Chapter 1 notes](00-Foundations/Chapter-01-Role-of-Algorithms/README.md)
- [Chapter 1 exercises and Problem 1-1](00-Foundations/Chapter-01-Role-of-Algorithms/Exercises-and-Problem-1-1.md)

## Chapter 2

- [x] Section 2.1: sorting problem, keys and satellite data, insertion sort, loop invariant, correctness
- [x] Pseudocode conventions: blocks, loops, comments, local variables, indexing, subarrays, objects/references, NIL, parameters, return, short-circuit Boolean operators, error
- [x] Section 2.2: RAM model, word-size assumptions, input-size measures, statement-count analysis, best/worst case, average-case caveat, order of growth
- [x] Section 2.3: incremental method, divide/conquer/combine, MERGE, MERGE-SORT, recurrence and recursion-tree analysis
- [x] Exercises 2.1-1 through 2.3-8 and Problems 2-1 through 2-4
- [x] Original SVG visuals: playing-card insertion sort, array trace, merge-sort recursion
- [x] Python insertion sort and merge sort implementations
- [x] Committed sorting test suite executed: 5 tests passed
- [x] Additional algorithm/input checks: 14 function/input combinations passed
- [x] Mathematical formatting and chapter-note summary audited

Files:
- [Chapter 2 notes](00-Foundations/Chapter-02-Getting-Started/README.md)
- [Chapter 2 exercises and problems](00-Foundations/Chapter-02-Getting-Started/Exercises-and-Problems.md)
- [Playing-card illustration](00-Foundations/Chapter-02-Getting-Started/images/insertion-sort-playing-cards.svg)
- [Insertion-sort array trace](00-Foundations/Chapter-02-Getting-Started/images/insertion-sort-array-trace.svg)
- [Merge-sort recursion illustration](00-Foundations/Chapter-02-Getting-Started/images/merge-sort-recursion.svg)
- [Insertion sort Python](Implementations/Python/insertion_sort.py)
- [Merge sort Python](Implementations/Python/merge_sort.py)
- [Sorting tests](Implementations/Python/test_sorting.py)

## Chapter 3

- [x] Section 3.1: intuitive O, Omega, Theta bounds and insertion-sort lower/upper arguments
- [x] Section 3.2: formal O, Omega, Theta, little-oh, little-omega; algebraic properties; two-parameter notation
- [x] Section 3.3: monotonicity, floors/ceilings, modular arithmetic, polynomials, exponentials, logarithms, factorials, iteration, log-star, Fibonacci
- [x] Exercises 3.1-1 through 3.3-9
- [x] Problems 3-1 through 3-7, including all 30 expressions in Problem 3-3
- [x] Original SVG illustration for O, Omega, and Theta bounds
- [x] Chapter notes and mathematical formatting audited
- [x] Three-way audit against source PDF pages 71–97, this conversation, and GitHub main

Files:
- [Chapter 3 notes](00-Foundations/Chapter-03-Characterizing-Running-Times/README.md)
- [Chapter 3 exercises and problems](00-Foundations/Chapter-03-Characterizing-Running-Times/Exercises-and-Problems.md)
- [Asymptotic bounds illustration](00-Foundations/Chapter-03-Characterizing-Running-Times/images/asymptotic-bounds.svg)

## Chapter 4 — Audit checklist

- [x] Sections 4.1–4.2: standard recursive matrix multiplication and Strassen
- [x] Sections 4.3–4.4: substitution method and recursion trees
- [x] Sections 4.5–4.6: master method and continuous-master proof
- [x] Section 4.7: Akra–Bazzi, polynomial-growth condition, floors and ceilings
- [x] Exercises 4.1-1 through 4.7-6
- [x] Problems 4-1 through 4-7
- [x] Original SVG recursion-tree illustration
- [x] Final mathematical and source-coverage review
- [x] Three-way audit: source PDF pages 98–147, this conversation, and GitHub `main`
- [x] Fetch every Chapter 4 file again after final edits and reconcile all findings

Files:
- [Chapter 4 notes](00-Foundations/Chapter-04-Divide-and-Conquer/README.md)
- [Chapter 4 exercises and problems](00-Foundations/Chapter-04-Divide-and-Conquer/Exercises-and-Problems.md)
- [Recursion-tree illustration](00-Foundations/Chapter-04-Divide-and-Conquer/images/recursion-tree-level-costs.svg)

## Chapter 5

- [x] Section 5.1: hiring problem, worst case, probabilistic analysis, randomized algorithms
- [x] Section 5.2: indicator random variables, linearity of expectation, expected hiring cost
- [x] Section 5.3: randomized hiring, uniform random permutations, loop-invariant proof
- [x] Section 5.4: birthday paradox, balls and bins, streaks, online hiring
- [x] Exercises 5.1-1 through 5.4-8
- [x] Problems 5-1 and 5-2
- [x] Three-way audit: source PDF pages 148–177, this conversation, and GitHub main

Files:
- [Chapter 5 notes](00-Foundations/Chapter-05-Probabilistic-Analysis/README.md)
- [Chapter 5 exercises and problems](00-Foundations/Chapter-05-Probabilistic-Analysis/Exercises-and-Problems.md)

## Chapter 6 — Complete

- [x] Sections 6.1–6.5 drafted: heaps, heapify, linear-time build, heapsort, priority queues
- [x] d-ary heaps and Young tableaux covered
- [x] Exercises 6.1-1 through 6.5-11 drafted
- [x] Problems 6-1 through 6-3 drafted
- [x] Original heap tree/array SVG added
- [x] Python heap, heapsort, and max-priority-queue implementation added
- [x] Python unittest file added
- [x] Recheck all 35 exercises, 3 problems, and worked heap traces
- [x] Execute the 9-test Python heap validation suite — all passed
- [x] Three-way audit: source PDF pages 183–202, this conversation, and GitHub `main`
- [x] Fetch all Chapter 6 files again after final edits

Files:
- [Chapter 6 notes](00-Foundations/Chapter-06-Heapsort/README.md)
- [Chapter 6 exercises and problems](00-Foundations/Chapter-06-Heapsort/Exercises-and-Problems.md)
- [Heap tree and array illustration](00-Foundations/Chapter-06-Heapsort/images/max-heap-tree-array.svg)
- [Python heap implementation](Implementations/Python/heaps.py)
- [Python heap tests](Implementations/Python/test_heaps.py)

## Chapter 7 — Complete

- [x] Sections 7.1–7.4 drafted, including partition invariant and expected comparison analysis
- [x] Exercises 7.1-1 through 7.4-6 drafted
- [x] Problems 7-1 through 7-7 drafted
- [x] Deterministic, randomized, Hoare, three-way, and bounded-stack Python quicksort implementations added
- [x] Python test suite added
- [x] Original partition invariant illustration added
- [x] Recheck Hoare trace, recurrence derivations, median-of-three probabilities, and fuzzy-sort design against the PDF
- [x] Validate 510 arrays across five quicksort variants; validate 1,000 fuzzy-sort inputs and the Hoare partition boundary
- [x] Fetch all Chapter 7 files after final edits; no control-character corruption detected
- [x] Three-way audit: source PDF pages 205–226 (printed pages 183–204), this conversation, and GitHub main

Files:
- [Chapter 7 notes](00-Foundations/Chapter-07-Quicksort/README.md)
- [Chapter 7 exercises and problems](00-Foundations/Chapter-07-Quicksort/Exercises-and-Problems.md)
- [Partition invariant illustration](00-Foundations/Chapter-07-Quicksort/images/partition-invariant.svg)
- [Python quicksort implementations](Implementations/Python/quicksort.py)
- [Python quicksort tests](Implementations/Python/test_quicksort.py)

## Chapter 8 — Complete

- [x] Sections 8.1–8.4 drafted: decision-tree lower bound, counting sort, radix sort, bucket sort
- [x] Exercises 8.1-1 through 8.4-6 drafted
- [x] Problems 8-1 through 8-7 drafted
- [x] Stable counting sort, radix sort, and bucket sort Python implementations added
- [x] Python test suite added
- [x] Original counting-sort stability illustration added
- [x] Recheck Exercise 8.1-3 and the exact wording of 8.3-4 and 8.3-6 against the printed source
- [x] Strengthen the decision-tree and merging lower-bound proofs; correct the restricted-input argument in 8.1-4
- [x] Finish the half-column boundary proof for Problem 8-7(f)
- [x] Recheck the 8.3-6 MSD pass-count bound and strengthen its attainability argument
- [x] Correct the restricted-input lower-bound argument in 8.1-4
- [x] Clarify the inverse-CDF versus forward-CDF assumption in Exercise 8.4-6
- [x] Prove the nondivisible dirty-row bound and sufficient condition in 8-7(g)
- [x] Verify the even, divisible padding construction in 8-7(h)
- [x] Execute all 10 tests from the exact committed implementation and test-file contents fetched from GitHub main; all passed (the repository clone itself was unavailable)
- [x] Re-fetch all seven Chapter 8 files after the proof edits and verify the source/chat/GitHub audit
- [x] Run the exact fetched Python suite: 10 tests passed

Files:
- [Chapter 8 notes](00-Foundations/Chapter-08-Sorting-in-Linear-Time/README.md)
- [Chapter 8 exercises and problems](00-Foundations/Chapter-08-Sorting-in-Linear-Time/Exercises-and-Problems.md)
- [Counting sort illustration](00-Foundations/Chapter-08-Sorting-in-Linear-Time/images/counting-sort-stability.svg)
- [Python implementations](Implementations/Python/linear_sorting.py)
- [Python tests](Implementations/Python/test_linear_sorting.py)

## Chapter 9 — Complete

- [x] Source pages 227–247 reopened and section structure captured
- [x] Sections 9.1–9.3 drafted
- [x] Exercises and Problems companion drafted
- [x] Python minimum/maximum, randomized selection, and deterministic selection added
- [x] Python tests added; equivalent local checks passed for min/max and randomized/deterministic selection (the committed test file itself was not executed)
- [x] Selection partition diagram added
- [x] Resolve and recheck: six-comparison median-of-five; simplified randomized-select expected-time recurrence; indicator probabilities including target-at-endpoint cases and 4n comparison bound; SELECT3 exact rounding recurrence; simultaneous min/max candidate-membership lower bound; small-order-statistics recurrence
- [x] Audit every exercise 9.1-1 through 9.3-10 and Problems 9-1 through 9-6 against source pages 249–269
- [x] Correct the lower-median convention in 9.3-10; clarify exact k-quantile recursion and distance-tie handling
- [x] Correct candidate-set roles in 9.1-4 and make the weighted-median threshold recursion explicit
- [x] Reconcile chapter notes, exercises, Python implementation/tests, repository map, and progress tracker
- [x] Fetch all Chapter 9 files from GitHub main after final edits and verify the committed content
- [x] Equivalent local algorithm checks passed for min/max and randomized/deterministic selection; committed unittest file not executed

Files:
- [Chapter 9 notes](00-Foundations/Chapter-09-Medians-and-Order-Statistics/README.md)
- [Chapter 9 exercises and problems](00-Foundations/Chapter-09-Medians-and-Order-Statistics/Exercises-and-Problems.md)
- [Selection partition illustration](00-Foundations/Chapter-09-Medians-and-Order-Statistics/images/selection-partition.svg)
- [Python implementations](Implementations/Python/order_statistics.py)
- [Python tests](Implementations/Python/test_order_statistics.py)

## Completion standard

A chapter is complete only after its source pages, the relevant conversation instructions and prior decisions, and the committed GitHub files agree. The notes are original explanations; SVGs are original teaching diagrams, not textbook scans. Tests are reported as passed only after execution.

## Chapter 10 — Complete

- [x] Source pages 251–271 reopened; sections 10.1–10.3 and all exercise/problem statements captured
- [x] Core notes drafted: arrays, matrices, stacks, circular queues, deques, linked lists, sentinels, binary trees, and left-child/right-sibling trees
- [x] Solutions for Exercises 10.1-1 through 10.3-6 and Problems 10-1 through 10-3
- [x] Add Python implementations for stacks, queues, deques, linked lists, reversal, and tree traversals
- [x] Add unittest coverage for core implementations and a circular-queue illustration
- [x] Resolve and verify the two-pointer/one-boolean representation in Exercise 10.3-6; parent lookup follows the sibling chain to its last-child marker
- [x] Audit Problem 10-3 tail-sum/integral bound and construct a repeated-key input where strict skips cannot advance within the duplicate run
- [x] Execute the fetched implementation and test contents in a temporary local package; all 9 unittest cases passed
- [x] Fetch all Chapter 10 files after final edits and finish source/chat/GitHub audit

Files:
- [Chapter 10 notes](00-Foundations/Chapter-10-Elementary-Data-Structures/README.md)
- [Chapter 10 exercises and problems](00-Foundations/Chapter-10-Elementary-Data-Structures/Exercises-and-Problems.md)
- [Circular queue illustration](00-Foundations/Chapter-10-Elementary-Data-Structures/images/circular-queue.svg)
- [Python implementations](Implementations/Python/elementary_structures.py)
- [Python tests](Implementations/Python/test_elementary_structures.py)

**Current:** Chapter 10 complete. Chapter 11 is next.


## Chapter 11 — Complete

- [x] Reopen source PDF printed pages 273–311; capture Sections 11.1–11.5, all exercises 11.1-1–11.5-3, and Problems 11-1–11-4
- [x] Draft notes on direct addressing, chaining, load-factor analysis, hash-function families, open addressing, linear probing, deletion and memory hierarchy
- [x] Draft exercise and problem solutions
- [x] Add Python direct-address, chained-hash and open-address implementations
- [x] Add initial Python unit tests
- [x] Audit Exercises 11.3-5, 11.5-3 and Problems 11-3/11-4; correct the epsilon lower-bound proof and bit-dependency derivation
- [x] Solve Exercise 11.2-4 with circular singly linked chains and successor-copy deletion; document the stable-handle caveat
- [x] Add linear-probing backward-shift deletion; randomized local checks across table sizes 2–19 passed
- [x] Execute exact fetched Python implementation and test contents in a temporary package; all 11 unittest cases passed
- [x] Add an original chaining diagram
- [x] Fetch every Chapter 11 file after final edits; verify README, exercise solutions, SVG, Python implementation/tests, repository map and tracker on GitHub main
- [x] Complete three-way reconciliation against source PDF printed pages 273–311, conversation instructions and GitHub main

Files:
- [Chapter 11 notes](00-Foundations/Chapter-11-Hash-Tables/README.md)
- [Chapter 11 exercises and problems](00-Foundations/Chapter-11-Hash-Tables/Exercises-and-Problems.md)
- [Python hash-table implementations](Implementations/Python/hash_tables.py)
- [Python tests](Implementations/Python/test_hash_tables.py)

**Current:** Chapter 14 complete. Chapter 15 — Greedy Algorithms (draft in progress).


## Chapter 12 — Complete

- [x] Reopen source PDF printed pages 313–330; capture Sections 12.1–12.3, Exercises 12.1-1–12.3-7 and Problems 12-1–12-4
- [x] Draft core notes on BST invariants, traversals, queries, successor/predecessor, insertion, transplant and deletion
- [x] Draft exercise/problem solutions
- [x] Add Python BST implementation and initial unit tests
- [x] Audit Exercise 12.1-1 exact height-2-through-6 constructions and Exercise 12.2-1 invalid search traces (c and e)
- [x] Correct Exercise 12.2-4 with a minimal five-node unsuccessful-search counterexample; verify Exercise 12.3-5 with an explicit noncommuting deletion example
- [x] Complete O(h) successor-pointer-only algorithms for Exercise 12.3-6, including predecessor links and parent lookup
- [x] Audit Problem 12-1 duplicate-key strategies and strengthen the randomized expected-cost argument; verify Problem 12-3 recurrence and Problem 12-4 Catalan derivation
- [x] Exercise BST insertion/deletion logic locally across all 120 insertion permutations of five distinct keys and all 600 deletion steps; every invariant and inorder check passed
- [x] Reconstruct the fetched implementation and all 9 committed unittest cases in local Python; all 9 passed after correcting a test's expected duplicate-key height (the repository checkout itself was unavailable)
- [x] Add original search-path counterexample SVG
- [x] Fetch every Chapter 12 file after final edits; verify notes, exercise solutions, SVG, Python implementation/tests, repository map and tracker on GitHub main
- [x] Complete three-way reconciliation against source PDF printed pages 313–330, conversation instructions and GitHub main

Files:
- [Chapter 12 notes](00-Foundations/Chapter-12-Binary-Search-Trees/README.md)
- [Search-path counterexample illustration](00-Foundations/Chapter-12-Binary-Search-Trees/images/search-path-counterexample.svg)
- [Chapter 12 exercises and problems](00-Foundations/Chapter-12-Binary-Search-Trees/Exercises-and-Problems.md)
- [Python BST implementation](Implementations/Python/binary_search_tree.py)
- [Python BST tests](Implementations/Python/test_binary_search_tree.py)


## Chapter 13 — Draft and audit in progress

- [x] Reopen source PDF printed pages 331–359; capture Sections 13.1–13.4, Exercises 13.1-1–13.4-9 and Problems 13-1–13-3
- [x] Draft notes on red-black properties, black-height, height proof, rotations, insertion fixup and deletion fixup
- [x] Solve Exercises 13.1-1–13.1-6, 13.1-8, 13.2-1–13.2-5, 13.3-1–13.3-6 and 13.4-1–13.4-9; 13.1-7 finite-n extremal ratio still needs a final exact treatment
- [x] Draft solutions for Problems 13-1 persistent sets, 13-2 RB-JOIN and 13-3 AVL trees; final proof audit remains
- [x] Implement sentinel-based red-black tree in Python with search, insert, delete, rotations and invariant validation
- [x] Add initial Python unit tests; expand coverage to all insertion/deletion fixup cases
- [x] Add original red-black insertion/deletion case diagrams
- [x] Reconstruct fetched red-black implementation and all 8 unittest cases locally; all 8 passed, plus 31,434 seeded stress operations with invariant/order checks
- [x] Fetch every Chapter 13 file after final edits; verify notes, exercise solutions, diagrams, Python implementation/tests, repository map and tracker on GitHub main
- [x] Complete three-way reconciliation against source PDF printed pages 331–359, conversation instructions and GitHub main

Files:
- [Chapter 13 notes](00-Foundations/Chapter-13-Red-Black-Trees/README.md)
- [Chapter 13 exercises and problems](00-Foundations/Chapter-13-Red-Black-Trees/Exercises-and-Problems.md)
- [Insertion fixup cases](00-Foundations/Chapter-13-Red-Black-Trees/images/insertion-fixup-cases.svg)
- [Deletion fixup cases](00-Foundations/Chapter-13-Red-Black-Trees/images/deletion-fixup-cases.svg)
- [Python red-black tree implementation](Implementations/Python/red_black_tree.py)
- [Python red-black tree tests](Implementations/Python/test_red_black_tree.py)


## Chapter 14 — Draft and audit in progress

- [x] Reopen source PDF pages for Chapter 14; capture Sections 14.1–14.5, exercises and problems
- [x] Draft notes on rod cutting, matrix-chain multiplication, DP ingredients, longest common subsequence and optimal BSTs
- [x] Solve and audit Exercises 14.1-1 through 14.5-4 and Problems 14-1 through 14-12
- [x] Add Python rod-cutting, matrix-chain, LCS and optimal-BST implementations
- [x] Add initial Python tests and original matrix-chain/LCS diagrams
- [x] Reconstruct fetched Python implementations and all 10 committed unittest scenarios locally; all passed after adjusting the edit-distance test's operation costs. Also passed 350 randomized LCS/matrix-chain checks and 500 randomized LIS checks
- [x] Fetch every Chapter 14 file after final edits; verify notes, exercise/problem solutions, diagrams, Python implementation/tests, repository map and tracker on GitHub main
- [x] Complete three-way reconciliation against source PDF printed pages 361–416, conversation instructions and GitHub main

Files:
- [Chapter 14 notes](00-Foundations/Chapter-14-Dynamic-Programming/README.md)
- [Chapter 14 exercises and problems](00-Foundations/Chapter-14-Dynamic-Programming/Exercises-and-Problems.md)
- [Matrix-chain split diagram](00-Foundations/Chapter-14-Dynamic-Programming/images/matrix-chain-split.svg)
- [LCS dependency diagram](00-Foundations/Chapter-14-Dynamic-Programming/images/lcs-dependencies.svg)
- [Python dynamic-programming implementations](Implementations/Python/dynamic_programming.py)
- [Python dynamic-programming tests](Implementations/Python/test_dynamic_programming.py)


## Chapter 15 — Draft and audit in progress

- [x] Reopen source PDF pages for Chapter 15; capture Sections 15.1–15.4, Exercises 15.1-1–15.4-5 and Problems 15-1–15-2
- [ ] Draft notes on greedy-choice property, activity selection, fractional knapsack, Huffman coding and online caching
- [ ] Solve and audit all exercises and problems against the source
- [ ] Add Python activity-selection, fractional-knapsack, Huffman and caching implementations
- [ ] Add Python tests and original greedy-choice/Huffman diagrams
- [ ] Execute reconstructed fetched implementation/tests and randomized checks; fix failures
- [ ] Fetch every Chapter 15 file and reconcile source, chat and GitHub main

Files:
- [Chapter 15 notes](00-Foundations/Chapter-15-Greedy-Algorithms/README.md)
- [Chapter 15 exercises and problems](00-Foundations/Chapter-15-Greedy-Algorithms/Exercises-and-Problems.md)
- [Python greedy algorithms](Implementations/Python/greedy_algorithms.py)
- [Python tests](Implementations/Python/test_greedy_algorithms.py)
