- GitHub: https://github.com/Schefflera-Arboricola
- LinkedIn: linkedin.com/in/aditi-juneja-940838204 
- Open source blogs/work: https://github.com/Schefflera-Arboricola/blogs
- Blog website: schefflera-arboricola.github.io/Schefflera-Arboricola/ 

## Cover Letter : Open-source Internship at Quansight Labs

I’m writing to express my interest in Quansight Lab’s open-source internship. Over the
past two years, I’ve contributed across the Scientific Python ecosystem, and now I
would like to dive further into the PyData ecosystem. As a Quansight intern, I’d love to
tackle fresh projects in NumPy, SciPy, conda-forge, Polars, Narwhals, data-apis.org, or
stdlib.js under the guidance of your team.

The thing that I love most about open source is that no one is judged based on who
they are or how they look.. but based on the contents of their PRs, their work, the value
that they add to a project. And the final product is savoured by everyone– across
borders. It’s both surreal and inspiring to me, and Quansight’s diverse team embodies
this idea. And I think this internship would let me learn from experienced mentors who
could help me grow into a stronger long-term contributor, while also working on
something technically challenging and impactful.

I believe my previous open-source experiences as a user, contributor, maintainer and
mentor would be of great use during this internship. In my previous roles, I worked on
accelerating NetworkX and contributed extensively to the project and its nx-parallel
backend. I also led the development of the dispatching mechanism in the scikit-image
project. These collaborative roles helped me enhance my software engineering and
programming skills through in-depth discussions on design decisions and guidance from
experienced maintainers and mentors, while also delivering real and impactful projects.
I believe that these skills that I have acquired would be highly valuable for contributing
to Quansight’s high-impact ecosystem work.

Beyond technical skills, I enjoy volunteering in communities and conferences--
highlights include serving as a Proceedings paper reviewer for SciPy 2025 (where I
reviewed a paper on ML inference techniques in High Energy Physics, I enjoyed
learning something new and interacting with the author), and participating in the DISC
(Diversity and Inclusion in Scientific Computing) 2025 Unconference, which was an
incredibly inclusive and productive experience, and lastly working to restart the SciPy
India community.

I’m excited about the opportunity to bring my skills and passion to Quansight Lab and
I’m eager to work on something impactful and meaningful over these three months– and
beyond. Thank you for considering my application.


---

## Tell us about one project you’re proud of. Include: what you built, what your role was, and what you learned. (200–300 words) *

One of the most impactful and technically challenging projects I've worked on so far is nx-parallel (https://github.com/networkx/nx-parallel), a parallel backend for the graph analysis library NetworkX. The goal was to make NetworkX interoperable with the various parallel libraries in the ecosystem, while also maintaining a simple and intuitive user API. This allowed algorithms in NetworkX to scale across multiple cores or distributed systems(through libraries like Dask or Ray) without requiring users to rewrite their code. nx-parallel was built on top of Joblib, which provides a flexible abstraction layer for a diverse set of parallel backends.

The three main challenges: First was to setup and ensure that the NetworkX’s dispatch and configuration system worked seamlessly with Joblib’s configuration system and user API; second was implementing over 20 parallel graph algorithms and making them as efficient as possible (for which I introduced the get_chunks functionality); and lastly developing benchmarking pipeline to evaluate performance of different algorithms across hardwares and environments. At the end we were able to obtain speed-ups upto 8.8x on an 8 core CPU machine, while also maintaining a simple user-API and writing a comprehensive testing suite and documentation.

I began as a user of the NetworkX library. Then I started contributing with bug fixes and improvements, later I joined the project as an intern, that's when I carried out most of the work on the nx-parallel backend with guidance from my mentors and the NetworkX community. Later, I also had the privilege of being a maintainer.

While working on nx-parallel, the initial research piqued my interest in parallelism- the different approaches such as map-reduce. I developed a strong interest in interoperability within the PyData ecosystem, learning how array API standards and dispatch mechanisms in various other projects work. Lastly, I gained first-hand experience of how open-source collaborations work.

---

## Have you contributed to an OSS project before? Please describe.*


My open source journey began through a competition where college students hosted their open-source projects for contributions and mentored first-time contributors. With their guidance, I started exploring larger open-source projects and eventually began contributing to NetworkX.

I stared exploring my favourite, Traveling Salesman Problem, portion of the codebase and opened two documentation PRs. While exploring the codebase further, I noticed several #TODO comments related to parallelizing parts of algorithms. This led me to playing around with the nx-parallel backend, where I made my first contribution by fixing a bug in its benchmarking script. This was followed by me setting up a benchmarking infrastructure using Airspeed Velocity (ASV) to observe the performance improvements.

Alongside, I was also getting familiar with the dispatching mechanism within NetworkX. At the time, this mechanism was not documented, so I worked on documenting a user guide and a developer guide, and also made some improvements to parts of the dispatch-related codebase, making it easier for future contributors to understand and navigate.

I was later selected as a Google Summer of Code intern, where I worked extensively on developing the nx-parallel backend. During this period I also performed a significant amount of maintenance work in both networkx and nx-parallel projects(read more in final report and blogs in CV), and presented talks, posters and conducted sprints. I also added nx-parallel on conda-forge, which got me interested in how packaging and distribution works and the internals of the conda package manager.

I've also made some contributions to these libraries that I like and regularly use in my work - SciPy, NumPy, scikit-hep/vector, skore, Scikit-image, HIPS/autograd, napari, manim



---

## Why are you interested in this internship, and how does it align with your career goals?*


I am interested in this internship because open source has been central to how I learn, build, and collaborate. As a user, open-source software has been invaluable-- many of the tools I rely on for coursework, scientific computing projects, and data analysis are open-sourced. As a contributor, I find it especially meaningful to help improve these tools and give back to the communities that build and maintain them.

I enjoy the technical problem-solving involved in building and designing open-source software, fixing bugs, reviewing pull requests, and working with maintainers to steadily improve a project over time. Quansight’s focus on strengthening the PyData ecosystem--including projects such as NumPy, SciPy, conda-forge, Polars, Narwhals, data-apis.org, and Jupyter-- aligns closely with my interests. These projects have played an important role in the tools and skills I have today, and the opportunity to contribute to them is particularly exciting.

In the long term, I want to continue working in open-source scientific computing and contribute as a maintainer or long-term open-source sustainer. This internship would allow me to deepen my experience contributing to widely used projects while learning under the guidance of the experienced mentors and collaborating with others who care about building and sustaining reliable open-source infrastructures.



---

## What do you hope to learn this summer?*

I hope to deepen both my technical skills and my understanding of how large open-source projects in the PyData ecosystem are developed and sustained. I would like to get more involved in the PyData ecosystem and support and contribute to the open-source projects that I've been using for a long time.

During the internship, I hope to gain more hands-on experience building impactful features for open-source projects alongside experienced maintainers. I hope to work on something challenging that would also make me a better contributor and a software engineer. Working closely with mentors, would also help me better understand how maintainers approach challenges of interoperability, benchmarking, and performance when designing libraries used by a broad community. I am particularly interested in learning how maintainers design APIs, manage backward compatibility, and ensure interoperability between libraries in the PyData ecosystem--especially for mature projects that have evolved over decades and must balance innovation with stability. I would also be open to contribute to projects that are new to me and expand my understanding of the ecosystem.
