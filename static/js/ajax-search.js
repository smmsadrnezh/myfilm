$(function () {
    $("#search-string").autocomplete({
        source: "/search/ajax/",
        delay: 400,
        minLength: 2
    });
});

//$("#search-string").autocomplete({
//    //source: availableTags,
//    delay: 3,
//    minLength: 2,
//    source: function () {
//            xhr.open('get', '/search/' + document.getElementById('search-string').value);
//            xhr.onreadystatechange = function () {
//                if (xhr.readyState === 4) {
//
//                    if (xhr.status === 500) {
//                        alert(xhr.responseText)
//
//                        //var availableTags = xhr.responseText;
//                    }
//                }
//            };
//
//            xhr.send(null);
//    }
//});

//$(function() {
//  var availableTags = [
//    "ActionScript",
//    "AppleScript",
//    "Asp",
//    "BASIC",
//    "C",
//    "C++",
//    "Clojure",
//    "COBOL",
//    "ColdFusion",
//    "Erlang",
//    "Fortran",
//    "Groovy",
//    "Haskell",
//    "Java",
//    "JavaScript",
//    "Lisp",
//    "Perl",
//    "PHP",
//    "Python",
//    "Ruby",
//    "Scala",
//    "Scheme"
//  ];
//  $( "#search-string" ).autocomplete({
//
//  });
//});