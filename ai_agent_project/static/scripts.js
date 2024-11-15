// Add event listeners for the upload and query forms to handle responses
document.addEventListener("DOMContentLoaded", function() {
    const uploadForm = document.getElementById("uploadForm");
    const queryForm = document.getElementById("queryForm");
    const messageDiv = document.getElementById("message");

    // Handle file upload form submission
    if (uploadForm) {
        uploadForm.addEventListener("submit", async function(event) {
            event.preventDefault();
            messageDiv.textContent = "Uploading file...";
            messageDiv.classList.remove("error", "success");

            const formData = new FormData(uploadForm);
            const response = await fetch("/upload", {
                method: "POST",
                body: formData
            });

            const result = await response.json();
            if (response.ok) {
                messageDiv.textContent = result.message;
                messageDiv.classList.add("success");
                // Optionally reload the page to show query form
                location.reload();
            } else {
                messageDiv.textContent = result.error;
                messageDiv.classList.add("error");
            }
        });
    }

    // Handle query form submission
    if (queryForm) {
        queryForm.addEventListener("submit", async function(event) {
            event.preventDefault();
            messageDiv.textContent = "Processing query...";
            messageDiv.classList.remove("error", "success");

            const formData = new FormData(queryForm);
            const response = await fetch("/query", {
                method: "POST",
                body: formData
            });

            const result = await response.json();
            if (response.ok) {
                messageDiv.textContent = result.message;
                messageDiv.classList.add("success");
            } else {
                messageDiv.textContent = result.error;
                messageDiv.classList.add("error");
            }
        });
    }
});
