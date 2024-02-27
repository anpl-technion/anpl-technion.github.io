---
title: Sparsification for Decision Making in High-Dimensional State Spaces
research_code: ABC125
layout: research
image: /img/research/CBS/00123_LogDetRandRc_plus.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 9 # for sorting 

descriptio: "In this research we introduce and investigate simplification of decision making problems in partially observable domains, while providing performance guarantees. Specifically, we propose the conceptual idea of resorting to sparsification and conservative information fusion techniques for information-theoretic decision making, aiming to address challenges involved with decision making over a potentially high-dimensional and highly-correlated, information space.

ur key observation is that in certain cases, the impact of any two actions (or policies) on an appropriate utility measure, such as entropy, has the same trend regardless if using the original probability distribution function (pdf) or an appropriately sparsified approximation of thereof. This observation suggests that in these cases, decision making can be performed over a sparsified (possibly conservative) pdf, instead of the original pdf, without sacrificing performance. We call such a simplification as action-consistent simplification. 

Finding an action-consistent simplification, in our case, belief sparsification, is not trivial in general. However, a computationally-easy simplification that is not necessarily action-consistent can still be very useful if the potential loss in performance (regret) can be quantified or bounded. In this research we investigate these and additional aspects considering decision making in high dimensional state spaces."

---

<!-- add  youtube and bibliography Here-->


# Related Publications: 
{% bibliography --file research-projects-bib/pubs-CBS --order descending %}

