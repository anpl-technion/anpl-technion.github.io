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
  <div class="column is-12">
    <div class="box">
      
      <!-- Twitter Feed -->
      {% if site.data.tweets %}
        {% for tweet in site.data.tweets limit: 4 %}
          <div class="media">
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>{{ tweet.handle }}</strong>
                  <small>{{ tweet.created_at | date: "%b %d" }}</small>
                  <br>
                  {{ tweet.text | linkify_tweet: tweet.urls }}
                </p>
                
                <!-- View Tweet button -->
                {% if tweet.link %}
                  <div style="margin-top: 0.5rem;">
                    <a href="{{ tweet.link }}" target="_blank" class="button is-small is-info is-outlined">
                      <span class="icon is-small">
                        <i class="fab fa-twitter"></i>
                      </span>
                      <span>View Tweet</span>
                    </a>
                  </div>
                {% endif %}
              </div>
            </div>
          </div>
          {% unless forloop.last %}<hr style="margin: 0.5rem 0;">{% endunless %}
        {% endfor %}
      {% endif %}
      
      
      <div style="margin-top: 1rem;">
        <a class="button is-primary is-small" href="https://twitter.com/ANPL_Technion" target="_blank">
          <span class="icon is-small">
            <i class="fab fa-twitter"></i>
          </span>
          <span>Follow @ANPL_Technion</span>
        </a>
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

