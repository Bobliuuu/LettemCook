chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'displayMessage') {
      console.log(request.message); 
      alert(request.message); 
    }
  });
  