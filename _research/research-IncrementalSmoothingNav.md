---
title: Factor Graph based Incremental Smoothing
research_code: ABC125
layout: research
image: /img/research/IncrementalSmoothingNav/CFS-bayes-tree.jpg
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 15 # for sorting 

---

In this DARPA-funded project, we collaborate with SRI International ltd. to develop a plug and play framework for navigation. The goal is to produce the best possible solution in real time based on different multi-rate and asynchronous sensors that may become inactive and/or resurrected at any time. A factor graph formulation is used as a representation of the joint probability function, and an efficient inference algorithm is used to calculate the MAP estimate given measurements from different sensors.

Following a recently-developed IMU pre-integration theory, an equivalent IMU factor is introduced to summarize consecutive IMU measurements into a non-linear factor, which can be re-linearized if required. This factor is then incorporated into the optimization whenever measurements from other sensors are received, while high-rate navigation solution is contentiously obtained by composing the last navigation state in the factor graph with the current summarized IMU measurements. This is in contrast to the commonly used navigation-aiding approach where IMU measurements are processed outside of the estimator, without being able to perform re-linearization of past IMU measurements. 

We also present a parallelized navigation architecture (right image above) that is capable of running in real-time and incorporating long-term loop closure constraints while producing the optimal Bayesian solution. This architecture splits the inference problem into a low-latency update that incorporates new measurements using just the most recent states (filter), and a high-latency update that is capable of closing long loops and smooths using all past states (smoother).

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-IncrementalSmoothingNav --order descending %}

