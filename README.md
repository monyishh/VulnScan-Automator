# 🛡️ VulnScan Automator
### Automated Vulnerability Scanner using Python, Nmap, and Nikto (WSL Linux)

VulnScan Automator is a Python-based security scanning tool that performs **automated port scanning, service enumeration, and basic web vulnerability detection** using:

- **Nmap** (for ports, services, OS detection, SSL info)
- **Nikto** (for web server misconfigurations & vulnerabilities)
- **WSL Ubuntu** (to run Linux-based scanning tools accurately)

The tool generates a **combined security report** containing Nmap & Nikto results.

---

## 🚀 Features

- ✔ Automated **Nmap scan**
  - Open ports
  - Service versions
  - OS detection
  - SSL issues
  - Firewall analysis
  
- ✔ Automated **Nikto scan**
  - Directory exposures
  - Insecure headers
  - Dangerous files
  - Outdated server versions
  - SSL/certificate issues
  
- ✔ **Report generation**
  - Saved in `reports/`
  - Timestamped filenames
  - Clean combined output

- ✔ **WSL-based scanning** for Linux accuracy  
- ✔ Python error-handling and safe execution

---

## 📦 Requirements

### **Windows**
- Python 3.x  
- WSL (Ubuntu 20.04+)  
- Git installed

### **Install tools inside Ubuntu**
```bash
sudo apt update
sudo apt install nmap nikto -y


📂 Project Structure
VulnScan-Automator/
│── vulnscan_automator.py
│── README.md
└── reports/
     └── vulnscan_<target>_<timestamp>.txt

▶️ Usage

Run the script:

python vulnscan_automator.py


Enter a target when prompted:

Enter target IP or domain: scanme.nmap.org


After scanning, results will be saved in:

reports/

🔍 Safe Test Targets

Use these ONLY for practice (legal & safe):

Target	Purpose
scanme.nmap.org	Nmap test server
testphp.vulnweb.com	Web vulnerability testing
juice-shop.heroku.com	OWASP vulnerable web app
demo.testfire.net	Banking demo web app
📜 Example Report Output
=== NMAP RESULTS ===
22/tcp open ssh OpenSSH 6.6.1p1 (Ubuntu)
80/tcp open http Apache 2.4.7

=== NIKTO RESULTS ===
+ Server: Apache/2.4.7
+ Cookie flags missing
+ X-Frame-Options header not set
+ Outdated Apache version

⚠️ Legal Disclaimer

This tool is intended only for learning and ethical security testing.
Do NOT scan targets without explicit permission.

👨‍💻 Author

Manish Kumar
