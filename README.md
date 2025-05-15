# 🔐 CTF-Toolkit

CTF-Toolkit is a toolkit designed for Capture The Flag (CTF) competitions and security testing. It integrates popular tools like **Nmap**, **Gobuster**, **Metasploit**, **Bettercap**, **Wireshark** and **Hydra**

![Security](https://img.shields.io/badge/CTF-Toolkit-critical?logo=hackthebox&color=red)
![Tested](https://img.shields.io/badge/Tested-Kali%20Linux-green?logo=linux)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Nmap](https://img.shields.io/badge/Tool-Nmap-blue?logo=nmap&logoColor=white)
![Wireshark](https://img.shields.io/badge/Tool-Wireshark-blue?logo=wireshark&logoColor=white)
![Metasploit](https://img.shields.io/badge/Tool-Metasploit-blue?logo=metasploit&logoColor=white)
![Hydra](https://img.shields.io/badge/Tool-Hydra-blue?logo=hydra&logoColor=white)
![Bettercap](https://img.shields.io/badge/Tool-Bettercap-blue?logo=bettercap&logoColor=white)
![Gobuster](https://img.shields.io/badge/Tool-Gobuster-blue?logo=gobuster&logoColor=white)
![Version](https://img.shields.io/badge/Version-v1.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-blue.svg)





## Security Warning

>>CTF-Toolkit is for ethical and authorized security testing only. Any unauthorized use may lead to legal consequences. The author is not responsible for any damage or misuse. Always obtain explicit permission before testing any system.

---

## Banner Created With:
-This ASCII banner was created using the [**ASCII Art Generator**](https://www.asciiart.eu/text-to-ascii-art) website.

---
## 🚀 Features
- > **Nmap**: Performs network scanning and vulnerability analysis.
- > **Gobuster**: Used for directory and file enumeration in web applications.
- > **Hashing**: Generate and crack hashes using various cryptographic algorithms.
- > **Metasploit**: Exploit target systems and test vulnerabilities.
- > **HashGenerator**: A custom tool to generate hashes using algorithms like `MD5`, `SHA-1`, `SHA-256`, `SHA-512`
- > **HashCracker**: A custom tool to crack hashes using brute-force or dictionary-based methods. `MD5`, `SHA-1`, `SHA-256`, `SHA-512`
- > **MACAddressChanger**: A custom utility to change your MAC address for anonymity or testing purposes.
- > **Automation**: Combines these tools and automates processes to speed up testing.

---
## Installation

### Requirements
**Nmap** | **Gobuster** | **Metasploit** | **Hydra** | **John** | **ssh2john** | **Wireshark** | **Bettercap**
>[Required Python Libraries](requirements.txt)



### Installation Steps

```bash
git clone https://github.com/furares/ctf-toolkit.git
cd ctf-toolkit
pip install -r requirements.txt
```
---

## 🧠 Usage

```bash
sudo python3 main.py
```
<p float="left">
  <img src="images/mainmenu.png" width="1250" />
</p>



---

### Important Notice 
Some tools require certain dependencies to be pre-installed on your system. Please ensure that the necessary tools are already installed before using them. 🛠️

### Nmap Scan Results
The results of your Nmap scans will be stored in the `nmap_results/` directory. 

### RSA Key Cracking
The `ssh2john.py` script required for cracking RSA keys should be located in the current directory. 

### MAC Address Changer
The MAC Address Changer tool was created by me. Please note that it may not always work perfectly on all systems, as it has been tested mainly on Linux Mint and Kali Linux.

Use it with caution, and ensure you're on a supported system for the best results! ⚠️

### Wordlists
If you'd like, you can move your wordlists into the `wordlists/` directory for better organization.


### 🔥 Check Out My TryHackMe Profile
> **[TryHackMe Profile](https://tryhackme.com/p/furares)** 👾







