let copyText = document.getElementById("new_url")

function myFunction() {
  navigator.clipboard.writeText(copyText.value);
}
