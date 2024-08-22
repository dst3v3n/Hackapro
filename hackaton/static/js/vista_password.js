const Eye = document.querySelector(".Eye");

Eye.addEventListener('click', function() {
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

const Eye1 = document.querySelector(".Eye1");

Eye1.addEventListener('click', function() {
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
