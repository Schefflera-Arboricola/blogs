---
title: "Blog2: : GSoC (nx-parallel)"
author: Aditi Juneja
date: 2024-06-01 18:15:00 +0530
---

# Blog2: GSoC (nx-parallel)

## Week 3-4 (17th May to 30th May, 2024)

### GSoC - Community Bonding Period

## 1. Revisiting nx-parallel ([PR#63](https://github.com/networkx/nx-parallel/pull/63))

### 1.1 Making docstrings more aligned with Sphinx guidelines

In nx-parallel, while creating the `get_info` function for the `networkx.backend_info` entry_point, we extract the docstrings of all the functions in the nx_parallel package and then do some simple string manipulations to get the function's information in a dictionary format that is needed by NetworkX docs to build the "Additional backend implementation" box (see `_make_doc` method in the `_dispatchable` class in [`backends.py`](https://github.com/networkx/networkx/blob/main/networkx/utils/backends.py) for more).

Earlier, the way nx-parallel function's docstrings needed to be written in a format that was not fully aligned with the sphinx guidelines. Like, we needed 2 leave 2 blank lines between two parameters in the `Parameter` section instead of the standard one blank line, and there is a link to NetworkX docs at the end which also doesn't align with the sphinx guidelines. So, I updated the docstrings of the functions in the nx-parallel package to make them more aligned with the [Sphinx guidelines](https://the-ultimate-sphinx-tutorial.readthedocs.io/en/latest/_guide/_styleguides/docstrings-guidelines.html) and I also updated the string manipulations used for dictionary extraction. It was necessary to keep it aligned with the Sphinx guidelines because NetworkX and my other Scientific Python libraries use the Sphinx theme for their docs and keeping it aligned would be helpful in the future when nx-parallel is big enough to have a docs website.

Now, the docstrings are more aligned with the Sphinx guidelines. We only extract the first paragraph of the function's description and the first paragraph of each parameter's description to create the `functions` dictionary returned by `get_info`. Also, the NetworkX docs link is now moved just above the `Parameters` section, as the last paragraph of the function's description. Also now, we only need to leave one blank line between two parameters in the `Parameter` section. Refer [PR#63](https://github.com/networkx/nx-parallel/pull/63) for implementation details.

### 1.2 Updating the `Dispatcher` class

In nx-parallel the `networkx.backends` entry_point points to the `Dispatcher` class in `interface.py`. It is used at many places as an Interface and doesn't have much to do directly with the dispatching process as mentioned in [this review comment](https://github.com/networkx/networkx/pull/7404#discussion_r1610816636) by Erik. So, I renamed it to `BackendInterface`. I also updated the `convert_from_nx` method in the `BackendInterface` class by removing the unused args in the header.

### 1.3 Enhancing `ParallelGraph` class

While I was going over the `BackendInterface` class, I also updated the `ParallelGraph` class in `interface.py`, which was one of the points in the experimental section of my proposal. I updated it so that now it does not give errors with `nxp.ParallelGraph()` or `nxp.ParallelGraph([(1, 2), (2, 3)])` kind of initializations. I also added the `__str__` method to the `ParallelGraph` class so that when a `ParallelGraph` object is passed in `print()`, it prints `ParallelGraph with n nodes and m edges` instead of `<nx_parallel.interface.ParallelGraph object at 0x10495e6d0>`.

In the proposal, I talked about having parallel versions of `add_weighted_edges_from`, `clear_edges`, etc. in the `ParallelGraph` class. However, I have started to think that it would not be a great idea as this could lead to having too many parallel processes when these methods would be used in parallel implementations. And in nx-parallel, the first thing we do in all the algorithms is to assign the graph variable `G` as the `graph_object` of the `ParallelGraph`, which is the NetworkX graph, so then, having parallel versions of these methods in the `ParallelGraph` class would not be of much use. But, this still needs to be discussed with my mentors.

I also did some other maintenance things in this revisiting PR, like, updating the `pip install`s in the `test.yml` GitHub workflow file.

## 2. Future implementation plans and proposal updates

In the coming weeks, I plan on working on making the `ParallelGraph` class more consistent with NetworkX's `Graph` class by adding more methods like `__len__`, etc.

And working on adding config and updating benchmarks seems more important to me right now than working on creating a decorator as proposed in the GSoC proposal's first point. And last time I asked my mentors about moving the benchmarking stuff to the experimental section and they agreed on it, but now I think benchmarking is more important than I initially thought it was so I'm keeping it in the main proposal items only. And I think I'll be able to give more hours in the coming weeks as my final exams will end on 6th June.

And about updating the timing script, I have started to think it will be better if we benchmarked on datasets, like python-graphblas, instead of random graphs. I also plan on only having a few heatmaps(or any other better visualisation for showing speedups) in the `timing` folder because not all algorithms in nx-parallel show significant speedups. Also, Mridul suggested me to look into using [conbench](https://conbench.github.io/conbench/) for benchmarking instead of ASV. So, in the coming weeks, I plan on doing that as well, and discussing this more with my mentors.

I also converted the GSoC proposal into a `.md` file so that it's easier to keep track of the updates I'm making for my mentors and for me as well.

Apart from the GSoC proposal items, I'm also planning to get [PR#7398](https://github.com/networkx/networkx/pull/7398) and [PR#7404](https://github.com/networkx/networkx/pull/7404) merged in the next few days. In [PR#7398](https://github.com/networkx/networkx/pull/7398), I have to rebase the development branch, update a docstring example, and then address [this review comment](https://github.com/networkx/networkx/pull/7398#pullrequestreview-2069173536) about having `v_structures` in a `dag` namespace. In [PR#7404](https://github.com/networkx/networkx/pull/7404), I have to address Erik's review comments, clarify in the docs which features are experimental and which are not going to change(based on the review I got in nx-community meetings), add a few lines about recently added logging. I also plan on reviewing [PR#60](https://github.com/networkx/nx-parallel/pull/60) and getting it merged and then making corresponding changes in the revisiting PR#63.

## 3. Other Activities in the community

- https://github.com/networkx/nx-parallel/pull/60
- https://github.com/networkx/networkx/pull/7300
- In the nx-community and dispatch meetings, there were talks about creating a cookie-cutter from the [nx-j4f](https://github.com/Schefflera-Arboricola/nx-j4f) backend, which I created a while ago. So, I did some cleaning and maintenance stuff in the nx-j4f repo, to make it more usable by a potential backend developer.
- submitted a talk proposal on NetworkX dispatching and nx-parallel for EuroSciPy and PyCon India
- updated the poster for Scipy Con
