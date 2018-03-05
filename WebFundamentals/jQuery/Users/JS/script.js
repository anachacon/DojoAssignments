// JavaScript Document

$('document').ready(function(){
	"use strict";
	
	$('form').submit(function(){
		
		var firstname = $('#firstname').val();
		var lastname = $('#lastname').val();
		var email = $('#email').val();
		var contact = $('#contact').val();
		
		$('table').append("<tr><td>"+firstname+"</td><td>"+lastname+"</td><td>"+email+"</td><td>"+contact+"</td></tr>");
		
		return false;
	});
	
	
});