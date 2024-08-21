[original](https://hackmd.io/MBQfVs6lSaar_ARM9jHxNw) + weekly work updates

# NetworkX Internship - 2024
Link: https://colgate.zoom.us/j/92619161786

## February 28, 2024

Attendees: Aditi, Dan, Mridul

### Topics:

- https://github.com/networkx/nx-parallel/pull/49

### Work update : Week 8 - 21st Feb to 29th Feb 2024
#### Worked on:
- improved all_pairs_bellman_ford_path algo, yielding instead of returning a generator, chunking and added get_chunks kwarg, updated heatmap 
- Bench chunking(summarised and closed) 
- MAINT: updating backend.get_info 
- renaming backend info keys in networkx’s backend.py 
- improved all all_pairs_ algos(added improved heatmaps, benchmarks and get_chunks to all algos), added 2 more algos and updated threading backend to loki for all_pairs_node_connectivity 
- Reviewed PR - addition of a unit test in bipartite module
- [DOC, DISPATCH]: updated and added `backend.py`'s docs 
- added chunking and get_chunk, and added the improved heatmap to node redundancy (in the bipartite module) and square clustering 
- added get_chunks to johnson 

## February 21, 2024

Attendees: Aditi, Dan

### Topics:

- returning a generator VS yielding
- when will we need to use a different backend through joblib?(examples - todo Aditi)

### Work update : Week 7 - 14th Feb to 20th Feb 2024
#### Worked on:
- DOC: Adding CONTRIBUTING.md, updating readme, etc.
- [DOC, DISPATCH]: updated and added `backend.py`'s docs
- Bench chunking(added benchmark results with updated algorithms to the PR) 
- added get_chunk(updated test for get_chunk so that workflow tests don’t fail) 
- MAINT: updating backend.get_info(renaming keys) 
- centrality/reaching.py(added heatmaps, but no speedups; investigated on what happens on recursively calling joblib.Parallel) 
- node_redundancy in bipartite(added heatmap) : PR
- all_pairs_ algos(added heatmaps) 
- MAINT: removed `NETWORKX_GRAPH_CONVERT`

## February 14, 2024

Attendees: Mridul, Aditi, Dan

### Topics:

- No speed ups in `global_reaching_centrality` and `local_reaching_centrality`.
- `Error: The log was not found. It may have been deleted based on retention settings.` for `test_betweenness_centrality_get_chunks` with 1100 node graph(but it might not have anything to do with the size of the graph bcoz the same error is showing up in the lint test with a smaller test graph).


### To do:
- for bipartite.node_redundancy need to use different graph generation function(or add checks?), bcoz of `nx.NetworkXError(
networkx.exception.NetworkXError: Cannot compute redundancy coefficient for a node that has fewer than two neighbors.)` https://github.com/networkx/nx-parallel/pull/45
- running chunking vs no chunking benchmarks (https://github.com/joblib/joblib/issues/1543)
- handling `edge_attr`, `node_attr`, etc. : how to handle this on the nx-parallel side
- Merge approved PRs.
- check that renaming `is_strongly_connected` is the right approach: https://github.com/networkx/nx-parallel/pull/32

### Work update : Week 6 - 7th Feb to 13th Feb 2024
#### Worked on:
- Bench chunking(figured the issue with chunking with generators) 
- added get_chunk to betweenness_centrality and additional tests for get_chunk(smoke test)
- Added 2 algos(global_reaching_centrality, local_reaching_centrality) in centrality/reaching.py
- Added node_redundancy in bipartite 
- Added heatmap with speedups for johnson algo and square clustering algos 
- updated and added benchmarks and docs in all_pairs_ algos PR
- [merged]Added default_benchmark_timeout to asv.conf.json


## February 7, 2024

Attendees: Mridul, Aditi, Dan

### Topics:

1. benchmarks for node chunk vs individual nodes
    - how does joblib's `batch_size` fit into this?
        - joblib was set to "auto"(default) for these tests.
        
2. when to use shared resources between jobs
    - what happens with very large graphs and copying it to each job?

### To do:

- [Aditi] Graph size = RAM size (https://github.com/networkx/networkx/issues/5922)
- [Aditi] multiple args in the subset func or look up the outer namespace, in a parallel setting
- [Mridul] backends docs status

### Work update : Week 5 - 31st Jan to 6th Feb 2024
#### Worked on:
- MAINT: Styling fixes 
- MAINT : added `seed` to `gnm_random_graph` in `community/tests/test_label_propagation.py`
- added self-loops related docs and tests for functions in `cluster.py`
- Implemented chunking and no chunking versions of all 7 algorithms in nx-parallel and benchmarked them on VM and fixed a few bugs
- Added heatmap, benchmark, and docs for johnson algo 
- Style fixes and rebasing in square clustering 
- Style fixes modified ParallelGraph class in all_pairs_ algos PR 
- MAINT : Added default_benchmark_timeout to asv.conf.json


## January 31, 2024

Attendees: Mridul, Aditi, Dan

### Topics:

1. how do we decide when to chunk and compute and when to iterate over nodes, compute individual nodes on each core?(https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/centrality/betweenness.py#L16 VS https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L8) 
    - can yield one node at a time(if running nodes in parallel, instead of node_chunks) , speed up depends on chunks
    - chunking might be helpful when combining the results after parallel computation.
    - startup and tear down cost of chunks VS individual nodes
    - joblib's batch_size and node chunk : https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html
    - chunking speed up in cases like `number_of_isolates` (where the individual node's computation takes negligible time)?
2. when to use shared resources?
    1. chunking and computing each chunks on different cores and then combining the result_chunks(dicts) at the end to get the final_result(combined dictionary) : https://github.com/networkx/nx-parallel/blob/3ea018c816a5ce7a89f9f99e0e1387501d988b76/nx_parallel/algorithms/shortest_paths/weighted.py#L68 (Johnson)
    2. just like 1 but computing individual nodes(in parallel) instead of node_chunks : https://github.com/networkx/nx-parallel/blob/7eb5c614dd629b5c1ef78d1f9da4defed1441bbe/nx_parallel/algorithms/cluster.py#L7 (square_clustering)
    3. chunking and having shared resources(backend=“threading”, default is “loky”), had to create an empty “all_pairs”(the shared resource) dict of dicts to begin with here, uses threads not processes : https://github.com/networkx/nx-parallel/blob/0dd112bfe06fa284520f773a11dfe299814e8b0b/nx_parallel/algorithms/approximation/connectivity.py#L10 (all_pairs_node_connectivity)

- When we use joblib.Parallel with backend="threading", it creates user-level threads. The threading backend in Joblib is based on the threading module in Python. However, due to the Global Interpreter Lock present in the CPython interpreter, which allows only one thread to execute Python bytecode at a time, threading might not be well-suited for parallelizing CPU-bound tasks in Python. but it can be useful for tasks that are I/O-bound, as threads can make progress during I/O operations, such as reading or writing to files. For CPU-bound tasks, using processes (backend="loky" in Joblib) might be more effective, as each process gets its own Python interpreter with its own GIL. (ref. https://docs.python.org/3/library/threading.html , https://joblib.readthedocs.io/en/latest/parallel.html#shared-memory-semantics , https://stackoverflow.com/questions/46657885/how-to-write-to-a-shared-variable-in-python-joblib)

- [Mridul] Python 3.13 might remove GIL

- global config is over written by hard coded `return_as="generator"`

- inspiration from libraries dependent on joblib(for chunking etc.)

- drop in replacements and configuration independent of code implementation

- [Aditi]having a config for kwargs like `get_chunk` on nx-parallel's side

### Topics for next meet:

- nxp's backend docs issue
- additional tests(for `get_chunks`)

### Work update : Week 4 - 22nd Jan to 30th Jan 2024
#### Worked on:
1. MAINT: updated test_edge_current_flow_betweenness_partition to handle symmetry cases 
2. [merged]MAINT: style fixes in nx-parallel repo 
3. ENH: added johnson to nx-parallel 
4. Updated PR to add only 7 “all_pairs_” algos to nx-parallel
5. Fixed implementation of square_clustering in nx-parallel
6. renaming tournament like in the main networkx repo
7. [merged]updated to remove rename tournament function in a separate PR and resolved conflict with the main branch(backend_info PR) 
8. Backend func_info keys renaming PR : used walrus operator to make the code concise 
9. Added notes for self-loops in transitivity and generalized_degree and added test_self_loops_square 
10. [merged]dfs sort_neighbors : made sort_neighbors keyword only arg 
11. [merged]updated pre-commit-config 
12. [merged]added linting wf test 
#### Issues:
1. Unexpected test failures in test_algebraic_connectivity.py(in nx-parallel) (ref. Issue)
2. Unexpected test failures in test_edge_current_flow_betweenness_partition in nx-parallel for windows (ref. Issue)
3. [Discussion]self-loops consideration for clustering functions (ref. Discussion)

## January 24, 2024

Attendees: Aditi

Only one attendee.

### Work update : Week 3 - 15th Jan to 21st Jan 2024
#### Worked on:
1. [Ready for review] added square_clustering algo’s implementation to nx-parallel (ref. [PR](https://github.com/networkx/nx-parallel/pull/34))
2. [Ready for review] adding backend_info entry pt to nx-parallel : after discussing, decided to remove redundant docs and updated the get_info accordingly, made this PR independent from PR 7219(renaming PR) and created separate PR for pre-commit-config file (ref. [PR](https://github.com/networkx/nx-parallel/pull/27))
3. [Ready for review] updating pre-commit-config.yaml (ref. [PR](https://github.com/networkx/nx-parallel/pull/35))
4. [Ready for review] renaming backend `func_info` dictionary's keys : decided to remove “backend_func_examples” and made the code more concise by using the walrus operator (ref. [PR](https://github.com/networkx/networkx/pull/7219))
5. [Quick merge] added `time_tournament_is_strongly_connected` benchmark (ref. [PR](https://github.com/networkx/nx-parallel/pull/32))
6. [Merged] added lint wf test (ref. [PR](https://github.com/networkx/nx-parallel/pull/28))
7. [Ready for review] Adding sort_neighbors to DFS funcs : made the definition of get_children concise and resolved conflicts with the main branch (ref. [PR](https://github.com/networkx/networkx/pull/7196))
8. [WIP] Adding get_chunks kwarg : decided to remove joblib related kwargs and use a config dict instead, and added get_chunk kwarg (ref. [PR](https://github.com/networkx/nx-parallel/pull/29))
9. [Ready for review] added `all_pairs` functions to nx-parallel (ref. [PR](https://github.com/networkx/nx-parallel/pull/33))
10. [Not ready for review] experimented with adding parallelism to circleci in networkx - WIP (ref. [PR](https://github.com/networkx/networkx/pull/7231))
11. [Merge at EoC] removed TODO comment in tournament func (ref. [PR](https://github.com/networkx/networkx/pull/7226))

#### Issues closed/opened:
1. [resolved]No attributes 'from_numpy_matrix' and 'to_numpy_matrix' (ref. [Issue](https://github.com/networkx/networkx/issues/7239)) 
2. [opened]`test_ring_of_cliques` test fails unexpectedly (ref. [Issue](https://github.com/networkx/networkx/issues/7240))



## January 17, 2024

Attendees: Mridul, Aditi, Dan

### Topics:

Docs: Lets add a /doc directory to nx-parallel with 2 main documents:
    - a webpage that describes the option in joblib that we can control through backend_config with examples of how to change them.
    - a tutorial 

Both Dan and Aditi should send ssh key to Mridul to get us set up with a benchmarking cloud compute machine he is setting up. This link describes how to do that -- only send the public key -- and should be similar on Mac and only slightly different on windows.
https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-22-04

### Work update : Week 2 - 8th Jan to 14th Jan 2024

#### Worked on:
1. Renaming and adding backend func_info dict’s keys: 2 renamed(“extra_docstring” to “backend_func_docs” and “extra_parameters” to “additional_parameters”) and 2 keys added(“backend_func_url” and “backend_func_examples” (ref. [PR](https://github.com/networkx/networkx/pull/7219))
2. adding backend_info entry point (the get_info func) and updating docs for all funcs accordingly (ref. [PR](https://github.com/networkx/nx-parallel/pull/27))
    - maybe split get_info part into a separate PR
3. Added 4 more joblib-related kwargs and create_iterables functions to utils (ref. [PR](https://github.com/networkx/nx-parallel/pull/29))
4. [Approved]adding sort_neighbors to dfs funcs : changing name from sort_children to sort_neighbor, removing “callable” and returning the error to the user instead, and updating the docs accordingly (ref. [PR](https://github.com/networkx/networkx/pull/7196))
5. removing “TODO : This can be trivially parallelized” comments from networkx codebase (ref. [PR](https://github.com/networkx/networkx/pull/7226))
#### PRs reviewed :
1. Add nx.backend_config dict (ref. [PR](https://github.com/networkx/networkx/pull/7225 ))
#### Issues :
1. Refactoring and Simplification Suggestions(based on PR #7) : reviewed PR#7 in nx-parallel repo and created a detailed summary having suggestions and general analysis and the reasoning behind all of them (ref. [Issue](https://github.com/networkx/nx-parallel/issues/30))
    
## January 10, 2024

Attendees: Mridul, Aditi, Dan

### Topics:

- documentation:
    - adding to networkx main docs. Currently NX loads a dict from the backend that contains the text for each function.  See an example here: [graphblas's dict](https://github.com/python-graphblas/graphblas-algorithms/blob/main/_nx_graphblas/__init__.py) and [backend_info](https://github.com/python-graphblas/graphblas-algorithms/blob/35dbc90e808c6bf51b63d51d8a63f59238c02975/pyproject.toml#L70)(automate making the dictionary)
    - should we have a documentation website for nx-parallel? We might want one at some later point, but for now let's hold off until we have a better idea of what nx-parallel will be providing.
- networkx PRs
     - nice work here... reviewing as well as contributing. :)
- nx-parallel new algorithms
    - find TODO with "trivially parallelizable"
    - find old PR/Issues that talk about parallel and implement tose functions
- which joblib parameters should we have set via the function and which can be set outside the function signature? 
        - context manager(advantage : if joblib adds more parameters) : adding tests for this
        - function args(disadvantage : overloads the function calls)
    - we like the joblib context manager approach. Let's include in nx-parallel some tests that use the joblib context manager
- should we include functions that let users choose their own chunking?
    - let's wait to provide this. What situations might someone want to do this?
        - if the user has info on which nodes might take a lot of time -- they can split them so they are evenly distributed in each chunk.
        - chunking with some random seed

### Work update : Week 1 - 1st Jan to 7th Jan 2024

#### Worked on:
1. updated pre-commit-config.yaml and docs for all funcs(added nx-parallel specific egs and docs), tried adding n_jobs kwarg, researched how joblib and sklearn configure it (ref. [PR](https://github.com/networkx/nx-parallel/pull/27))
2. added lint work-flow test and made style fixes accordingly (ref. [PR](https://github.com/networkx/nx-parallel/pull/28))
3. Created a separate PR for adding joblib-related kwargs(later decided to have a config. dictionary instead) (ref. [PR](https://github.com/networkx/nx-parallel/pull/29))
4. adding sort_children to dfs funcs : had discussions on iterable VS iterator and modifying the code and docs accordingly in dfs and bfs functions (ref. [PR](https://github.com/networkx/networkx/pull/7196))
5. [merged]Updated docstring in panther_similarity (ref. [PR](https://github.com/networkx/networkx/pull/7175))
6. [merged]Replaced “plugin” with “backend” and updated README in nx-parallel (ref. [PR](https://github.com/networkx/nx-parallel/pull/26))
7. [merged]Developed a benchmarking infrastructure : changed config files and updated README (ref. [PR](https://github.com/networkx/nx-parallel/pull/24))
#### PRs co-reviewed :
1. corner cases in rich_club_coefficient (ref. [PR](https://github.com/networkx/networkx/pull/7212))
2. corner cases in random_spanning_tree (ref. [PR](https://github.com/networkx/networkx/pull/7211))

## January 3, 2024 - Kickoff 2024 meeting

Attendees: Aditi, Dan

### Topics:

- doc_strings (nx vs nx-parallel)
    - we are assuming that most of the users of nx-parallel are coming from networkx, so the docs should be written accordingly
    - we discussed including description of how we parallelize the algorithm. Include parameters not in the networkx function and maybe all the parameters for completeness??. Benchmarking should be part of the docs, but maybe separate from the function descriptions. We'll try this and see if it needs changing.
    - The 2-5 lines of documentation we put into the NetworkX documentation are important too because they invite the user to the nx-parallel package.
- n_jobs default value
    - let's stick with the joblib name n_jobs and use joblib's default value and handling of negative values.
- testing
    - run network tests with nx-parallel backend. Look for types of tests that would be helpful to test the parallel aspects. Look for algos which give different results based on number of cpus. 
- benchmarking
    - parameter : type of graph generation method(barabasi_albert_graph, real world graphs, fast_gnp_random_graph, small world graphs)
    - using different OSs
    - benchmarks on SNAP datasets
- extra
    - we decided we should have functions in nx-parallel that are already in networkx(flexible)

## December 20, 2023 - Kickoff meeting

Attendees: Aditi, Mridul, Dan

### Topics:
- Documentation?
    - Should nx-parallel have it's dedicated doc website?
    - Each function which is implemented by nx-parallel should have a link in it's NX docs. The backend docs need to have information about extra keyword args or args that have constraints.

        - for example, there should be an argument for the number of jobs that can be run at once.

- Benchmarks?
    - Where to keep an encompassing benchmark which uses all the backends? To bring up in community/dispatching.
    - Adding memory benchmarks. asv has some memory measurement systems. Also [memray](https://github.com/bloomberg/memray) was mentioned.
    - benchmarks for how good(accurate) the approximation is, for approx. algos?

- Testing?
    - One idea is to just use networkx tests. [Graphblas-algorithms has this](https://github.com/python-graphblas/graphblas-algorithms/blob/main/graphblas_algorithms/tests/test_match_nx.py)
    - Can run locally for nx-parallel:
    ```NETWORKX_GRAPH_CONVERT=parallel \
          NETWORKX_TEST_BACKEND=parallel \
          NETWORKX_FALLBACK_TO_NX=True \
                python -m pytest --pyargs networkx

          python -m pytest --doctest-modules --pyargs nx_parallel```
