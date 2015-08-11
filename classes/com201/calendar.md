---
title: COM 201 - Communications Ethics
layout: default
tags: syllabus_page
category: com201
---
<div id="current">
Replace this.
</div>
{% for meeting in site.data.com201.calendar %}
<div id="{{ meeting.date }}" class="class_meeting">
<ul>
  <li><strong>{{ meeting.date | convert:"date" | date:"%A %B %-d" }}</strong></li>
  <li><em>Read:</em> {{ meeting.reading }}</li>
  <li><em>Class Activity:</em> {{ meeting.in_class }}</li>
  <li><em>Assignment Due:</em> {{ meeting.assignment }}</li>
</ul>  
</div>
{% endfor %}

{% include highlight.html %}
