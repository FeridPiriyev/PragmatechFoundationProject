let item=document.querySelector('.alert')
let lampStatus=true
item.addEventListener('click',function(){
    if(lampStatus){
        document.querySelector('.item p').style.display='none'
        // document.querySelector('item').querySelector('.alert').querySelector('i')
        document.querySelector('.item .alert i').className='bi bi-arrow-up'
        lampStatus=false
    }else{
        document.querySelector('.item p').style.display='block'
        document.querySelector('.item .alert i').className='bi bi-arrow-down'
        lampStatus=true
    }

})