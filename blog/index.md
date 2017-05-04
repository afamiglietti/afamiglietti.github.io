---
title: Blog
layout: default
---

  {% for post in site.posts %}
  <div class="post">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <small>{{post.date}}</small>
      <br>
      {{ post.excerpt }}
  </div>    
  {% endfor %}
