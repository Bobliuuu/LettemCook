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

const apiKey = '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';

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs){
    let tabList = document.getElementById("tabList");
    tabs.forEach(function(tab) {
        var activeTabId = tab.id;
        let executeScriptPromise = new Promise((resolve, reject) => {
            chrome.scripting.executeScript({
                target: { tabId: activeTabId },
                injectImmediately: true,
                func: DOMtoString,
            }, (results) => {
                if (chrome.runtime.lastError) {
                    reject(new Error(chrome.runtime.lastError));
                } else {
                    resolve(results);
                }
            });
        });

        executeScriptPromises.push(executeScriptPromise);

        Promise.all(executeScriptPromises)
        .then((resultsArray) => {
            // Append each result to tabList
            resultsArray.forEach((results) => {
                tabList.appendChild(document.createTextNode(results));
            });
        })
        .catch((error) => {
            tabList.appendChild(document.createTextNode(error.message));
        });
    })
    //chrome.tabs.remove(tabs[0].id);
});
