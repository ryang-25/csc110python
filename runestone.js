// open as little tabs as possible.
 
async function openAndMark(activities) {
    let tab = await chrome.tabs.create({ active: false });
    for (let [url, number] of activities) {
        let property = { active : false, url };
        tab = await chrome.tabs.update(tab.id, property);
        // the epitome of js async
        await new Promise(resolve => {
            let listen = (_, sender) => {
                if (sender.tab.id === tab.id) {
                    chrome.runtime.onMessage.removeListener(listen);
                    resolve(null);
                }
            };
            chrome.runtime.onMessage.addListener(listen);
        });
        let response = await chrome.tabs.sendMessage(tab.id, number);
        if (!response)
            tab = await chrome.tabs.create({ active: false });
    }
    return true;
}
 
chrome.runtime.onMessage.addListener(async message => {
    if (Array.isArray(message))
        await openAndMark(message);
});
