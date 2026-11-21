# CLRS Study Progress

**Primary source:** CLRS, Fourth Edition (2022)  
**Working language:** Python  
**Target branch:** `main`

## Completion audit — 21 November 2026

Chapters 1 and 2 have been expanded, cross-checked against the complete chapter page ranges in the uploaded PDF, and published to `main`. Chapter 2 includes original SVG teaching illustrations and Python implementations with unit tests.

| Chapter | Coverage | Status |
|---|---|---|
| 1 — The Role of Algorithms in Computing | Sections 1.1–1.2, Exercises 1.1-1–1.2-3, Problem 1-1 complete table | <badge>Study package complete</badge> |
| 2 — Getting Started | Sections 2.1–2.3, pseudocode conventions, all chapter exercises 2.1-1–2.3-8, Problems 2-1–2-4 | <badge>Study package complete</badge> |

## Chapter 1
- [x] Section 1.1: algorithms, problem specifications and instances, correctness, applications, data structures, techniques, NP-completeness, approximation, parallel and online models
- [x] Section 1.2: efficiency, insertion-sort/merge-sort growth comparison, hardware example, algorithms as a technology, machine learning and data science
- [x] Exercises 1.1-1 through 1.1-6
- [x] Exercises 1.2-1 through 1.2-3
- [x] Problem 1-1: all eight functions and seven time budgets
- [x] Independent numerical checks for integer thresholds and inverse formulas

Files:
- [Chapter 1 notes](00-Foundations/Chapter-01-Role-of-Algorithms/README.md)
- [Chapter 1 exercises and Problem 1-1](00-Foundations/Chapter-01-Role-of-Algorithms/Exercises-and-Problem-1-1.md)

## Chapter 2
- [x] Section 2.1: sorting problem, keys and satellite data, insertion sort, loop invariant, correctness
- [x] Pseudocode conventions: block structure, loops, comments, local variables, indexing, subarrays, objects/references, NIL, parameters, return, short-circuit Boolean operators, error
- [x] Section 2.2: RAM model, word-size assumptions, input-size measures, statement-count analysis, best/worst case, average-case caveat, order of growth
- [x] Section 2.3.1: incremental method, divide/conquer/combine, MERGE, MERGE-SORT
- [x] Section 2.3.2: recurrence setup, floors/ceilings, merge-sort recurrence and recursion-tree analysis
- [x] Exercises 2.1-1 through 2.3-8
- [x] Problems 2-1 through 2-4
- [x] Original SVG visuals: playing-card insertion sort, insertion-sort array trace, merge-sort recursion
- [x] Python implementations for insertion sort and merge sort
- [x] Unit tests for examples, empty/singleton arrays, duplicates, negative values, sorted and reverse-sorted inputs
- [x] Local algorithm checks: 14 function/input combinations passed

Files:
- [Chapter 2 notes](00-Foundations/Chapter-02-Getting-Started/README.md)
- [Chapter 2 exercises and problems](00-Foundations/Chapter-02-Getting-Started/Exercises-and-Problems.md)
- [Playing-card illustration](00-Foundations/Chapter-02-Getting-Started/images/insertion-sort-playing-cards.svg)
- [Insertion-sort array trace](00-Foundations/Chapter-02-Getting-Started/images/insertion-sort-array-trace.svg)
- [Merge-sort recursion illustration](00-Foundations/Chapter-02-Getting-Started/images/merge-sort-recursion.svg)
- [Insertion sort Python](Implementations/Python/insertion_sort.py)
- [Merge sort Python](Implementations/Python/merge_sort.py)
- [Sorting unit tests](Implementations/Python/test_sorting.py)

## Completion standard
The notes are original explanations aligned to the source's organization. The SVGs are newly drawn teaching diagrams, not scans or reproductions of CLRS figures. The Python implementations are translations for study; they are not the textbook's pseudocode verbatim.

**Next:** Begin Chapter 3 only after reviewing Chapters 1 and 2 and completing the self-assessment prompts.
