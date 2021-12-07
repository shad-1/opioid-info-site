const spinnerbox = document.getElementById("spinner-box")

$.ajax({
    type: 'GET',
    url: 'details/',
    success: function(response){
        spinnerbox.classList.add('not-visible')
    }
})