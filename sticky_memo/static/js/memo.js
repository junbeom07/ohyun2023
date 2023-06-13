// DOM 요소
const $modalWrap = document.querySelector(".modal-wrap");
const $newBtn = document.querySelector(".new-btn");
const $open = document.querySelector(".open-btn");
const $close = document.querySelector(".close-btn");
const $deleteBtn = document.querySelector(".delete-btn");
const $title = document.querySelector(".title");

$title.classList.add("change-color");

const remove = () => {
  $modalWrap.classList.remove("hidden");
};

// .new-btn 클릭시, .modal-wrap의 hidden 클래스 없애기
$newBtn.addEventListener("click", () => {
  remove();
});

// .close-btn 클릭시, .modal-wrap에 hidden 클래스 추가
// 힌트) remove대신 add 사용하기
$close.addEventListener("click", () => {
  $modalWrap.classList.add("hidden");
});

// .open-btn 클릭시, .modal-wrap의 hidden 클래스 없애기
$open.addEventListener("click", () => {
  remove();
});

// .delete-btn 클릭시, 삭제 여부 물어보는 창 띄워주기
$deleteBtn.addEventListener("click", () => {
  confirm("정말 삭제하실건가요?");
});
