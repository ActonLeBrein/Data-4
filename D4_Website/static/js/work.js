$(document).ready(function(){

  $(".wor_art").hover(function(){
  	$(this).find(".wor_art_hidden").show();
  	},function(){
  	$(this).find(".wor_art_hidden").hide();
  });

});