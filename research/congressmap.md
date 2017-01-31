---
title: Research
layout: twin_column
---

<div class="row">
    <div class="col-md-8">
      <h3>Map of Republican Congressional Districts w/ PVI R+5 or Less</h3>
      <div id="googft-mapCanvas"></div>
    </div>
    <div class="col-md-4">
      <h3>About This Map</h3>

    </div>
</div>
<script type="text/javascript" src="https://maps.google.com/maps/api/js?v=3"></script>

<script type="text/javascript">
  function initialize() {
    google.maps.visualRefresh = true;
    var isMobile = (navigator.userAgent.toLowerCase().indexOf('android') > -1) ||
      (navigator.userAgent.match(/(iPod|iPhone|iPad|BlackBerry|Windows Phone|iemobile)/));
    if (isMobile) {
      var viewport = document.querySelector("meta[name=viewport]");
      viewport.setAttribute('content', 'initial-scale=1.0, user-scalable=no');
    }
    var mapDiv = document.getElementById('googft-mapCanvas');
    mapDiv.style.width = isMobile ? '100%' : '500px';
    mapDiv.style.height = isMobile ? '100%' : '300px';
    var map = new google.maps.Map(mapDiv, {
      center: new google.maps.LatLng(39.285024899870585, -91.42889291015626),
      zoom: 5,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    layer = new google.maps.FusionTablesLayer({
      map: map,
      heatmap: { enabled: false },
      query: {
        select: "col6\x3e\x3e1",
        from: "1OkFL1B9wI6nWyUFGtodLl7FOyCoChcVUt9Lk_TRW",
        where: "col2\x3e\x3e0 in (\x27CA-10\x27, \x27CA-21\x27, \x27CA-25\x27, \x27CA-31\x27, \x27CA-39\x27, \x27CA-49\x27, \x27CO-03\x27, \x27CO-06\x27, \x27FL-07\x27, \x27FL-13\x27, \x27FL-25\x27, \x27FL-27\x27, \x27IA-03\x27, \x27IA-04\x27, \x27IL-06\x27, \x27IL-13\x27, \x27IL-14\x27, \x27IL-16\x27, \x27MI-01\x27, \x27MI-03\x27, \x27MI-04\x27, \x27MI-06\x27, \x27MI-07\x27, \x27MI-08\x27, \x27MI-11\x27, \x27MN-02\x27, \x27MN-03\x27, \x27NE-02\x27, \x27NJ-02\x27, \x27NJ-03\x27, \x27NJ-05\x27, \x27NM-02\x27, \x27NV-02\x27, \x27NV-03\x27, \x27NY-02\x27, \x27NY-11\x27, \x27NY-19\x27, \x27NY-22\x27, \x27NY-23\x27, \x27OH-10\x27, \x27OH-14\x27, \x27PA-06\x27, \x27PA-07\x27, \x27PA-08\x27, \x27PA-15\x27, \x27PA-16\x27, \x27VA-02\x27, \x27VA-04\x27, \x27VA-05\x27, \x27VA-10\x27, \x27WA-03\x27, \x27WA-08\x27, \x27WI-01\x27, \x27WI-06\x27, \x27WI-07\x27, \x27WI-08\x27)"
      },
      options: {
        styleId: 2,
        templateId: 2
      }
    });

    if (isMobile) {
      var legend = document.getElementById('googft-legend');
      var legendOpenButton = document.getElementById('googft-legend-open');
      var legendCloseButton = document.getElementById('googft-legend-close');
      legend.style.display = 'none';
      legendOpenButton.style.display = 'block';
      legendCloseButton.style.display = 'block';
      legendOpenButton.onclick = function() {
        legend.style.display = 'block';
        legendOpenButton.style.display = 'none';
      }
      legendCloseButton.onclick = function() {
        legend.style.display = 'none';
        legendOpenButton.style.display = 'block';
      }
    }
  }

  google.maps.event.addDomListener(window, 'load', initialize);
</script>
