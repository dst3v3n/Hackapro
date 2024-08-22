const Eye2 = document.querySelector(".Eye2");

Eye2.addEventListener('click', function() {
    const icon = this.querySelector("i");

    if (this.nextElementSibling.type === 'password'){
        this.nextElementSibling.type = 'text' ;
        icon.classList.remove("bx-hide");
        icon.classList.add("bx-show-alt");
    } else {
        this.nextElementSibling.type = 'password'
        icon.classList.add("bx-hide");
        icon.classList.remove("bx-show-alt");
    }
})

const Eye3 = document.querySelector(".Eye3");

Eye3.addEventListener('click', function() {
    const icon = this.querySelector("i");

    if (this.nextElementSibling.type === 'password'){
        this.nextElementSibling.type = 'text' ;
        icon.classList.remove("bx-hide");
        icon.classList.add("bx-show-alt");
    } else {
        this.nextElementSibling.type = 'password'
        icon.classList.add("bx-hide");
        icon.classList.remove("bx-show-alt");
    }
})
