const loginForm = document.getElementById("loginForm");
const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");

togglePassword.addEventListener("click", () => {
  const isHidden = passwordInput.type === "password";
  passwordInput.type = isHidden ? "text" : "password";
  togglePassword.textContent = isHidden ? "visibility_off" : "visibility";
});

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = passwordInput.value.trim();
  const remember = document.getElementById("remember").checked;

  if (!email || !password) {
    alert("Vui lòng nhập đầy đủ email và mật khẩu.");
    return;
  }

  console.log("Thông tin đăng nhập:", {
    email,
    password,
    remember
  });

  alert("Đăng nhập thành công!");
});