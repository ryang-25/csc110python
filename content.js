async function sendLinks() {
	const incomplete = document.querySelectorAll(".started, .notstarted");
	const links = [...incomplete].map(n => n.firstElementChild.href);
	await chrome.runtime.sendMessage(links);
}

runtime.onMessage.addEventListener(() => {
	const button = document.getElementById("completionButton");
	if (button)
		return button.click();
	return true;
});
