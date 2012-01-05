$(document).ready(function(){

    $('.homebox-wrapper.slide ul.slide-controls').tabs('div.subcontent', {
        // enable "cross-fading" effect
        effect: 'fade',
        fadeInSpeed: 500,
        fadeOutSpeed: 500,

        // start from the beginning after the last tab
        rotate: true,

    // use the slideshow plugin. It accepts its own configuration
    }).slideshow({
        autoplay: true,
        interval: 6000,
    });

});