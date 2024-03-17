async function sendActivities() {
    let incomplete = document.querySelectorAll(".started, .notstarted");
    let matchActivity = node => {
        let regex = /(\d+) activities/;
        // first match group
        return Number(node.innerText.match(regex)[1]);
    }
    let activities = [...incomplete].filter(n => n.firstElementChild)
        .map(n => [n.firstElementChild.href, matchActivity(n)]);
    await chrome.runtime.sendMessage(activities);
    // reload when we're done.
    let grade = document.getElementById("gradeMeButton");
    grade.click();
    location.reload();
}
 
document.getElementById("assignment_name").onclick = sendActivities;
