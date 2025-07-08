---
title: Lab News & Updates
layout: page
show_sidebar: false
---

# ANPL Lab News & Updates

{% assign all_news = site.news | sort: 'date' | reverse %}

<div class="content">
  {% for news in all_news %}
    <div class="box">
      <h3>{{ news.title }}</h3>
      <p class="has-text-grey">{{ news.date | date: "%B %d, %Y" }} • {{ news.author }}</p>
      <div class="content">
        {{ news.content }}
      </div>
      {% if news.category %}
        <span class="tag is-info">{{ news.category }}</span>
      {% endif %}
    </div>
  {% endfor %}
</div>

---

## Follow Our Social Media

Stay connected with the latest updates from ANPL:

<div class="buttons">
  <a class="button is-info" href="https://twitter.com/ANPL_Technion" target="_blank">
    <span class="icon">
      <i class="fab fa-twitter"></i>
    </span>
    <span>@ANPL_Technion</span>
  </a>
  <a class="button is-info" href="https://twitter.com/vadim_indelman" target="_blank">
    <span class="icon">
      <i class="fab fa-twitter"></i>
    </span>
    <span>@vadim_indelman</span>
  </a>
</div>