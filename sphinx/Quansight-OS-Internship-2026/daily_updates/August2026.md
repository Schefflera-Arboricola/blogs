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

