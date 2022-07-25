console.log("djklaf");
// 1. JavaScript

const wow = () => {
  console.log(wow);
};

const requestLike = new XMLHttpRequest();
const onClickLike = (isClicked) => {
  const url = "/like_post/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  if (isClicked === 1) requestLike.send(JSON.stringify({ isClicked: true }));
  else requestLike.send(JSON.stringify({ isClicked: false }));
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    const { isClicked } = JSON.parse(requestLike.response);
    const element = document.querySelector(".like");
    if (isClicked === true) {
      element.innerHTML = (
        <button class="likeBtn" onclick="onClickLike(1);">
          <i class="fa-solid fa-heart"></i>
        </button>
      );
    } else {
      element.innerHTML = (
        <button class="likeBtn" onclick="onClickLike(0);">
          <i class="fa-regular fa-heart"></i>
        </button>
      );
    }
  }
};
