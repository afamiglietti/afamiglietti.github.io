---
title: Blog
layout: default
---

  {% for post in site.posts %}
  <div class="post">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="postDate">{{post.date | date: '%B %d, %Y'}}</div>
      <a href="{{ post.url }}"> With {{ site.data.comments[post.slug] | size }} comments</a>
      <br>
      {{ post.excerpt }}
  </div>    
  {% endfor %}
