// open as little tabs as possible.

async function openAndMark(urls) {
	const props = urls.map(u => { active: false, url });
	let tab = await chrome.tabs.create({ active: false });
	for (const prop in props) {
		await chrome.tabs.update(tab.id, prop);
		const resp = await chrome.tabs.sendMessage(tab.id, null);
		if (resp === true)
			tab = await chrome.tabs.create(prop);
	}
}

chrome.runtime.onMessage.addListener((urls) => {
	openAndMark(urls);
});

