Note: This is the initial project description provided by my mentors.

## Strategies for profiling and optimising Sphinx documentation builds

Skills needed: Python programming, comfort  reading and navigating a large existing codebase, some familiarity with profiling tools, benchmarking frameworks, and CI workflows (can be learned as part of the internship). It would also be useful to have some exposure to writing compiled code exposed as Python extension modules (Cython/PyO3 would be good options), but is not expected beforehand. Rust can be picked up, too.

### Project description

> This write-up is an early draft and notes various themes of an experimental nature for a project, and the scope may change as it proceeds and based on the discoveries that show up.

Sphinx is the documentation generation engine used throughout much of the Python ecosystem, including CPython, NumPy, SciPy, PyTorch, and the Linux kernel. On large projects, a full build can take several minutes, and there is currently no benchmark suite or profiling setup inside the Sphinx repository that tells us where all that time goes. Without a reliable way to measure builds, it is hard to know which changes are worth making, so much of the performance discussion so far has relied on various educated guesses by the community in the absence of structured data.

This project is meant to be open-ended and a little experimental. The first part is about building the higher-level tools to measure where Sphinx spends its time, and the second part is about using what we learn to make builds faster, including some lower-level experiments with compiled code. There is also scope to contribute towards fixing various identified issues in the ecosystem that slow down documentation builds (see below).

One goal is to set up a dependable way to benchmark and profile Sphinx builds, and then use it to land real speedups by combining safe, upstreamable fixes with a few more adventurous prototypes.

A few items of note, which can be picked up during the twelve weeks:
- We want a small set of representative (medium to large sized, with more than a few hundreds of files) documentation projects that can be built repeatedly under timing and profiling, ideally broken down by phase so we can see how much time goes into reading the source files, resolving cross references, autodoc, writing outputs, and the finishing steps. The only timing tool that ships with Sphinx today covers just the reading phase, so most of this will be untested waters for us.
- An investigation into the problem as noted in https://github.com/sphinx-doc/sphinx/issues/14277
- A fix for this issue in the PyData Sphinx Theme, as an example of harbouring support across the Sphinx ecosystem as a whole, beyond the repository: https://github.com/pydata/pydata-sphinx-theme/issues/762. This can be a good way to learn more about Sphinx's internals.
- Here's a list of some Sphinx optimisations that can be pursued (not all need to be done during the internship timeline, and even a portion of them would be useful):
    - The work that the HTML builder does as part of the finish phase work runs serially right now. The parallel executor for the finish-up tasks is disabled in the code, so index generation, asset copying, and the search index dump all run sequentially, even in a parallel build (`Builder.build` always uses `SerialTasks`). This should use `ParallelTasks`, if feasible.
    - Resolving cross-references does not parallelise, so under `sphinx-build -j`, the worker processes only run `write_doc`. The main process still resolves every page on its own (which runs the post-transforms and toctree resolution) before handing off the work.
    - Parallel reads re-pickle the whole environment, so each worker pickles the entire `BuildEnvironment` and ships it back to the main process for merging, which adds a reasonable amount of overhead that scales with project size.
    - The intersphinx inventory parsing is single-threaded per file. Fetching across projects is already parallel, but each `.inv` file is fully decompressed and parsed line by line with a regex on a single thread.
    - Reference lookups can be linear. For example, when resolving short or ambiguous Python references, the domain falls back to scanning every registered object – so the cost grows with the number of objects per lookup.

A second, and I'd say more experimental goal is to take one well-isolated path that the profiler flags after it's set up and prototype it in Cython or Rust via PyO3 to extract speedups. This does not need to be a single large native extension with a bunch of features – rather, it can be designed as a Sphinx extension that incrementally speeds up builds with each version.

There might also be some scope to explore some libraries in Rust that are already written for a subset of tasks that Sphinx does: https://github.com/flying-sheep/rust-rst

### Expected outcomes

- A reproducible benchmark and profiling setup for Sphinx builds for a few websites, with a per-phase breakdown, that can either live in the Sphinx repository or, perhaps better, as a companion tool elsewhere.
- A bunch of measured optimisations that are either merged or proposed upstream in Sphinx or as a Sphinx extension, or so on.
- One compiled or otherwise experimental prototype that can be taken far enough to give a clear answer on whether it is worth pursuing further.
- A blog post (or a series of smaller ones) of what we learned about Sphinx build performance, so that the work done can stay useful for the community even for the parts that do not make it into a release.
- If time allows:
    - A simple dashboard to track Sphinx documentation build times across commits, in the same spirit as https://speed.python.org, set up via GitHub Pages.

### Useful links

- https://github.com/sphinx-doc/sphinx
- https://github.com/sphinx-doc/sphinx/issues/14277
- https://github.com/pydata/pydata-sphinx-theme/issues/762
- https://github.com/chrisjsewell/sphinx-process-graph
- https://github.com/python/pyperformance
- https://speed.python.org
