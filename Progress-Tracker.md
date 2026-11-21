# CLRS Study Progress

**Primary source:** CLRS, Fourth Edition (2022)  
**Working language:** Python  
**Target branch:** `main`

## Completion audit — 21 November 2026

Chapters 1–4 are complete study packages. Each chapter has been checked against the uploaded PDF, this conversation's requirements and prior decisions, and the committed GitHub files.

| Chapter | Coverage | Status |
|---|---|---|
| 1 — The Role of Algorithms in Computing | Sections 1.1–1.2, Exercises 1.1-1–1.2-3, Problem 1-1 | **Complete** |
| 2 — Getting Started | Sections 2.1–2.3, pseudocode conventions, Exercises 2.1-1–2.3-8, Problems 2-1–2-4 | **Complete** |
| 3 — Characterizing Running Times | Sections 3.1–3.3, Exercises 3.1-1–3.3-9, Problems 3-1–3-7 | **Complete** |
| 4 — Divide-and-Conquer | Sections 4.1–4.7, Exercises 4.1-1–4.7-6, Problems 4-1–4-7 | **Complete** |
| 5 — Probabilistic Analysis and Randomized Algorithms | Sections 5.1–5.4, Exercises 5.1-1–5.4-8, Problems 5-1–5-2 | **Complete** |

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

## Completion standard

A chapter is complete only after its source pages, the relevant conversation instructions and prior decisions, and the committed GitHub files agree. The notes are original explanations; SVGs are original teaching diagrams, not textbook scans. Tests are reported as passed only after execution.

**Next:** Begin Chapter 5 after reviewing Chapters 1–4 and completing the self-assessment prompts.
