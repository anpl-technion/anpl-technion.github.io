---
title: Autonomous Navigation and Perception Lab (ANPL)
subtitle: Technion - Israel Institute of Technology
layout: page
show_sidebar: false
hide_footer: false
hero_height: is-medium
hero_image: /img/ANPL_quantum_field.jpg 
---

# Welcome! 

The Autonomous Navigation and Perception Lab performs research related to single and multi-robot autonomous perception, navigation and planning under uncertainty in the context of mobile robotics. Research in the lab is highly multidisciplinary, involving both fundamental theoretical studies and experimental verification. Please visit [<span style="color:red">
<b>Research</b>
</span>](https://anpl-technion.github.io/research/) and [<span style="color:red">
<b>Publications</b>
</span>](https://anpl-technion.github.io/publications/) pages to see ongoing research activities. The lab was founded by Assoc. Prof. Vadim Indelman in 2014.


<span style="color:red">
<b>
We are always looking for highly-motivated individuals to join our group, see details [here.](https://anpl-technion.github.io/Positions/)
</b>
</span>

<div class="slick-slider">
  {% for slide in site.data.home_slides %}
    <div>
      <img src="{{ slide.image }}" alt="{{ slide.description }}">
    </div>
  {% endfor %}
</div>


## Recent News & Updates

<div class="columns is-multiline">
  <div class="column is-6">
    <div class="box">
      <h4>Lab News</h4>
      <p>Follow our latest research updates and announcements.</p>
    </div>
  </div>
  <div class="column is-6">
    <div class="box">
      <h4>Latest Updates</h4>
      
      <!-- Twitter Feed -->
      {% if site.data.tweets %}
        <h5 class="subtitle is-6">Recent Tweets</h5>
        {% for tweet in site.data.tweets limit: 4 %}
          <div class="media">
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>{{ tweet.handle }}</strong>
                  <small>{{ tweet.created_at | date: "%b %d" }}</small>
                  <br>
                  {{ tweet.text }}
                </p>
              </div>
            </div>
          </div>
          {% unless forloop.last %}<hr style="margin: 0.5rem 0;">{% endunless %}
        {% endfor %}
      {% endif %}
      
      <!-- Lab News -->
      {% assign recent_news = site.news | sort: 'date' | reverse | limit: 2 %}
      {% if recent_news.size > 0 %}
        <h5 class="subtitle is-6" style="margin-top: 1rem;">Lab News</h5>
        {% for news in recent_news %}
          <div class="content">
            <p>
              <strong>{{ news.title }}</strong><br>
              <small>{{ news.date | date: "%B %d, %Y" }}</small><br>
              {{ news.content | strip_html | truncate: 80 }}
            </p>
          </div>
          {% unless forloop.last %}<hr style="margin: 0.5rem 0;">{% endunless %}
        {% endfor %}
      {% endif %}
      
      <div style="margin-top: 1rem;">
        <a class="button is-primary is-small" href="/news/">All Updates</a>
        <a class="button is-info is-small" href="/publications/">Publications</a>
      </div>
    </div>
  </div>
</div>

<hr>

### We gratefully acknowledge our funding sources over the years: 

<div class="horizontal-grid-container">
  <div class="grid-item">
    <img src="/img/funding/ISF-logo3.png" alt="ISF">
  </div>
  <div class="grid-item">
    <img src="/img/funding/NSF-logo.jpeg" alt="BSF">
  </div>
  <div class="grid-item">
    <img src="/img/funding/BSF-logo.png" alt="BSF">
  </div>
  <div class="grid-item">
    <img src="/img/funding/MOST-logo3.jpeg" alt="MOST">
  </div>
  <div class="grid-item">
    <img src="/img/funding/meta.png" alt="meta">
  </div>
  <div class="grid-item">
    <img src="/img/funding/intel-150x150.png" alt="intel">
  </div>
  <div class="grid-item">
    <img src="/img/funding/ISTRC.png" alt="ISTRC">
  </div>
  <div class="grid-item">
    <img src="/img/funding/MAFAT-logo.png" alt="MAFAT">
  </div>
  <!-- <div class="grid-item">
    <img src="/img/funding/TASP-logo.png" alt="TASP">
  </div> -->
  <!-- Add more grid items for more images -->
</div>

