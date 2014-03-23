$(".django-logo")
  .mouseover(function() {
    $(this).attr({src : "https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif"});
  })
  .mouseout(function() {
    $(this).attr({src : "https://www.djangoproject.com/m/img/badges/djangopowered126x54_grey.gif"});
  });