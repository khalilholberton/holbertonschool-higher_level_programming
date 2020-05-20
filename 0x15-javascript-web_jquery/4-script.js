$('Div#toggle_header').click(function () {
  $('header').toggleClass(function () {
    return $(this).hasClass('red') ? 'green' : 'red';
  });
});
