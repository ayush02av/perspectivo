function Redirect(url){
	window.location = url;
}

$("span#home-link").click(function(){
	Redirect("/");
});

$("#left_navigation_bar_content > ul > li").click(function(){
	Redirect("/#"+this.id);
});