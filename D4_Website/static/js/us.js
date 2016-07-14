$(document).ready(function(){

  $(".twitter").hover(function(){
    $(this).attr("src","/static/img/TWITTER_b.png");
    },function(){
    $(this).attr("src","/static/img/TWITTER.png ");
  });

  $(".skype").hover(function(){
    $(this).attr("src","/static/img/SKYPE_b.png");
    },function(){
    $(this).attr("src","/static/img/SKYPE.png");
  });

  $(".linkedin").hover(function(){
    $(this).attr("src","/static/img/LINKEDIN_b.png");
    },function(){
    $(this).attr("src","/static/img/LINKEDIN.png");
  });

  $(".img-circle").hover(function(){
  	$(this).parents("div:first").find(".info").show();
  	},function(){
  	$(this).parents("div:first").find(".info").hide();
  });

});