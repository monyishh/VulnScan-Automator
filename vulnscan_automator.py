#nmap and nikto scanner
import subprocess
import nmap
import datetime
import os

TARGET = input("Enter target IP or domain: ")

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"{REPORT_DIR}/vulnscan_{TARGET}_{timestamp}.txt"

# file header
with open(report_file, "w") as f:
    f.write(" VulnScan Automator Report \n")
    f.write(f"Target: {TARGET}\n")
    f.write(f"Timestamp: {timestamp}\n\n")

print("\n[+] Starting Nmap Scan...")

# nmap running
nm = nmap.PortScanner()
nm.scan(TARGET, arguments="-A -sV -O")

with open(report_file, "a") as f:
    f.write("\n NMAP RESULTS \n")
    f.write(nm.csv())  # all detected ports + services

print("[+] Nmap scan complete.")

# nikto running
print("[+] Starting Nikto Scan (web vulns)...")

try:
    nikto_cmd = f"wsl nikto -h {TARGET}"
    nikto_output = subprocess.getoutput(nikto_cmd)

    with open(report_file, "a") as f:
        f.write("\n NIKTO RESULTS \n")
        f.write(nikto_output)

    print("[+] Nikto scan complete.")

except Exception as e:
    print("Nikto error:", e)

# finished
print(f"\n Scan Complete!")
print(f"Report saved to: {report_file}")
