---
layout: gallery
title: Photo Gallery
show_sidebar: false
---

<div class="slick-slider">
  {% for slide in site.data.gallery_slides %}
    <div>
      <img src="{{ slide.image }}" alt="{{ slide.description }}">
    </div>
  {% endfor %}
</div>