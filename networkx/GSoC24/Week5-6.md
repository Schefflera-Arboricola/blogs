---
title: "Blog3: : GSoC (nx-parallel)"
author: Aditi Juneja
date: 2024-06-16 20:00:00 +0530
---

# Blog3: GSoC (nx-parallel)

## Week 5-6 (31th May to 13th June, 2024)

### GSoC - Coding Period (Phase 1)

## 1. From the last week

- Revisiting nx-parallel [PR#63](https://github.com/networkx/nx-parallel/pull/63) got merged. In the last blog, I talked about adding more methods to the `ParallelGraph` class but on further reflection, it seemed better to not add them because we don't use `ParallelGraph` in any of the algorithms right now. We convert them to NetworkX graphs at the start of all the algorithms. So, I just updated the ones that I had already added.
- Reviewed and merged the adding parallel version of `edge_betweenness_centrality` [PR#60](https://github.com/networkx/nx-parallel/pull/60). I pushed a few final changes in the README and the tests and merged this one.
- [PR#7398](https://github.com/networkx/networkx/pull/7398)(added `colliders` and `v_structures` and deprecated `compute_v_structures` in `dag.py`) is almost ready. Only [one discussion](https://github.com/networkx/networkx/pull/7398#discussion_r1636138470) on an appropriate `stacklevel` for the deprecation warning is going on.
- [Approved] Waiting for 2nd review from Erik on [PR#7404](https://github.com/networkx/networkx/pull/7404) (Refactoring and enhancing user-facing `Backend and Configs` docs)

## 2. A draft PR for adding config to nx-parallel ([PR#68](https://github.com/networkx/nx-parallel/pull/68))

I started by understanding how the config system works with backends in networkx using the existing documentation and code and seeing how config is used in the networkx's dispatching code. Based on that I created a draft PR, with an `NxpConfig` class that inherits from networkx's `Config` class and I explicitly added all the configurations that joblib offers. So, the additional `**args` and `**kwargs` that joblib allows based on the specified backend cannot be used right now. But, this will of course be changed in the future to directly extract parameters from joblib's signature using `inspect`.

Currently, I add the `parallel` backend to `backend_priority` and `NxpConfig` class instance to the `parallel` configuration at the time of import of nx-parallel, by adding the following lines at the end of the `config.py` file of nx-parallel:

```.py
nx.config.backend_priority = [
    "parallel",
]
nx.config["backends"]["parallel"] = NxpConfig()
```

But, this shouldn't be the case(ref. [comment](https://github.com/networkx/nx-parallel/pull/68/files#r1628357424)). NetworkX should be able to find the `NxpConfig` class on its own. I think (based on what I could make out of how I saw config being used in the networkx's dispatching code) that can be done by adding config in the `get_info` function. But, I'm not sure. I'll have to look more into this.

Another function in `config.py` is the `get_configs(config=None)` which returns a dictionary containing all the configs if `config=None`, a dictionary of only a few selected configs if a list of configs is passed in, or a value of a config setting if only one config setting is passed in. The returned value of this function is directly passed into the `joblib.Parallel(**configs)` call inside all nx-parallel algorithms. It is also used to get the `n_jobs` parameter to perform the chunking accordingly. But, I believe there is probably a better way in which configs can be handled without calling the `get_configs` in all the algorithms. Maybe a more centralized approach and thereby chunking will also be centralized and taking inspiration from [PR#7](https://github.com/networkx/nx-parallel/pull/7) would be a good idea here. But, I would also like to keep the architecture simple enough that it's easy for first-time contributors to understand.

In the coming days, I want to investigate why is `Config` in networkx is a `@dataclass` and why it cannot be a normal Python class. I also want to figure out if there is a way to check which algorithm is being called and according to that run different checks on the config parameters. And, lastly, try to figure out a way to test this config system in nx-parallel.

Also, we won't need an `nxp.cpu_count` function in the future because we can use the `n_jobs` parameter in the config to specify the number of jobs to run in parallel. So, I'll remove that from the nx-parallel's `utils.py`. And then probably add a default config for users and a config for testing purposes.

My future plans for this would be to first review [PR#7485](https://github.com/networkx/networkx/pull/7485) and [PR#7363](https://github.com/networkx/networkx/pull/7363) which add context managers for backend configurations. And then I would like to shift my focus on this draft config [PR#68](https://github.com/networkx/nx-parallel/pull/68). And once I'm somewhat satisfied with the state of this config PR, I'll start shifting toward the benchmarking goals.

## 3. Switching to setuptools

As suggested by Ross, I split the [PR#67](https://github.com/networkx/nx-parallel/pull/67) into two. One that changed the building to setuptools([PR#69](https://github.com/networkx/nx-parallel/pull/69)) and another that had all the style changes([PR#67](https://github.com/networkx/nx-parallel/pull/67)). I initially assumed that all the style changes in the ordering of the `import` statements were occurring due to the switching of the building tool from hatchling to setuptools. But, in the last meeting, Dan pointed out that it was probably happening because I added an additional linting setting.

```.toml
[tool.ruff.lint]
select = [
    'I',
    'F403',
]
```

And removing this fixed all the linting errors. And, we decided to add more linting settings later in a different PR. So, I made [PR#67](https://github.com/networkx/nx-parallel/pull/67) draft for now and [PR#69](https://github.com/networkx/nx-parallel/pull/69) is ready for the first review.

## 4. Other Activities in the Community

- [Reviewed] Various improvements in information centrality: [PR#7475](https://github.com/networkx/networkx/pull/7475)
- [Reviewed] Add "networkx" backend for dispatching: [PR#7496](https://github.com/networkx/networkx/pull/7496)
- [Reviewed] Add nx.config.backend option: [PR#7485](https://github.com/networkx/networkx/pull/7485)
- [Merged] minor doc_string changes to check write access: [PR#70](https://github.com/networkx/nx-parallel/pull/70) (Earlier, I was using a PAT with myself as the resource owner for authentication with GitHub while pushing commits. But, I wasn't able to push commits from my local machine to a contributor's PR because I don't own networkx repositories. So, I added an SSH key in my GitHub for authentication as nobody else uses PATs in networkx for pushing commits. So, this PR was just created to check if I can push commits to a contributor's PR or not.)
- [Merged] Renaming PR ([PR#7492](https://github.com/networkx/networkx/pull/7492))
- I became a member of NetworkX's core developer team on 6th June. And a lot of people have written really nice blogs on maintaining open-source projects and one of them that I really liked was ["The cost of an open source contribution"](https://rgommers.github.io/2019/06/the-cost-of-an-open-source-contribution/) by Ralf Gommers. And the ["Three Components for Reviewing a Pull Request" presentation](https://youtu.be/dyxS9KKCNzA?si=_3JibXzw5zfBTJCy) by Thomas J. Fan was also really helpful.
- worked on [nx-j4f](https://github.com/Schefflera-Arboricola/nx-j4f) backend.
