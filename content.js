async function sendLinks() {
	const incomplete = document.querySelectorAll(".started, .notstarted");
	window.alert(incomplete);
	const links = [...incomplete].filter(n => n.firstElementChild).map(n => n.firstElementChild.href);
	await chrome.runtime.sendMessage(links);
}

chrome.runtime.onMessage.addListener(() => {
	const button = document.getElementById("completionButton");
	if (button)
		return button.click();
	return true;
});

document.getElementById("assignment_name").onclick = sendLinks;