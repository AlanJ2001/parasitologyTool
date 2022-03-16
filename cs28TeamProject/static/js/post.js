$(document).ready(function(){
   var onoff = false;
   $('.item').each(function() {
    var article = $(this).find('.context');
    var str = article.html().replace(/<br>/g, "\n").replace(/<p>/g, "").replace(/<\/p>/g, "");
    var see = $(this).find('.see');
    if (str.length > 200) {
     article.text(str.substr(0, 200) + '......');
     see.text('Show All');  
    }
    see.click(function() {
     if (onoff) {
      article.text(str.substr(0, 200) + '......');
      see.text('Show All');
     } else {
      article.text(str);
      see.text('Show Less');
     }
     onoff = !onoff
    });
   });
  });
