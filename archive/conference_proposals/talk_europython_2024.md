---
author: Aditi Juneja
title: "Talk - EuroPython 2024"
status: "rejected"
date: 15-03-2024 02:03:00 +0530
---

# Title: “Parallelising graph algorithms : nx-parallel”

# Abstract

Hi! Join me as we explore the parallel graph algorithms in nx-parallel, going over the implementation details, performance enhancements, the effects of chunking, and challenges of parallelizing functions that “yield” instead of “return”. We’ll start by indulging in a social network analysis problem and play around with it using NetworkX and then see the need for a parallel backend. Then we’ll dive into the NetworkX’s backend dispatching architecture and walk through setting up a custom backend and testing it using the existing suite. We'll also delve into the internals of parallel algorithms, observing process creation and CPU cores' usage distribution and memory usage distribution by each parallel process running in parallel. Finally, we'll discuss the future directions for handling even larger graphs by using distributed graphs. And ending with an interactive Q&A!

# Outline

During the first 7-8 minutes of the talk, I will guide the audience through a brief journey into the world of network analysis through a social network example and showcasing the need for parallel algorithms over NetworkX's sequential algorithms. The initial segment will unravel NetworkX's backend dispatching, shedding light on the automated testing and the significance of the \_dispatchable decorator. The subsequent 15-20 minutes will be dedicated to dissecting how parallel algorithms are implemented in nx-parallel. I'll showcase the internal workings of parallelization and the behavior of parallel processes in the activity monitor. A focal point of this section will be the role of chunking in nx-parallel and its impact on speedups. I will also address some of the challenges encountered while parallelizing functions that yield instead of return. In the closing minutes, we'll take a glimpse into the future of nx-parallel and NetworkX dispatching and an interactive Q&A.

**My presentation can be delivered**: in-person at the conference venue

**Public link to supporting material.**: https://github.com/networkx/nx-parallel , https://schefflera-arboricola.github.io/Schefflera-Arboricola/NetworkX-Internship-Working-on-nx-parallel

**Are you planning to apply for Financial Aid?**: yes

**Expected audience expertise**: Intermediate
