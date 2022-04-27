var search_btn = document.getElementById('search-btn');
var search_btn2 = document.getElementById('search-button2');

search_btn2.addEventListener('click', function(e){
    e.preventDefault();
    toggle_search2();
})

search_btn.addEventListener('click', function(e){
    e.preventDefault();
    toggle_search();
})

$("#search").on("keydown",function search(e) {
    if(e.keyCode == 13) {
        toggle_search();
    }
});

$("#mobile-search").on("keydown",function search(e) {
    if(e.keyCode == 13) {
        toggle_search2();
    }
});


toggle_search = ()=>{
    _search = document.getElementById('search');
    window.location.href = '/search/' + _search.value
}



toggle_search2 = ()=>{
    _search = document.getElementById('mobile-search');
    window.location.href = '/search/' + _search.value
}