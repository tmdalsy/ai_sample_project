// 초보자 수업용으로 흐름이 잘 보이도록
// 1) 폼 제출을 감지하고
// 2) 이름 입력값을 검사한 뒤
// 3) 결과 메시지를 화면에 보여줍니다.

const form = document.getElementById("nameForm");
const nameInput = document.getElementById("nameInput");
const messageBox = document.getElementById("messageBox");

function showMessage(type, text) {
  // 이전 상태를 지우고 새 상태만 보여줍니다.
  messageBox.className = `message-box ${type}`;
  messageBox.textContent = text;
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // 앞뒤 공백을 제거한 뒤 실제 이름이 있는지 확인합니다.
  const name = nameInput.value.trim();

  if (name) {
    showMessage("success", `${name}님, 환영합니다! AI 협업 개발 실습을 시작합니다.`);
    return;
  }

  showMessage("warning", "이름을 먼저 입력해주세요.");
});
