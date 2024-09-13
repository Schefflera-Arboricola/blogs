---
author: Aditi Juneja
title: "Poster - SciPy 2024"
status: "accepted - presented virtually"
date: 05-03-2024 21:33:00 +0530
---

[link to proposal](https://cfp.scipy.org/2024/talk/review/MJYM8FDXXRDGEVXDBCFRF9TQXB3XKCRU)

# Title: Parallel graph algorithms and Building backends with entry_point

# Abstract

Hi! Join me to dive into the details of implementing parallel graph algorithms and NetworkX's backend dispatching architecture!

As graphs grow in size, the traditional graph analysis algorithms face scalability issues, leading to prolonged computation times even for moderately sized graphs. Nx-parallel backend implements parallel versions of NetworkX algorithms. The plugin backend architecture of NetworkX utilizes `entry-points` to redirect function calls to nx-parallel's implementations. We will go into various challenges and limitations of parallelizing different kinds of functions, the effects of chunking, and the possibility of creating an architecture that allows distributed graph algorithms and also allows users to play around with parameters like `n_jobs` in a parallel setting. I'd love to answer any questions on parallel graph algorithms and NetworkX backend dispatching! Your feedback and contributions to nx-parallel would be invaluable in advancing parallel graph analysis capabilities!

# Description

Graph analysis faces scalability challenges as graph size increases, leading to longer computation times for various algorithms such as `square_clustering`, `all_pairs_node_connectivity`, etc., sometimes even for 200-300 node graphs. To address this, nx-parallel introduces parallel processing capabilities, leveraging `joblib.Parallel` to implement parallel versions of NetworkX algorithms. This backend package integrates seamlessly with NetworkX's plugin backend architecture leveraging [`entry-points`](https://packaging.python.org/en/latest/specifications/entry-points/) to redirect NetworkX function calls to the nx-parallel backend implementations. The `backends` entry-point facilitates backend discovery, while `backend_info` adds backend implementation details to the main NetworkX documentation website. One can also test their backend using the existing NetworkX test suite by setting appropriate environment variables (see [docs](https://networkx.org/documentation/latest/reference/backends.html) for more!).

One of the key features of nx-parallel is its support for custom chunking. Chunking is a pretty common practice in parallel computing and usually reduces the computation time. In nx-parallel, most algorithms allow users to optimize computation by dividing their graph data into manageable chunks tailored to their specific use cases. While parallelizing the functions that `yield`, it was hard to define what "parallelizing" and "chunking" even meant there. So, a solution I could come up with was to create a chunked generator using `delayed(_process_node_chunk)(node_chunk) for node_chunk in node_chunks` and then pass this into the `joblib.Parallel` instance and then yield the results chunk by chunk, node by node. And this seems to give the best speedups in time so far(ref. [PR](https://github.com/networkx/nx-parallel/pull/49)).

Along with several embarrassingly parallel algorithms, the ASV benchmarking is also set up in nx-parallel which compares the parallel implementations against the sequential implementations. Additionally, ongoing efforts include adding configurable options to the backend, empowering users to fine-tune parameters such as `n_jobs`, and exploring alternative parallel backends through joblib. However, challenges persist, such as the inherent limitations of parallelizing certain algorithms due to their innate sequential nature and/or the overhead associated with consolidating results from each independent parallel process. Looking ahead, nx-parallel also aims to expand its capabilities by supporting distributed backends like dask or ray, optimizing memory usage, and implementing distributed graph algorithms. Continuous improvements include improving nx-parallel's infrastructure, adding more algorithms, and exploring algorithmic optimizations to further enhance performance.

Any ideas/questions/feedback on the currently implemented parallel graph algorithms and on the currently implemented pipeline connecting NetworkX to nx-parallel to joblib to joblib's different parallel backends would be invaluable! Also, please feel free to nuture the nx-parallel repository with your PRs and contributions!

Thank you :)

# Initially it was a talk proposal

**Proposal title**: nx-parallel : NetworkX's parallel backend

**Abstract**: Hi! Join me as we explore parallel algorithms in nx-parallel, examining implementation details, performance enhancements, the effects of chunking, and overcoming the challenges of parallelizing the functions that “yield” instead of “return”. We’ll start by exploring a social network analysis problem and see the need for a parallel backend. Then we’ll dive into the NetworkX’s backend dispatching architecture and walk through setting up a custom backend and testing it using the existing suite, and understand the significance of the dispachable decorator. We'll delve into the internals of parallel algorithms, observing process creation and CPU core utilization. Finally, we'll discuss future directions for handling even larger graphs. Experience how nx-parallel accelerates network analysis through parallel processing!

**Description**: During the first 5-6 minutes of the talk, I will guide the audience through a comprehensive, but brief, journey into the world of network analysis through an example. I’ll start with an introduction to NetworkX, then move on to the need for a parallel backend. The initial segment will unravel the core concepts of NetworkX and backend dispatching, shedding light on the automated testing framework and the significance of the dispatchable decorator.

Transitioning into the crux of the discussion, the subsequent 10-15 minutes will be dedicated to dissecting how parallel algorithms are implemented in nx-parallel. I will elucidate the internal workings of parallelization, showcasing the increase in processes and the activity distribution across different CPU cores while the parallel algorithms are running. A focal point of this section will be the role of chunking in nx-parallel and its impact on speedups. Furthermore, I may present benchmarking results that demonstrate the performance benefits derived from parallel computing and chunking. Moreover, I will also address challenges encountered while parallelizing functions that yield instead of return values. By sharing my experiences in overcoming and working with these obstacles, attendees might gain valuable insights into navigating similar hurdles in their own projects.

In the closing minutes, we'll glimpse into the future of nx-parallel and NetworkX dispatching, by discussing some of the “bigger picture” questions about the pipeline connecting NetworkX to nx-parallel to joblib to joblib's different parallel backends and using something like distributed graph processing for a much more memory-efficient parallelization. And then this section will lead to a much more interactive 5-minute window for the audience to participate, ponder and raise more questions, and share their thoughts, knowledge, and perspectives!
