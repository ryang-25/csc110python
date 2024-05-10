async function clicker() {
    await mChoiceCorrect();
    await activeCode();
    return true;
}

chrome.runtime.sendMessage(true);
chrome.runtime.onMessage.addListener(clicker);
