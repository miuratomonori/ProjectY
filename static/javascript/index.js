src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
crossorigin="anonymous"

let loginNo = document.getElementById('no');
let passwd = document.getElementById('pass');

function loginClick(event){
    event.preventDefault();
    
    $.ajax({
        url:'/login',
        type:'POST',
        dataType:'json',
        data:{
            'number':loginNo.value,
            'password':passwd.value,
        }
    })
    .then(function (response){
        if(response.success){
            window.location.href = "/admin";
        }
        else{
            console.log("error");
        }
    })
    .catch(function (error) {
        console.error("通信エラー: ", error);
    });
    
}