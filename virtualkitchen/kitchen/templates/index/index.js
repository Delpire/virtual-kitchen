$(document).ready(function() {

	$("#about-button").mouseover( function() {
		$("#about-bar").css("background-color", "#FFFFBB");
		$('html,body').css('cursor','pointer');
	});

	$("#about-button").mouseout( function() {
		$("#about-bar").css("background-color", "#0099FF");
		$('html,body').css('cursor','default');
	});

	$("#sign-in-button").mouseover( function() {
		$("#sign-in-bar").css("background-color", "#FFFFBB");
		$('html,body').css('cursor','pointer');
	});

	$("#sign-in-button").mouseout( function() {
		$("#sign-in-bar").css("background-color", "#0099FF");
		$('html,body').css('cursor','default');
	});

});