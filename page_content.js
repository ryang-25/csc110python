const button = document.getElementById("completionButton");
if (button)
    button.click();
chrome.runtime.sendMessage(!!button);
