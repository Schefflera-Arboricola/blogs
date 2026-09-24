
## Week of Sep 21 - Sep 25

### What went well this week? ✨

- v0.2.0 release: pls see the commit history on Github for more: https://github.com/Schefflera-Arboricola/sphinx-benchmark/compare/v0.1.0...v0.2.0
- worked on the blog : https://github.com/Quansight/Quansight-website/pull/1011
- worked on the QShare presentation and talk proposal for IndiaFOSS
- 1 PTO
- will give a lightening talk at IndiaFOSS on Sunday, if the proposal gets accepted.

### What do you want to achieve/complete next week? ✅

- address any reviews on the blog PR and get it merged/published.
    - need to fix the alignment and formatting of the figures
- Qshare presentation
- try implementing an optimisation based on the benchmarks
- update/add benchmarking outputs
- discuss implications of feature proposed in issue [#38](https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/38) with mentors
- spread the word about the extension in different community forums/channels/groups/conferences
- off-boarding
- work on other open issues and create some more open issues
- move extension to QS or sphinx-doc or sphinx-contrib github org

### If only one deliverable/project could get done this week what would it be? 🚀

- address any reviews on blog PR and get it merged/published.
- Qshare presentation
- try implementing an optimisation based on the benchmarks
- update/add benchmarking outputs
- discuss implications of issue [#38](https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/38) with mentors
- spread the word about the extension in different community forums/channels/groups/conferences
- off-boarding
- work on other open issues and create some more open issues
- move extension to QS or sphinx-doc or sphinx-contrib github org

### What's your biggest challenge right now, and how can I help? 🤝

I just want to say thank you. Your guidance, patience, and time over these three months meant a lot to me and I'm truly grateful to you both! Working on sphinx-benchmark taught me how to find my way around unfamiliar concepts and challenges, and how to ask for help and improve the quality of the code I write. And I think I've grown a lot as an open-source contributor and as a software developer, and I'd love to stay in touch after the internship.

I'd love to keep contributing after the internship, so if there's anything I can take off your plate, let me know. I hope we stay in touch. And I hope to contribute more and get more involved in the Scientific Python community. Thanks!


---


## Week of Sep 14 - Sep 18

### What went well this week? ✨

- PRs merged/worked on (see the PR description for more):
    - improved workflows, added zizmor and pre-commit.ci: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/30
    - Sampling the docs build's function call stack: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/27
- opened issues
    - Include a per-document time breakdown table/page to the benchmarks report: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/28
    - allow users to configure the sampling time interval: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/29
    - Add support for free-threaded python: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/31
- worked on drafting the internship blog
- got a lot of additional, useful feedback and support in the coffee-buddies session with Melissa (and also by Agriya over the weekend)

## What do you want to achieve/complete next week? ✅

- PR #27
    - improve code quality
    - add more documentation - about the internal workings and in the benchmarks report
    - Update benchmarks: upload `json`s instead of outputs
    - improve the report interface and CLI
- Enable changing the default sampling interval time: issue #29
- Add serial build warning in the benchmarks report
- Move write_json and classify_all_handler outside EventLogger-- find any other similar improvements-- following system design principles
- reduce Sphinx version to 8
- post about this extension in different groups, channels, etc. -- spread the word
- Add more projects benchmarks: CPython, PyWavelets, pytest (furo theme), sympy, and others in the Scientific Python ecosystem
- change github org to quansight labs and Make release v0.2
- Work on the blog and final QShare presentation
- work on adding optimisations based on the benchmarking results

### If only one deliverable/project could get done this week what would it be? 🚀

- merge PR #27, resolve issue #29
- Add serial build warning in the benchmarks report
- Move write_json and classify_all_handler outside EventLogger-- find any other similar improvements-- following system design principles
- reduce Sphinx version to 8
- post about this extension in different groups, channels, etc.
- change github org to quansight labs and Make release v0.2
- Work on the internship blog
- PTO: traveling for IndiaFOSS (will give a lightening talk on sphinx-benchmark if my proposal gets accepted.)

### What's your biggest challenge right now, and how can I help? 🤝

My main challenge is mainly trying to make the most of these last few weeks by getting as much important work done as possible, while also balancing blog and presentation deadlines, travel, and preparation for the upcoming conferences.

I'd really appreciate any feedback on how I should prioritize tasks in the coming days-- and in general on the work I've been doing, the code quality, user interface, or anything else that could be improved. Also anything to help spread the word about this extension and get more feedback would be great!


---


## Week of Sep 7 - Sep 11

### What went well this week? ✨

- [WIP] Gap breakdown: capturing what runs in between events, since a large share of build time currently falls outside any sphinx event emissions. Approach: a parallel [daemon thread](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) sampling [`sys._current_frames`](https://docs.python.org/3/library/sys.html#sys._current_frames) during the gaps. Related: [discussion](https://discuss.python.org/t/getting-rid-of-daemon-threads/68836) on the future of daemon threads (maybe a risk to this approach).
- Merged PRs:
    - added more options to CLI and more details to the html report : [PR#15](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/15)
    - added project info(project name, version, HEAD commit, copyright) and build info(builder, start time, total time) to the json and output : [PR#20](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/20)
    - Including unique identifiers (date, start time, HEAD) in the benchmarks json filename : [PR#23](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/23)
    - added github workflows (lint, pytest, publish) : [PR#24](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/24)
- issues opened:
    - [AI] Handlers are misattributed between sibling namespace packages: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/26
    - Add serial build warning in the report : https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/25
- 1 PTO

### What do you want to achieve/complete next week? ✅

- Add a gap-breakdown to the benchmarks
- Address review comments on [PR #24](https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/24)
- Add zizmor (GitHub Actions linting) as a pre-commit hook for now
- Lower the minimum Sphinx version to 8 so SciPy can run this extension
- Add a warning msg to the benchmarking output about serial build
- 0.2.0 release
- work on blog
- enabling parallel builds
- optimisations
- Add more projects' benchmarks: CPython, PyWavelets, pytest (furo theme), sympy, and others in the Scientific Python ecosystem
- work on other open issues

### If only one deliverable/project could get done this week what would it be? 🚀

- The gap-breakdown PR
- push some of the quick and easy items from the above list and make 0.2.0 release.
- work on blog

### What's your biggest challenge right now, and how can I help? 🤝

The gap-breakdown design is the biggest challenge right now, I think. Any feedback on this would be great: if the sampling overhead distorts the benchmarking numbers, whether there's a more durable alternative approach given the daemon-thread discussion above, any user interface related feedback.


---


## Week of Aug 31 - Sep 4

### What went well this week? ✨

- WIP:
    - adding more options to CLI and more details to the html report: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/15
    - added project info(project name, version, HEAD commit, copyright) and build info(builder, start time, total time) to the json and output: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/20
    - running cProfile alongside the docs build to analyse the gaps in the benchmarks
- Merged PRs (based on users/mentors feedback)
    - Improve output message with file path for JSON: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/10
    - Updating handler classification for extensions in `sphinx.ext.` module: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/19
    - Update hatchling requirement and license fields: https://github.com/Schefflera-Arboricola/sphinx-benchmark/pull/17
- issues opened:
    -  a more detailed gaps summary table: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/9
    -  allow users to name sphinx_benchmarks.json or add some unique identifier in the file name so that it doesn't get over-written and lost: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/22
    - Flag network-related overheads and failures in the benchmarks (intersphinx fetches, kernel connection timeouts): https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/18
    - add more projects' benchmarks: https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/16

### What do you want to achieve/complete next week? ✅

- address any reviews comments on open PR#15 and #20 and get those merged.
- Close https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/22 : stop overwriting `sphinx_benchmarks.json`
- Set up GitHub Actions, switch to trusted publishing, and make a second release :https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/14
- post about the extension on the Write the Docs Slack.
- Account for the gaps breakdown : https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/9
- Add a CLI option to compare two JSON outputs
- Draft the blog post

### If only one deliverable/project could get done this week what would it be? 🚀

- address any reviews comments on open PR#15 and #20 and get those merged.
- Close https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/22 : stop overwriting `sphinx_benchmarks.json`
- Set up GitHub Actions, switch to trusted publishing, and make a second release :https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/14
- post about the extension on the Write the Docs Slack.
- Account for the gaps breakdown : https://github.com/Schefflera-Arboricola/sphinx-benchmark/issues/9

### What's your biggest challenge right now, and how can I help? 🤝

I'm new to working with stacked PRs-- the merge sequence, keeping the dependent branches in order, rebasing cleanly when the base PRs change, etc. I've been reading the official github docs on stacked PRs, but any pointers to any useful resources would be helpful.

Also, I'd really value any feedback on the extension itself-- the CLI, HTML report, and JSON output, and anything you'd like me to prioritize or rethink. And any feedback on how I'm approaching the work and how I'm doing overall as an intern/contributor. Concrete, critical feedback is genuinely welcome -- it'll be very useful for me to be better.


---

