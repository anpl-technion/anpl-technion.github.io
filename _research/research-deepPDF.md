---
title: Probabilistic Inference via Deep Learning
research_code: ABC125
layout: research
image: /img/research/deepPDF/PSO_drawing.png
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
price: 14 # for sorting 

descriptio: "Probabilistic inference, such as density (ratio) estimation, is a fundamental and highly important problem that needs to be solved in many different domains, and in particular in robotics. Recently, a lot of research was done to solve it by producing various objective functions optimized over neural network (NN) models. Such Deep Learning (DL) based approaches include unnormalized and energy models, as well as critics of Generative Adversarial Networks, where DL has shown top approximation performance. In this research we contribute a novel algorithm family, which generalizes all above, and allows us to infer different statistical modalities (e.g. data likelihood and ratio between densities) from data samples. The proposed unsupervised technique, named Probabilistic Surface Optimization (PSO), views a model as a flexible surface which can be pushed according to loss-specific virtual stochastic forces, where a dynamical equilibrium is achieved when the pointwise forces on the surface become equal. 
"
---

Concretely, the surface is pushed up and down at points sampled from two different distributions, with overall up and down forces becoming functions of these two distribution densities and of force intensity magnitudes defined by the loss of a particular PSO instance. Upon convergence, the force equilibrium associated with the Euler-Lagrange equation of the loss enforces an optimized model to be equal to various statistical functions, such as data density, depending on the used magnitude functions. Furthermore, this dynamical-statistical equilibrium is extremely intuitive and useful, providing many implications and possible usages in probabilistic inference. We connect PSO to numerous existing statistical works which are also PSO instances, and derive new PSO-based inference methods as demonstration of PSO exceptional usability. Additionally, we investigate the impact of Neural Tangent Kernel (NTK) on PSO equilibrium. Our study of NTK dynamics during the learning process emphasizes the importance of the model kernel adaptation to the specific target function for a good learning approximation.

Earlier, we investigated the following related concept. Typical inference approaches that work with high-dimensional visual measurements use hand-engineered image features (e.g. SIFT) that require combinatorial data association, or predict only hidden state mean without considering its uncertainty and multi-modality aspects. We develop a novel approach to infer system hidden state from visual observations via CNN features which are outputs of a CNN classifier. To that end, at pre-deployment stage we use neural networks to learn a generative viewpoint-dependent model of CNN features given the robot pose and approximate this model by a spatially varying Gaussian distribution. Further, at deployment this model is utilized within a Bayesian framework for probabilistic inference, considering a robot localization problem. Our method does not involve data association and provides uncertainty covariance of the final estimation. Moreover, we show empirically that the CNN feature likelihood is unimodal which simplifies the inference task. We test our method in simulated a Unreal Engine environment, where we succeed to retrieve high-level state information from CNN features and produce trajectory estimation with high accuracy. Additionally, we analyze robustness of our approach to different light conditions.

<img src="/img/research/InfoRecoveryCNN/drawing.png" alt="drawing" style="width: 45%; height: auto;"><img src="/img/research/InfoRecoveryCNN/traj_extended-eps-converted-to.png" alt="traj_extended-eps-converted-to" style="width: 45%; height: auto;">

<!-- add  youtube and bibliography Here-->

# Related Publications: 
{% bibliography --file research-projects-bib/pubs-deepPDF --order descending %}

