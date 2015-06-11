/**
 * Created by arman on 05/03/2015.
 */

function isvalid() {
    var inputs = document.getElementsByClassName("form-control");
    var error = document.getElementById("error");


    var mail = "a@b.c";
    var pass = "123";
    if (!(inputs[0].value == mail && inputs[1].value == pass)) {
        error.addClass("show");
        //window.location.href = "/timeline";
    }

}