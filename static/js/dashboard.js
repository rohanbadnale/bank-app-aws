const eye = document.getElementById("toggleBalance");
const balance = document.getElementById("balanceAmount");

let visible = true;

eye.addEventListener("click", () => {

    if (visible) {

        balance.innerHTML = "₹ ******";

        eye.classList.remove("bi-eye-fill");
        eye.classList.add("bi-eye-slash-fill");

    } else {

        balance.innerHTML = "₹50,000.00";

        eye.classList.remove("bi-eye-slash-fill");
        eye.classList.add("bi-eye-fill");

    }

    visible = !visible;

});
const card = document.getElementById("bankCard");

if(card){

    card.addEventListener("click", ()=>{

        card.classList.toggle("flipped");

    });

}