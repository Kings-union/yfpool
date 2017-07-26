$(document).ready(function($){
    $('#myCarousel').carousel({
        interval: 4000,
        pause: null
    });

    $('.input_search').focus(function(){
        $('.input_search').animate({width:'600px'});
    });
    $('.input_search').blur(function(){
        $('.input_search').animate({width:'400px'});
    });

//    $('.input_search').click(function(){
//        $('.input_search').animate({width:'400px'});
//    });

});