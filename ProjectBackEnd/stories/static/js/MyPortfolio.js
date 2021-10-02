let activeLangs=document.querySelectorAll(".active-lang")
let langs=document.querySelectorAll(".lang")
let langBox=document.querySelector(".lang-box")
let languages=document.querySelector(".languages")





languages.addEventListener("click",()=>{
    langBox.classList.toggle("")
})


for(let i=0;i<langs.length;i++){
    langs[i].addEventListener("click",()=>{
        for(let i=0;i<langs.length;i++){
            langs[i].style.display="block"
            activeLangs[i].style.display="none"
        }

        langs[i].style.display="none"
        activeLangs[i].style.display="block"
    })
}


