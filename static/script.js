const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

console.log("Script loaded");

function addMessage(text, sender){

    const message = document.createElement("div");

    message.classList.add("message");
    message.classList.add(sender);

    message.innerText = text;

    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.addEventListener("click", async () => {

    const text = userInput.value.trim();

    if (text === "") return;

    addMessage(text, "user");

    userInput.value = "";

    // Disable button while AI is thinking
    sendBtn.disabled = true;
    sendBtn.innerText = "Thinking...";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: text
        })
    });

    const data = await response.json();

    addMessage(data.response, "bot");

    // Enable button again
    sendBtn.disabled = false;
    sendBtn.innerText = "Send";

});

const uploadBtn = document.getElementById("uploadBtn");
const pdfFile = document.getElementById("pdfFile");

uploadBtn.addEventListener("click", async () => {

    if(pdfFile.files.length === 0){
        alert("Please choose a PDF first.");
        return;
    }

    const formData = new FormData();

    formData.append("pdf", pdfFile.files[0]);

    const response = await fetch("/upload",{
        method:"POST",
        body:formData
    });

    const data = await response.json();

    addMessage(data.message,"bot");

});