$(document).ready(function($){
    $('#myCarousel').carousel({
        interval: 4000,
        pause: null
    });

    $('.input_search').hover(function(){
        $('.category_frame').show("1000");
    },function(){
    });

    $('.input_search').click(function(){
        $('.input_search').animate({width:'400px'});
    });

});