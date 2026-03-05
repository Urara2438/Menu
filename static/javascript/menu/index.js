const cardNew = document.getElementById("card_new");
const cardNewSplitted = document.getElementById("card_new_splitted");
const splitNew = document.getElementById("split_new");
const splitEdit = document.getElementById("split_edit");

const cardEdit = document.getElementById("card_edit");
const cardEditSplitted = document.getElementById("card_edit_splitted");
const dishImg = document.getElementById("dish_img");

//ふやすカード
splitNew.addEventListener("mouseenter", () => {
    cardNew.classList.add("hidden");
    cardNewSplitted.style.display = "flex";
    setTimeout(() => {
        cardNewSplitted.style.opacity = "1";
    }, 150);
});

splitNew.addEventListener("mouseleave", () => {
    cardNewSplitted.style.opacity = "0";
    setTimeout(() => {
        cardNewSplitted.style.display = "none";
        cardNew.classList.remove("hidden");
    }, 200);
});


//ととのえるカード
splitEdit.addEventListener("mouseenter", () => {
    cardEdit.classList.add("hidden");
    cardEditSplitted.style.display = "flex";
    setTimeout(() => {
        cardEditSplitted.style.opacity = "1";
    }, 150);
});

splitEdit.addEventListener("mouseleave", () => {
    cardEditSplitted.style.opacity = "0";
    setTimeout(() => {
        cardEditSplitted.style.display = "none";
        cardEdit.classList.remove("hidden");
    }, 200);
});











