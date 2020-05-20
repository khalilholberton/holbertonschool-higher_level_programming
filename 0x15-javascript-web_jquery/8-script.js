const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, (data) => {
  for (let counter = 0; counter < data.results.length; counter++) {
    $('ul#list_movies').append('<li>' + data.results[counter].title + '</li>');
  }
});
