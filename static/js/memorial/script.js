 // Define the text to be typed
 var text = "What can I help you?";

 // Define the delay between each character
 var delay = 50;

 // Get the chat text element
 var chatText = document.getElementById("chat-text");

 // Define the index of the character being typed
 var index = 0;

 // Start the typing animation
 var intervalId = setInterval(function() {
   // Add the next character to the chat text
   chatText.innerHTML += text[index];

   // Increment the index
   index++;

   // Check if all characters have been typed
   if (index >= text.length) {
     // Stop the typing animation
     clearInterval(intervalId);
   }
 }, delay);

 const mailIcon = document.getElementById("mail-icon");
 const chatBox = document.getElementById("chatbox");
 const collapseBtn = document.getElementById("collapse-btn");
 
 mailIcon.style.display = "none";
 
 collapseBtn.addEventListener("click", () => {
   if (chatBox.style.display === "none") {
     chatBox.style.display = "block";
     mailIcon.style.display = "none";
   } else {
     chatBox.style.display = "none";
     mailIcon.style.display = "block";
   }
 });
 
 mailIcon.addEventListener("click", () => {
   if (chatBox.style.display === "none") {
     chatBox.style.display = "block";
     mailIcon.style.display = "none";
   }
 });

 const chatForm = document.querySelector('#chatbox form');
 chatForm.addEventListener('submit', (event) => {
   event.preventDefault(); // Prevent the form from submitting normally
   
   // Show an alert message to let the user know the message was sent
   alert('Thank you for your question. Please wait for a response via email.');
   
   // Clear the input field
   chatForm.querySelector('input').value = '';
 });
 