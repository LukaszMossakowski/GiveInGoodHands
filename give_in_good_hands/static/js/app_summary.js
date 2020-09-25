let summary1 = document.querySelector("#summary1")
let summary2 = document.querySelector("#summary2")
let summary3 = document.querySelector("#summary3")
let button = document.querySelector("#last_button")
let quantity = document.querySelector("#quantity")
let institution = document.querySelector("#institution")
let street = document.querySelector("#street")
let city = document.querySelector("#city")
let postCode = document.querySelector("#post_code")
let phone = document.querySelector("#phone")
let date = document.querySelector("#date")
let time = document.querySelector("#time")
let comment = document.querySelector("#comment")

function clearValues() {
    quantity.value = ""
    institution.value = ""
    street.value = ""
    city.value = ""
    postCode.value = ""
    phone.value = ""
    date.value = ""
    time.value = ""
    comment.value = ""
}

button.addEventListener("click", function () {
    list_of_errors = []

    if (list_of_errors.length > 0) {
        alert("Wystąpił błąd!")
        return false
    }
    else {
        let part1 = document.createElement("ul");
        part1.innerHTML = `<li><span class="icon icon-bag"></span><span class="summary--text">${quantity.value} worki</span></li>
<li><span class="icon icon-hand"></span><span class="summary--text">Dla fundacji: ${institution.textContent}</span></li>`;
        summary1.appendChild(part1);

        let part2 = document.createElement("ul");
        part2.innerHTML = `<li>${street.value}</li>
                        <li>${city.value}</li>
                        <li>${postCode.value}</li>
                        <li>${phone.value}</li>`;
        summary2.appendChild(part2);

        let part3 = document.createElement("ul");
        part3.innerHTML = `<li>${date.value}</li>
                        <li>${time.value}</li>
                        <li>${comment.value}</li>`;
        summary3.appendChild(part3);
    }
})
