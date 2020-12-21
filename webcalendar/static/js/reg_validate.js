function validate() {
    var conf_pass = document.getElementById("confirm_password");
    var pass = document.getElementById("password");

    if (pass.value != conf_pass.value){
        document.getElementById('alert').style.display = "flex";
        document.getElementById('submit').disabled = true;
    }
    else {
        document.getElementById('alert').style.display = "none";
        document.getElementById('submit').disabled = false;
    }
}