let sec = 0;
let milisec = 0;
let intervalID;

const startBtn = document.querySelector(".startBtn");
const stopBtn = document.querySelector(".stopBtn");
const resetBtn = document.querySelector(".resetBtn");

const secText = document.querySelector(".sec");
const milisecText = document.querySelector(".milisec");

const unordered = document.getElementById("record-list-ul");

const allBtn = document.querySelector(".checkBtn-first");
const delBtn = document.getElementById("delBtn");

function fillZero(num) {
   return String(num).padStart(2, "0");
}

startBtn.addEventListener("click", () => {
   startBtn.disabled = true;
   intervalID = setInterval(function () {
      milisecText.innerText = fillZero(++milisec);
      if (milisec % 100 == 0) {
         secText.innerText = fillZero(++sec);
         milisec = 0;
         milisecText.innerText = fillZero(milisec);
      }
   }, 10); // 1000ms가 1초
});

stopBtn.addEventListener("click", function () {
   startBtn.disabled = false;
   clearInterval(intervalID);
   let li_argument = document.createElement("li");
   let sel_btn = document.createElement("button");
   sel_btn.value = "0";
   let record_st = document.createElement("div");
   let del_btn = document.createElement("button"); // flex 맞추기용
   record_st.innerText = fillZero(sec) + " : " + fillZero(milisec);
   sel_btn.classList.add("checkBtn");
   li_argument.appendChild(sel_btn);
   li_argument.appendChild(record_st);
   li_argument.appendChild(del_btn);
   unordered.appendChild(li_argument);
});

resetBtn.addEventListener("click", () => {
   startBtn.disabled = false;
   clearInterval(intervalID);
   sec = 0;
   milisec = 0;
   secText.innerText = fillZero(sec);
   milisecText.innerText = fillZero(milisec);
});

delBtn.addEventListener("click", () => {
   let delLists = document.querySelectorAll('[value="checked"]');
   delLists.forEach((e) => {
      let pN = e.parentNode;
      pN.remove();
   });
   allBtn.style.backgroundColor = "white";
   allBtn.value = "0";
});

allBtn.addEventListener("click", () => {
   if (allBtn.value == "0") {
      allBtn.value = "check";
      allBtn.style.backgroundColor = "rgb(169, 202, 255)";
      let selLists = document.querySelectorAll(".checkBtn");
      selLists.forEach((e) => {
         e.value = "checked";
         e.style.backgroundColor = "rgb(169, 202, 255)";
      });
   } else {
      let selLists = document.querySelectorAll(".checkBtn");
      selLists.forEach((e) => {
         e.value = "0";
         e.style.backgroundColor = "white";
      });
      allBtn.value = "0";
      allBtn.style.backgroundColor = "white";
   }
});

function hasClass(elem, className) {
   return elem.className.split(" ").indexOf(className) > -1;
}

document.addEventListener(
   "click",
   function (e) {
      if (hasClass(e.target, "checkBtn")) {
         if (e.target.value == "0") {
            e.target.style.transition = "0.5s";
            e.target.style.backgroundColor = "rgb(169, 202, 255)";
            e.target.value = "checked";
         } else {
            e.target.style.backgroundColor = "white";
            e.target.value = "0";
         }
      } else if (hasClass(e.target, "test")) {
         // .test clicked
         // Do your other thing
      }
   },
   false
);
