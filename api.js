const 

function options(body) {
    return {
        body: JSON.stringify(body),
        headers: {
            Accept: "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json; charset=utf-8",
        },
        method: "POST"
    };
}

// Sends the actual event to answer the questions.
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
    return fetch("https://runestone.academy/ns/logger/bookevent",
        options(body));
}

func runlog(div_id) {
    let body = {
        code: "",
        course: "CSC110PythonASY2324"
    }
}


document.querySelectorAll('textarea:not([visibility="hidden"])')

/*)
clientLoginStatus: true

code: "import random↵import turtle↵↵↵def isInScreen(w, t):↵    if random.random() > 0.1:↵        return True↵    else:↵        return False↵↵↵t …"

course: "CSC110PythonASY2324"

div_id: "iter_randwalk1"

errinfo: "success"

language: "python"

partner: ""

prefix: ""

timezoneoffset: 4

to_save: "False"
*/

/*
*/

function answerToNum(node) {
    let letter = node.id.at(-1);
    return letter.charCodeAt(0) - "a".charCodeAt(0);
}

export async function bookCorrect() {
    let nodes = document.querySelectorAll('ul[data-component="multiplechoice"]');
    for (let node of nodes.values()) {
        let answers = [...node.querySelectorAll("[data-correct]")]
            .map(answerToNum);
        await bookEvent(node.id, answers.toString());
    }
}

