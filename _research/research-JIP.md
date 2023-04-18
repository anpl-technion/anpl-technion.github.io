---
title: Incremental Belief Space Planning
research_code: ABC125
layout: research
image: /img/research/JIP/Ex_Layout.png
hero_height: is-medium
hero_image: /img/ANPL_quantum_field.jpg 
price: 7 # for sorting 

---

Decision-making is a fundamental problem in robotics and Artificial Intelligence. Under belief space planning (BSP), in a partially observable setting, it involves calculating the expected cumulative belief-dependent re- ward (cost) concerning all future measurements. Since solving this general problem quickly becomes intractable, state-of-the-art approaches turn to approximations while still calculating planning sessions from scratch. 

In this research, we investigate a shift from the theoretical formulation, incremental eXpectation BSP (iX-BSP), based on our key insight that calculations across planning sessions are similar and thus can be appropriately re-used. We demonstrate how iX-BSP could benefit existing approximations of the general problem. Introducing iX-BSP and iML-BSP, which re-use calculations across planning sessions for an open-loop sampling-based BSP estimator and the common Maximum-Likelihood assumption respectively. 


# Related Publications: 
{% bibliography --file research-projects-bib/pubs-JIP --order descending %}

