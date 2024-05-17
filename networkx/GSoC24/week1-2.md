---
title: "Blog1: : GSoC (nx-parallels)"
author: Aditi Juneja
date: 2024-05-17 16:30:00 +0530
---

# Blog1: GSoC (nx-parallels)

## Week 1-2 (3rd May to 16th May, 2024)

### GSoC - Community Bonding Period

#### 1. Automating `get_info` updation

NetworkX uses [`entry-points`](https://packaging.python.org/en/latest/specifications/entry-points/) to automatically discover its backends. Backends can define two `entry-points`, the `networkx.backends` entry-point which stores the `Dispatcher` class and `networkx.backend_info` entry-point which stores the `get_info` function which is loaded and called by networkx while creating the docs website. The `get_info` function returns a dictionary having all the information(metadata) about the backend, something like this:

```.py
{
    "backend_name": "parallel",
    "project": "nx-parallel",
    "package": "nx_parallel",
    "url": "https://github.com/networkx/nx-parallel",
    "short_summary": "Parallel backend for NetworkX algorithms",
    "functions": {
        "square_clustering": {
            "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/cluster.py#L10",
            "additional_docs": "The nodes are chunked into `node_chunks` and then the square clustering coefficient for all `node_chunks` are computed in parallel over all available CPU cores.",
            "additional_parameters": {
                'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes (or nbunch) as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the number of CPU cores."
            },
        },
        ...
        ...
    }
}
```

This metadata is used to add a note about the additional backend implementation for the functions present in the `functions` dictionary above (ref. end of [`square_clustering` docs](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.square_clustering.html)). Check out the [NetworkX backend docs](https://networkx.org/documentation/latest/reference/backends.html) to know more about the NetworkX backend architecture.

Earlier, the `get_info` function was generating the `functions` dictionary using another function that parsed through all the functions in the nx_parallel package, and extracted their docstrings and from each docstring extracted `additional_docs` and `additional_parameters`. But, creating a `functions` dictionary like this was causing this [issue#52](https://github.com/networkx/nx-parallel/issues/52) because I was importing nx_parallel in the `get_info` and I resolved it in [PR#53](https://github.com/networkx/nx-parallel/pull/53) just by directly writing the `functions` dictionary and moving the `get_info` function outside of `nx_parallel` package to the `_nx_parallel` package.

But, this approach caused us to manually update the `functions` dictionary every time we updated a docstring in the nx_parallel package. So, my initial solution was to add a pre-commit hook that would automatically update the `get_info` function. I was working on it before writing my GSoC proposal(ref. [PR#55](https://github.com/networkx/nx-parallel/pull/55)) and by the time I submitted my proposal I started to see the problems with this approach like there could be lots of merge conflicts in PRs if we do the updation in a pre-commit as I've explained in [this comment](https://github.com/networkx/nx-parallel/pull/55#issuecomment-2026804506). I also thought of doing this automatic update in GitHub workflow tests but that also had its own issues. So, at the start of the community bonding period, I created [issue#62](https://github.com/networkx/nx-parallel/issues/62) summarising all the approaches I could think of along with the issues they had. And [Erik's comment](https://github.com/networkx/nx-parallel/issues/62#issuecomment-2102256774) on this issue got me started into looking at how nx-cugraphs(GPU-accelerated backend for networkx) does it. I think they use a decorator which extracts the additional docs and parameters from a function. They also use `Makefile`s which I'm trying to understand how they work. And they are also doing the update in a pre-commit hook and Erik mentioned that merge conflicts were managable.

But, seeing a decorator being used in nx-cugraph gave me some ideas on how I could use a decorator for nx-parallel algorithms for a bunch of things that I proposed in my GSOC proposal. Like:

- for extracting additional docs and parameters from a function's docstring and adding them to the `get_info` function
- for automatically adding the function to the `Dispatcher` class
- and having a `name` parameter in the decorator that will let us change the name of the function at the time of dispatching, and it would resolve the naming issue we were having(ref. [PR#56](https://github.com/networkx/nx-parallel/pull/56),  [PR#32](https://github.com/networkx/nx-parallel/pull/32))
- this decorator could also perform the graph conversion(from `nxp.ParallelGraph` to `nx.Graph`) that we perform in all the functions, as of now.
- and this might also help in indicating if a function doesn't show any speedups (wrt to its sequential implementation) or if a function is proven to be impossible to parallelize.

#### 2. Timing script

A while back I reported this [issue#51](https://github.com/networkx/nx-parallel/issues/51) about how re-running the present timing script generates some very inconsistent heatmaps. These were caused because we were running the algorithms only once and timing them. So, if your laptop was running a heavier process in the background or it went into sleep mode then the time reported in heatmaps would be way more than the actual time. I also opened the [PR#61](https://github.com/networkx/nx-parallel/pull/61) in which I used the `timeit.time` function instead of `time.time` but I don't think it made any difference. So, I started looking into how to time processes that create other parallel processes. Also, it didn't seem very clear to me what exactly it meant to time processes that are running in parallel. Do we take the process that took the maximum time or take an average time? And also we don't just have to time the parallel part, but also the non-parallel part of an algorithm. So, it seemed reasonable to account for the start time and end time of running an algorithm multiple times and then average out the time differences.

I also looked into how ASV benchmarks time their benchmarks and they use [`timeit.default_timer()`](https://docs.python.org/3/library/timeit.html#timeit.default_timer) and it doesn't remove the inconsistencies caused by the laptop going into sleep mode or other heavier processes running in the background, etc. But, they run it multiple times to minimize the effects of such inconsistencies so it seemed reasonable to me to do the same for heatmaps as well. (ref. [asv timing docs](https://github.com/airspeed-velocity/asv/blob/main/docs/source/writing_benchmarks.rst#timing))

But, before implementing all this and re-generating all the heatmaps, I want to dig a bit deeper and figure out how exactly the `timeit.default_timer()` works internally in the coming weeks. And also if there are any other better alternative timing functions. And also look into how running and timing parallel processes on my local machine is different from running and timing them on the NetworkX's VM over SSH.

#### 3. Revisiting nx-parallel algorithms

At the start of the community bonding period, I opened the [PR#63](https://github.com/networkx/nx-parallel/pull/63) in which I revisited all the algorithms in nx-parallel and added chunking and `get_chunks` to all the algorithms and this goal was in the "expanding" section and not the "revisiting" section in my GSoC proposal, but it seemed more apt to include it this PR(to know more about chunking and and `get_chunks` refer the [chunking section](https://github.com/networkx/nx-parallel/blob/main/CONTRIBUTING.md#chunking) in Contributor's guide of nx-parallel that I wrote or [this previous blog](https://schefflera-arboricola.github.io/Schefflera-Arboricola/NetworkX-Internship-Working-on-nx-parallel) by me).

I also had to add testing for all `get_chunks`. So, instead of adding a lot of tests, I decided to test `get_chunks` for all functions together in one general test that tests the `get_chunks` for any given function. And the `get_chunk` generates a random chunking for testing. But, right now it ignores functions that require extra arguments other than G. So, I'll probably have to write separate tests for such functions but I wanted to know what my mentors think of this so I marked it "Ready for review" and am waiting for their reviews.

I also revisited and enhanced the `is_reachable` and the `tournament_is_strongly_connected` in `tournament.py`, which were earlier not showing any speedups. This was probably happening because the parallel processes were creating multiple parallel child processes which were further creating multiple parallel child processes, so, so many parallel processes were probably slowing down these algorithms. I observed this behavior earlier also when I was working on the [PR#44](https://github.com/networkx/nx-parallel/pull/44) and I talked a little bit about it in my [previous blog](https://schefflera-arboricola.github.io/Schefflera-Arboricola/NetworkX-Internship-Working-on-nx-parallel) as well. After reducing the number of parallel processes being created in these algorithms I was able to achieve a speedup of 2.9x for `is_reachable` for a 400-node random tournament graph and a speedup of 3.3x for `tournament_is_strongly_connected` for a 50-node random tournament graph.

And lastly, I checked if there were any updates from nx 3.3 and there were none for the algorithms in nx-parallel.

#### 4. Switching from `hatchling` to `setuptools`

One more goal in the proposal was to switch from `hatchling` to `setuptools` as  nx-parallel is growing and maturing it’d be better to use setuptools because of its better feature support, flexibility, compatibility, and interactive capabilities as compared to Hatchling. Also, setuptools is more widely used and it's better for bigger projects and we need to explicitly mention all the packages(unlike hatchling), which ensures that all packages are being built. I switched to setuptools in [PR#67](https://github.com/networkx/nx-parallel/pull/67).

#### 5. Proposal updates

As suggested to all contributors in the GSoC contributor's meeting, I updated my proposal in the community bonding period.

[old proposal](https://docs.google.com/document/d/1xF8dW5-1OAapsTnvsdp9EBEuWAf-Jbxq3kC9kTroAiE/edit?usp=sharing) --> [updated proposal](https://docs.google.com/document/d/1Y1SjRx9hy9xzvRF3QlhLyCBPjulezOkuNMEqwhIC8Fo/edit?usp=sharing)

I restructured the proposal into 8 development branches instead of 3 sections("Things to revisit", "Things to expand", "Experimental things"). I haven't added any new deliverables. I bundled all the deliverables mentioned in the last paragraph of the "Automating `get_info` updation" section above into a "Decorator branch". And bundled all the things mentioned above in the revisiting algorithms section into one branch. I also created and added an ideal workflow diagram in the updated proposal.

And more importantly, I have updated the "Schedule of Deliverables" section to reflect additional tasks I have undertaken beyond those initially proposed for the community bonding period. Please refer to the original proposals for details, as other changes in this section are straightforward.

Additionally, I have requested permission from my mentors to relocate the benchmarking tasks to the experimental section. This adjustment is necessary because as I was going through the joblib docs, I realised that setting up the configuration will require significant time due to my unfamiliarity with the various parallel backends. Understanding and integrating these with nx-parallel will be time-consuming. If relocating the tasks is not feasible at this point, I have suggested a possible extension of the project timeline by 2 weeks.

#### 6. Other participations/contributions in NetworkX in the past two weeks

- https://github.com/networkx/networkx/pull/7434
- https://github.com/networkx/networkx/discussions/7450
- https://github.com/networkx/networkx/discussions/7439
- https://github.com/networkx/networkx/discussions/7440
