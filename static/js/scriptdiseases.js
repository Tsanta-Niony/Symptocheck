document.getElementById('openPopup').onclick =  function (){
    document.getElementById('popup').style.display = 'block';
}

document.getElementById('closePopup').onclick = function() {
    document.getElementById('popup').style.display = 'none';
}

//ferme le popup si l'utilisateur clique en dehors
window.onclick = function(event) {
    const popup = document.getElementById('popup');
    if (event.target == popup) {
        popup.style.display = 'none';
    }
}