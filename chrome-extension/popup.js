chrome.tabs.query({}, function(tabs) {
    let tabList = document.getElementById("tabList");
    tabs.forEach(function(tab) {
        let li = document.createElement("li");
        li.textContent = tab.title;
        tabList.appendChild(li);
    });
});

chrome.tabs.query({ active: true, lastFocusedWindow: true }, function(tabs) {
  let tabList = document.getElementById("tabList");
  tabs.forEach(function(tab) {
      let li = document.createElement("li");
      li.textContent = tab.title;
      tabList.appendChild(li);
  });
});

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs){
    chrome.tabs.remove(tabs[0].id);
});
