---
title: scikit_image_NumFOCUS_SDG_R3_2024
---

This document is intended to provide you with a copy of the questions that are asked in the Small Development Grant Proposal Submission form, so that you can prepare, share, and edit your answers prior to submission.

Please note: All proposals for the SDG program must be submitted through the form to be considered for funding.

---

### Name of Submitter: 



### Your Email:



### Is your project Sponsored or Affiliated?

Sponsored

### Select Your Project:

scikit-image

### Proposal Title:

Incorporating Dispatching Mechanism in scikit-image 

### Two Sentence Summary of Proposal:

This project will introduce a plugin mechanism to scikit-image, allowing users to seamlessly dispatch functions to optimized backend implementations(like `cucim`'s GPU accelerated implementations) based on array type (like `cupy`) or specific keyword argument. The project will also include several other smaller goals, along with the comprehensive testing and documentation for this new mechanism.

> [name=Tim] Need to make this shorter so it is two (short) sentences. I'd do that by removing specific things about how the work
> will be done. For example "This project will add a plugin mechanism to scikit-image so that users can take advantage of
> hardware accelerators like GPUs. We will lead the implementation in scikit-image and work with projects that can provide
> the plugins". I think at the high level the details of how it will be done are not as important as what and why it
> will be done (as well as being short :)

> [name=Aditi] Thank you :) I have updated the summary. LMK if this LGTY :)


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

The proposed project seeks to enhance the performance and flexibility of scikit-image by introducing an `entry_points`-based dispatching mechanism. This mechanism will allow scikit-image users to select optimized backend implementations based on array types (e.g., `cupy` arrays) or explicit `backend` keyword arguments. By doing so, scikit-image users can leverage hardware accelerations such as GPUs, boosting image processing efficiency with little to no code modifications.

This effort is valuable not only because it expands scikit-image’s usability for high-performance workflows, but the grant for this project will also support us to think more deeply about the implementation details of dispatching mechanisms not just in scikit-image but in general as well. Thereby, promoting cross-project collaboration and discussions, allowing the broader scientific Python community to get more engaged. Additionally, the new backends for scikit-image, would add more projects, and hence more value, to the whole scientific Python ecosystem.

The dispatching approach is inspired by similar work in NetworkX but requires special considerations for scikit-image’s reliance on numpy arrays for image data, which presents unique challenges. There would be complexities in backend's metadata handling, building an efficient testing framework for dispatching, output compatibility, and many more things yet to be discovered; and all this would require deeper investigation and collaboration with senior developers across related projects.

This grant will fund Aditi Juneja to lead the design, implementation, testing and documentation of this dispatching mechanism in scikit-image. A key part of the effort involves gathering feedback from developers and users of potential backends, integrating their insights to ensure the dispatch system aligns with real-world needs and is flexible enough to evolve with future use cases.

This project will include the following key components:

1. Type-based and `backend` kwarg dispatching: The dispatching mechanism will allow scikit-image functions to detect array types (e.g., numpy, cupy arrays) and dispatch the function call to the appropriate backend. The `backend=` keyword will give users explicit control over which backend to use, but it will also prohibit them from practicing a "zero code change" principle.
   
2. Backend metadata integration: We also plan on communicating the scikit-image users about which backends are available and what types of optimizations they offer. We are still exploring better approaches for achieving this (Refer https://github.com/scikit-image/scikit-image/issues/7550).

> [name=Tim] I'd not lock in this implementation detail. Lars proposed a nice solution that is different from this
> for the documentation. Which one of the two, or a third it'll be in the end is I think an open question.

> [name=Aditi] Thank you :) I've updated this point. LMK if this LGTY.
 
3. Implementation and testing: The core of this project involves implementing this dispatching mechanism in a way that integrates smoothly with scikit-image's architecture. This would include investigating into what could be the best ways of testing an `entry-point`-based dispatch mechanism.

4. Community engagement and documentation: The project will also produce comprehensive documentation to guide backend developers and end users of dispatching. The development work will also be documented in regular blogs and a final report for future reference. Also wrapping the work by creating issues for all the future work that can be done and all the related project ideas that Aditi would have to offer.

If time permits, Aditi would also work on automating testing for backend packages, so that they can be tested using scikit-image's existing test suite and some other utilities as well like `can_run`, `should_run`, etc. 

---

### Please explain the benefit of this proposal including:

-Impact to the project
-Impact to the scientific ecosystem
-Impact to the community

<i>No more than 400 words (2,500 characters max)</i>


The proposed dispatching mechanism will significantly enhance scikit-image by enabling more efficient execution of image processing algorithms across multiple backends, such as cucim (GPU-accelerated), while preserving scikit-image’s familiar user API. This functionality not only benefits scikit-image directly by boosting performance but also encourages developers across the scientific Python ecosystem to create new backend packages for more efficient image analysis. Beyond high-performance backends, this mechanism could be extended to support other applications as well. For example, a researcher could implement a single algorithm, that they have improved upon, as a scikit-image backend, omitting the need to learn a new API for people who want to test out the researcher's work. So, including dispatching in various projects I think will surprise us with the different creative ways developers/researchers would use this.

NetworkX has already implemented an `entry_point`-based dispatching mechanism, and as more projects adopt this approach, the collective understanding of dispatching architectures will expand. This insight will contribute to formalizing the SPEC 2 recommendations and improving the `spatch` repository as a resource for future projects looking to implement similar mechanisms. Our contributor has previously worked on the draft of SPEC 2 for API dispatching and, through this project, will be well-positioned to advance it from draft form to a set of concrete recommendations for widespread use across the scientific Python ecosystem. Following the scikit-image implementation, they are planning to extend dispatching into scikit-learn as well, which is a more complex task.

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

- Month 1: Aditi will engage with senior developers of scikit-image project and the developers of the potential scikit-image backends either through weekly meetings or on GitHub, based on the developer's time availability, and also refer previous works(https://github.com/scikit-image/scikit-image/pull/7520 , https://github.com/scikit-image/scikit-image/issues/7550 , `spatch` discussions, etc.) to better understand the specific requirements for implementing the dispatching mechanism and the needs of backend developers and also the scikit-image maintainers. While learning all this she also plan on simultaneously reiterate on her implemention of a type-based and `backend` kwarg based dispatching mechanism.
- Month 2: Running through multiple feedback loops and enhancing and improving the basic dispatching implementation added during the learning phase, while also ensuring compatibility with scikit-image’s architecture.

> [name=Tim] Maybe include "connecting with potential backend implementors" here? Maybe it is obvious but I tihnk
> getting the people who will write the backends involved early will be important both to get their feedback on
> the mechanism, but also to get them excited (so that they will eventually write a backend).

> [name=Aditi] Thank you :) I have updated it. LMK if this LGTY :)

- Month 3: Finalizing the implementation, add initiate adding tests, and documentation for both backend developers and users. Concurrently, Aditi will familiarize herself with scikit-image’s testing and documentation practices to ensure seamless integration of the dispatching mechanism.
- Month 4: Wrapping up with comprehensive tests and well-written documentation and a final report summarising the work done. And adding any final touch-ups. And creating issues for future developments.

> [name=Sanket]: I think splitting last two months individually and assigning specific tasks for each month would enhance readability and improves confidence.
Also, if you want you can work on a final report for the community and some sort of feedback mechanism for yourself. (if that's fine with Stéfan and others)

> [name=Aditi] For feedback mechanism, I think blogs(twice a month), and monthly invoices that we have to submit as an independent contractor and updates in the scikit-image meetings and dispatching meetings(based on other people's time availability), and a final report would be enough. Any other ideas on this are very much welcomed :)
> Also thank you very much for the feedback on spliting the months :) I've updated it. LMK if that LGTY.


Throughout this period, Aditi will provide regular updates to the community through blog posts, highlighting key milestones and any challenges encountered. Also providing updates and getting feedback in the weekly meetings. Some amount of testing and documentation would probably be done in sync with the implementation but these would get significant attention in the last 2 months. 

---

### Has someone been identified to carry out the work in the proposal?

YES

### If YES: Please list the name(s) of the person(s) who will be carrying out the work and a short statement (approximately 1 sentence) of why they are qualified.

Aditi Juneja (GitHub: https://github.com/Schefflera-Arboricola ; Gmail: aditijuneja7@gmail.com) will be carrying out this project work. She has extensive experience working on dispatching mechanisms, having contributed to SPEC 2(API Dispatching) document, heavily contributed to documenting NetworkX’s dispatching code and building the nx-parallel backend. She has also drafted a PR (https://github.com/scikit-image/scikit-image/pull/7513) implementing a skeleton dispatching mechanism in scikit-image, during EuroSciPy 2024 sprints.

---

### How will someone be identified to carry out the work?

Independent contractor 

### Please list the name and email address of a project leader(s) who has approved this proposal.



