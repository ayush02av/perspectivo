function Redirect(url, newTab=false){
	if(newTab){
		window.open(url);
	}else{
		window.location = url;
	}
}

$("span#home-link").click(function(){
	Redirect("/?view-home=true");
});

$("#left_navigation_bar_content > ul > li").click(function(){
	Redirect("/#"+this.id);
});