# 📤 Simple File Sharing App Using Python Sockets

A lightweight Python-based file sharing app using TCP sockets. This project allows one device to host files (server) and another to request and download them (client) over the same network.

---

## 💡 Features

- Share any type of file (text, image, PDF, etc.)
- Runs on local networks (LAN) or localhost
- Simple and beginner-friendly code using raw sockets
- Supports keyboard-based filename input

---

## 🗂️ Project Structure

```
file_sharing/
├── server.py       # File sharing server
├── client.py       # File downloader client
└── shared/         # Folder containing files to share (server side)
```

---

## 🔧 Requirements

- Python 3.x (Tested on 3.10)
- No external libraries needed — only built-in modules

---

## 🚀 How to Run

### 1. Prepare Files to Share
- Create a folder named `shared` in the same directory as `server.py`.
- Put files inside that folder to be shared.

### 2. Start the Server
On the server machine:

```bash
python server.py
```

You will see:
```
[SERVER] Listening on 0.0.0.0:5001
```

### 3. Run the Client
On the client machine (same network):

```bash
python client.py
```

Enter the exact filename when prompted (e.g., `sample.txt`).

The file will be downloaded into a folder called `downloads`.

---

## 🌐 Network Configuration

| Situation      | Server `HOST`      | Client `SERVER_IP`        |
|----------------|--------------------|----------------------------|
| Same Computer  | `'127.0.0.1'`      | `'127.0.0.1'`              |
| Same Wi-Fi     | `'0.0.0.0'`        | Use server's local IP (e.g., `192.168.1.x`) |
| Internet       | `'0.0.0.0'`        | Use public IP (with port forwarding) |

---

## 🧠 How It Works

- Server listens for client connections on a TCP port.
- Client connects and sends a filename request.
- Server checks if the file exists in `shared/` folder:
  - If yes: sends the file in chunks.
  - If no: sends `NOTFOUND`.

---

## 🛡️ Security Notes

- No encryption is used — not suitable for public internet without SSL.
- Add authentication and logging for production use.

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙋‍♂️ Author

Created by [virothi karthikeya]. Feel free to modify or upgrade it!
