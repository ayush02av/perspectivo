const glimpses_container = document.querySelector('#glimpse .inner-section');

class Glimpse{
    constructor(glimpse){
        this.id = "/" + glimpse.ByUser + "/" + glimpse.Title;
        this.glimpse = document.createElement('div');
        this.glimpse.className = 'work-card';
        this.glimpse.id = this.id;
        this.glimpse.innerHTML = '<h3 style="font-weight: 500; color: var(--primary-2);">' + glimpse.Title + '</h3><small><small style="font-weight: 300; color: var(--primary-2)">By : <i>' + glimpse.ByUser.username + '</i><br>Rating : <i>' + glimpse.Rating + '</i></small></small><br><br><p style="font-weight: 300;"><small>' + glimpse.MainLiner + '<small><i>...read more</i></small></small></p>';
        this.glimpse.onclick = () => Redirect(this.id, true);
        glimpses_container.appendChild(this.glimpse);
    }
}

$.get( "/api/glimpses", function( data ) {
    document.getElementById('glimpses-length').innerHTML = data.length;
    for(i=0; i<data.length; i++){
        new Glimpse(data[i]);
    }
});
