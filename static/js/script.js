$(document).ready(function() {
    var $magic = $(".magic"),
        magicWHalf = $magic.width() / 2;
    $(document).on("mousemove", function(e) {
      $magic.css({"left": e.pageX - magicWHalf, "top": e.pageY - magicWHalf});
    });
});


$('input').on('change', function () {
  var file = $(this).prop('files')[0];
  $('p').text(file.name);
});

$(function(){
  $('input').on('change', function () {
      var file = $(this).prop('files')[0];
      $('.select-image').text(file.name);
  });
});