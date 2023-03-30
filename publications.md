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

Sort publications <b>chronologically</b> or by [type](https://anpl-technion.github.io/publications_by_type/). You are also welcome to browse slides from [talks](https://anpl-technion.github.io/talks).


# 2023
{% bibliography --query @*[year=2023] %}
# 2022
{% bibliography --query @*[year=2022] %}

# 2021
{% bibliography --query @*[year=2021] %}

# 2020
{% bibliography --query @*[year=2020] %}

# 2019
{% bibliography --query @*[year=2019] %}

# 2018
{% bibliography --query @*[year=2018] %}

# 2017
{% bibliography --query @*[year=2017] %}

# 2016
{% bibliography --query @*[year=2016] %}

# 2015
{% bibliography --query @*[year=2015] %}

# 2014
{% bibliography --query @*[year=2014] %}

# 2013
{% bibliography --query @*[year=2013] %}

# 2012
{% bibliography --query @*[year=2012] %}

# 2011
{% bibliography --query @*[year=2011] %}

# 2010
{% bibliography --query @*[year=2010] %}

# 2009
{% bibliography --query @*[year=2009] %}

# 2008
{% bibliography --query @*[year=2008] %}

# 2007
{% bibliography --query @*[year=2007] %}

{% bibliography --group_by type  --sort_by year --order descending %}