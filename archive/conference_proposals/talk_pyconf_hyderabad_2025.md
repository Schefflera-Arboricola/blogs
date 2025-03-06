---
author: Aditi Juneja
title: "Talk - PyConf Hyderabad 2025"
status: "accepted"
date: 07-01-2025
---

## Title

Understanding API dispatching

## Elevator Pitch

(<i>You have 300 characters to sell your talk. This is known as the "elevator pitch". Make it as exciting and enticing as possible.</i>)

Want to accelerate your Python libraries without changing your huge codebase or the user-API? Discover how NetworkX’s backend dispatching mechanism works and boosts the performance seamlessly, with real-world use cases, and its future in the Scientific Python Ecosystem. Code faster, stay Pythonic.

## Talk Format

Talk (~30-45 minutes)

## Audience Level

All

## Description

Have you ever wished your pure Python libraries were faster? Or wanted to fundamentally improve a Python library by rewriting everything in a faster language like C or Rust? Well, wish no more... NetworkX's backend dispatching mechanism redirects your plain old NetworkX function calls to a FASTER implementation present in a separate backend package by leveraging the Python's [`entry_point`](https://packaging.python.org/en/latest/specifications/entry-points) specification!

[NetworkX](https://github.com/networkx/networkx) is a popular, pure Python library used for graph(aka network) analysis. But as the graph size increases (like a network of everyone in the world), the NetworkX algorithms could take days to solve a simple graph analysis problem. So, to address these performance issues, a backend dispatching mechanism was recently developed. In this talk, we will unveil this dispatching mechanism and its implementation details, and how we can use it just by specifying a `backend` kwarg like this:

    >>> nx.betweenness_centrality(G, backend=“parallel”)

or by passing the backend graph object(type-based dispatching):

    >>> H = nxp.ParallelGraph(G)
    >>> nx.betweenness_centrality(H)

We'll also go over the limitations of this dispatch mechanism. Ending with a brief overview of how this API dispatch mechanism could be integrated in other scientific Python libraries, along with the potential challenges that may arise with them.

---

In the first few minutes, we will familiarize ourselves with the NetworkX library and graph analysis in general. Moving on to a quick demo of the performance limitations of existing NetworkX algorithms such as `betweenness_centrality` and `square_clustering` when applied to a larger [SNAP graph dataset](https://snap.stanford.edu/data/ca-HepTh.html), underscoring the critical necessity for more optimised implementations. Balancing this need for more efficient and faster algorithms with the core values of NetworkX-- to remain free from any external dependencies and to uphold its pure Python nature, led to the development of a new backend dispatching system in NetworkX.

Next, we will understand what API dispatching is in a broader sense, what are `entry_points`, how NetworkX utilises them to discover the backend packages and then redirect the NetworkX function calls to the faster backend implementations. We will then delve into some of the details of the features a backend developer can utilise, like the usage of `NETWORKX_TEST_BACKEND` environment variable, the second `entry_point` for backend meta-data, the `backend_priority`, `can_run`, `should_run` etc. And a summary of other NetworkX backends and some future to-dos for NetworkX’s dispatching.

After that, we will understand how and when this API dispatching mechanism could be adopted by a scientific Python library, and what are some of the challenges that they might face during its integration. We will also go over some of the recent developments in integrating API dispatching in the scikit-image project and the challenges of integrating API dispatching in an array-based library. Finally, concluding with an interactive Q&A.

---

Intended audience:

- Contributors of Python libraries who are interested in offering their users faster algorithms without changing their codebase and the user-API much
- People who work with large graph datasets
- anyone interested in API dispatching, graphs or any of the above stuff :)

Some basic knowledge of Python is expected; should know what objects and classes are.

---

Resources:

- slides from previous version of this talk which was only about NetworkX's API Dispatching - https://github.com/Schefflera-Arboricola/blogs/blob/main/archive/PythonPune_December2024_Meetup.pdf
- https://networkx.org/documentation/latest/reference/backends.html
- https://github.com/networkx/nx-parallel
- https://packaging.python.org/en/latest/specifications/entry-points/


Thank you :)
