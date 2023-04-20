---
title: Incremental Light Bundle Adjustment
research_code: ABC125
layout: research
image: /img/research/LBA/FactorGraph_LBA.jpg
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 13 # for sorting 

descriptio: "Bundle adjustment (BA) is essential in many robotics and structure-from-motion applications: given a set of images, captured by a single or multiple users (or autonomous platforms), BA provides the maximum a posteriori estimate of camera poses and observed environment (e.g. 3D points). Assuming Gaussian image noise, the problem is equivalent to minimizing the re-projection errors of all image observations in all images. However, as more images are acquired, the involved optimization becomes increasingly computationally expensive: on-line performance over long time periods is therefore and challenging problem.

In this research we introduce incremental light bundle adjustment (iLBA): an efficient optimization framework that substantially reduces computational complexity compared to incremental bundle adjustment. First, the number of variables in the optimization is reduced by algebraic elimination of observed 3D points, leading to a /structureless/ BA. The resulting cost function is formulated in terms of /three-view/ constraints instead of re-projection errors and only the camera poses are optimized. Second, the optimization problem is represented using graphical models and incremental inference is applied, updating the solution using adaptive partial calculations each time a new camera is incorporated into the optimization. Typically, only a small fraction of the camera poses are recalculated in each optimization step. The 3D points, although not explicitly optimized, can be reconstructed based on the optimized camera poses at any time."
---

<!-- add  youtube and bibliography Here-->

<div style="display: flex; justify-content: center;">
    <iframe width="40%" height="315" src="https://www.youtube.com/embed/1k9FEq8sb4o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


# Related Publications: 
{% bibliography --file research-projects-bib/pubs-LBA --order descending %}

