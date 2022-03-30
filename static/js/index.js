let copyText = document.getElementById("new_url")
let copy_link = document.getElementById("copy_link")
function copyLink(){
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value)
}
copy_link.addEventListener("click", copyLink())
