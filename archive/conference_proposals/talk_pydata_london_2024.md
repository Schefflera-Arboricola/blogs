---
author: Aditi Juneja
title: "Talk - Pydata London 2024"
status: "rejected"
date: 05-03-2024 05:26:00 +0530
---

# Title: nx-parallel : Parallel backend for NetworkX

# Abstract

In this talk, I will take the audience through parallel algorithms in nx-parallel, focusing on the implementation details, performance enhancements through chunking, and overcoming challenges like parallelizing functions that yield instead of returning. I will do a quick walk-through on setting up a custom NetworkX backend, and how you can use the NetworkX test suite to test it. I’ll also go over the future direction of adding new algorithms that could handle really big graphs using distributed graph processing. Join me for an insightful exploration of how nx-parallel speeds up networkx analysis through parallel processing.

# Description

During this 40-minute talk, I will guide the audience through a comprehensive journey into the world of network analysis. I’ll start with a brief introduction of NetworkX, then move on to the need for a parallel backend, and then dive into the parallel algorithms within nx-parallel. The initial segment will unravel the core concepts of networkx and networkx dispatching, shedding light on the automated testing framework and the significance of the dispatchable decorator. Attendees will gain insights into setting up their own networkx backends and leveraging automated testing for enhanced efficiency.

Transitioning into the crux of the discussion, the subsequent 20 minutes will be dedicated to dissecting how parallel algorithms are implemented in nx-parallel. I will elucidate the internal workings of parallelization, showcasing the increase in processes and the activity distribution across different CPU cores. A focal point of this section will be the role of chunking in nx-parallel and its impact on speedups. Furthermore, I will present benchmarking results that demonstrate the performance benefits derived from chunking.

Moreover, I will also address challenges encountered while parallelizing functions that yield instead of return values. By sharing my experiences in overcoming these obstacles, attendees will gain valuable insights into navigating similar hurdles in their own projects.

In the last 5 minutes of the talk, I will offer a glimpse into the future by discussing upcoming algorithms that delve into distributed graph processing, expanding the horizons of computational capabilities.

The talk will culminate with a dedicated 5-minute window for questions, fostering interactive dialogue and knowledge exchange among participants.
