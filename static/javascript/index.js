
const newBtnArea = document.getElementById("newBtnArea")
const newBtn = document.getElementById("newBtn");
const newBtnAreaClicked = document.getElementById("newBtnAreaClicked")

newBtn.addEventListener("click", function () {
    newBtn.classList.toggle("hidden");
    newBtnAreaClicked.classList.toggle("hidden");
    newBtnArea.classList.toggle("transparent");
});

const editBtnArea = document.getElementById("editBtnArea")
const editBtn = document.getElementById("editBtn");
const editBtnAreaClicked = document.getElementById("editBtnAreaClicked")

editBtn.addEventListener("click", function () {
    editBtn.classList.toggle("hidden");
    editBtnAreaClicked.classList.toggle("hidden");
    editBtnArea.classList.toggle("transparent");
});


