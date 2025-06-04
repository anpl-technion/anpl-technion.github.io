---
title: Multi-Robot POMDPs with Inconsistent Beliefs
research_code: ABC125
layout: research
image: /img/research/MRBSPinconsistentHistories/motivating-example-d.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 3 # for sorting 

descriptio: "Multi-robot POMDP and belief space planning (MR-BSP) is essential for reliable and safe autonomy. While planning, each robot maintains a belief over the state of the environment and reasons how the belief would evolve in the future for different candidate actions. Yet, existing multi-robot POMDP and MR-BSP approaches have a common assumption that the beliefs of different robots are consistent at planning time. Such an assumption is often highly unrealistic, as it requires prohibitively extensive and frequent communication capabilities. In practice, each robot may have a different belief about the state of the environment. Crucially, when the beliefs of different robots are inconsistent, state-of-the-art MR-BSP approaches could result in a lack of coordination between the robots, and in general, could yield dangerous, unsafe, and sub-optimal decisions. In this project, we tackle this crucial gap. Specifically, we develop a novel decentralized MR-BSP framework that explicitly accounts for inconsistent beliefs and self-triggers communication only when the same joint action selection by different robots cannot be guaranteed.
"
---
<!-- add  youtube and bibliography Here-->

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-MRBSPinconsistentHistories --order descending %}
