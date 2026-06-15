async function startGame(){

    const role =
        document.getElementById("role").value;

    const name =
        document.getElementById("name").value;

    const gender =
        document.getElementById("gender").value;

    if(name.trim()===""){

        alert("Please enter your name.");
        return;
    }

    try{

        const response = await fetch("/start",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                role,
                name,
                gender
            })
        });

        const data = await response.json();

        document.querySelector(".hero")
            .style.display = "none";

        document.querySelector(".setup-card")
            .style.display = "none";

        document.getElementById("chatSection")
            .style.display = "block";

        document.getElementById("chatBox").innerHTML = `
            <div class="bot-message">
                ${data.message}
            </div>
        `;

        document.getElementById("message").focus();

    }
    catch(error){

        console.error(error);

        alert("Unable to start chat.");
    }
}

async function sendMessage(){

    const input =
        document.getElementById("message");

    const msg =
        input.value.trim();

    if(!msg) return;

    const chatBox =
        document.getElementById("chatBox");

    chatBox.innerHTML += `
        <div class="user-message">
            ${msg}
        </div>
    `;

    input.value = "";

    try{

        const response = await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:msg
            })
        });

        const data =
            await response.json();

        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.reply}
            </div>
        `;

        chatBox.scrollTop =
            chatBox.scrollHeight;

    }
    catch(error){

        console.error(error);
    }
}

document.addEventListener("click",function(e){

    if(e.target.id==="sendBtn"){

        sendMessage();
    }
});

document.addEventListener("keydown",function(e){

    if(e.key==="Enter"){

        const messageBox =
            document.getElementById("message");

        if(messageBox &&
           document.getElementById("chatSection").style.display==="block"){

            sendMessage();
        }
    }
});