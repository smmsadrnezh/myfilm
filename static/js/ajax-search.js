$(function () {
    $("#search-string").autocomplete({
        source: "/search/ajax/",
        delay: 400,
        minLength: 2
    });
});