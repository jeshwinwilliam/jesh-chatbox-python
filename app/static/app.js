const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");

function appendMessage(role, text, label) {
  const article = document.createElement("article");
  article.className = `message ${role}`;

  const badge = document.createElement("span");
  badge.className = "badge";
  badge.textContent = label;

  const paragraph = document.createElement("p");
  paragraph.textContent = text;

  article.appendChild(badge);
  article.appendChild(paragraph);
  messages.appendChild(article);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const message = input.value.trim();
  if (!message) {
    return;
  }

  appendMessage("user", message, "You");
  input.value = "";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error("Request failed");
    }

    const data = await response.json();
    appendMessage("assistant", data.reply, `AI • ${data.provider}`);
  } catch (error) {
    appendMessage("assistant", "Something went wrong while reaching the chat API.", "AI");
  }
});

