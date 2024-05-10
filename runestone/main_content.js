/*
 * Main content script that runs at page load.
 */

async function sendActivities() {
    let incomplete = [...document.querySelectorAll(".completed, .started, .notstarted")]
        .filter(n => n.lastChild.textContent.startsWith("0.0"))
        .map(n => n.firstElementChild.href);
    await chrome.runtime.sendMessage(incomplete);
}

document.getElementById("assignment_name").onclick = sendActivities;
