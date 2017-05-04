---
title: Blog
layout: default
---

  {% for post in site.posts %}
  <div class="post">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <span class="postDate">{{post.date | date: '%B %d, %Y'}}</span>
      <br>
      {{ post.excerpt }}
  </div>    
  {% endfor %}
