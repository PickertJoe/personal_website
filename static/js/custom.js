//Function helps the browser to load markdown text
$(document).ready(function(){
    $(".content-markdown").each(function(){
      var content = $(this).text()
      console.log(content)
      var markedContent = marked(content)
      console.log(markedContent)
      $(this).html(markedContent)
    })
    $('.content-markdown img').each(function(){
          $(this).addClass('img-fluid');
    })

  })

/*Function makes fixed navbar turn solid upon scrolling
  Source code obtained from open-source contribution by Erin Manahan
  https://codepen.io/sonorangirl/pen/XmRBjq-*/
$(document).ready(function() {
    $(window).scroll(function() {
      if($(this).scrollTop() > 50) {
          $('.navbar').addClass('solid');
      } else {
          $('.navbar').removeClass('solid');
      }
    });
});

//Helper function to determine 'style' status of the homepage for hide button-->

function showHide() {
  var x = document.getElementById("toggle");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

