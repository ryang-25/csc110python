const ASSIGNMENT_URL = "https://runestone.academy/assignment/student/doAssignment";

// open as little tabs as possible.
async function openAndMark(urls) {
    console.log(urls);
    let tab = await chrome.tabs.create({ active: false });
    for (let url of urls) {
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
        let response = await chrome.tabs.sendMessage(tab.id, null);
        console.log(respone);
        if (!response)
            tab = await chrome.tabs.create({ active: false });
    }
}
 
chrome.runtime.onMessage.addListener(async (message, sender) => {
    if (Array.isArray(message))
        await openAndMark(message);
});
