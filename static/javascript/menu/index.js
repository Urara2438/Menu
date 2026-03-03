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
    divNew.style.display = "flex";
    divNew.style.justifyContent = "center";
});

cardNew.addEventListener("mouseleave", () => {
    divNew.style.display = "none";
});


//ととのえるカード
cardEdit.addEventListener("mouseenter", () => {
    divEdit.style.display = "flex";
    divEdit.style.justifyContent = "center";
});

cardEdit.addEventListener("mouseleave", () => {
    divEdit.style.display = "none";
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










