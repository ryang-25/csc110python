// open as little tabs as possible.

async function openAndMark(urls) {
    chrome.runtime.onMessage.removeListener(openAndMark);
    const props = urls.map(url => { return { active: false, url } });
    let tab = await chrome.tabs.create({ active: false });
    for (const prop of props) {
        console.log(prop);
        await chrome.tabs.update(tab.id, prop, async wait => {
            const block = new Promise(resolve => {
                const listener = request => {
                    chrome.runtime.onMessage.removeListener(listener);
                    if (request === false)
                        tab = chrome.tabs.create({ active: false });
                    resolve(request);
                }
                chrome.runtime.onMessage.addListener(listener);
            });
            await block;
        });

    /*
        await chrome.scripting.executeScript({ target: { tabId: tab.id }, func: () => {
            const button = document.getElementById("completionButton");
            if (button) {
                button.click();
            }
            chrome.
        }});
        */
        // await chrome.tabs.remove(tab.id);
    }
    chrome.runtime.onMessage.addListener(openAndMark);
}

chrome.runtime.onMessage.addListener(openAndMark);
