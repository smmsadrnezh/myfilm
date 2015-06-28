function comment() {
    var url = window.location.pathname + "comment/"; // the script where you handle the form input.

    $.ajax({
        type: "POST",
        url: url,
        data: $("#commentForm").serialize(), // serializes the form's elements.
        success: function (data) {
            document.querySelector("#comment").innerHTML = data;
        }
    });

    return false; // avoid to execute the actual submit of the form.
}


function like() {
    likebtn = document.getElementById("likebtn");
    if (likebtn.innerHTML == "Like")
        likebtn.innerHTML = "UnLike"
    else
        likebtn.innerHTML = "Like"
    $.ajax({
        url: window.location.pathname + "like/",
        success: function (response) {
            document.querySelector("#like").innerHTML = response;
        }
    });
}
