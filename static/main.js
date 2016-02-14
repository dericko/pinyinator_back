$(function() {
  $displayBox = $('.chinese-output');
  $('#submit-button').bind('click', function() {

    var text = $('#chinese-text').val();
    var url = "pinyinify";
    var data = {data:text};
    // console.log(text);
    // console.log(data);
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
  var $displayArea = $('#chinese-output');
  console.log($displayArea);
  var titlePairs = data.title;
  var paragraphs = data.paragraphs;
  var $paragraphWrap = $('<div></div>');
  var $titleChar = $('<h1></h1>');
  var $titlePiyin = $('<h2></h2>');
  // var titleChar = '';
  // var pinyinChar = '';
  titlePairs.forEach(function (pair) {
    var stringRep =  pair[0] + pair[1]
    $titleChar.append(pair[[0]]);
    $titlePiyin.append(pair[1]);
  });


  paragraphs.forEach(function (paragraph) {
    var $displayChar = $('<p></p>');
    var $displayPinyin = $('<p></p>');

    paragraph.forEach(function (pair) {
      var stringRep =  pair[0] + pair[1];
      $displayChar.append(pair[0]);
      $displayPinyin.append(pair[[1]]);
    });
    $paragraphWrap.append($displayPinyin);
    $paragraphWrap.append($displayChar);
  });

  $displayArea.append($titlePiyin);
  $displayArea.append($titleChar);
  $displayArea.append($paragraphWrap);
}
