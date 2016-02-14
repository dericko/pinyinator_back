$(function() {
  $displayBox = $('.chinese-output');
  $('#submit-button').bind('click', function() {

    var text = $('#chinese-text').val();
    var url = "pinyinify";
    var data = {data:text};
    console.log(text);
    console.log(data);
    $.ajax({
      type: "POST",
      url: url,
      data: data,
      //contentType: "application/json; charset=UTF-8",
      success: displayPairs
    });
  });
});

var displayPairs = function (data) {
  console.log(data);
  var pairs = data.sentence;
  var $display = $('p');
  var stringRep = '';
  pairs.forEach(function (pair) {
    console.log(pair[0] + ': ' + pair[1]);
    stringRep = stringRep + ' ' + pair[0];
  });
  console.log(stringRep);
}
