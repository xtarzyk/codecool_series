let modalBtn = document.getElementById("filter-rating");
let modal = document.querySelector(".modal");
let closeBtn = document.querySelector(".close-btn");
let ratingValue = document.getElementById("filter").value
let saveRating = document.getElementById("save");


saveRating.onclick = function () {
    console.log(ratingValue)
}

modalBtn.onclick = function(){
  modal.style.display = "block"
}

closeBtn.onclick = function(){
  modal.style.display = "none"
}

window.onclick = function(e){
  if(e.target == modal){
    modal.style.display = "none"
  }
}