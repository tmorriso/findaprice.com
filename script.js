

//prompt("What is your name?");


//jquery stuff
//$(document).ready(function('div'){
//    .slideDown('slow')

//});

// java function outline
var main = function() {
	// Select a class with jquery (login menu)
	$('.icon-menu').click(function() {
        $('.menu').animate({
            left: '0px'
        }, 200);
	    $('body').animate({
    	    left: '285px'
        }, 200);

	});
};
    


// jquery to run the function as soon as the HTML document has loaded
$(document).ready(main);