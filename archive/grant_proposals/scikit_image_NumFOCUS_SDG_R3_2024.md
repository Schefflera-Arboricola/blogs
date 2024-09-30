---
title: scikit_image_NumFOCUS_SDG_R3_2024
status: submitted
author: Aditi Juneja
reviewers: Tim Head, Stéfan Van Der Walt, Erik Welch, Sanket Verma, Sebastian Berg, Gregory Lee
---

Grant website : https://numfocus.org/programs/small-development-grants

Grant submission form : https://numfocus.typeform.com/to/mbtH7w?typeform-source=numfocus.org

---

### Name of Submitter: 

Aditi Juneja

### Your Email:

aditijuneja7@gmail.com

### Is your project Sponsored or Affiliated?

Sponsored

### Select Your Project:

scikit-image

### Proposal Title:

Incorporating a Dispatching Mechanism into scikit-image 

### Two Sentence Summary of Proposal:

This project introduces a plugin mechanism for scikit-image, allowing users to seamlessly dispatch function calls to a more optimized backend implementations (like NVIDIA's GPU-accelerated `cuCIM`), either based on array type (e.g., `CuPy` array) or a specific keyword argument. The project also includes comprehensive testing and documentation of the new mechanism.

> [name=Tim] Need to make this shorter so it is two (short) sentences. I'd do that by removing specific things about how the work
> will be done. For example "This project will add a plugin mechanism to scikit-image so that users can take advantage of
> hardware accelerators like GPUs. We will lead the implementation in scikit-image and work with projects that can provide
> the plugins". I think at the high level the details of how it will be done are not as important as what and why it
> will be done (as well as being short :)

> [name=Aditi] Thank you :) I have updated the summary. LMK if this LGTY :)

> [name=Stéfan] Hope it's OK, but I'm making some light edits as I'm reading. I believe hackmd has a history, in case you want to revert any of my changes.

> [name=Aditi] No worries! Thank you :)

---

### Description of Proposal:
<i>No more than 750 words (4,500 characters max)</i>

> [name=Tim] I'd start with answering "why is this project important/worth doing?" - but maybe this is a personal bias,
> I think the most interesting question is "why?". "what?" and "how?" are somehow less interesting and if I was the person
> making the funding decision I'd want the proposal to convince me about why this needs funding, without that it doesn't
> matter what/how the work will be done.

> [name=Tim] I'd not "lock in" details like specific techniques or implementations by mentioning entry paths, how many of
> them there will be, keyword arguments, etc. I think most readers will have no idea of Python and plugin mechanisms,
> so it will all be jargon to them. Or you get a reader who is an experienced Python-ista, for whom it is obvious that
> a plugin mechanism will be based on entry points. It also constrains the project to this particular approach, which
> I think isn't great given that you want to have the freedom to explore options in order to arrive at the best solution
> for scikit-image. Why is this an important thing to work on? Why is it hard to do (aka why do you need $10,000?)?
> Why can't the solution be copy&pasted from somewhere else?
> It looks like the next section of the form goes more in this direction. The "deliverables and timeline" section seems
> like the place to talk about what and how and when. But then I am confused about what should
> go in this section. Given it is the first one that people will see I'd still focus on the "why?", maybe including
> some "setting the scene"?

> [name=Stéfan] I agree with Tim that it helps to put the motivation upfront. There are many ways to frame it, here's one rough outline: "Scikit-image is popular for its Pythonic, well documented API. However, it does not currently compete with optimized implementations, such as OpenCV. To accelerate the code sufficiently to compete with such libraries would introduce much additional complexity, and increase maintenance burden. An alternative approach, the one proposed here, is to instead provide a dispatching mechanism, so that external implementers can provide accelerated algorithms, while scikit-image remains focused on designing and testing the best version of its API."

> [name=Aditi] Thank you for the nice feedback :) I've updated and added the starting, motivation paragraph that you suggested above. Thanks! LMKWYT :)

Scikit-image is popular for its intuitive and well-documented Pythonic API. However, compared to more optimized image processing libraries like OpenCV, it faces performance challenges. To address these limitations without adding unnecessary complexity to the core library or increasing maintenance overhead, this project proposes to enhance scikit-image’s flexibility and performance through an `entry_points`-based dispatching mechanism. This approach will allow scikit-image to offload computationally intensive tasks to external libraries (like `cuCIM`) that provide optimized implementations, while still maintaining its focus on API design and user experience. This allow users to leverage hardware accelerations, such as GPUs, while requiring little to no code change, thereby preserving scikit-image's ease of use.

This effort is valuable, not only because it expands scikit-image’s usability for high-performance workflows, but because it lets us to think more deeply about the implementation details of dispatching mechanisms in general. This, in turn, promotes cross-project collaboration and discussions, allowing us to engage the broader scientific Python community. The new backends for scikit-image would connect more image processing projects, adding more value to our users and to the scientific Python ecosystem as well.

Build on work done in NetworkX, the dispatching system will address challenges unique to scikit-image, like scikit-image’s reliance on NumPy arrays for image data, complexities in handling each backend's metadata, building an efficient testing framework for dispatching, output compatibility, and other things yet to be discovered. All of this would require deeper investigation and collaboration with senior developers across related projects.

This grant will support Aditi Juneja to lead the design, implementation, testing and documentation of this dispatching mechanism in scikit-image. A key part of the effort involves gathering feedback from developers and users of potential backends, integrating their insights to ensure the dispatch system aligns with real-world needs and is flexible enough to evolve with future use cases.

This project will include the following key components:

1. Ways of dispatching a function call: We would explore various ways to we would want to offer a scikit-image user to dispatch a function call to the appropriate backend. Like, type-based dispatching (like `skimg_func(cupy_arr)`), this will allow scikit-image functions to detect array types (e.g., NumPy, CuPy arrays) and dispatch the function call to the appropriate backend. Also, the `backend=` keyword will give users explicit control over which backend to use, but it also diverge from the "zero code change" principle because it would require the user to input extra argument in their function calls, like `skimg_func(numpy_arr, backend="cucim")`. We may also experiment with other ways of dispatching a function call like, `skimg_func.invoke(...)` or `skimg_func.get_backend_function(...)`, etc., and then arrive at a set of ways that we would like to offer to an user in scikit-image, based on the discussions with scikit-image's developers and backends' (like, cuCIM's) developers.

> [name=Erik] What do you mean by "but it will also prohibit them from practicing a "zero code change" principle"? Using `backend=` is explicit, but does having this option available actually prohibit anything? Also, we may explore other ways to explicitly choose a backend that doesn't modify the signature, such as `myfunc.invoke(...)` or `myfunc.get_backend_function(...)` or whatever.

> [name=Aditi] Thank you for the review Erik :) I've updated this point. LMKWYT :)
   
2. Implementation and testing: The core of this project involves implementing this dispatching mechanism in a way that integrates smoothly with scikit-image's architecture. This would include investigating into what could be the best ways of testing an `entry-point`-based dispatch mechanism.

3. Backend metadata integration: We also plan on communicating the scikit-image users about which backends are available and what types of optimizations they offer. We are still exploring better approaches for achieving this (see https://github.com/scikit-image/scikit-image/issues/7550).

> [name=Tim] I'd not lock in this implementation detail. Lars proposed a nice solution that is different from this
> for the documentation. Which one of the two, or a third it'll be in the end is I think an open question.

> [name=Aditi] Thank you :) I've updated this point. LMK if this LGTY.

4. Community engagement and documentation: The project will also produce comprehensive documentation to guide backend developers and end users of dispatching. The development work will also be documented in regular blogs and a final report for future reference. Also wrapping the work by creating issues for all the future work that can be done and all the related project ideas that Aditi would have to offer.

If time permits, Aditi would also work on automating testing for backend packages, so that they can be tested using scikit-image's existing test suite and some other utilities as well like `can_run`, `should_run`, etc. 

---

### Please explain the benefit of this proposal including:

-Impact to the project
-Impact to the scientific ecosystem
-Impact to the community

<i>No more than 400 words (2,500 characters max)</i>


The proposed dispatching mechanism will significantly enhance scikit-image by enabling more efficient execution of image processing algorithms across multiple backends, such as cuCIM (GPU-accelerated), while preserving scikit-image’s familiar user API. This functionality not only benefits scikit-image directly by boosting performance but also encourages developers across the scientific Python ecosystem to create new backend packages for more efficient image analysis. Beyond high-performance backends, this mechanism could be extended to support other applications as well. For example, a researcher could implement a single algorithm, that they have optimised using CNNs, as a scikit-image backend, omitting the need to learn a new API for the people who want to test out the researcher's work. And the alternate implementation in the backend might not just be a more optimized implementation but it can also be something entirely different, like having an image database backend. So, including dispatching in various projects I think will surprise us with the different creative ways developers/researchers would use this.

NetworkX has already implemented an `entry_point`-based dispatching mechanism, and as more projects adopt this approach, the collective understanding of dispatching architectures in general will expand. This will further contribute to formalizing the Scientific Python Ecosystem Coordination(SPEC) recommendations and improving the spatch: https://github.com/scientific-python/spatch as a resource for future projects looking to implement similar mechanisms. Our contributor has previously worked on the [draft of SPEC 2](https://scientific-python.org/specs/spec-0002/) for API dispatching and, through this project, will be well-positioned to advance it from draft form to a set of concrete recommendations for widespread use across the scientific Python ecosystem. Following the scikit-image implementation, they are planning to extend dispatching into scikit-learn as well, which is a more complex task.

In addition to the technical advancements, this project will bring a unique perspective to the scikit-image community through Aditi's involvement. Her proven dedication to long-term engagement in past projects and her focus on ensuring the work is accessible to future developers demonstrate that she will bring the same level of commitment and professionalism to scikit-image, contributing to its ongoing success and to the broader scientific Python ecosystem.

---

### Amount Requested:

10000 USD

> [name=Sanket]: Do you know whether NumFOCUS adjusts grant proposals' budgets based on various regions across the globe? This is related to PPP (Purchase Power Parity - https://en.wikipedia.org/wiki/Purchasing_power_parity). For e.g. GSOC pays different stipends based on the developer's location.
AFAIK, NumFOCUS doesn't consider PPP but feel free to check with them.

---

### Brief Budget Justification: (Please include hours and/or pay rates)
<i>How will the money be spent?</i>

The requested funds will be used to compensate Aditi Juneja as an independent contractor for carrying out the proposed work. The compensation will cover 400 hours at a rate of 25 USD per hour. 

> [name=Aditi] open for discussion; not carved in stone

> [name=Sanket]: I think your hourly rates are low. Maybe you can adjust the hourly rate and total hours given that the overall work and efforts remains same.

> [name=Aditi] I changed hours from 500 to 400 hours and hourly rate from 20 to 25 USD/hr. LMK if that LGTY. Thank you :)

---

### Timeline of Deliverables:
<i>Please include specific timelines showing when you will achieve the proposed work.</i>

The project will span four months, starting in December (or the earliest available date).

- Month 1: Aditi will engage with senior developers of scikit-image project and the developers of the potential scikit-image backends either through weekly meetings or on GitHub, based on the developer's time availability, and also refer previous works(https://github.com/scikit-image/scikit-image/pull/7520 , https://github.com/scikit-image/scikit-image/issues/7550 , `spatch` discussions, etc.) to better understand the specific requirements for implementing the dispatching mechanism and the needs of backend developers and also the scikit-image maintainers. While learning all this she also plan on simultaneously reiterate on her implementation of a type-based and `backend` kwarg based dispatching mechanism.

- Month 2: Running through multiple feedback loops and enhancing and improving the basic dispatching implementation added during the learning phase, while also ensuring compatibility with scikit-image’s architecture.

> [name=Tim] Maybe include "connecting with potential backend implementors" here? Maybe it is obvious but I tihnk
> getting the people who will write the backends involved early will be important both to get their feedback on
> the mechanism, but also to get them excited (so that they will eventually write a backend).

> [name=Aditi] Thank you :) I have updated it. LMK if this LGTY :)

- Month 3: Finalizing the implementation, add initiate adding tests, and documentation for both backend developers and users. Concurrently, Aditi will familiarize herself with scikit-image’s testing and documentation practices to ensure seamless integration of the dispatching mechanism.

- Month 4: Wrapping up with comprehensive tests and well-written documentation and a detailed final report summarising the work done (This would also be submitted to the NumFOCUS's SDG team via the form provided on the website). And adding any final touch-ups. And creating issues for future developments.

> [name=Sanket]: I think splitting last two months individually and assigning specific tasks for each month would enhance readability and improves confidence.
Also, if you want you can work on a final report for the community and some sort of feedback mechanism for yourself. (if that's fine with Stéfan and others)

> [name=Aditi] For feedback mechanism, I think blogs(twice a month), and monthly invoices that we have to submit as an independent contractor and updates in the scikit-image meetings and dispatching meetings(based on other people's time availability), and a final report sould be enough. Any other ideas on this are very much welcomed :)
> Also thank you very much for the feedback on spliting the months :) I've updated it. LMK if that LGTY.


Throughout this period, Aditi will provide regular updates to the community through blog posts, highlighting key milestones and any challenges encountered. Also providing updates and getting feedback in the weekly meetings. Some amount of testing and documentation would probably be done in sync with the implementation but these would get significant attention in the last 2 months. 

Finally, thank you very much to Tim Head, Stéfan Van Der Walt, Erik Welch, Sanket Verma, Sebastian Berg and Gregory Lee for reviewing and improving this proposal :)

Proposal hackmd for reference : https://hackmd.io/JKNyCOqsTYOteJfFIUFS3g

---

### Has someone been identified to carry out the work in the proposal?

YES

### If YES: Please list the name(s) of the person(s) who will be carrying out the work and a short statement (approximately 1 sentence) of why they are qualified.

Aditi Juneja (GitHub: https://github.com/Schefflera-Arboricola ; email: aditijuneja7@gmail.com) will be carrying out this project work. She has extensive experience working on dispatching mechanisms, having contributed to SPEC 2(API Dispatching) document, heavily contributed to documenting NetworkX’s dispatching code and building the nx-parallel backend. She has also drafted a PR (https://github.com/scikit-image/scikit-image/pull/7513) implementing a skeleton dispatching mechanism in scikit-image, during EuroSciPy 2024 sprints. Additionally, she is very involved in the NetworkX community as a core developer.

> [name=Erik] I think we should include names of mentors as well. Sebastian Berg and I are happy to volunteer to be mentors, and it may be helpful to include somebody from skimage or cucim as well.

> [name=Aditi] Thank you so much for mentoring me :) I think you can also add your name and email in the last question as well :)

Erik Welch (GitHub: https://github.com/eriknw ; email: erik.n.welch@gmail.com) will be an unpaid mentor. He is a senior developer with deep OSS experience (a core developer of NetworkX, python-graphblas, and toolz), and in the last 10+ years has been involved in many projects that use dispatching and backends including NetworkX, [metagraph](https://github.com/metagraph-dev/metagraph/), Dask, Blaze, and closed source systems.

Sebastian Berg (GitHub: https://github.com/seberg ; email sebastian@sipsolutions.net) a NumPy maintainer who has been involved in discussions and implementations of the NumPy dispatching protocols will also serve as an unpaid mentor and help push forward the proposal.

Stéfan van der Walt (GitHub: https://github.com/stefan; email: stefanv@berkeley.edu) is a core scikit-image developer involved with the project since its inception, and who has been following the dispatching discussions. He will act as unpaid mentor and reviewer.

> [name=Sebastian] please don't hesitate to freely edit (or even remove) my note.  I honestly doubt it changes much for the proposal.

> [name=Aditi] Thank you very much :) 

--- 

### How will someone be identified to carry out the work?

Independent contractor: Aditi Juneja (aditijuneja7@gmail.com)


### Please list the name and email address of a project leader(s) who has approved this proposal.

> [name=Sebastian] I think the point of this question is just to list skimage folks who approve/endorse the grant as officially requested by the project?! (and who NumFOCUS can double check with)

> [name=Aditi] Ok, so should we move Gregory's details  above? "emeritus core developer" seems like a grey area! And I think other people who helped in reviewing and improving this proposal could be mentioned above somewhere :) 

> [name=Sebastian] Yeah, that would be my understanding.

> [name:Aditi] removing "Gregory Lee (grlee77@gmail.com) : maintainer of cuCIM, emeritus core developer for scikit-image" from here. Instead added a thank you note at the end of proposal including everyone.

Stéfan van der Walt (stefanv@berkeley.edu)
