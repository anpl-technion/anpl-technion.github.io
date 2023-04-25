---
title: Localization in a 3D Aerial Model
layout: student_project
image: /img/student_project/Project-LocalizationIn3DAerialModel1.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 4 # for sorting 
descriptio: 
---

Each one of us needs to solve a localization problem many times each day: whether if it about
getting to our office, to a shop, or even to our room at home, the first step is to know where we
are. Usually, we localize ourselves using our memory of the same place from a previous time we
visited there, but we can use also use other sources of information such as maps.
In this project we will develop a computer vision algorithm to solve the localization problem
using a 3D aerial model. The goal is to estimate, given a sequence of ground images, where the
cameras have been located. We split the principal problem to several steps, beginning with an
easier case when good pose priors exist, and gradually decrease the quality of this prior. We
will also use the movement of the camera in order to better understand the scene that we see.

The main challenge is the fact that the model was reconstructed from aerial images, while we
live on the ground. Therefore, when rendered to a ground level viewpoint, the model is
severely distorted and the images look different, although representing the same viewpoint
and the same scene. An example is given below. This is the main difference between this
project and previous work in the subject of visual localization.

![drawing](/img/student_project/Project-LocalizationIn3DAerialModel2.png) 

### Prerequisites:
- Strong programming skills (preferably Python or C++). Background in (deep) reinforcement learning, computer vision, robotics is an advantage.

### Project expected outcome: 
- Working algorithmic prototype and publication in a leading robotics or computer vision conference/journal

### Academic supervisor:
- Prof. Vadim Indelman [mail](mailto:vadim.indelman@technion.ac.il)

Duration: 1 or 2 semesters
