function copyLink() {
    var copyText = document.getElementById();
    copyText.select();
    copyText.setSelectionRange(0, 1000)
    document.execCommand("copy");
    alert("Copied the text: " + copyText.value);
  }