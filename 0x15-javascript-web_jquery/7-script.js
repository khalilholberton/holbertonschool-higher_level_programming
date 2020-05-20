$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (characters) => {
  $('DIV#character').text(characters.name);
});
