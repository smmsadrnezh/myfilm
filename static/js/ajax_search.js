var xhr = new XMLHttpRequest();

var input = document.querySelector("#search_string");

$("input#search_string").autocomplete({
    delay: 1,
    minLength: 1,
    source: function () {
        alert("hoy")

        if (this.value.length > 1) {
            xhr.open('get', '/search/' + this.value);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        var cdt = document.querySelector("#ajax-search-container");
                        cdt.innerHTML = xhr.responseText;
                    }
                }
            };

            xhr.send(null);
        }
    }
});