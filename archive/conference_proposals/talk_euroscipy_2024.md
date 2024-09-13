---
author: Aditi Juneja
title: "Talk - EuroSciPy 2024"
status: "accepted"
date: 27-05-2024 02:37:00 +0530
---

[link to proposal](https://pretalx.com/euroscipy-2024/talk/QLVBYY/)

Similar proposals submitted at:

- PyData Amsterdam 2024 - Accepted but couldn't deliver because of visa issues.
- PyCon AU 2024 - Withdrawn; tired of visa application processes; also financial aid only for attendees travelling from within Australia, or from a location in the Pacific/Oceania region.
- PyCon India 2024 - Rejected

# Title: Understanding NetworkX's API Dispatching with a parallel backend

# Abstract

Hi! Have you ever wished your pure Python libraries were faster? Or wanted to fundamentally improve a Python library by rewriting everything in a faster language like C or Rust? Well, wish no more... NetworkX's backend dispatching mechanism redirects your plain old NetworkX function calls to a FASTER implementation present in a separate backend package by leveraging the Python's [`entry_point`](https://packaging.python.org/en/latest/specifications/entry-points) specification!

NetworkX is a popular, pure Python library used for graph(aka network) analysis. But when the graph size increases (like a network of everyone in the world), then NetworkX algorithms could take days to solve a simple graph analysis problem. So, to address these performance issues this backend dispatching mechanism was recently developed. In this talk, we will unveil this dispatching mechanism and its implementation details, and how we can use it just by specifying a `backend` kwarg like this:

    >>> nx.betweenness_centrality(G, backend=“parallel”)

or by passing the backend graph object(type-based dispatching):

    >>> H = nxp.ParallelGraph(G)
    >>> nx.betweenness_centrality(H)

We'll also go over the limitations of this dispatch mechanism. Then we’ll use the example of nx-parallel as a guide to building our own custom NetworkX backend. And then, using NetworkX's existing test suite, we'll test this backend that we build. Ending with a quick dive into the details of the nx-parallel backend.

# Description

## Ideal flow

In the first few minutes, we will familiarize ourselves with the NetworkX library and graph analysis in general. Subsequently, we will delve into the growing demand for faster graph algorithms driven by numerous PRs proposing to include parallel implementations for various algorithms in NetworkX. Moving on to a quick demo of the performance limitations of existing NetworkX algorithms such as `betweenness_centrality` and `square_clustering` when applied to larger SNAP graph datasets, underscoring the critical necessity for more efficient implementations. Balancing this need for more efficient and faster algorithms with the core values of NetworkX-- to remain free from any external dependencies and to uphold its pure Python nature, led to the development of a new backend dispatching system in NetworkX.

Next, we will understand what `entry_points` are and how NetworkX utilizes them to discover the backend packages and then redirect the NetworkX function calls to the backend implementations according to the specified backend. I will then delve into the details of the features a backend developer can utilize, like how they can use NetworkX's existing testing suite to test their backend just by setting the `NETWORKX_TEST_BACKEND` environment variable. Using the nx-parallel backend as an example, I will explain these implementation details and features. Finally, I will provide a brief demo on building your own backend.

In the last few minutes, we will get to know the nx-parallel backend that runs NetworkX's single-core graph algorithms on multiple CPU cores using [joblib](https://joblib.readthedocs.io/en/stable/generated/joblib.Parallel.html). We will discuss its implementation details and observe the parallel processes running concurrently and their CPU core usage distribution in the Activity Monitor. Next, we will explore the concept of chunking, and learn how and when it helps in parallel computing, particularly in the context of graph algorithms. Many algorithms in nx-parallel are generator functions, so we’ll also go over how chunking is done for generator functions. In the end, we’ll engage in a quick demo comparing nx-parallel and NetworkX using a large graph dataset with custom chunking enabled.

We will end with a summary of other NetworkX backends and some future to-dos for NetworkX’s backend dispatching and the nx-parallel backend. And then finally conclude with an interactive Q&A.

Refer to the linked poster below for more!

Thank you :)

# Abstract as a tweet

Ever wished your pure Python libraries were faster? Well, wish no more... NetworkX's dispatching mechanism redirects your plain old NetworkX function calls to a FASTER backend implementation, leveraging Python's `entry_point` specification!
