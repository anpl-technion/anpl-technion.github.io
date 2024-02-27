---
title: Qualitative SLAM and Belief Space Planning
research_code: ABC125
layout: research
image: /img/research/QualitativeAutonomousPerception/composition1.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 7 # for sorting 

descriptio: "Many robotics applications rely on accurate metric estimations of the environment and robot’s location to accomplish their aims.
However, in the absence of high-quality sensors, accurate robotics methods encounter significant diﬀiculties. These methods are typically noise-sensitive and tend to accumulate errors as they rely on metrical estimates of map and robot’s trajectory. Thus, noisy measurements can significantly impair their accuracy, cause undesir- able drifts, and eventually lead to divergence if the loop-closer fails. Another concern that arises from the metric approaches is the need to maintain a dense, potentially large map representation, which often comes at the cost of substantial computational and memory resources. 

While maintaining accurate information is often essential, it might be unnecessary in some cases, and therefore a burden. For instance, consider an autonomous cleaning robot operating in a living room. A typical living room contains a relatively small number of meaningful objects. Relying on rough relative relationships between the different objects, rather than on exact metric coordinates, may be suﬀicient for the robot to maneuver within the room successfully. E.g., if the robot seeks to clean under the table, it must pass safely between the table’s legs. However, neither the exact metric coordinates of the legs nor the exact robot’s location between them is required. Moreover, in long-term autonomous navigation missions, the robot is often required to travel long distances, so relying on a small number of critical landmarks along the way might be a good enough strategy.
"
---

Qualitative approaches are motivated by the above. In contrast to the metrical methods, the environment and robot’s poses are tracked using coarse, relative geometrical relations, known as qualitative spatial relationships (QSRs). This coarse manner of reasoning about spatial information is potentially more noise-robust and suitable for low-cost platforms. Also, Qualitative Relational Mapping (QRM) algorithms produce QSR-based maps that sparsely represent the environment. Lastly, the robot can reason about the environment and even plan while accounting for partial information involved in a single or few QSR only, thus saving computational energy.

Motivated by the above, in this research project we develop qualitative approaches for SLAM and belief space planning.
<!-- add  youtube and bibliography Here-->

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-QualitativeAutonomousPerception --order descending %}

