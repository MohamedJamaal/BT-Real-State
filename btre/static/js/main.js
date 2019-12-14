const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// This for message alert 
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);