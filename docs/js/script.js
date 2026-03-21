// const API_URL = "https://phising-website-detection.up.railway.app/check_url";

// document.getElementById("checkBtn").addEventListener("click", async () => {
//     const url = document.getElementById("urlInput").value.trim();
//     const resultDiv = document.getElementById("result");

//     if (!url) {
//         resultDiv.textContent = "Please enter a URL!";
//         resultDiv.style.color = "orange";
//         return;
//     }

//     resultDiv.textContent = "Checking...";
//     resultDiv.style.color = "black";

//     try {
//         const response = await fetch(API_URL, {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ url })
//         });

//         if (!response.ok) throw new Error("Failed to reach backend");

//         const data = await response.json();

//         resultDiv.innerHTML = `
//             <p><strong>URL:</strong> ${data.url}</p>
//             <p><strong>Status:</strong> ${data.prediction}</p>
//             <p><strong>Confidence:</strong> ${data.confidence}%</p>
//         `;
//         resultDiv.style.color = data.prediction === "SAFE" ? "green" : "red";
//     } catch (err) {
//         resultDiv.textContent = `Error: ${err.message}`;
//         resultDiv.style.color = "orange";
//         console.error(err);
//     }
// });


const API_URL = "https://phising-website-detection.up.railway.app/check_url";

document.getElementById("checkBtn").addEventListener("click", async () => {
    const url = document.getElementById("urlInput").value.trim();
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.textContent = "Please enter a URL!";
        resultDiv.style.color = "orange";
        return;
    }

    resultDiv.textContent = "Checking...";
    resultDiv.style.color = "black";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        if (!response.ok) throw new Error("Failed to reach backend");

        const data = await response.json();
        resultDiv.innerHTML = `
            <p><strong>URL:</strong> ${data.url}</p>
            <p><strong>Status:</strong> ${data.prediction}</p>
            <p><strong>Confidence:</strong> ${data.confidence}%</p>
        `;
        resultDiv.style.color = data.prediction === "SAFE" ? "green" : "red";
    } catch (err) {
        resultDiv.textContent = `Error: ${err.message}`;
        resultDiv.style.color = "orange";
        console.error(err);
    }
});
