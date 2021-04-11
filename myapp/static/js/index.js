const form = document.getElementById('myform');

form.addEventListener('submit', function (event) {
  if (!confirm('送信しますか？')) {
    event.preventDefault();
  }
});