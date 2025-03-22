meeting_notes_hackmd: https://hackmd.io/4oRcgg9EQeWQ18Mv2sdfMA

# scikit-image dispatching meetings

# 2025-03-19

Wednesday : 08:00 AM to 09:00 AM UTC

Meeting link https://meet.jit.si/scikit-image-dispatching

**Attending**: Only one attendee; No meeting

-
# 2025-03-05

Wednesday : 08:00 AM to 09:00 AM UTC

Meeting link https://meet.jit.si/scikit-image-dispatching

**Attending**: Sebastian. Aditi

- [PR 7520](https://github.com/scikit-image/scikit-image/pull/7520) merged! :tada: 
- Feedback on: 
    - including `should_run` ([see here](https://github.com/scikit-image/scikit-image/pull/7723#issuecomment-2692378689))
        - we can merge `can_has` into `should_run` if conversion is already done by the cucim
        - `should_run`'s place in dispatching could be figured out after seeing where the conversion is happening.
    - avoiding conversion and testing([see here](https://github.com/scikit-image/scikit-image/issues/7738))
        - bundling cucim calls in a context to reduce the conversion steps
        - CPU and GPU shared memory(unified memory - in new hardwares) --specific to GPU and CPU conversions (`cp.asarray(np_arr)`)
        - which args to convert?
    - https://github.com/scikit-image/scikit-image/pull/7727 -- review and should this PR be broken down into smaller PRs?
    - renaming `can_has`?

# 2025-02-19

Wednesday : 08:00 AM to 09:00 AM UTC

Meeting link https://meet.jit.si/scikit-image-dispatching

**Attending**: Aditi, Sebastian

- Adding `_dispatchable` to more scikit-image functions ([review comment by @grlee77](https://github.com/scikit-image/scikit-image/pull/7520#discussion_r1960525428)):
    - skimage.morphology.binary_erosion [DEP]
    - skimage.morphology.binary_dilation [DEP]
    - skimage.measure.label
    - skimage.measure.regionprops_table
    - skimage.transform.resize
    - skimage.transform.warp
    - ...?

- Discussions with cuCIM: https://github.com/rapidsai/cucim/issues/829
    - [Gregory] `From March I may be able to have a bit more dedicated time for it[dispatching], but we can try to make some initial progress before then`
    - discussions on `can_has`, array conversions, etc.
    - adding `should_run` like thing-- for cuCIM like backends which cannot handle really small arrays?
    - cuCIM can support both array types(cupy and numpy)
    - conversion can get complicated
    - conversion in testing? 
        - backends might like to run scikit-image's test suite to compare themselves with scikit-image than to use scikit-image's testing solely for testing(bcoz of the conversion cost)
    - caching arrays is hard - arrays are mutable

- After [PR 7520](https://github.com/scikit-image/scikit-image/pull/7520):
    - PR https://github.com/betatim/scikit-image/pull/1
        - open this PR on scikit-image's main 
        - [ToDo: Aditi] setting backend priority via context manager/function
    - renaming `can_has`?


# 2025-02-12

Wednesday : 08:30 AM to 09:00 AM UTC

Meeting link https://meet.jit.si/scikit-image-dispatching

**Attending**: No meeting


# 2025-02-05

Wednesday : 08:00 AM to 09:00 AM UTC

Meeting link https://meet.jit.si/scikit-image-dispatching

**Attending**: Tim, Aditi, Lars, Sebastian


- Tim's Dispatching PR
  - Nitpick: [`public_api_name` -> `public_api_module`](https://github.com/scikit-image/scikit-image/pull/7520/files#r1920296476)
      - :+1: from @betatim
  - Nitpick: Might want to conform docstrings to rest of library (parameter section, etc) 
    - Will defer that to Aditi's PR
  - Nitpick: https://github.com/scikit-image/scikit-image/pull/7520#discussion_r1879754422
      - in Aditi's PR --> change wording `we don't check the passed args and kwargs...`
  - Nitpick: document backends should not be imported in `can_has` but in `get_implementation`
      - in Aditi's PR
  - what should happen to https://github.com/betatim/scikit-image-backend-phony
      - proposal: move it to the scikit-image org as reference/example/documentation
  - Lars Todo:
    - Lars to check if we can `BackendInformation` make it a [protocol based class](https://docs.python.org/3/library/typing.html#typing.Protocol)
    - Ping Jarrod about timeline of patch release 0.25.2
    - Approve Tim's PR
    - Review Aditi's PR
  - Aditi's todo:
      - [Done] update docstrings and handle above comments in [PR#1](https://github.com/betatim/scikit-image/pull/1)
      - [Done] reach out to cuCIM (issue or PR)
      - [Doing] look into [skimage2](https://github.com/scikit-image/scikit-image/wiki/API-changes-for-skimage2)


## Topics left from previous meeting:

- using env. variable or something else, to set backend priority?
        - Tim: in what situations does a user have multiple backends and needs to override the automatic ordering?
            - understanding concrete use-cases will help with coming up with the answer
        - Tim: why not use a context manager?
    - any requirements for `cuCIM` backend?
    - ...

- revisiting roadmap
    - documentation and testing approaches ([Issue#7550](https://github.com/scikit-image/scikit-image/issues/7550))
        - Documenting backend implementation(s):
            - Add it in the algorithms’ `__doc__`. any disadvantages to this?
            - `I am a little hesitant about doing this because it feels like you have to reach a little too deep into the Python box of tricks. Meaning there will be some weird side effects of doing this.` (from https://github.com/scikit-image/scikit-image/issues/7550)
        - will providing automated testing be useful, since `cuCIM` have their own tests?
            - S: (partial?) list of previous discussions: https://discuss.scientific-python.org/t/api-dispatching-in-scikit-image-summary-and-future-enhancements/1497
            - S: [principles discussion](https://github.com/scientific-python/spatch/issues/1)
            - S: Discuss how to allow backends to hook into the test suite
            - S: We don't know under which circumstances a backend will accept a function + args for dispatching
            - S: Therefore, we'd have to rely on the backend to decide which parts of the test suite it wants to run; or, at minimum, which functions it wants to run during testing
            - S: Does it make sense, even, to try and provide dispatch libraries with our test suite? They may support different accuracies, not care about warnings, type checks, etc. etc.
    - This can also be a backend? - https://github.com/dask/dask-image
    - 




# 2025-01-29

Poll - https://crab.fit/scikitimage-weekly-dispatching-meetings-382531

Wednesday : 08:00 AM to 09:00 AM UTC

Meeting link - https://meet.google.com/rbd-tuqd-tbh

**Attending**: Tim Head, Aditi Juneja, Lars Grüter, Sebastian Berg


## Topics

- A quick summary of the current state of dispatching in scikit-image (by Aditi) to update everyone.
    - summary diagrams: https://drive.google.com/file/d/1xHLs6rK1P1XGt83ueL-DUbPO-dF0ZKFQ/view?usp=drive_link
        - https://github.com/scikit-image/scikit-image/pull/7520#issuecomment-2620880273
    - Should we make `BackendInformation` a interface?
        - https://realpython.com/python-interface/
        - allows type checkers to check that an object implements it
        - backends can still inherit from
    - what other info should go in `BackendInformation`?
        - compatible versions of scikit-image?
            - or should this be handled by `pip install ...`? As in, it should not be possible to install an incompatible version of a backend
        - 
- Gather feedback on design choices made in [PR#7520](https://github.com/scikit-image/scikit-image/pull/7520) and [PR#1](https://github.com/betatim/scikit-image/pull/1)
    - combining `can_has` in `get_implementation`? (ref. [comment](https://github.com/scikit-image/scikit-image/pull/7520#discussion_r1921030374))
        - Stefan (from [scikit-image community meeting notes](https://hackmd.io/-HCxhoU4RSiC-RzVMyoweg)): `can_has` was a joky name during the sprint; thought it would be replaced by something more meaningful
        - S: Need to document, for backends, that the `can_has` part needs to be very fast, since we need to cycle through various backends; maybe place some restrictions there on, e.g., whether imports are allowed during that process etc.
            - T: how about moving the test/dummy backend from https://github.com/betatim/scikit-image-backend-phony to the scikit-image org and using it as part of the documentation?
            - T: currently the docs say that `can_has` needs to fail fast, I don't think it needs to be fast if it succeeds (it is useful if it is fast, but in the end )
        - S: Think merging is OK, if it's simply "return quickly if you don't have it, otherwise do the work to return the function to be called"
        - merging `can_has` with `BackendInformation`
            - here `can_has` does not need to import the backend package
            - assumption/expected(by Tim) : `can_has` should not import backend implementation
                - should we make `get_implementation` a namespace to make it very obvious?
    - using env. variable or something else, to set backend priority?
        - Tim: in what situations does a user have multiple backends and needs to override the automatic ordering?
            - understanding concrete use-cases will help with coming up with the answer
        - Tim: why not use a context manager?
    - any requirements for `cuCIM` backend?
    - ...

- revisiting roadmap
    - documentation and testing approaches ([Issue#7550](https://github.com/scikit-image/scikit-image/issues/7550))
        - Documenting backend implementation(s):
            - Add it in the algorithms’ `__doc__`. any disadvantages to this?
            - `I am a little hesitant about doing this because it feels like you have to reach a little too deep into the Python box of tricks. Meaning there will be some weird side effects of doing this.` (from https://github.com/scikit-image/scikit-image/issues/7550)
        - will providing automated testing be useful, since `cuCIM` have their own tests?
            - S: (partial?) list of previous discussions: https://discuss.scientific-python.org/t/api-dispatching-in-scikit-image-summary-and-future-enhancements/1497
            - S: [principles discussion](https://github.com/scientific-python/spatch/issues/1)
            - S: Discuss how to allow backends to hook into the test suite
            - S: We don't know under which circumstances a backend will accept a function + args for dispatching
            - S: Therefore, we'd have to rely on the backend to decide which parts of the test suite it wants to run; or, at minimum, which functions it wants to run during testing
            - S: Does it make sense, even, to try and provide dispatch libraries with our test suite? They may support different accuracies, not care about warnings, type checks, etc. etc.
    - This can also be a backend? - https://github.com/dask/dask-image
    - 


Can/has get implementation (notes Sebastian): In theory, there are three points:
1. We cannot run because the types don't match (no import)
2. We only implement e.g. one method, and it might be nice to not import.
3. Sometimes the actual logic may be complicated for when we can't do it.  And returning a `defer` singleton is nice.

`3.` seems a bit easier.  Splitting `1` out is important enough, I think.  (Sebastian: I don't thinkt he choice for `2+3` matters too much right now.)

## Work plan

- PR https://github.com/scikit-image/scikit-image/pull/7520 gets reviewed and merged
- Then creating PR https://github.com/betatim/scikit-image/pull/1 to the main branch of scikit-image for more reviews
- carrying out the work more independently and in parallel
- creating a google calendar invite link for dispatch meetings

# 2024-10-21

Notes for the meeting.

DateTime:  18:00h Paris, 16:00h UTC, 10am Denver, 9am Los Angeles on 21st October 2024
Video link: https://meet.google.com/pei-ynej-qrt

Attending: Tim (@betatim), Sebastian (@seberg), Erik Welch, Vyas, Stefan, Aditi

Aditi's notes hackmd.io/@Schefflera-Arboricola/BkHgBzxeye/edit


## Topics

* [name=Lars] Which PR (this one #7520) or "Adding dispatching to scikit-image" #7513 should we focus our attention on? I feel like this one might be the furthest along. Would you agree?
  - [name=Lars] suggest's to continue with 7520
  - Later consolidate with networkx's approach in dedicated `spatch` package


### Roadmap

* [name=Lars] Discuss a roadmap. I'm less interested in the "when" but more in the milestones and work items themselves.
    * [name=Tim] how many backend implementations needed to get a good feeling for how well things work?
    * what needs completing before first release with backend system?
    * meta issue collecting some of the open issues https://github.com/scikit-image/scikit-image/issues/7550

- Pros and cons of developing jointly with nx, vs skimage separate PR
  - Good long term goal to have joint functionality in spatch
  - But may be easiest for now to experiment with different designs in PR
  - Tim and Eric have been talking about design choices / how to implement features, so there are quite a few similarities
  - Tim: May be good for spatch to be a collection of the various components that you may want to combine to build a generic dispatching solution?
    - Erik: largely agrees, that a fully configurable, generic solution may be complex; but should probably ship a small workable solution in spatch
  - Lars: [... capturing user-facing API ...]
  - Sebastian: +1 to writing down user facing API/experience as part of spatch to help getting a uniform experience across libraries

- Nov 11, we might get feedback for Aditi's grant
  - Will be plenty of work remaining to do on aggregating components into spatch

**Actual roadmap items**
- Get prototype merged in scikit-image
  - Just a minimal working prototype, with narrative documentation
- Experimental backend from nvidia library, maybe cucim
    - maybe openCV based backend to avoid GPU requirement?
    - Possible backend-behavior: same output type as input type
- Consolidation of skimage's and networkx's approach in dedicated `spatch` package
- Documentation for backend developers
  - Must include guidance, because results might change (see note about backend differences).
- Figure out how to document the dispatching experience on the front-end side
- Blog post
- ...


### Detailed discussions

- *Backend differences* in increasing order of "breakingness" (we have to allow 1, 2, probably not 3, documentation is important):
    1. Different type return
    2. Slightly different floating point numbers (numerical error)
    3. Different algorithm (implements same idea, but may yield different results)
  - Threshold could be defined as "whether passes test suite"
    - Either way, library should probably provide guidance / rule
    - Backends could advertise how closely they adhere to library (as long as users have the option to explicitly enable backends)
      - May eventually provide an API to enable all "reasonably safe" APIs installed

* [name=Stéfan] Big picture: spatch vs nx implementation
  - (Needed) differences
  - Re-use of package in both libraries
* [name=Tim] Displaying potential backends in the user facing documentation
    * proposal from Lars(?) is to have a system where the docs fetch up to date information when the docs page is visited.
        * avoid having to rebuild the scikit-image docs
        * no need to install backends during the docs build
        * backends can add/remove independent of scikit-image releases (the point in time when the docs page is built)
    * implement by having a small bit of JS to fetch a JSON document from each backend
    * link to each backend's documentation for details
    * needs a sphinx extension
* [name=Tim] Return type matches input type
    * what should the return type of a function that was dispatched be?
        * simple rules
            * "return type matches input type"
                * numpy in, numpy out
                * cupy in, cupy out
            * "return type is the backend's preferred type"
                * a backend implemented with CUDA will always return a CuPy array
                * [name=seberg] I think this needs to be very explicit.  And because of that, I think it is a second step.
        * something else?
    * Any given backend probably only implements a subset of scikit-image, don't want to require users to modify their code half way to handle conversion -> "return type matches input type"?
