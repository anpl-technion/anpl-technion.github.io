---
title: Hybrid Belief POMDP Planning
subtitle: Data Association Aware Belief Space Planning
research_code: ABC125
layout: research
image: /img/research/RAP/belief_tree_inference_path_screenshot.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 3 # for sorting 

---

 Real-world problems often require reasoning about hybrid beliefs, over both discrete and continuous random variables. As an example, one might consider matching images from two different but similar in appearance places (possibly observed by different robots), or attempting to recognize an object that is similar in appearance, from the current viewpoint, to another object. Both cases are examples of ambiguous situations, where naive and straightforward approaches are likely to yield incorrect results, i.e. mistakenly considering the two places to be the same place, and incorrectly associating the observed object. These and numerous other applications necessitate reasoning about hybird beliefs, where the discrete variables correspond to hypotheses (e.g. data association and/or classification hypotheses).

 Yet, such a setting has hardly been investigated in the context of planning. Moreover, existing online Partially Observable Markov Decision Processes (POMDPs) solvers do not support hybrid beliefs directly. In particular, these solvers do not address the added computational burden due to an increasing number of hypotheses with the planning horizon, which can grow exponentially. In this research project we develop online hybrid belief POMDP planning approaches that address these challenges.


# Related Publications: 
{% bibliography --file research-projects-bib/pubs-RAP --order descending %}

