// the goal is to just call the api eventually

function bookEvent(div_id, answer) {
    let body = {
        // multiple choice
        event: "mChoice",
        act: `answer:${answer}:correct`,
        answer,
        correct: "T",
        div_id,
        course_name: "CSC110PythonASY2324",
        clientLoginStatus: true,
        timezoneoffset: 4,
        percent: 1
    };
    let options = {
        body: JSON.stringify(body),
        headers: {
            Accept: "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json; charset=utf-8",
        },
        method: "POST"
    };
    return fetch("https://runestone.academy/ns/logger/bookevent", options);
}

// given an answer list element, find the right answer and submit
function solveAnswer(answer_list) {
    let answer = "";
    for (let i = 0; i < answer_list.children.length; i++)
        if (answer.getAttribute("data-correct"))
            answer = String(i);
    return bookEvent(answer_list.id, answer)
}

function submitCode(div_id) {
    let body = {
        clientLoginStatus: true,
        code: "",
        course_name: "CSC110PythonASY2324",
        div_id,
        errinfo: "success",
        language: "python",
        partner: "",
        prefix: "",
        timezoneoffset: 4,
        to_save: "False"
    };
    let options = {
        body: JSON.stringify(body),
        headers: {
            Accept: "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json; charset=utf-8",
        },
        method: "POST"
    };
    return fetch("https://runestone.academy/ns/logger/runlog", options)
}

function test() {
    // get opt_a from id 
    let answers = [...document.querySelectorAll("[data-correct='yes']")].map(node => [node.parentElement.id, ]);


    let active_id = [...document.querySelectorAll('[data-component="activecode"]')].map(node => node.id);


}



// i think this is still a little bit broken but i'm not sure why, will have to
// figure out next time I get an assignment...
function clicker(number) {
    let [enabled,] = [...document.getElementsByClassName("run-button")]
        .reduce(([enabled, disabled], button) => {
            if (button.disabled)
                disabled.push(button);
            else
                enabled.push(button);
            return [enabled, disabled]
        });

    let run_buttons = [...document.getElementsByClassName("run-button")]
        .filter(button => !button.disabled);
    for (let button of buttons)
        button.click();



    let progress = document.getElementById("scprogresstotal");
    for (let i = 0; i < run_buttons.length &&
        Number(progress.innerText) < number; i++) {
        run_buttons[i].disabled = false;
        run_buttons[i].click();
    }
    if (Number(progress.innerText) < number)
        return false;
    document.getElementById("completionButton")?.click()
    return true;
}
 
// minimal impact?
chrome.runtime.sendMessage(null);
chrome.runtime.onMessage.addListener(clicker);
