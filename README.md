
# ASN to IPs Scraper

🎯 **asn_to_ips_Scraper** is a simple Python tool by [NightfallSecDev](https://github.com/NightfallSecDev) to fetch IP ranges (both IPv4 and IPv6) from any given ASN using the [bgpview.io API](https://bgpview.io), display them in a colorized format, and save them to a `.txt` file.

---

## 🚀 Features

- 🔍 Query any ASN (Autonomous System Number)
- 🌈 Color-coded terminal output
  - IPv4 → Cyan
  - IPv6 → Magenta
- 💾 Save to a custom `.txt` file via `-o`
- ✅ No API key required
- 🖼️ Fancy ASCII banner

---

## 📦 Requirements

```bash
pip install requests colorama
````

---

## 🧠 Usage

```bash
python asn_to_ips.py <ASN> [-o output.txt]
```

### 🔹 Examples:

```bash
python asn_to_ips.py AS15169 -o google_ranges.txt
python asn_to_ips.py 32934               # Facebook ASN
```

* Output:

  * Terminal: Colorized list of IP ranges
  * File: Plain `.txt` with 1 IP/CIDR per line

---

## 📁 Project Structure

```
asn_to_ips_Scraper/
├── asn_to_ips.py       # Main script
├── README.md           # This file
```

---

## 📌 Notes

* You can use ASN with or without the `AS` prefix (e.g., `AS32934` or `32934`)
* Default output filename is `AS<ASN>_ranges.txt` if `-o` is not used

---

## 🧑‍💻 Author

**Trojan Hax / NightfallSecDev**
🔗 [GitHub](https://github.com/NightfallSecDev)

---

## 📜 License

MIT License. Free to use, modify, and distribute.

---

## ⭐️ Give a Star!

If this project helped you, please consider ⭐ starring the repo:
👉 [github.com/NightfallSecDev/asn\_to\_ips\_Scraper](https://github.com/NightfallSecDev/asn_to_ips_Scraper)

````


