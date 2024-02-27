---
title: Three-View Geometry Constraints for Navigation-Aiding
research_code: ABC125
layout: research
image: /img/research/ThreeViewNav/Three_View_Geometry3.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 18 # for sorting 

descriptio: "In this research, we introduced the usage of three-view constraints for navigation-aiding in a monocular camera configuration. A new formulation of three-view constraints was developed, that includes in addition to the well-known epipolar constraints, a new constraint that allows to maintain a consistent scale even in co-linear camera configurations (which is not possible with only epipolar constraints). Given three overlapping images and the associated navigation solutions, the three-view constraints allow to reduce position errors in all axes to the levels present while the ﬁrst two images were captured. The developed approach (see TAES2012) eliminates the need in the intermediate step of 3D point estimations and can be used for navigation-aiding based on nearby overlapping imagery as well as loop closures. In the latter case, only 3 images are required to incorporate loop closure information into the navigation system, as opposed to processing all images in the loop chain as conventionally done in other methods.

Three-view geometry constraints are also applied in distributed cooperative navigation and in incremental light bundle adjustment (iLBA)."
---

<!-- add  youtube and bibliography Here-->

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-ThreeViewNav --order descending %}

