const cardSearch = document.getElementById("card_search")
const cardNew = document.getElementById("card_new");
const divNew = document.getElementById("divcard_new");

const cardEdit = document.getElementById("card_edit");
const divEdit = document.getElementById("divcard_edit");
const dishImg = document.getElementById("dish_img");

const dishImgList = [
    "gixyouza.png",
    "nikujixyaga.png",
    "curryrice.png",
    "humburg.png",
    "yamunyomu_chiken.png",
    "omurice.png",
    "nimono.png",
];


//ふやすカード
cardNew.addEventListener("mouseenter", () => {
    cardNew.classList.add("hidden");
    divNew.style.display = "flex";
    divNew.style.justifyContent = "center";
    divNew.style.gap = "2rem";
});

cardNew.addEventListener("mouseleave", () => {
    divNew.style.display = "none";
    cardNew.classList.remove("hidden");
});


//ととのえるカード
cardEdit.addEventListener("mouseenter", () => {
    cardEdit.classList.add("hidden");
    divEdit.style.display = "flex";
    divEdit.style.justifyContent = "center";
    divEdit.style.gap = "2rem";
});

cardEdit.addEventListener("mouseleave", () => {
    divEdit.style.display = "none";
    cardEdit.classList.remove("hidden");
});


//さがすカードにランダムで料理の画像を表示させる
function getRandomDishImg() {
    randomNum = Math.floor(Math.random() * dishImgList.length);
    randomDishImg = dishImgList[randomNum];
    console.log(randomDishImg);
    dishImg.setAttribute("src", "/static/img/dish/"+randomDishImg)
}

cardSearch.addEventListener("mouseenter", () => {
    getRandomDishImg();
})

cardSearch.addEventListener("mouseleave", () => {
    getRandomDishImg();
})










