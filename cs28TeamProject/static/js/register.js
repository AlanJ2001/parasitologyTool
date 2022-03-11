 function validate() {
        var pw1 = document.getElementById('password').value;
        var pw2 = document.getElementById('confirm-password').value;

        if(pw1 == pw2) {
            document.getElementById("rel").innerHTML="<font color='green'>The passwords match</font>";
            document.getElementById('submit').disabled = false;
        }
        else {
            document.getElementById("rel").innerHTML="<font color='red'>The password don't match</font>";
            document.getElementById('submit').disabled = true;
        }
    }