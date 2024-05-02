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

function answerToNum(node) {
    let letter = node.id.at(-1);
    return letter.charCodeAt(0) - "a".charCodeAt(0);
}

async function gatherCorrect() {
    let nodes = [...document.querySelectorAll('ul[data-component="multiplechoice"]')];
    for (let node of nodes) {
        let answers = [...node.querySelectorAll("[data-correct]")]
            .map(answerToNum);
        await bookEvent(node.id, answers.toString());
    }
}

(async () => {
    await gatherCorrect();
    location.reload();
})();