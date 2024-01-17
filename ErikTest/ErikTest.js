let profileData;

//org 86487
//99999
async function loadQuestion(questionID) {
    await fetch(`http://localhost:5000/getPostByID/${questionID}`, {
        method: "GET",
        headers: {
            Accept: "application/json",
        },
    })
        .then((response) => response.json())
        .then((json) => {
            profileData = json;
        });

    console.log(profileData);
    document.getElementById("question").innerText = profileData[0][18];
    document.getElementById("questionBody").innerHTML = profileData[0][3];
    document.getElementById("questionUpvotes").innerText = profileData[0][16];
    document.getElementById("questionViews").innerText = profileData[0][19];
}

//Load default question could be gotten from url 
loadQuestion(86487)

document.getElementById("getQuestionBT").addEventListener("click", () => {
    const vQuestionID = document.getElementById("questionInput").value
    loadQuestion(vQuestionID)
})

//QuestionUpvotes

// TODO: fetch comments

// await fetch("http://localhost:5000/getCommentsByPostID/86487", {
//     method: "GET",
//     headers: {
//         Accept: "application/json",
//     },
// })
//     .then((response) => response.json())
//     .then((json) => {
//         console.log(json);
//     });
