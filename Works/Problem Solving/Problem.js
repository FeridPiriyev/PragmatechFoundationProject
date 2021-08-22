function openModal(){
    document.querySelector('.ks-overlay').style.display='block'
    document.querySelector('.ks-modal-content').style.top='50%'
}

function hideModal(){
    document.querySelector('.ks-overlay').style.display='none'
}

function findElement(e){
    console.log(e.target)
}