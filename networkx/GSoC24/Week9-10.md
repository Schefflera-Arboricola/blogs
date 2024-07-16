---
title: "Blog5: GSoC (nx-parallel)"
author: Aditi Juneja
date: 2024-07-16 23:41:00 +0530
---

# Blog5: GSoC (nx-parallel)

## Week 9-10 (28th June to 11th July, 2024)

### GSoC - Coding Period (Phase 1)

## 1. From the last blog

[PR#7363](https://github.com/networkx/networkx/pull/7363) was merged by Ross! And there were discussions between me and Erik on [PR#7485](https://github.com/networkx/networkx/pull/7485) about having the backend name (or `backend_priority` list) and the backend configs in the same context manager and what will be the advantages and disadvantages of having only a single `backends` arg in place of `backend` and `backend_priority`.

I also had some discussions on Discord with Erik, where he shared some valuable insights about various projects like Metagraph, Blaze, Dask, and Ibis, highlighting their approaches to dispatching and the challenges they faced. This helped me understand the complexities of implementing dispatching systems and the importance of usability, maintainability, and community adoption. We discussed the goal of `spatch` to generalize the NetworkX dispatching system and how we will test this backend mechanism, which could be used across different projects.

Additionally, I explored the idea of setting up a comprehensive test suite for backend configurations in NetworkX, recognizing the similarities in how different backends would test their configs. We both agreed to keep such discussions within the `spatch` repo to engage the community and document our progress. And I plan on creating an issue summarizing our discussions more clearly.

Through these conversations, I gained a deeper understanding of dispatching systems, the challenges of product fit and usability, and the importance of effective testing. I also learned about the broader implications of dispatching in the scientific Python ecosystem and the potential for contributing to projects like scikit-image. These interactions underscored the value of communication, collaboration, and continuous learning in my GSoC project and beyond.

Apart from this, I am yet to do most of the things I mentioned in the "Adding configs to nx-parallel" section of my last blog.

## 2. Conda forge of nx-parallel

The conda feedstock for `nx-parallel` was successfully created. At Mridul's request, I initiated a pull request to add him as a maintainer. During this process, one of the checks indicated that the build number needed to be updated. I proceeded to update the build number and re-rendered the PR. However, I recalled reading somewhere (while I was creating the recipe for nx-parallel) that the build number is updated when there are changes to the project's dependencies. To ensure accuracy, I reviewed the official conda-forge documentation. Following the recommended approach, I created an issue to add a maintainer and then merged the PR created by the conda-forge-bot. And I really liked how everything was automated via these bots while creating and maintaining a conda-forge package. This bot-controlled system piqued my curiosity, and I would really like to understand how these mechanisms work in detail in the future, if possible.

## 2. Other Activities in the Community

### Some highlights

- The talk titled - "Understanding NetworkX's API Dispatching with a parallel backend" that Erik and I submitted for EuroSciPy 2024 got accepted! Thanks to Dan for reviewing my initial talk proposal and Erik for reviewing it repeatedly as I kept updating it :)
- Created and presented virtually my poster titled "Parallel graph algorithms and Building backends with entry_point" at SciPyCon 2024 (10th to 13th July)!
<a href="https://github.com/Schefflera-Arboricola/Stuff/blob/main/Projects/networkx-related/aditi_juneja_nxp_scipycon24_poster.png"><img src="https://github.com/Schefflera-Arboricola/Stuff/raw/main/Projects/networkx-related/aditi_juneja_nxp_scipycon24_poster.png"></img></a>
    - ([Poster-Booth-link](https://www.airmeet.com/event/b21647f0-38b7-11ef-a03c-fd16c137ca62?booth=6689a402d4316e0dcdeba27c) - Hopefully this link won't break in the future).
    - Thank you very much to Jim (Weiss-- I assume) from SciPyCon team, who very generously offered me a free virtual pass to the conference :)
    - And lightening talks were fun :)
- Became a member of the conda-forge organisation on 1st July, 2024!
- And I passed the GSoC'24 mid-term evaluation!

### Other Contributions

- **Merged** [PR#26768](https://github.com/conda-forge/staged-recipes/pull/26768) - Added nx-parallel to conda-forge
- **Closed** [Issues#65](https://github.com/networkx/nx-parallel/issues/65) - Create a conda-forge feedstock for nx-parallel
- **Reviewed** [PR#3](https://github.com/conda-forge/nx-parallel-feedstock/pull/3) - [ci skip] adding user @MridulS
- **Closed** [Issue#2](https://github.com/conda-forge/nx-parallel-feedstock/issues/2) - @conda-forge-admin, please add user @MridulS
- **Reviewed** [PR#7535](https://github.com/networkx/networkx/pull/7535) - Minor doc/test tweaks for dorogovtsev_goltsev_mendes
- **Reviewed** [PR#7545](https://github.com/networkx/networkx/pull/7545) - More accurate NodeNotFound error message
- **Reviewed** [PR#7556](https://github.com/networkx/networkx/pull/7556) - Add Introspection section to backends docs
- **Commented** [PR#7485](https://github.com/networkx/networkx/pull/7485) - Add nx.config.backend option
- **Merged** [PR#7226](https://github.com/networkx/networkx/pull/7226) - Remove parallelization related TODO comments

PS: Due to a malfunctioning laptop screen, I had to set up everything on the new temporary laptop and recreate the SciPy poster from scratch, as I only had a .jpeg version of the [old one](https://github.com/Schefflera-Arboricola/Stuff/blob/main/Projects/networkx-related/A_juneja_nx-parallel_illustration_old.jpeg), which was not of the correct dimensions, and I also wanted to add and remove a few things. But I think the new poster turned out pretty nice as well! Additionally, I was also occupied with my visa application for EuroSciPy and some other personal matters (communicated to my mentor), which slightly reduced my contributions over the past two weeks. I aim to increase my productivity in the coming weeks to compensate for this.
