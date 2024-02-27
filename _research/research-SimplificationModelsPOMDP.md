---
title: Simplifying Complex Observation Models in Continuous POMDPs
research_code: ABC125
layout: research
image: /img/research/SimplifyingObservations/LevYehudi24aaai-concept.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 1 # for sorting 

descriptio: "Solving partially observable Markov decision processes (POMDPs) with high dimensional and continuous observations, such as camera images, is required for many real life robotics and planning problems. Recent researches suggested machine learned probabilistic models as observation models, but their use is currently too computationally expensive for online deployment. We deal with the question of what would be the implication of using simplified observation models for planning, while retaining formal guarantees on the quality of the solution. Our main contribution is a novel probabilistic bound based on a statistical total variation distance of the simplified model. We show that it bounds the theoretical POMDP value w.r.t. original model, from the empirical planned value with the simplified model, by generalizing recent results of particle-belief MDP concentration bounds. Our calculations can be separated into offline and online parts, and we arrive at formal guarantees without having to access the costly model at all during planning, which is also a novel result. Finally, we demonstrate in simulation how to integrate the bound into the routine of an existing continuous online POMDP solver.
"
---



<!-- add  youtube and bibliography Here-->

<!-- ![inplace_simp](/img/research/SimplificationPOMDP/inplace_simp.png) 
![Concept_PAC_version2](/img/research/SimplificationPOMDP/Concept_PAC_version2.png)  -->


# Related Publications: 
{% bibliography --file research-projects-bib/pubs-SimplifiedModelsPOMDP --order descending %}

