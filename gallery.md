---
layout: page
title: Photo Gallery
---

<div class="slick-slider">
  {% for slide in site.data.slides %}
    <div>
      <img src="{{ slide.image }}" alt="{{ slide.description }}">
    </div>
  {% endfor %}
</div>