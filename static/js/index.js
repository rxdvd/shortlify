function myFunction() {
  let copyText = document.getElementById("new_url")
  navigator.clipboard.writeText(copyText.textContent);
  alert("Copied the text: " + copyText.textContent);
}

const newURL = document.querySelector("#new_url");
if(newURL) newURL.textContent = `http://${window.location.host}/${newURL.textContent}`;
