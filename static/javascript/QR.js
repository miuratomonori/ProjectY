src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"

let formID = document.getElementById('studentID');
let keyword = document.getElementById('keyword');

function buttonClick(){
    // Ajax通信を開始
    $.ajax({
      url: '',
      type: 'POST',
      dataType: 'json',
      data: {
        'studentID':formID.value,
        'keyword': keyword.value,
      }
      //timeout: 5000,
    })
    .done(function(data) {
        // 通信成功時の処理を記述
        alert("success!");
    })
    .fail(function() {
        // 通信失敗時の処理を記述
        alert('error!');
    });
  }
    