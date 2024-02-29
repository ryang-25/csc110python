function sendLinks() {
	const incomplete = document.querySelectorAll(".started, .notstarted");
	const links = [...incomplete].map(n => n.firstChild.href);
	chrome.runtime.sendMessage(links);
}

function openAndMark(url) {
	const properties = {
		active: false,
		url
	};
	const tab = await chrome.tabs.create(properties);

}


function markDone() {
	document.getElementById("completionButton").click();
}


window.addEventListener("DOMContentLoaded", () => {

});


runtime.onMessage("click", () => {
	
}) 