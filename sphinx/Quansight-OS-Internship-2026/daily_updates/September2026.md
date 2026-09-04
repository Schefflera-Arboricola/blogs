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

