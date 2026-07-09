Notes : https://hackmd.io/@Schefflera-Arboricola/H1Gvmv5zGg/edit

# ~~7th~~ 9th July, 2026 (07:30pm IST, 11:00am BRT)

**Attendees**: Aditi, Agriya, Melissa

## Agenda

- Summary of the week:
    - Testing a few different projects, building the docs and noting their workflows and setups
    - tested some profiling tools and used statsmodels and cpython docs for investigation
    - investigating docs build steps 
    - using graph profiling tool to outline cpython docs build
- Use Matplotlib as an experiment instead of cpython
    - image-heavy and lots of gallery examples
    - point people: Melissa, Tim Hoffman(also sphinx maintainer) - could provide insightful feedback
    - places to get feedback by the project maintainers using sphinx on different pain-points in the docs build process: 
    - https://discourse.matplotlib.org/ (Melissa: chat space gets more eyes-- but you can't see it if not logged in)
    - scikit-learn discord (point person: Loïc Estève) - also sphinx-gallery heavy project
    - scientific python discord (matplotlib) - https://github.com/QuLogic and https://github.com/ksunden

- Issue https://github.com/sphinx-gallery/sphinx-gallery/issues/1519 : [Agriya] place to look at - the interaction between sphinx and sphinx-gallery when sphinx hands the different examples to sphinx-gallery and how it hands them

- sphinx-gallery
    - point person: Lucy Liu
    - Look at https://github.com/sphinx-gallery/sphinx-gallery/blob/master/sphinx_gallery/gen_gallery.py (specifically https://github.com/sphinx-gallery/sphinx-gallery/blob/b956e2e15c3025c0552d59db67e5cd3afc2d3520/sphinx_gallery/gen_gallery.py#L1719)
    - First idea: run sphinx process graph with sphinx-gallery enabled and investigate when each sphinx-gallery action happens in the sphinx build process
    - Maybe investigate each sphinx build stage separately for potential performance improvements (like parallelization)
    - Agriya points out the finishing phase (writing files) may be done in parallel?

- napari
    - https://github.com/napari/docs/blob/main/docs/conf.py
    - has notebooks, gallery examples, screenshots/screen recording of napari GUI 
    - napari_scraper, etc.
    - a lot of customisation in its build process


---


# 29th June, 2026 (06:30pm IST, 10:00am BRT)

**Attendees**: Aditi, Agriya, Melissa

## Agenda

- knowing each other better 
    - working/co-ordinating styles

- priorities/milestones/ways for evaluations, 

- guidance on how best to proceed with the project: initial next steps and work items

---

### Understanding the Community:

- Any community meetings for sphinx project? Or the pydata sphinx theme project I should attend? 
    - no regular sphinx project meetings
    - https://www.sphinx-doc.org/en/master/support.html#support-index
    - Other ways to engage with the community?
        - https://github.com/orgs/sphinx-doc/discussions
        - Write the Docs Slack #sphinx channel
        - Scientific Python discord #pydata-sphinx-theme channel
        - community meeting thread
        - https://www.jareddillard.com/about: Jared Dillard
        - Matthias Bussonnier (@Carreau on GitHub, also on QS Slack). Currently mentoring Yann Pellegrini on the PST
        - Adam Turner (Sphinx, CPython, etc.) – AA-Turner on GitHub
        - 
- Does the sphinx community have this benchmarking and profiling project in their roadmap— will they have time to review and give feedback?
    - Mostly in the Quansight-Labs org for now
    - more leaning towards having a benchmarking tool in quansight's github-- but can look into integrating into the sphinx project

### Understanding the project better:

- do you currently have a hypothesis about where the bottlenecks (or potential areas of optimisations) are, or is the first goal genuinely to build a profiling mechanism and let the data guide us?
    - auto-summary generating a lot of pages
    - This issue for the sidebar too: https://github.com/pydata/pydata-sphinx-theme/issues/762
    - Sphinx finishing pages could be parallelised (maybe-- todo: investigate)

- How will people use this benchmarking tool? And who will be using it?
    - is the goal mainly for Sphinx (and sphinix themes) core developers to identify bottlenecks and optimize their projects, or is it also something that documentation maintainers(i.e. users of sphinx, like numpy, scipy etc.) could run on their own projects to understand why and where their builds are slow— and which theme would build their website the fastest?
    - more as a benchmark suite (similar to pyperformance) where we track a few large projects over time, or as a local, command-line profiling tool where someone can run something like `make html --profile` for their own docs and get a breakdown of build time— reading files, autodoc, cross-reference etc?
    - Answer: more for sphinx developers than end users
    - instead on different themes focus on a general theme:
        - Basic sphinx setup template: https://github.com/melissawm/minimalsphinx
    - having diverse set of projects - heavy in autosummary(scipy), nb, etc.
    - playwright - https://github.com/microsoft/playwright

- https://github.com/chrisjsewell/sphinx-process-graph — can I create this kind-of graph for any docs build? Are there any docs on how to use this project? No, read code!
    - [Agriya] idea: node weights representing the time taken by that step

- Any particular contributors, projects, or doc builds that would be good examples for me to study and understand?
    - https://github.com/sphinx-doc/sphinx
    - https://github.com/sphinx-doc/sphinx/issues/14277
    - https://github.com/pydata/pydata-sphinx-theme/issues/762
    - https://github.com/chrisjsewell/sphinx-process-graph <- super useful!
    - https://github.com/python/pyperformance
    - https://speed.python.org
	- https://github.com/flying-sheep/rust-rst
    - 


### Understanding the Mentoring style(s):

- Reporting: As the problem space is not fully defined, how do you usually like to structure mentorship? 
    - “More frequent discussions to decide direction” Vs “longer periods where I explore independently and bring back findings”
    - early stages: would you expect code contributions quickly, or is spending the first 2-3 weeks understanding Sphinx internals and setting up some goals considered good progress?
        - Spending time is exploring is great! We would like to check in regularly though, both to understand where you are and to give you the opportunity to ask questions when needed.
        - Melissa: don't stay stuck-- meeting once a week is good with async communications

- Project goals/priority:
    - At the end of the internship, what would make you feel like this project was successful even if we don’t explore and implement every possible optimisation?
    - Which part of the project holds more value to you? — profiling/benchmarking foundation or concrete speedups/optimisations
    - focus a bit more time on benchmarking tool initially (first 5-6 weeks)
    - success of the project : doing the investigation and research even if the project is not "completed" in a traditional sense
    - engage with community and coordinate - 

### ToDos

- go through the above resources and build process
    - https://github.com/chrisjsewell/sphinx-process-graph -- possibly document this
- join write-the-docs slack - sphinx channel
- meeting times :
    - 8:30 pm IST Wednesday- interns' meeting
    - Mentors meeting- Tuesdays: 5:30 pm IST
- Py03 tutorials - for personal learning -- maybe we will use it in the later phase -- might use it in an extension but sphinx project would probably prefer to not have any compiled rust code in it.

