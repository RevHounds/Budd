var button = [];

$(document).ready(function(){
	buttons = $('.btn');
	$.get("/getdata", function(data) {
		ledData = $.parseJSON(data);
	    console.log(ledData);
	});
});

