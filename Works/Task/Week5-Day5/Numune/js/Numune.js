let btn=document.querySelector('.btn')
let initialWidth=200;
let initialMargin=10;
let count=1;
btn.addEventListener('click',function(){
    let box=document.createElement('div')
    box.className='box'
    box.style.width=`${initialWidth}px`
    box.style.marginRight=`${initialMargin}px`
    box.innerHTML=count
    initialWidth+=20
    initialMargin+=10
    count++
    box.addEventListener('click',function(){
        document.querySelector('.boxContainer').removeChild(this)
    })
    document.querySelector('.boxContainer').appendChild(box)

})