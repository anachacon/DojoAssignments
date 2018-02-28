// JavaScript Document

$(document).ready(function(){
	"use strict";
	$('img').click(function(){
			var temp =  $(this).attr("src");
			$(this).attr("src",$(this).attr('data-alt-src'));
			$(this).attr("data-alt-src",temp);
	 });
});