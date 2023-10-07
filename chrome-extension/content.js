chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'print') {
      window.print();
    }
});
