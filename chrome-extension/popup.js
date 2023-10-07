chrome.tabs.query({}, function(tabs) {
    let tabList = document.getElementById("tabList");
    tabs.forEach(function(tab) {
        let li = document.createElement("li");
        li.textContent = tab.title;
        tabList.appendChild(li);
    });
});
