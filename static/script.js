$(document).ready(function(){
	$.get("/getdata", function(data) {
	    console.log($.parseJSON(data))
	});
})