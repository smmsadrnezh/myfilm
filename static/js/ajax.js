    var i=0;
    var xhr = new XMLHttpRequest();
    $(window).scroll(function() {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            xhr.open('get', '/getdata/'+i);
            i+=1;
            xhr.onreadystatechange = function() {
                if(xhr.readyState === 4) {
                    if(xhr.status === 200) {
                        var cdt = document.querySelector("#container");
                        cdt.innerHTML = xhr.responseText;
                    }
                    else {
                        alert(xhr.status)
                    }
                }
            };

		xhr.send(null);
        }
    });



