const form = document.querySelector("#shorten-form");

const resultDiv = document.querySelector("#result");

const shortUrlInput = document.querySelector("#short-url");

const copyBtn = document.querySelector("#copy-btn");


form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const url = document.querySelector("#url-input").value;

    const customCode = document.querySelector("#custom-code").value;

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

    shortUrlInput.value = data.short_url;

    resultDiv.classList.remove("hidden");
});


copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(shortUrlInput.value);

    copyBtn.innerText = "Copied!";

    setTimeout(() => {
        copyBtn.innerText = "Copy";
    }, 2000);
});