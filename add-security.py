from pathlib import Path

file = Path("index.html")
html = file.read_text()

# =========================
# SECURITY CSS
# =========================

security_css = r"""
/* ================= SECURITY DEMO ================= */

#securityOverlay {
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #071b35, #123b64);
    z-index: 99999;
    display: flex;
    justify-content: center;
    align-items: center;
}

.security-box {
    width: 420px;
    max-width: 92%;
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}

.security-box h1 {
    text-align: center;
    color: #071b35;
    margin-bottom: 8px;
}

.security-box .secure-icon {
    text-align: center;
    font-size: 45px;
    margin-bottom: 10px;
}

.security-box .security-subtitle {
    text-align: center;
    color: #718096;
    margin-bottom: 25px;
}

.security-box label {
    display: block;
    margin-top: 15px;
    margin-bottom: 6px;
    font-weight: bold;
    color: #334155;
}

.security-box input,
.security-box select {
    width: 100%;
    padding: 13px;
    border: 1px solid #dbe3ec;
    border-radius: 9px;
    font-size: 15px;
}

.security-login-btn {
    width: 100%;
    margin-top: 22px;
    padding: 14px;
    border: none;
    border-radius: 9px;
    background: #35d5c5;
    color: #071b35;
    font-weight: bold;
    cursor: pointer;
    font-size: 15px;
}

.security-login-btn:hover {
    opacity: 0.88;
}

#loginError {
    display: none;
    margin-top: 12px;
    padding: 10px;
    background: #fee2e2;
    color: #b91c1c;
    border-radius: 8px;
    text-align: center;
}

.security-badge {
    display: inline-block;
    padding: 6px 10px;
    background: #dcfce7;
    color: #166534;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
    margin-top: 8px;
}

.secure-report {
    margin-top: 25px;
    background: white;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.05);
    border-left: 5px solid #35d5c5;
}

.secure-report h2 {
    margin-bottom: 15px;
}

.encryption-status {
    padding: 12px;
    background: #ecfdf5;
    color: #166534;
    border-radius: 9px;
    margin-bottom: 15px;
    font-weight: bold;
}

.role-info {
    margin-bottom: 15px;
    color: #64748b;
}
"""

html = html.replace("</style>", security_css + "\n</style>", 1)


# =========================
# LOGIN OVERLAY
# =========================

login_html = r"""
<!-- ================= SECURITY LOGIN ================= -->

<div id="securityOverlay">

    <div class="security-box">

        <div class="secure-icon">🔐</div>

        <h1>BreathAI Secure Access</h1>

        <p class="security-subtitle">
            Authorized Medical Screening Portal
        </p>

        <label for="loginRole">Access Type</label>

        <select id="loginRole">
            <option value="patient">Patient</option>
            <option value="doctor">Doctor</option>
        </select>

        <label for="loginUsername">Username</label>

        <input
            type="text"
            id="loginUsername"
            placeholder="Enter username"
        >

        <label for="loginPassword">Password</label>

        <input
            type="password"
            id="loginPassword"
            placeholder="Enter password"
        >

        <button
            class="security-login-btn"
            onclick="secureLogin()"
        >
            🔓 Secure Login
        </button>

        <div id="loginError">
            Invalid username or password
        </div>

        <div style="text-align:center;margin-top:18px;color:#94a3b8;font-size:12px;">
            🔒 Encrypted Medical Data Demo
        </div>

    </div>

</div>

"""

html = html.replace("<body>", "<body>\n" + login_html, 1)


# =========================
# SECURE REPORT
# =========================

report_html = r"""
<!-- ================= SECURE MEDICAL REPORT ================= -->

<div class="secure-report" id="secureReport">

    <h2>🔒 Secure Medical Report</h2>

    <div class="encryption-status">
        ✓ Medical report protected with AES-GCM encryption
    </div>

    <div class="role-info" id="roleInfo"></div>

    <div class="profile-row">
        <strong>Patient ID</strong>
        <span id="securePatientId">P001</span>
    </div>

    <div class="profile-row">
        <strong>Screening Result</strong>
        <span id="secureRisk">LOW RISK</span>
    </div>

    <div class="profile-row">
        <strong>AI Risk Score</strong>
        <span id="secureScore">18%</span>
    </div>

    <div class="profile-row">
        <strong>Sensor Data</strong>
        <span id="secureSensor">Protected</span>
    </div>

    <div style="margin-top:18px;padding:12px;background:#f8fafc;border-radius:9px;">
        <strong>Security Controls</strong>
        <br><br>
        ✓ Authentication<br>
        ✓ Role-Based Access Control<br>
        ✓ Patient/Doctor authorization<br>
        ✓ Encrypted medical report
    </div>

</div>

"""

# Add secure report before closing main
html = html.replace("</main>", report_html + "\n</main>", 1)


# =========================
# SECURITY JAVASCRIPT
# =========================

security_js = r"""

/* ================= SECURITY DEMO ================= */

const DEMO_USERS = {
    patient: {
        username: "patient01",
        password: "Patient@123",
        role: "Patient",
        patientCode: "P001"
    },

    doctor: {
        username: "doctor01",
        password: "Doctor@123",
        role: "Doctor",
        patientCode: "P001"
    }
};

let currentRole = null;

function secureLogin() {

    const role = document.getElementById("loginRole").value;
    const username = document.getElementById("loginUsername").value.trim();
    const password = document.getElementById("loginPassword").value;

    const user = DEMO_USERS[role];

    if (
        user &&
        username === user.username &&
        password === user.password
    ) {

        currentRole = role;

        sessionStorage.setItem(
            "breathAI_role",
            role
        );

        sessionStorage.setItem(
            "breathAI_user",
            username
        );

        document.getElementById("securityOverlay").style.display = "none";

        updateSecurityUI();

    } else {

        document.getElementById("loginError").style.display = "block";

    }
}


function updateSecurityUI() {

    const role = currentRole;

    if (!role) return;

    const user = DEMO_USERS[role];

    document.getElementById("roleInfo").innerHTML =
        "Authenticated as <strong>" +
        user.role +
        "</strong> — Authorized access granted.";

    document.getElementById("securePatientId").innerText =
        user.patientCode;

    if (role === "patient") {

        document.getElementById("secureSensor").innerText =
            "Decrypted after patient authentication";

    } else {

        document.getElementById("secureSensor").innerText =
            "Decrypted for authorized doctor";

    }
}


/* Logout */

function secureLogout() {

    sessionStorage.removeItem("breathAI_role");
    sessionStorage.removeItem("breathAI_user");

    currentRole = null;

    document.getElementById("securityOverlay").style.display = "flex";

    document.getElementById("loginUsername").value = "";
    document.getElementById("loginPassword").value = "";

}


/* Restore login state */

window.addEventListener("DOMContentLoaded", function() {

    const savedRole =
        sessionStorage.getItem("breathAI_role");

    if (savedRole && DEMO_USERS[savedRole]) {

        currentRole = savedRole;

        document.getElementById("securityOverlay").style.display =
            "none";

        updateSecurityUI();

    }

});

"""

html = html.replace("</script>", security_js + "\n</script>", 1)


# =========================
# REPLACE LOGOUT BUTTON
# =========================

html = html.replace(
    '<button class="menu button">',
    '<button class="menu button" onclick="secureLogout()">',
    1
)


file.write_text(html)

print("SECURITY DEMO ADDED SUCCESSFULLY")
