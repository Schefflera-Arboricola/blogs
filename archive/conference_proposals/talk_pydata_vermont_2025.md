---
author: Aditi Juneja
title: "Talk - Pydata Vermont 2025"
status: "rejected"
date: 13-09-2025
---

- Title: Understanding API Dispatching in Scientific Python Ecosystem
- Session type: Talk
- Duration: 00:45 min

## Abstract

Have you ever wished your Python libraries could run faster with huge data? Could run on GPUs without changing your huge codebase, or switching to a different library, or rewriting everything in a faster language (C, Rust)? Discover how API dispatching mechanism redirects function calls to a FASTER implementation present in a separate backend package by various approaches like leveraging the Python's [`entry_point`](https://packaging.python.org/en/latest/specifications/entry-points) specification (NetworkX and scikit-image), and [Array API Standards](https://data-apis.org/array-api/latest/) (NumPy, SciPy, sklearn, and more) in various Scientific Python projects!

## Description

In the first five minutes, I'll introduce the general concept of dispatching with a short demo using dummy libraries. We will explore the challenges of dispatching a function call to an alternative implementation-- when the implementation resides in a different package that is written in another programming language, or is designed for a different hardware, like GPUs.

In the next five minutes, we will discuss Python `entry-point`s using a simple example. We will see how entry points can extend a project’s functionality and how they can be used for dispatching--building upon the demo from the previous section.

Following this, over the next five minutes, we will look at [NetworkX](https://github.com/networkx/networkx), a widely used pure-Python library for graph (network) analysis. Through a quick demo with [a large network dataset](https://snap.stanford.edu/data/ca-HepTh.html), we will illustrate how performance issues arise in real-world scenarios.

In the next 5-10 minutes, we will examine how NetworkX leverages entry points for dispatching-- and supports both type-based and backend-name-based dispatching. We will walk through the details and steps involved in NetworkX dispatching: discovering backend packages, converting argument types, redirecting function calls to faster backend implementations, and returning results after converting to apt. types.

In the following 5-10 minutes, we will shift focus to the broader array library ecosystem and the type-based dispatching mechanisms. We will discuss how NumPy’s type-based dispatching works via the [`__array_function__`](https://numpy.org/neps/nep-0018-array-function-protocol.html) dunder method, how this led to the creation of the Array API standard, and how adoption of this standard has progressed in libraries such as SciPy and scikit-learn.

Next, in five minutes, we will explore the challenges of adopting Array API standards in scikit-image. We will explain why entry-point–based dispatching is better suited in this context, and how scikit-image is adopting a hybrid approach that blends type-based and entry-point–based dispatching.

In the following five minutes, we will highlight ecosystem-wide initiatives aimed at coordinating and supporting adoption of dispatching mechanisms-- such as [`spatch`](https://github.com/scientific-python/spatch) and [SPEC-2](https://scientific-python.org/specs/spec-0002/). We will also provide an overview of future directions, summarizing the dispatching approaches covered, their advantages and disadvantages, and insights on when and where it would be better to which dispatching approach based on the project and its needs.

Then if time permit, I'd also like to go into some interesting developments in the [nx-parallel](https://github.com/networkx/nx-parallel) backend or the [DataFrame API standards](https://data-apis.org/dataframe-api/draft/) and some of the nice features of the NetworkX dispatching, like the usage of `NETWORKX_TEST_BACKEND` environment variable, the second entry-point for backend's meta-data, the backend_priority, `can_run`, `should_run`, other NetworkX backends, etc. And finally, concluding with an interactive Q&A.

---

Intended Audience:

- Contributors and maintainers of Python libraries who want to provide faster algorithms without changing their codebase or user-facing APIs.
- Researchers and practitioners working with large graph, image, or array datasets.
- Anyone interested in API dispatching or related ecosystem efforts.


Prerequisites: Some basic knowledge of Python is expected, including familiarity with objects and classes.


Thank you :)