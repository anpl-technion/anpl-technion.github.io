---
layout: page
title: Publications
show_sidebar: false
hide_footer: false
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
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

 <div id="Top"></div>

Sort publications [<span style="color:red">
chronologically
</span>](https://anpl-technion.github.io/publications/) or by <span style="color:red">
<b>type</b>
</span>. You are also welcome to browse slides from [<span style="color:red">
talks
</span>](https://anpl-technion.github.io/talks).


[[Journal Articles]](#Journal-Articles) [[Book Chapters]](#Book-Chapters) [[Conference Articles]](#Conference-Articles) [[ArXiv & Technical Reports]](#Technical-Reports) [[PhD Theses]](#PhD-Theses) [[Master's Theses]](#Master-Theses)

# Journal Articles
<div id="Journal-Articles"></div>
{% bibliography --group_by none --query @article --order descending %}

[Back to Top](#Top)

# Book Chapters
<div id="Book-Chapters"></div>
{% bibliography --group_by none --query @incollection --order descending %}

[Back to Top](#Top)

# Conference Articles
<div id="Conference-Articles"></div>
{% bibliography --group_by none --query @InProceedings --order descending %}

[Back to Top](#Top)

# ArXiv and Technical Reports
<div id="Technical-Reports"></div>
{% bibliography --group_by none --query @TechReport --order descending %}

[Back to Top](#Top)

# PhD Theses
<div id="PhD-Theses"></div>
{% bibliography --group_by none --query @phdthesis --order descending %}

[Back to Top](#Top)

# Master's Theses
<div id="Master-Theses"></div>
{% bibliography --group_by none --query @mastersthesis --order descending %}

[Back to Top](#Top)

