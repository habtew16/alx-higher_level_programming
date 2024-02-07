// $('document').ready(function () {
//   $.getJSON('https://swapi.co/api/people/5/?format=json', function (value) {
//     $('DIV#character').text(value.name);
//   });
// });
$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        let characterName = data.name;
        $('#character').text(characterName);
      },
      error: function(error) {
        console.error('Error fetching character data:', error);
      }
    });
  });
