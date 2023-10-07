document.getElementById('printButton').addEventListener('click', function () {
    chrome.runtime.sendMessage({ action: 'displayMessage', message: 'I AM GOD' });
});
  