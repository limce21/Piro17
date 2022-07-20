function plusInterest(id) {
  state = document.getElementById(id).innerText;
  document.getElementById(id).innerText = ++state;

  console.log(id);
  $.ajax({
    url: "/",
    type: "POST",
    data: {
      id: id,
      interest: state,
    },
    success: function (data) {
      console.log("성공!");
    },
    error: function () {
      console.log("ERROR");
    },
  });
}

function minusInterest(id) {
  state = document.getElementById(id).innerText;
  document.getElementById(id).innerText = --state;

  console.log(id);
  $.ajax({
    url: "/",
    type: "POST",
    data: {
      id: id,
      interest: state,
    },
    success: function (data) {
      console.log("성공!");
    },
    error: function () {
      console.log("ERROR");
    },
  });
}
