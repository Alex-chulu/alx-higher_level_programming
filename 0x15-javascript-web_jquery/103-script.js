$(document).ready(function() {

  function translateHello() {
    let languageCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(function() {
    translateHello();
  });

  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

});
