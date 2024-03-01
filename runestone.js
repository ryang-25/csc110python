// open as little tabs as possible.

async function openAndMark(urls) {
	const props = urls.map(u => { active: false, url });
	let tab = await chrome.tabs.create(prop);
	for prop in props {
		const resp = await chrome.tabs.sendMessage(tab.id, null);
		if (resp === true)
			tab = chrome.tabs.create(prop);
	}
}

runtime.onMessage.addEventListener((urls) => {
	openAndMark(urls).then(());
});
