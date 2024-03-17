// i think this is still a little bit broken but i'm not sure why, will have to
// figure out next time I get an assignment...
function clicker(number) {
    let run_buttons = document.getElementsByClassName("run-button");
    let progress = document.getElementById("scprogresstotal");
    for (let i = 0; i < run_buttons.length &&
        Number(progress.innerText) < number; i++) {
        run_buttons[i].disabled = false;
        run_buttons[i].click();
    }
    if (Number(progress.innerText) < number)
        return false;
    let completed = document.getElementById("completionButton");
    if (completed)
        completed.click();
    return true;
}
 
// minimal impact?
chrome.runtime.sendMessage(null);
chrome.runtime.onMessage.addListener(clicker);
