async function sendLinks() {
    const incomplete = document.querySelectorAll(".started, .notstarted");
    const links = [...incomplete].filter(n => n.firstElementChild)
        .map(n => n.firstElementChild.href);
    await chrome.runtime.sendMessage(links);
}

document.getElementById("assignment_name").onclick = sendLinks;

