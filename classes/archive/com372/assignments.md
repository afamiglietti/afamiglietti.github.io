---
title: COM 372 - Web Design
layout: twin_column
tags: syllabus_page
category: com372
---

<div class="row">
  {% for assignment in site.data.com372.assignments %}
  <div class="col-md-4">
  <img class="pull-right assignment_img" src="/assets/img/{{ assignment.img }}">
  <h3>{{ assignment.title }}</h3>
  <strong>Due:</strong> {{assignment.date_due}} <br>
  <strong>Worth:</strong> {{assignment.grade_percentage}} of total grade
  <p>{{ assignment.short_description }}
  {% if assignment.full_description_link %}
  <a href="/classes/com372/assignments/{{assignment.full_description_link}}.html">(Read more...)</a>
  {% endif %}
  </p>
  </div>
  {% endfor %}
</div>
