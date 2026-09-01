# 🔎 Python Network Scanner

A simple TCP network scanner written in Python.

This project was created for **educational purposes** to learn about:

* TCP/IP networking
* TCP ports
* Socket programming
* Network reconnaissance
* Python automation
* Basic cybersecurity concepts

## ⚙️ Features

* Scan a hostname or IP address
* Scan a custom TCP port range
* Detect open TCP ports
* Display scan information
* Simple command-line interface
* No external Python libraries required

## 📁 Project Structure

```text
network-scanner/
├── scanner.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/network-scanner.git
```

Open the project directory:

```bash
cd network-scanner
```

Python 3 is required.

No external packages are needed.

## 💻 Usage

Scan the first 1024 TCP ports:

```bash
python scanner.py 127.0.0.1
```

Scan a custom port range:

```bash
python scanner.py 127.0.0.1 -p 1-100
```

You can also use a hostname:

```bash
python scanner.py localhost -p 1-1000
```

## 🧪 Example

```text
=======================================================
        PYTHON NETWORK SCANNER
=======================================================
Target   : localhost
IP       : 127.0.0.1
Ports    : 1-100
Started  : 2026-09-01 14:00:00
-------------------------------------------------------
[+] Port 22    OPEN
[+] Port 80    OPEN
-------------------------------------------------------
[+] Open ports: 22, 80
=======================================================
```

## 🛡️ Legal & Ethical Use

This tool is intended for **educational purposes and authorized security testing only**.

Only scan:

* Your own computer
* Your own virtual machines
* Your own laboratory network
* Systems for which you have explicit permission to test

Do not scan networks or systems without authorization.

## 📚 What I Learned

Through this project, I practiced:

* Python sockets
* TCP connections
* IP address resolution
* Command-line arguments
* Error handling
* Basic network reconnaissance

## 🔮 Future Improvements

Possible future features:

* Multithreaded scanning
* Service detection
* Banner grabbing
* Export results to JSON
* Export results to CSV
* Configurable timeout
* Logging
* IPv6 support

## 👨‍💻 Author

**Asadillayev G'ayratbek**

Student | Python Developer | Cybersecurity Enthusiast

Telegram: **@syran0x**
