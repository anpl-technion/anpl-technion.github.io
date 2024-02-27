---
title: Belief Space Planning via Factor Graphs and Re-use of Calculation
research_code: ABC125
layout: research
image: /img/research/rAMDL/drawing_more_factors2.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 11 # for sorting 

descriptio: "We propose a computationally-efficient approach for evaluating the information-theoretic term within belief space planning (BSP), where during belief propagation the state vector can be constant or augmented. We consider both unfocused and focused problem settings, whereas uncertainty reduction of the entire system or only of chosen variables is of interest, respectively. State of the art approaches typically propagate the belief state, for each candidate action, through calculation of the posterior information (or covariance) matrix and subsequently compute its determinant (required for entropy). In contrast, our approach reduces run-time complexity by avoiding these calculations. We formulate the problem in terms of factor graphs and show that belief propagation is not needed, requiring instead a one-time calculation that depends on (the increasing with time) state dimensionality, and per-candidate calculations that are independent of the latter. 
"
---

To that end, we develop an augmented version of the matrix determinant lemma, and show that computations can be re-used when evaluating impact of different candidate actions. These two key ingredients and the factor graph representation of the problem result in a computationally-efficient (augmented) BSP approach that accounts for different sources of uncertainty and can be used with various sensing modalities.  We examine the unfocused and focused instances of our approach, and compare it to the state of the art, in simulation and using real-world data, considering problems such as autonomous navigation in unknown environments, measurement selection and sensor deployment. We show that our approach significantly reduces running time without any compromise in performance.
<!-- add  youtube and bibliography Here-->

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-RAMDL --order descending %}

