---
title: Autonomous Viewpoint-Dependent Semantic Perception
research_code: ABC125
layout: research
image: /img/research/AutonomousObjectLevelPerception/track_3d_b.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 7 # for sorting 

descriptio: "In this research project we investigate approaches for autonomous semantic perception. 

In particular, we proposed an algorithm for robust visual classification of an object of interest observed from multiple views using a black-box Bayesian classifier which provides a measure of uncertainty, in the presence of significant ambiguity and classifier noise, and of localization error. The fusion of classifier outputs takes into account viewpoint dependency and spatial correlation among observations, as well as pose uncertainty when these observations are taken and a measure of confidence provided by the classifier itself.

Furthermore, we developed a novel approach that infers a distribution over posterior class probabilities within a Bayesian framework, while accounting for model uncertainty. This distribution enables reasoning about uncertainty in the posterior classification, and thus is of prime importance for robust classification and object-level perception in uncertain and ambiguous scenarios, and for safe autonomy in general.

Additional related works are provided below."

---
<!-- add  youtube and bibliography Here-->

<div style="display: flex; justify-content: center;">
    <iframe width="40%" height="315" src="https://www.youtube.com/embed/OvIHOEl3Oy8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<p class="title is-4">Related Publications:</p>
{% bibliography --file research-projects-bib/pubs-AutonomousObjectLevelPerception --order descending %}
