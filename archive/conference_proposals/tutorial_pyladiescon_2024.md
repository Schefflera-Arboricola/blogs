---
author: Aditi Juneja
title: "Tutorial - PyLadiesCon 2024"
status: "under-review"
date: 18-10-2024 19:11:00 +0530
---

## Title : 

Making Python libraries FASTER and NetworkX's API Dispatching


## Description:

This tutorial will broadly have 3 parts as described below:

### Part 1 - Understanding NetworkX : 30 min

- Engage the audience members in an interactive social networks activity to get them curious about the domain of graphs (interactive breakout rooms may be needed to conduct this)
- Delve into the technical details of this activity
- Simulate this activity using NetworkX in a Python notebook


### Segway to the Part 2 

Running the activity for a larger dataset—observe that it takes a long loong time (question from audience could be taken while it runs).


### Part 2 - Understanding API Dispatching : 30-40 min

- 10 min presentation on dispatching in general—how it can speed up algorithms in libraries like NetworkX for large datasets, with a specific focus on its implementation details.
- Coding(audience would be expected to follow along) :
    - How do we dispatch a function call from the main Python package(like NetworkX) to the backend package(like nx-parallel)? How do we make two packages communicate with each other? (spoiler - using Python `entry_points`)
    - How to add a plug-in layer to the main library?
    - How to make a backend? (Audience could create along any kind of fun backends that they like at this point) 


### Segway to the Part 3 

NetworkX's backend : The nx-parallel backend (it's specifications and how backend interface and backend configurations are setup in nx-parallel)


### Part 3 - Ending Notes and QnA : 15-20 min

- Discuss some advanced features offered by NetworkX dispatching to the backend developers and backend users, like backend_priority, automatic testing, should_run, can_run, etc.
- Some of the areas of improvement and limitations of the dispatching mechanism implemented in NetworkX 
- Some of the challenges other Python libraries might face while adopting this dispatching mechanism in their libraries- Finally, ending with an interactive QnA

## Expected Learning Outcomes:

- Enabling people to use Python entry_points and enabling them to do cool things with python packages that can communicated with each other 
- Gain some basic knowledge of Python packaging
- Basic knowledge of parallel algorithms and graph algorithms
- People to leave with an interest in graphs, specifically social networks

## Intended Audience:

- Python library maintainers and contributors looking to offer faster algorithms without making any major changes in their codebase and user-API.
- NetworkX users who work with large graph datasets
- People invested in the graph world
- Anyone interested in any of the above stuff :)

**Some basic knowledge of Python is expected.**


## Duration: 

75-90 min

## Time Zone: 

APAC timezone - UTC 03:00 7th Dec to 10:50 7th Dec

## Resources:

- NetworkX's backend docs: https://networkx.org/documentation/latest/reference/backends.html
- nx-parallel repository: https://github.com/networkx/nx-parallel
- Python entry-points: https://packaging.python.org/en/latest/specifications/entry-points/ 
- Slides from PyConIndia, EuroSciPy talks and Poster from SciPy: https://github.com/Schefflera-Arboricola/blogs/tree/main/archive 
- SPEC 2: https://scientific-python.org/specs/spec-0002/

