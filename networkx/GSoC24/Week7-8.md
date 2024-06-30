---
title: "Blog4: : GSoC (nx-parallel)"
author: Aditi Juneja
date: 2024-06-29 04:07:00 +0530
---

# Blog4: GSoC (nx-parallel)

## Week 7-8 (14th June to 27th June, 2024)

### GSoC - Coding Period (Phase 1)

## 1. From the last blog

I'm excited to share that two significant pull requests have been merged:
- [PR#7404](https://github.com/networkx/networkx/pull/7404): Refactoring and enhancing user-facing `Backend and Configs` docs.
- [PR#7398](https://github.com/networkx/networkx/pull/7398): Added `colliders` and `v_structures` and deprecated `compute_v_structures` in `dag.py`.

## 2. Adding configs to nx-parallel

Initially, I planned to create a context manager in nx-parallel for modifying all the joblib-related parameters. However, with Erik proposing two context managers in [PR#7485](https://github.com/networkx/networkx/pull/7485) and [PR#7363](https://github.com/networkx/networkx/pull/7363), adding another context manager would be redundant. Instead, I plan to contribute to these PRs in the coming weeks.

In the previous blog, I mentioned that it might be possible to set the default config at the time of importing NetworkX by adding the default configs as a key-value pair in the dictionary returned by the `get_info` function. This approach has been updated in [PR#68](https://github.com/networkx/nx-parallel/pull/68). However, I was unsure about how `joblib.Parallel` calls should be made within each algorithm. Inspired by [PR#7](https://github.com/networkx/nx-parallel/pull/7), I discussed with Dan the possibility of consulting the PR's author. Unfortunately, that might not be the case.

Moving forward, I plan to seek inspiration from the sklearn or joblib projects. And the more that I think about it, I feel like the users might prefer changing parameters like `n_jobs` for each function call instead of having them as global config options. This doesn't necessarily mean adding `n_jobs` to each function's header; or it could be set explicitly, similar to sklearn. I also intend to contribute to [PR#7502](https://github.com/networkx/networkx/pull/7502), which adds this functionality.

## 3. Creating a conda recipe for nx-parallel

Towards the end of last week, I created a recipe PR for conda-feedstock for nx-parallel ([PR#26768](https://github.com/conda-forge/staged-recipes/pull/26768)), which addresses [Issue #65](https://github.com/networkx/nx-parallel/issues/65) ([a nice reference](https://www.pyopensci.org/python-package-guide/tutorials/publish-conda-forge.html) for creating a conda-feedstock). This PR depends on [PR#69](https://github.com/networkx/nx-parallel/pull/69), which switches the backend build tool from hatchling to setuptools. I hope this PR will be merged by the end of this week. Once merged, I plan to locally test the workflow tests under [PR#26768](https://github.com/conda-forge/staged-recipes/pull/26768) and make it ready for review.

## 4. Other Activities in the Community

In the last week, we welcomed two "first-time-contributors" to NetworkX, and their PRs were merged within a few days of opening(one merged, one about to be merged). This was a  result of creating "good-first-issues" and labeling existing issues as "good-first-issues". Hopefully, they will continue to contribute in the future. Additionally, @Peiffap has been very active in the community recently, and I want to thank them for their contributions. I also quickly fixed or reported CI failures due to the new numpy 2.0 and scipy 1.14.0 releases, ensuring NetworkX's compatibility with other new releases.

On 22nd June 2024, I gave a 10-minute lightning talk at PyRustLin meet-up in Delhi. Since most of the audience was unfamiliar with the graph data structure, I explained how we create backends using `entry_points` with an example from my main library [coco](https://github.com/Schefflera-Arboricola/coco)(with a `Chocolate` class) and its backend package [parallel-coco](https://github.com/Schefflera-Arboricola/parallel-coco)(with a `ParallelChocolate` class). I think it might be a very informal version of what I have heard [`spatch`](https://github.com/scientific-python/spatch)(Scientific Python dispATCH) will be in the future. Also, I think the talk sparked a few interesting conversations about backends and open source in general, among a small group of people. And I plan to expand more on `coco` and `parallel-coco` in the future. It was a great networking opportunity!

### Recent Contributions

- **Opened:** [PR#7518](https://github.com/networkx/networkx/pull/7518) - Made `plot_image_segmentation_spectral_graph_partition` example compatible with scipy 1.14.0
- **Reviewed:** [PR#7506](https://github.com/networkx/networkx/pull/7506) - Fix dispatch tests when using numpy 2
- **Resolved:** [Issue#7501](https://github.com/networkx/networkx/issues/7501) - Not compatible with Numpy 2.0
- **Reviewed:** [PR#7511](https://github.com/networkx/networkx/pull/7511) - Strong product docs update
- **Reviewed:** [PR#7524](https://github.com/networkx/networkx/pull/7524) - Fixed the citation in dominance.py
- **Reviewed:** [PR#7475](https://github.com/networkx/networkx/pull/7475) - Various improvements in information centrality
- **Reviewed:** [PR#7514](https://github.com/networkx/networkx/pull/7514) - Prettify README.rst
- **Reviewed:** [PR#7500](https://github.com/networkx/networkx/pull/7500) - Update NetworkX reference links in doc index
- **Commented:** [PR#7443](https://github.com/networkx/networkx/pull/7443) - Addition of DomiRank centrality to NetworkX
- **Raised:** [Issue #7505](https://github.com/networkx/networkx/issues/7505) - Dispatch test failing due to graph `adj` comparison for some algorithms in `expanders.py`
- **Raised:** [Issue #7510](https://github.com/networkx/networkx/issues/7510) - Fix the docs of `strong_product`
- **Raised:** [Issue #7519](https://github.com/networkx/networkx/issues/7519) - Clarification of `networkx.karate_club_graph()` dataset
- **Answered:** [Discussion #7509](https://github.com/networkx/networkx/discussions/7509) - Description on strong product
- **Closed:** [Issue #7189](https://github.com/networkx/networkx/issues/7189) - "dispatch" decorator needs documentation for contributors and readers of code
- Also, I worked on the [nx-j4f](https://github.com/Schefflera-Arboricola/nx-j4f) backend.
