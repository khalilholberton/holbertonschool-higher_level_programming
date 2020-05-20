$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.getJSON('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (language) {
      $('DIV#hello').html('<br />' + language.hello);
    });
  });
});
