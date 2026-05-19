const form = document.querySelector("#shorten-form");
const resultDiv = document.querySelector("#result");
const shortUrlInput = document.querySelector("#short-url");
const copyBtn = document.querySelector("#copy-btn");
const qrImage = document.querySelector("#qr-image");

form.addEventListener("submit", async (event) => {

    event.preventDefault();
    const url = document.querySelector("#url-input").value;
    const customCode = document.querySelector("#custom-code").value;

    try {
        const response = await fetch("/shorten", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url,
                custom_code: customCode
            })
        });
        const data = await response.json();

        if (!response.ok) {
            alert(data.error);
            return;
        }
        shortUrlInput.value = data.short_url;
        qrImage.src = data.qr_code;
        resultDiv.classList.remove("hidden");
    }

    catch (error) {
        console.error(error);
        alert("Something went wrong.");
    }

});

copyBtn.addEventListener("click", async () => {

    try {
        await navigator.clipboard.writeText(
            shortUrlInput.value
        );

        copyBtn.innerText = "Copied!";
        setTimeout(() => {
            copyBtn.innerText = "Copy";
        }, 2000);

    }
    catch (error) {
        console.error(error);
        alert("Failed to copy URL.");
    }
});

