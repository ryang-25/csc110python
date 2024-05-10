/*
 * API surface.
 */

const COURSE_NAME = "CSC110PythonASY2324";

// fetch wrapper with appropriate headers.
function fetch_options(url, body) {
    return fetch(url, {
        body: JSON.stringify(body),
        headers: {
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json; charset=utf-8"
        },
        method: "POST"
    })
}

function bookEvent(div_id, event) {
    let common = {
        clientLoginStatus: true,
        course_name: COURSE_NAME,
        div_id,
        timezoneoffset: 4
    }
    console.log({...common, ...event});
    return fetch_options("https://runestone.academy/ns/logger/bookevent",
        {...common, ...event})
}

function mChoice(div_id, answer) {
    return bookEvent(div_id, {
        answer,
        act: `answer:${answer}:correct`,
        correct: "T",
        event: "mChoice",
        percent: 1
    });
}

function codeLens(div_id) {
    return bookEvent(div_id, {
        act: "fwd",
        event: "codelens"
    });
}

// runlog / button clicker
function runLog(div_id) {
    return fetch_options("https://runestone.academy/ns/logger/runlog", {
        clientLoginStatus: true,
        code: "",
        course: COURSE_NAME,
        div_id,
        errinfo: "success",
        language: "python",
        partner: "",
        prefix: "",
        timezoneoffset: 4,
        to_save: "False"
    })
}

function answerToNum(node) {
    let letter = node.id.at(-1);
    return letter.charCodeAt(0) - "a".charCodeAt(0);
}

// clicks all correct multiple choice.
async function mChoiceCorrect() {
    let nodes = document.querySelectorAll('ul[data-component="multiplechoice"]');
    for (let node of nodes.values()) {
        let answers = [...node.querySelectorAll("[data-correct]")]
            .map(answerToNum);
        // window.alert(answers);
        await mChoice(node.id, answers.toString());
    }
}

// clicks all activecode boxes.
async function activeCode() {
    let nodes = document.querySelectorAll('[data-component="activecode"]');
    for (let node of nodes.values()) {
        await runLog(node.id);
    }
}
