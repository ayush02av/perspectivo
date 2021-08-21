function ToggleReviewForm(){
	var review_form = document.getElementById('review-box');

	if (review_form.style.display != "block"){
		review_form.style.display = "block";
	}else{
		review_form.style.display = "none";
	}
}