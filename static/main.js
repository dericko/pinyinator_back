$(function() {
  $('#submit-button').bind('click', function() {

    var text = $('#chinese-text').val(); 
    var url = "http://localhost:5000/pinyinify";
    var data = {"data": text};
    console.log(data);

    $.post(url, data, null, "json");
  });
})
