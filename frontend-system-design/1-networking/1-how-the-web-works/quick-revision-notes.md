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

- ![dns-lookup](./images/dns-lookup.png)
- ![isp](./images/isp.png)
- ![isp-network](./images/isp-network.png)

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

- ![isp-and-client-server-handshake](./images/isp-and-client-server-handshake.png)
- ![client-server-connection](./images/client-server-connection.png)
- ![https-client-server-connection](./images/https-client-server-connection.png)

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

---

# How the Web Page Renders — Quick Revision

---

## ⚡ Full Pipeline
```
HTML Parsing (DOM)  →  Fetch CSS/JS  →  CSS Parsing (CSSOM)
→  JS Execution  →  Render Tree  →  Layout  →  Paint  →  Compositing
```

---

## 📌 Each Step in Brief

| Step | Name | One-liner |
|------|------|-----------|
| 1 | **HTML Parsing** | Browser reads HTML top-to-bottom, builds DOM tree |
| 2 | **Fetch Resources** | Encounters `<link>`/`<script>` tags, fetches CSS & JS |
| 3 | **CSS Parsing** | Builds CSSOM — **render blocking** (waits for full CSS) |
| 4 | **JS Execution** | Runs JS — **parser blocking** by default (use `async`/`defer`) |
| 5 | **Render Tree** | Merges DOM + CSSOM — only visible elements, final styles |
| 6 | **Layout** | Calculates exact size & position of every element |
| 7 | **Paint** | Fills in colours, fonts, borders, backgrounds |
| 8 | **Compositing** | Stacks layers (`z-index`, `transform`, `opacity`) → final screen |

---

## 🌳 DOM vs CSSOM vs Render Tree

| | DOM | CSSOM | Render Tree |
|-|-----|-------|-------------|
| Built from | HTML | CSS | DOM + CSSOM merged |
| Contains | All elements | All CSS rules | Visible elements only |
| Includes `display:none`? | ✅ Yes | ✅ Yes | ❌ No |

---

## ⚙️ JS: async vs defer vs default

| | Download | Executes |
|--|----------|----------|
| **default** | Blocks HTML parsing | Immediately |
| **async** | Parallel with HTML | As soon as downloaded |
| **defer** | Parallel with HTML | After HTML fully parsed |

---

## ⚙️ JS Execution — 3 Internal Phases
```
Parsing  →  Compilation (JIT)  →  Execution (Call Stack)
```

- **Parsing** — Code → AST (Abstract Syntax Tree)
- **Compilation** — AST → bytecode (V8 engine, JIT compiled)
- **Execution** — Runs on the Call Stack

---

## 🔑 Key Terms

| Term | Meaning |
|------|---------|
| **DOM** | Tree of all HTML elements in memory |
| **CSSOM** | Tree of all CSS rules mapped to elements |
| **Render Tree** | DOM + CSSOM merged; only visible elements with final styles |
| **Render Blocking** | Browser won't render until this is done (CSS) |
| **Parser Blocking** | Browser stops parsing HTML until this is done (JS) |
| **Layout / Reflow** | Calculating size and position of every element |
| **Paint** | Drawing colours, fonts, borders on screen |
| **Compositing** | Stacking independent layers into final image |
| **JRE** | JS Runtime Environment — engine + Web APIs + Event Loop |
| **Call Stack** | Where JS functions are pushed/popped during execution |

---

## 💡 Analogies to Remember

| Step | Analogy |
|------|---------|
| **DOM** | Skeleton/structure of a building |
| **CSSOM** | Interior design plan |
| **JS** | Electrical wiring — can change the structure |
| **Render Tree** | Final blueprint with everything combined |
| **Layout** | Architect measuring exact room positions |
| **Paint** | Painters filling walls with colour and decoration |
| **Compositing** | Stacking transparent sheets on a projector |