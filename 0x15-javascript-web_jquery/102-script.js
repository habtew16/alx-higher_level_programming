$(document).ready(function() {
      $('#btn_translate').on('click', function() {
        let languageCode = $('#language_code').val();
	      
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/',
          method: 'GET',
          data: { lang: languageCode },
          dataType: 'json',
          success: function(data) {
            $('#hello').text(data.hello);
          },
          error: function(error) {
            console.error('Error fetching translation:', error);
          }
        });
      });
    });
