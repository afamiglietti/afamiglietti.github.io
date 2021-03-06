---
title: WRT 120 - Effective Writing 1
layout: default
tags: syllabus_page
category: wrt120
---

This calendar lists all of the readings, assignments, and activities for the class. Remember that material needs to be read, and assignments completed <em>prior to</em> the class meeting they are listed for. For your convenience, I list the information for the upcoming class meeting at the top of the page, but consult the full schedule below to get a sense of what's coming up in the weeks ahead.

<div id="meeting_jumbo" class="jumbotron">
  <h2>NEXT CLASS:</h2>
  <div id="next_meeting">
    This semester's over! You can find all our class meetings below!
  </div>
</div>
{% for meeting in site.data.wrt120.calendar %}
<div id="{{ meeting.date }}" class="class_meeting">
<h3>{{ meeting.date | convert:"date" | date:"%A %B %-d" }}</h3>
  <ul>
  <li><em>Read:</em>
    <ul>
    {% for reading in meeting.readings %}
      {% if reading.link %}
        <li><a href="{{ reading.link }}" target="_blank">{{ reading.title }}</a></li>
      {% else %}
        <li>{{ reading.title }}</li>
      {% endif %}
    {% endfor %}
    </ul>
    </li>  
  <li><em>Class Activity:</em> {{ meeting.in_class }}</li>
  <li><em>Assignment Due:</em> {{ meeting.assignment }}</li>
</ul>  
</div>
{% endfor %}
