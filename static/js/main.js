var modal = document.getElementById("myModal");

function openModal() {
    modal.style.display = "block";
}

function closeModal() {
    modal.style.display = "none";
}

function generateReport() {
    var dollar = document.querySelector("#dollar").checked
    var inflation = document.querySelector("#inflation").checked
    var interest = document.querySelector("#interest").checked
    var stock_market = document.querySelector("#stock_market").checked
    var crypto = document.querySelector("#crypto").checked

    var redirect = "/report?dollar=" + dollar + "&inflation=" + inflation + "&interest=" + interest + "&stock_market=" + stock_market + "&crypto=" + crypto

    window.location.assign(redirect)

    closeModal();
}