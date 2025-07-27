# GitHub Subdomain Takeover Checker

🚨 **GitHub 404 Subdomain Checker** – A simple Python tool to check if subdomains point to GitHub 404 pages, which may indicate a potential subdomain takeover vulnerability.

## 🔍 Features

- Reads subdomains from `list.txt`
- Detects and logs subdomains that return a GitHub-branded 404 page
- Saves vulnerable subdomains to `404.txt`

## 🛠️ Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/0xBakusedu/Github-404.git
   cd Github-404
   ```

2. **Install dependencies:**
   Make sure Python 3 and `pip` are installed.

   ```bash
   pip install -r requirements.txt
   ```

   Contents of `requirements.txt`:
   ```
   requests
   colorama
   ```

3. **Add your subdomains to `list.txt`:**
   Example:
   ```
   example.github.io
   subdomain.example.com
   ```

4. **Run the script:**
   ```bash
   python3 checker.py
   ```

## 📄 Output

- Subdomains returning a GitHub-branded 404 will be saved in `404.txt`
- Console output example:

  ```
  [404] https://example.github.io/
  [OK ] https://valid.example.com/
  ```

## ⚠️ Disclaimer

This tool is intended for educational and authorized security testing purposes only. Use it responsibly. The author is not responsible for any misuse or damages caused by this tool.

## 👨‍💻 Author

- [0xBakusedu](https://github.com/0xBakusedu/)
- [williamlaurent](https://github.com/williamlaurent/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
