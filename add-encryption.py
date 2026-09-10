from pathlib import Path

file = Path("index.html")
html = file.read_text(encoding="utf-8")

encryption_css = """
<style id="encryption-demo-style">
.encryption-demo {
    margin-top: 25px;
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.05);
}

.cipher-box {
    background: #071b35;
    color: #35d5c5;
    padding: 15px;
    border-radius: 10px;
    font-family: monospace;
    font-size: 12px;
    word-break: break-all;
    margin-top: 12px;
}

.decrypt-btn {
    margin-top: 15px;
    padding: 11px 18px;
    border: none;
    border-radius: 8px;
    background: #35d5c5;
    color: #071b35;
    font-weight: bold;
    cursor: pointer;
}

#decryptedReport {
    display: none;
    margin-top: 15px;
    padding: 15px;
    background: #ecfdf5;
    border-radius: 10px;
}
</style>
"""

html = html.replace("</head>", encryption_css + "\n</head>", 1)

report = """
<div class="encryption-demo">
    <h2>🔐 Secure Medical Report</h2>

    <p style="margin-top:8px;color:#718096;">
        Medical screening data is encrypted before storage.
    </p>

    <div style="margin-top:18px;">
        <strong>Encryption:</strong>
        <span style="color:#16a34a;"> AES-GCM</span>
    </div>

    <div style="margin-top:8px;">
        <strong>Status:</strong>
        <span style="color:#16a34a;"> ✓ Encrypted</span>
    </div>

    <p style="margin-top:18px;font-size:13px;color:#718096;">
        Encrypted data (ciphertext):
    </p>

    <div class="cipher-box" id="cipherText">
        Generating encrypted report...
    </div>

    <button class="decrypt-btn" onclick="decryptMedicalReport()">
        🔓 Decrypt Authorized Report
    </button>

    <div id="decryptedReport">
        <strong>✓ Authorized Medical Report</strong>
        <br><br>
        Patient ID: P001
        <br>
        AI Risk Score: 18%
        <br>
        Screening Result: LOW RISK
        <br>
        Sensor Status: Normal
    </div>
</div>
"""

html = html.replace("</main>", report + "\n</main>", 1)

encryption_js = """
<script id="encryption-demo-script">

let encryptionKey;
let encryptedReport;

async function setupEncryptionDemo() {

    const reportData = JSON.stringify({
        patient_id: "P001",
        risk_score: "18%",
        result: "LOW RISK",
        sensor_status: "Normal"
    });

    encryptionKey = await crypto.subtle.generateKey(
        {
            name: "AES-GCM",
            length: 256
        },
        true,
        ["encrypt", "decrypt"]
    );

    const encoder = new TextEncoder();

    const iv = crypto.getRandomValues(
        new Uint8Array(12)
    );

    const encrypted = await crypto.subtle.encrypt(
        {
            name: "AES-GCM",
            iv: iv
        },
        encryptionKey,
        encoder.encode(reportData)
    );

    const combined = new Uint8Array(
        iv.length + encrypted.byteLength
    );

    combined.set(iv);
    combined.set(
        new Uint8Array(encrypted),
        iv.length
    );

    encryptedReport = combined;

    document.getElementById("cipherText").innerText =
        Array.from(combined)
            .map(b => b.toString(16).padStart(2, "0"))
            .join("");
}


async function decryptMedicalReport() {

    if (!encryptionKey || !encryptedReport) {
        alert("Encryption is still initializing.");
        return;
    }

    const iv = encryptedReport.slice(0, 12);
    const ciphertext = encryptedReport.slice(12);

    try {

        const decrypted = await crypto.subtle.decrypt(
            {
                name: "AES-GCM",
                iv: iv
            },
            encryptionKey,
            ciphertext
        );

        const decoder = new TextDecoder();

        const report =
            JSON.parse(decoder.decode(decrypted));

        document.getElementById(
            "decryptedReport"
        ).style.display = "block";

        document.getElementById(
            "decryptedReport"
        ).innerHTML =
            "<strong>✓ Authorized Medical Report</strong>" +
            "<br><br>" +
            "Patient ID: " + report.patient_id +
            "<br>" +
            "AI Risk Score: " + report.risk_score +
            "<br>" +
            "Screening Result: " + report.result +
            "<br>" +
            "Sensor Status: " + report.sensor_status;

    } catch (error) {

        alert("Decryption failed.");

    }
}

setupEncryptionDemo();

</script>
"""

html = html.replace("</body>", encryption_js + "\n</body>", 1)

file.write_text(html, encoding="utf-8")

print("ENCRYPTION DEMO ADDED SUCCESSFULLY")
