const cardSearch = document.getElementById("card_search")
const cardNew = document.getElementById("card_new");
const divNew = document.getElementById("divcard_new");
const splitNew = document.getElementById("split_new");
const splitEdit = document.getElementById("split_edit");

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
splitNew.addEventListener("mouseenter", () => {
    cardNew.classList.add("hidden");
    divNew.style.display = "flex";
    setTimeout(() => {
        divNew.style.opacity = "1";
    }, 150);
});

splitNew.addEventListener("mouseleave", () => {
    divNew.style.opacity = "0";
    setTimeout(() => {
        divNew.style.display = "none";
        cardNew.classList.remove("hidden");
    }, 200);
});


//ととのえるカード
splitEdit.addEventListener("mouseenter", () => {
    cardEdit.classList.add("hidden");
    divEdit.style.display = "flex";
    setTimeout(() => {
        divEdit.style.opacity = "1";
    }, 150);
});

splitEdit.addEventListener("mouseleave", () => {
    divEdit.style.opacity = "0";
    setTimeout(() => {
        divEdit.style.display = "none";
        cardEdit.classList.remove("hidden");
    }, 200);
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










