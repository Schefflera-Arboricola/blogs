---
author: Aditi Juneja
title: "Talk - PyData Global 2024"
status: "accepted"
date: 14-10-2024
---

# Title

Understanding API Dispatching Implemented in NetworkX

# Abstract

Hi! Have you ever wished your pure Python libraries were faster? Or wanted to fundamentally improve a Python library by rewriting everything in a faster language like C or Rust? Well, wish no more... NetworkX's backend dispatching mechanism redirects your plain old NetworkX function calls to a FASTER implementation present in a separate backend package by leveraging the Python's [`entry_point`](https://packaging.python.org/en/latest/specifications/entry-points) specification!

[NetworkX](https://github.com/networkx/networkx) is a popular, pure Python library used for graph(aka network) analysis. But when the graph size increases (like a network of everyone in the world), then NetworkX algorithms could take days to solve a simple graph analysis problem. So, to address these performance issues, a backend dispatching mechanism was recently developed. In this talk, we will unveil this dispatching mechanism and its implementation details, and how we can use it just by specifying a `backend` kwarg like this:

    >>> nx.betweenness_centrality(G, backend=“parallel”)

or by passing the backend graph object(type-based dispatching):

    >>> H = nxp.ParallelGraph(G)
    >>> nx.betweenness_centrality(H)

We'll also go over the limitations of this dispatch mechanism. Then we’ll use the example of [nx-parallel](https://github.com/networkx/nx-parallel) backend as a guide to understand various NetworkX backend and backend configuration features. 

Finally, I'll conclude with a brief overview of how this API dispatch mechanism could be integrated in an non-graph-related Python libraries, such as an array-based or data-centric libraries, along with the potential challenges that may arise during integration. This will be followed by an interactive Q&A session.

# Description

In the first few minutes, we will familiarize ourselves with the NetworkX library and graph analysis in general. Moving on to a quick demo of the performance limitations of existing NetworkX algorithms such as `betweenness_centrality` and `square_clustering` when applied to a larger [SNAP graph dataset](https://snap.stanford.edu/data/ca-HepTh.html), underscoring the critical necessity for more efficient implementations. Balancing this need for more efficient and faster algorithms with the core values of NetworkX-- to remain free from any external dependencies and to uphold its pure Python nature, led to the development of a new backend dispatching system in NetworkX.

Next, we will understand what API dispatching is in a broader sense, what are `entry_points`, how NetworkX utilises them to discover the backend packages and then redirect the NetworkX function calls to the backend implementations. We will then delve into some of the details of the features a backend developer can utilise, like the usage of `NETWORKX_TEST_BACKEND` environment variable, the second `entry_point` for backend meta-data, the `backend_priority`, `can_run`, `should_run` etc. (Refer the linked docs to understand more!)

In the next few minutes, we will get to know the nx-parallel backend that runs NetworkX's single-core graph algorithms on multiple CPU cores using [joblib](https://joblib.readthedocs.io/en/stable/generated/joblib.Parallel.html). And we will discuss its implementation details and some of the future to-dos for the nx-parallel backend.

After that, we will understand how and when this API dispatching mechanism should be adopted by a Python library, and what are some of the challenges that they might face during its integration. Followed by a summary of other NetworkX backends and some future to-dos for NetworkX’s backend dispatching. And then finally conclude with an interactive Q&A.

Intended audience:
- maintainers and contributors of Python libraries who are interested in offering their users faster algorithms without changing their API standards
- NetworkX users who work with large graph datasets
- anyone interested in API dispatching, graphs or any of the above stuff :)

Some basic knowledge of Python is expected.


Thank you :)
