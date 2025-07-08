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

