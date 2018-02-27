// JavaScript Document

$(document).ready(function(){
	"use strict";
	
	for (var i=0; i<8; ++i){
		$('article').append('<img src="images/totoro.jpg" alt="totoro" class="totoro">');
	}
	
	 $('.totoro').click(function(){
    	$(this).css('visibility','hidden');
	 });
	
	
	$('.restore').click(function(){
    	$('.totoro').css('visibility','visible');
	 });
});