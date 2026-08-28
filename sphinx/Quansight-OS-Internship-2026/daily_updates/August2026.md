## TL;DR

The project has progressed from a basic event-wise Sphinx benchmarking tool into a more complete and usable profiling extension, now renamed **sphinx-benchmark** and released on both [PyPI](https://pypi.org/project/sphinx-benchmark/) and [GitHub](https://github.com/Schefflera-Arboricola/sphinx-benchmark/releases/tag/v0.1.0). Most of the work was carried out in [PR#2](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/2), [PR#3](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/3) and [PR#8](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/8). At the moment, the extension profiles and benchmarks a docs build and reports three things: a per-event breakdown of where time goes, a per-handler (with extension, theme and top-level module) breakdown within each event (so a slow event can be traced to the specific extension responsible), and a summary of the "gaps" -- the time that falls outside any event emissions. Events are tracked as a tree via a private stack, so that nested events don't get double-counted.

The extension now has basic tests and substantially improved documentation, and has been benchmarked against Matplotlib, NumPy, NetworkX, and Pandas. A basic CLI renders the benchmark data either as terminal summary tables or as a static three-page HTML report. Feedback has been gathered from downstream projects at QShare and is now being collected more widely -- via the sphinx-dev mailing list, [Sphinx's GitHub Discussions](https://github.com/sphinx-doc/sphinx/discussions/14652) (which also carries a proposal to shift the extension into the sphinx-doc organisation), the Scientific Python Discord, and Quansight's internal Slack. The main remaining challenge is that a meaningful portion of Sphinx build time still appears as unexplained "gaps" that cannot currently be attributed to specific events, handlers, extensions, or other parts of the build process -- which limits the tool's usefulness for finding optimisations inside Sphinx itself, as opposed to within extensions. Reducing the extension's own measurement overhead is the other open issue that needs to be addressed.


---


## Week of Aug 24 - Aug 28

### What went well this week? ✨

- [PR#3](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/3) merged!
    - replaced record_event with enter_ and exit_event: maintains a stack of currently in progress event emissions (events like a DFS-tree); 
    - keeping track of event's id, depth, parent_id and own_times; 
    - storing total_wall_time in the json; 
    - replaced print_summary with a separate script that prints the benchmarking summary, and printing gaps' summary table at the end, and printing number of emissions for each event
    - added try-except in setup()
    - updated README: added sections on Usage, installation, Limitations of the extension, How are benchmarks calculated?, how to read benchmarks and what benchmarks mean
    - updated and added benchmarks for matplotlib, numpy, networkx, pandas
    - added basic tests
- switched from setuptools to hatchling: https://github.com/Schefflera-Arboricola/sphinx-benchmark/commit/a1518f906d11ff621fa039e8b5ea3e552d86fab3
- closed https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/5
    - renamed the project to `sphinx-benchmark`
    - made a PyPI release: https://pypi.org/project/sphinx-benchmark/
    - made a Github release: https://github.com/Schefflera-Arboricola/sphinx-benchmark/releases/tag/v0.1.0
- gathering community feedback:
    - sphinx-dev mailing list(approval pending)
    - sphinx's github discussions: https://github.com/sphinx-doc/sphinx/discussions/14652
    - scientific python discord(documentation channel)
    - quansight's internal slack
- Wrote a proposal to add the sphinx-benchmark extension to the sphinx-doc github organisation: https://github.com/sphinx-doc/sphinx/discussions/14652
- added a basic CLI to display the benchmarks in `table` and `html` formats: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/8
    - Reads sphinx_benchmarks.json and renders it either as the two terminal summary tables or as a static three-page HTML report(overview with pie chart, events and handlers, gaps).
- opened: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/7


### What do you want to achieve/complete next week? ✅

- Break down the gaps : try wrapping `app.registry`, `SphinxTransformer.apply_transforms` or `Builder` and see if that gets us more information
- Reduce the extension's own overhead
- Test and benchmark against more scientific Python projects, and debug any issues
- Build on the CLI -- more options and improvements(needs to discuss with the mentors first)
- Work on the open issues and the limitations listed in the README
- Continue collecting feedback from mentors, Sphinx maintainers, extension authors, users and act on it
- Start drafting the internship blog post

### If only one deliverable/project could get done this week what would it be? 🚀

- Getting the gaps' breakdown
- Reduce the extension's own overhead
- Test and benchmark against more scientific Python projects, and debug any issues

### What's your biggest challenge right now, and how can I help? 🤝

- A meaningful chunk of build time still lands in gaps the extension can't attribute to anything, which makes the extension useful for optimising other sphinx extensions but not necessarily to add optimisations within the sphinx's codebase. I'm looking into methods and class that I could track to get more detailed gap break down-- any help on this would be great! 

- Another thing I would like help and suggestions on is reducing the overhead that the sphinx-benchmark extension adds itself to the build process.

- Another thing is that almost every design decision so far has been mine and my mentors alone-- the event-tree model, the JSON output, how the summary reads -- so what I'd most value is feedback from someone running this extension on their project and telling me whether the output actually tells them anything useful(like here: https://github.com/pydata/pydata-sphinx-theme/pull/2477).


---


## Week of Aug 17 - Aug 21

### What went well this week? ✨

- Worked on [PR#3](https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/pull/3)
    - addressed all the review comments (except one about accounting for gaps in benchmarks- WIP)
    - fetched theme packages from `sphinx.html_themes` entry-point
    - wrapped `app.connect` and accounted for more events and handlers registered all throughout the docs build process
    - as a result of above, moved handler classification towards the end (in build-finished handler)
    - undoing the wrapping of `emit_firstresult` to avoid overlap in the timing results
    - made the extension work for matplotlib docs (for when module=None i.e. handler is in conf.py)
    - using `functools.wraps` to wrap listeners
    - moved benchmarking output to a separate folder
    - WIP : integrating a notion of `depth` to avoid double counting of the durations of events/handlers (for cases of nested events and when handlers emit events)
- Drafted a work plan for the remaining internship weeks: https://docs.google.com/document/d/1QD5vizVFdMjJFkOb6FGRaDSFqUEPIMSo65_kMpaiFMI/edit?usp=sharing
- open 3 issues for next week: 
    - [Refactor extension to enable parallel reading and writing](https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/issues/4) 
    - [Rename extension (`sphinx-benchmark`) and publish a release on GitHub and PyPI](https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/issues/5) 
    - [Add a basic sphinx-benchmark CLI](https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/issues/6)
- Discussed the above with mentors and got really useful feedback and a clearer long-term direction for the project and its usage! (see [meeting note](../notes/mentor_meetings_notes.md) for more.)

### What do you want to achieve/complete next week? ✅

- In PR#3
    - Commit the `depth` implementation and display a meaningful breakdown of the gaps between the events (and in the build process, in general)
    - Add basic documentation and tests 
    - address any reviews/questions by mentors
- Work on the above 3 opened issues
- Organise and refactor the codebase into multiple files (`classes.py`, `utils.py`, `extension.py`) instead of one large file.
- Test with and benchmark different scientific python projects, and debug any issues.
- Start looking into the PyData sphinx theme sidebar issue: https://github.com/pydata/pydata-sphinx-theme/issues/762

### If only one deliverable/project could get done this week what would it be? 🚀

Get the extension to a basic, usable state with docs, tests, and a basic CLI, and then rename the extension and release.

### What's your biggest challenge right now, and how can I help? 🤝

Adding `depth` is a fairly big change because it affects several other methods/functions in the codebase-- so keeping track of variables and how they are updated, etc. 

Then another main challenge is presenting the gaps (in between events) break-down in a meaningful and intuitive way to a user. And also identifying and minimising any overlapping or double-counting due to nested events, handlers that emit other events or anything else (idk yet?).

I don't know if I need help with a specific thing but any questions/insights/feedback on any of the above stuff would be great!


---


## Week of Aug 10 - Aug 14

### What went well this week? ✨

- Extended the Sphinx build profiler/benchmarking tool to break down timings at the handler and extension level, not just per-event-- so we can now see exactly which extension/handler is responsible for time spent in a given build event. Details on the approach (and its current limitations) are in the PR description: https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/pull/3
- Spent significant time inspecting the benchmark accuracy itself -- tracing through the build lifecycle to catch gaps between what we were measuring and actual wall-clock time, so the durations reported can be trusted.

### What do you want to achieve/complete next week? ✅

- Close the remaining gaps so every component of the build process is accounted for and is reflected in the benchmarks
- Add test coverage for the profiling extension
- Investigate making the extension parallel-read/write safe
- Turn this into a CLI tool

### If only one deliverable/project could get done this week what would it be? 🚀

Getting full, accurate coverage of all build components in the benchmarks-- that's the foundation everything else (tests, CLI, parallel safety) builds on.

### What's your biggest challenge right now, and how can I help? 🤝

I'm still testing this against different projects to see how well it generalizes as a benchmarking tool, and most of next week's items (ensuring all components are reflected in benchmarks, testing, parallel safety, packaging as a CLI) are new territory for me, so I'm not yet sure whether it's a one-week or multiple weeks of workload. And I'd appreciate any feedback on the PR and the approach, and if you could suggest any projects to test it on that could help identify more limitations of the current code/approach.


---


## Week of Aug 3 - Aug 7

### What went well this week? ✨

- Implemented event-wise benchmarking: https://github.com/Schefflera-Arboricola/benchmark-sphinx-phase-wise/pull/2
- Benchmarked matplotlib, numpy and networkx; key observations:
    - `config-inited` takes close to 50% of build time in Matplotlib and NetworkX, largely due to the Sphinx-Gallery extension.
    - `doctree-resolved` is the most time-consuming event in NumPy, primarily due to resolving and cross-referencing during the writing phase.
- Experimented with visualising benchmark results as a directed graph using gprof2dot (thought of doing something like this in week 1). This approach was good for exploration, but i think this probably won't be the best format for presenting the final benchmarking results. See the graph visualisation [here](../notes/assets/static/event_graph.png).
- Reached out to downstream projects (at QShare) to gather feedback on the usefulness of phase-wise benchmarking data. Key feedback included:
    - Sidebar performance issues
    - Slow HTML writing
    - More detailed benchmarking results --> switched to event-wise benchmarking and will work more in this direction in the coming weeks
    - implementing some potential Sphinx/doctree optimisations for faster documentation builds
    - Performance issues with MyST and notebooks
    - Need for a `autoreload` system -- to automatically reflect source-code changes during the docs build/rebuild
    - Cache misses in SciPy
    - Several of these issues were also mentioned in the initial project description discussions with the mentors
- brainstormed and investigated approaches for identifying the extension associated with each Sphinx event, including introspecting the Sphinx `app` object and handler objects to identify the corresponding extension. Discussed possible approaches with mentors and LLMs-- still a WIP!

### What do you want to achieve/complete next week? ✅

- Figure out a reliable approach to add extension-level information to the current benchmarks:
    - Explore the event-listener approach in sphinx-process-graph repo
    - Investigate Sphinx internal APIs for obtaining extension-level breakdowns
    - Explore whether Sphinx's `emit()` mechanism can provide this information
- there has been some activity by a sphinx maintainer on [issue #14532](https://github.com/sphinx-doc/sphinx/issues/14532) so, I'll look through that and hopefully contribute a PR. I had previously worked on this issue during Week 2 and was waiting for feedback from the maintainers.

### If only one deliverable/project could get done this week what would it be? 🚀

Figure out and implement the most reliable approach to add the extension-level information and introspection to the existing event-wise benchmarks.

### What's your biggest challenge right now, and how can I help? 🤝

- The main challenge is identifying the right approach for attributing benchmarked events to specific extensions.
- I also need to determine how to capture performance from custom Sphinx code that is not implemented as an extension but in the downstream project itself.
- Another area to explore is capturing parallelism/concurrency information in the build process and displaying that in the benchmarks.


---

