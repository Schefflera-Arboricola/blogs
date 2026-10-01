---
author: Aditi Juneja
title: "Lightening talk - IndiaFOSS 2026"
status: "rejected"
date: 25-09-2026
---

# Introducing sphinx-benchmark: Why are my Sphinx docs builds taking so long?!

## Session Description

Sphinx builds the documentation for much of the scientific Python ecosystem, including NumPy, pandas, Matplotlib, and CPython itself. For large projects a docs build can take many minutes, sometimes more than an hour, and it often runs in CI on every pull request. Sphinx is downloaded more than 4 million times a week, mostly by CI runs, so slow builds cost the whole community a lot of time, compute, and energy. Still, when a maintainer asks why their build is slow, the best answer is usually a guess.

In this lightning talk, I'll introduce sphinx-benchmark (https://github.com/Schefflera-Arboricola/sphinx-benchmark), a Sphinx extension that answers that question. It shows where a build spends its time, down to the specific function in a specific extension, theme, or module.

Under the hood it does two things. It wraps and times some of the Sphinx's core components -- events listeners, handlers for each event emmission. Second, it samples the function call stack from a background daemon thread. With the sampling, it can measure the time spent between events, which event timing alone misses and where a lot of the cost turned out to be. I'll explain what events are, so no prior Sphinx knowledge is needed.

The talk will cover:

- A live demo: running the extension on a real project and walking through the report.
- An optimisation: a SunPy maintainer used this extension to find one slow theme handler, and a single PR (https://github.com/pydata/pydata-sphinx-theme/pull/2477) cut their docs build from 317 to 190 seconds, about 40% faster. The fix was in pydata-sphinx-theme, so every project using that theme benefits.
- How advanced features in python (like daemon threads and sys._current_frames()) could be applied while solving a technical problem.

Intended Audience:

- Anyone who writes or maintains documentation and has waited on a slow build/CI runs
- Developers curious about profiling a large Python application they didn't write
- Anyone who wants to see less common Python features, like daemon threads, function stacks, etc. , being used in a real-world project.


No prior knowledge of Sphinx internals is needed. Basic Python knowledge is expected.

## Key Takeaways

1. Find and fix slow docs builds. Attendees will know how to benchmark their own Sphinx build, read the results, and target the parts that matter.

2. Practical profiling techniques. How a background sampling thread with sys._current_frames() can profile code you don't control, and where deterministic profilers fall short.

3. How Sphinx works. A short, approachable look at Sphinx's build phases and event callback API, and at how extensions and themes hook into it.

References: https://labs-nvwpzkk6g-quansight.vercel.app/blog/sphinx-benchmark

## Session Categories

Introducing a FOSS project or a new version of a popular project
Tutorial about using a FOSS project
Contributing to FOSS
Technology architecture
Engineering practice - productivity, debugging
Story of a FOSS project - from inception to growth

**Talk License: MIT License**
