const chatbox = document.getElementById("chatbox");
const userInput = document.getElementById("userInput");
const nameInput = document.getElementById("nameInput");
const roleInput = document.getElementById("roleInput");
const genderInput = document.getElementById("genderInput");

const nameInputBox = document.getElementById("nameInputBox");
const chatInterface = document.getElementById("chatInterface");

function startGame() {
    const name = nameInput.value.trim();
    const role = roleInput.value.trim().toLowerCase();
    const gender = genderInput.value.trim().toLowerCase();

    // Ensure the name, role, and gender fields are filled
    if (!name || !role || !gender) {
        return alert("Please fill in all the fields: Name, Role, and Gender!");
    }

    // Sending the data to the backend with a POST request
    fetch("/start", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, role, gender })
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to start the game.");
        return res.json();
    })
    .then(data => {
        if (data.message) {
            chatbox.innerHTML = `🤖 Bot: ${data.message}\n`;
        }
        // Hide the name input box and show the chat interface
        nameInputBox.style.display = "none";
        chatInterface.style.display = "block";
        userInput.focus();
    })
    .catch(err => {
        console.error("Error:", err);
        alert("There was an issue starting the game. Please try again later.");
    });
}

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    chatbox.innerHTML += `👤 You: ${message}\n`;
    userInput.value = "";

    // Sending the user's message to the backend for processing
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        if (data.lieCheck) {
            chatbox.innerHTML += `🤖 Bot: ${data.lieCheck}\n`;
        }
        if (data.response) {
            chatbox.innerHTML += `🤖 Bot: ${data.response}\n`;
        }

        if (data.end) {
            userInput.disabled = true;
        }

        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(err => {
        console.error("Error:", err);
        alert("There was an issue communicating with the chatbot. Please try again later.");
    });
}
