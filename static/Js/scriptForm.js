
var cls = ["personal", "education", "contact", "profession", "about", "social"]
var index = 0
var pass = true
var next = document.querySelectorAll(".btn-success")
var back = document.querySelectorAll(".btn-danger")
var page = document.querySelector("#page")
console.log(page);
page.style.color = "white"
page.style.margin = "0"
page.style.padding = "0"
page.style.fontSize = "2rem"
page.style.fontWeight = "500"
page.style.lineHeight = "1.2"
page.style.textTransform = "capitalize"
page.style.textShadow = "0 0 10px black"

if(index == 0)
page.innerHTML = `${cls[index]}`

for(var i = 0; i < next.length; i++) {
    next[i].addEventListener("click", () => {
        var inp = document.querySelector(`.${cls[index]}`).querySelectorAll("input")
        for(var j = 0; j < inp.length; j++) {
            if(inp[j].hasAttribute("required")) {
                if(inp[j].value == "") {
                    alert("Please fill all the mandatory fields (marked with *)!")
                    pass = false
                    break
                }
                else
                pass = true
            }
        }
        if(pass == true) {
            document.querySelector(`.${cls[index]}`).classList.remove("active")
            ++index;
            document.querySelector(`.${cls[index]}`).classList.add("active")
            page.innerHTML = `${cls[index]}`
        }
    })
}

for(var i = 0; i < back.length; i++) {
    back[i].addEventListener("click", () => {
        document.querySelector(`.${cls[index]}`).classList.remove("active")
        --index;
        document.querySelector(`.${cls[index]}`).classList.add("active")
        page.innerHTML = `${cls[index]}`
    })
}