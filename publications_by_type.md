---
layout: page
title: Publications
show_sidebar: false
hide_footer: false
---

<style>
.csl-block {
    font-size: 16px;
}
.csl-title, .csl-author, .csl-event, .csl-editor, .csl-venue {
    display: block;
    position: relative;
    font-size: 16px;
}

.csl-title b {
    font-weight: 600;
}

.csl-content {
    display: inline-block;
    vertical-align: top;
    padding-left: 20px;
}

.bibliography {
   list-style-type: none;
}
</style>

 This material is presented to ensure timely dissemination of scholarly and technical work. Copyright and all rights therein are retained by authors or by other copyright holders. All persons copying this information are expected to adhere to the terms and constraints invoked by each author’s copyright. In most cases, these works may not be reposted without the explicit permission of the copyright holder.

Sort publications by [chronologically](https://anpl-technion.github.io/publications/), or <b>type</b>. You are also welcome to browse slides from [talks](https://anpl-technion.github.io/talks).

# Journal Articles
{% bibliography --query @article %}

# Book Chapters
{% bibliography --query @incollection %}

# Conference Articles
{% bibliography --query @InProceedings %}

# arXiv and Technical Reports
{% bibliography --query @TechReport %}

# PhD Theses
{% bibliography --query @phdthesis %}

# Master's Theses
{% bibliography --query @mastersthesis %}