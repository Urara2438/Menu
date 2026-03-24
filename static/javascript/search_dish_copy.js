const dishSearchInput = document.getElementById("dishSearchInput");
const searchResult = document.getElementById("searchResult");
const dishLinks = document.querySelectorAll("#dishContainer a");

dishSearchInput.addEventListener("focus", function () {
    searchResult.classList.remove("hidden");
});

dishSearchInput.addEventListener("input", function () {
    const keyword = dishSearchInput.value.trim();
    searchResult.innerHTML = "";

    if (keyword === "") {
        searchResult.textContent = "ここに検索結果が表示されます";
        return;
    }

    const matchedDishes = [];

    dishLinks.forEach(function (dishLink) {
        const dishName = dishLink.textContent;

        if (dishName.includes(keyword)) {
            matchedDishes.push({
                name: dishName,
                href: dishLink.href
            });
        }
    });

    if (matchedDishes.length === 0) {
        searchResult.textContent = "該当する料理はありません";
        return;
    }

    matchedDishes.forEach(function (dish) {
        const resultLink = document.createElement("a");
        resultLink.textContent = dish.name;
        resultLink.href = dish.href;
        searchResult.appendChild(resultLink);
    });
});

