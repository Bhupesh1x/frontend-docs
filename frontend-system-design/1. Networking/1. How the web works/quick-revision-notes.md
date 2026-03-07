# How the Web Works — Quick Revision

## ⚡ Full Flow (URL → Page)

| # | Stage | What Happens |
|---|-------|-------------|
| 1 | **DNS Lookup** | Browser → Router → ISP → DNS → IP returned (cached at each level) |
| 2 | **TCP Handshake** | SYN → SYN-ACK → ACK (3 steps, connection established) |
| 3 | **SSL Handshake** | *(HTTPS only)* Certificate exchanged, encrypted channel created |
| 4 | **HTTP Request** | Browser sends `GET` request to server using the IP |
| 5 | **Server Response** | HTML + CSS + JS + assets sent back |
| 6 | **Browser Renders** | Parses HTML structure, applies CSS, executes JS |

---

- ![dns-lookup](/1.%20How%20the%20web%20works/images/dns-lookup.png)
- ![isp](/1.%20How%20the%20web%20works/images/isp.png)
- ![isp-network](/1.%20How%20the%20web%20works/images/isp-network.png)

---

## 📌 Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Server** | Machine that listens for and responds to requests over the internet |
| **IP Address** | Unique numerical address of a device (e.g. `142.250.195.46`) |
| **Domain Name** | Human-readable alias for an IP (e.g. `google.com`) |
| **DNS** | Translates domain names → IP addresses (like a phone book) |
| **HTTP** | Protocol for browser-server communication (plain text) |
| **HTTPS** | HTTP + TLS encryption (all data encrypted) |
| **TCP** | Protocol ensuring data is delivered reliably and in order |
| **SSL Certificate** | Digital ID card proving a server's identity, enables encryption |
| **HTML** | Structure/skeleton of a webpage |
| **CSS** | Styling (colors, fonts, layout) |
| **JavaScript** | Logic and interactivity |
| **Caching** | Storing DNS/data results locally to skip repeat lookups |

---

## 🤝 TCP 3-Way Handshake
```
Client  ──SYN──▶  Server       "Hey, you there?"
Client  ◀──SYN-ACK──  Server   "Yep! Ready?"
Client  ──ACK──▶  Server       "Ready! Let's go." ✅ Connection open
```

---

## 🔒 HTTPS / SSL Handshake

| Step | Action |
|------|--------|
| 1 | TCP Handshake first |
| 2 | Client Hello → "I support these encryption methods" |
| 3 | Server Hello + Certificate → "Use this. Here's my ID" |
| 4 | Client verifies certificate with trusted Certificate Authorities (CAs) |
| 5 | Shared encryption key generated → all data encrypted 🔐 |

---

- ![isp-and-client-server-handshake](/1.%20How%20the%20web%20works/images/isp-and-client-server-handshake.png)
- ![client-server-connection](/1.%20How%20the%20web%20works/images/client-server-connection.png)
- ![https-client-server-connection](/1.%20How%20the%20web%20works/images/https-client-server-connection.png)

---

## 🌐 DNS Lookup Flow

**No cache:** `Browser → Router → ISP → DNS Server` → IP returned → `Browser → Server`

**With cache:** Browser finds IP in cache → skip DNS → go straight to server

**Cache levels:** Browser → OS/Router → ISP → Global DNS (Root → TLD → Authoritative)

---

## 💡 Analogies to Remember

| Concept | Analogy |
|---------|---------|
| **DNS** | Phone book — you know the name, need the number to call |
| **TCP Handshake** | Calling someone to confirm they can hear you before speaking |
| **HTTPS/TLS** | Sealed envelope — contents unreadable if intercepted |
| **Browser + HTML/CSS/JS** | Kitchen — raw ingredients assembled into the final meal |
| **Server** | Restaurant — takes orders (requests), sends back food (responses) |