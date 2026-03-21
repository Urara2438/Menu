const dishSearchInput = document.getElementById("dishSearchInput");
const searchResult = document.getElementById("searchResult");
const dishLinks = document.querySelectorAll("#dishContainer a");

dishSearchInput.addEventListener("input", function () {
    const keyword = dishSearchInput.value.trim();
    searchResult.innerHTML = "";

    if (keyword === "") {
        return;
    }

    let matchCount = 0;

    dishLinks.forEach(function (dishLink) {
        const dishName = dishLink.textContent.trim();

        if (dishName.includes(keyword)) {
            const resultLink = document.createElement("a");
            resultLink.textContent = dishName;
            resultLink.href = dishLink.href;
            resultLink.classList.add("searchResultItem");
            searchResult.appendChild(resultLink);
            matchCount++;
        }
    });

    if (matchCount === 0) {
        searchResult.textContent = "該当する料理はありません";
    }
});
