const form = document.getElementById("url-form");
const resultBox = document.getElementById("result");
const shortUrlInput = document.getElementById("short-url");
const copyBtn = document.getElementById("copy-btn");
resultBox.style.display = "none";
form.addEventListener("submit", async function (e) {
    e.preventDefault();
    const longUrl = document.getElementById("long-url").value;
    const customCode = document.getElementById("custom-code").value;
    try {
        const response = await fetch("/shorten", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: longUrl,
                custom_code: customCode
            })
        });
        const data = await response.json();

        if (response.ok) {
            shortUrlInput.value = data.short_url;
            resultBox.style.display = "block";
        } else {
            alert(data.error);
        }
    } catch (error) {
        console.error(error);
        alert("Server error");
    }
});

copyBtn.addEventListener("click", function () {
    navigator.clipboard.writeText(shortUrlInput.value);
    copyBtn.innerText = "Copied!";

    setTimeout(() => {
        copyBtn.innerText = "Copy";
    }, 2000);
});