---
layout: gallery
title: Photo Gallery
hero_height: is-small
hero_image: /img/ANPL_quantum_field.jpg 
show_sidebar: false
---

## ANPL Social And Lab Events 

<div class="slick-slider">
  {% for slide in site.data.gallery_slides %}
    <div>
      <img src="{{ slide.image }}" alt="{{ slide.description }}">
    </div>
  {% endfor %}
</div>

