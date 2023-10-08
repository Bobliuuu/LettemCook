const apiKey = '[redact]';

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs){
    let tabList = document.getElementById("tabList");
    tabs.forEach(async function(tab) {
        var activeTabId = tab.title;
        await fetch(
            `https://api.openai.com/v1/completions`,
            {
                body: JSON.stringify({"model": "text-davinci-003", "prompt": `Given this text, return whether it is related or not to linear algebra. It is related to linear algebra if it has the word LINEAR ALGEBRA in the title. Only return yes or no. Do not return anything else other than yes or no.\n${activeTabId}`, "temperature": 0, "max_tokens": 512}),
                method: "POST",
                headers: {
                    "content-type": "application/json",
                    Authorization: "Bearer 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",
                },
                    }
        ).then((response) => {
            if (response.ok) {
                response.json().then((json) => {
                    if (json['choices'][0]['text'].toLowerCase().includes("no")) {
                        chrome.tabs.remove(tabs[0].id);
                    }
                });
            }
        }); 
    })
    //
});
