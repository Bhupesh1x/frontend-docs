## Communication Protocols

When two systems need to communicate over the internet, they follow a set of rules called a **protocol**. Different protocols exist because different use cases have different needs, some need reliability, some need speed, some need security, some need live two-way communication.

> 💡 **Analogy:** Think of protocols like different modes of transport. TCP is like a courier with tracking (reliable, confirmed delivery). UDP is like dropping a flyer from a plane (fast, but some might not land). HTTPS is like a courier with a sealed tamper-proof box (secure + tracked).

---

**1. TCP (Transmission Control Protocol)**

TCP is a **connection-oriented, reliable** protocol. Before any data is sent, it establishes a connection using the **3-way handshake** (covered in detail in the "How the Web Works" doc).

**How it works:**
- Client sends a **SYN** → "Hey, are you available?"
- Server replies with **SYN-ACK** → "Yes, ready. Here's a sequence number to track packets."
- Client sends **ACK** → "Got it. Connection established."

The sequence numbers are key, they allow TCP to detect if any packets are lost and **re-send them automatically**. This guarantees that all data arrives completely and in the correct order.

> 💡 **Analogy:** TCP is like sending a parcel with a courier that requires a signature. The courier confirms delivery, and if the parcel gets lost, they send it again. Slower, but nothing gets lost.

**Use cases:** Web browsing, email, file transfers, anything where data integrity matters.

---

**2. UDP (User Datagram Protocol)**

UDP is a **connectionless, fast** protocol. There is no handshake, no connection setup, you just fire packets and move on.

**How it works:**
- Client sends data directly to server, no setup, no confirmation
- Server may or may not receive all packets, **no re-sending of lost packets**
- What you gain: **speed**. What you lose: **reliability**

> 💡 **Analogy:** UDP is like shouting across a noisy room. You say what you need to say as fast as possible. Maybe the other person hears everything, maybe they miss a word, but the conversation keeps moving.

**When is packet loss acceptable?**
In a video call, if one frame drops, the video skips a tiny moment, that's fine. You don't want the call to freeze and re-send old frames just to maintain order.

**Use cases:** Video conferencing, live streaming, online gaming, DNS lookups.

---

**3. HTTP (HyperText Transfer Protocol)**

HTTP is the foundation of data communication on the web. It runs **on top of TCP**, meaning TCP is used to establish the connection, and then HTTP defines the format of the request and response.

**How it works:**
1. Browser establishes a **TCP connection** with the server
2. Browser sends an **HTTP request** (e.g. `GET /index.html`)
3. Server responds with an **HTTP response** (e.g. HTML, JSON, etc.)
4. Connection closes

**Important:** In HTTP/1.1, each request-response cycle used to require its own TCP connection (or kept alive briefly). This added overhead.

**Structure of an HTTP Request:**
```
GET /home HTTP/1.1
Host: www.example.com
Accept: text/html
```

**Structure of an HTTP Response:**
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

**Use cases:** Web browsing, REST APIs, fetching web page resources.

---

**4. HTTPS (HTTP Secure)**

HTTPS is HTTP with an added **encryption layer** using **SSL/TLS**. The data transfer works the same way as HTTP, but nothing can be read by anyone intercepting the connection.

**How it works (extra step vs HTTP):**
1. TCP connection established (same as HTTP)
2. **SSL/TLS Handshake** — server sends its certificate (public key), client verifies it, both sides agree on an encryption key
3. All HTTP requests and responses from this point are **fully encrypted**

**HTTP vs HTTPS:**

| | HTTP | HTTPS |
|-|------|-------|
| Encrypted | ❌ No | ✅ Yes |
| SSL/TLS Handshake | ❌ No | ✅ Yes |
| Safe on public Wi-Fi | ❌ No | ✅ Yes |
| URL starts with | `http://` | `https://` |

> 💡 **Analogy:** HTTP is a postcard, anyone handling it can read it. HTTPS is a sealed, tamper-proof envelope, only the recipient can open and read it.

**Use cases:** All modern web browsing, login pages, payment pages, APIs.

---

**5. HTTP/3 (QUIC)**

HTTP/3 is the latest version of HTTP. Instead of running on TCP, it runs on **QUIC**, a protocol built on top of **UDP**.

**Why switch from TCP to UDP?**
TCP's reliability guarantees come at a cost, if one packet is lost, everything waits. This is called **Head-of-Line Blocking**. HTTP/3/QUIC solves this by handling multiple streams independently over UDP.

**What HTTP/3 adds on top of UDP:**
- **Built-in encryption** (TLS 1.3 baked in, no separate SSL handshake)
- **Header compression** — reduces redundant data sent with each request
- **Multiplexing** — multiple requests over one connection without blocking each other
- **Connection migration** — your connection survives switching from Wi-Fi to mobile data

> ✏️ **Correction from original notes:** Your notes mention HTTP/3 "can lose some packets", this is technically true of the underlying UDP, but QUIC itself handles reliability per-stream. So in practice, HTTP/3 is both fast **and** reliable, it gets the best of both worlds.

**Use cases:** Video streaming, IoT, Virtual Reality, mobile-heavy apps.

---

**6. WebSocket**

WebSocket enables **full-duplex, real-time communication** — meaning both the client and server can send messages to each other at any time over a single persistent connection.

**How it works:**
1. Client makes a normal **HTTP request** with an `Upgrade` header
2. Server agrees → connection is **upgraded from HTTP to WebSocket (ws://)**
3. A single long-lived connection stays open
4. Both sides can now push data to each other freely, no need to make a new request each time

**HTTP vs WebSocket:**

| | HTTP | WebSocket |
|-|------|-----------|
| Direction | Client requests, server responds | Both sides send freely |
| Connection | Opens and closes per request | Single persistent connection |
| Real-time? | ❌ Polling needed | ✅ Native push |
| Use case | Fetching pages/data | Live chat, live feeds |

> 💡 **Analogy:** HTTP is like sending letters back and forth, you write, wait for a reply, then write again. WebSocket is like a phone call, once connected, both people can speak and listen at any time.

**Use cases:** Live chat apps, real-time dashboards, collaborative tools (like Google Docs live editing), stock tickers.

---

**7. SMTP (Simple Mail Transfer Protocol)**

SMTP is the protocol used for **sending emails**. It is a one-directional push protocol, the sender pushes the email to an SMTP server, which then routes it to the recipient's mail server.

**How it works:**
1. You hit "Send" in your email client
2. Your client connects to your **SMTP server** (e.g. Gmail's SMTP)
3. SMTP server looks up the recipient's mail server (via DNS MX records)
4. Your SMTP server **pushes the email** to the recipient's mail server
5. Recipient retrieves the email using a different protocol (**IMAP** or **POP3**)

> 💡 **Note:** SMTP is only for **sending**. Reading/receiving emails uses **IMAP** (syncs across devices) or **POP3** (downloads and removes from server).

**Use cases:** Sending emails, transactional emails (order confirmations, OTPs), newsletters.

---

**8. FTP (File Transfer Protocol)**

FTP is a protocol specifically designed for **transferring large files** between systems. It uses two separate connections, one for commands (control) and one for actual data transfer.

**How it works:**
- Client connects to FTP server
- Authenticates (username/password)
- Can upload or download files of any size

**FTP vs HTTP for file transfer:**

| | HTTP | FTP |
|-|------|-----|
| Designed for | Web pages, APIs | File transfer |
| Large files | Possible but needs chunking/streaming | Native, built for it |
| Resumable transfers | ❌ Not natively | ✅ Yes |
| Authentication | Optional | Usually required |

> 💡 **Note:** SFTP (SSH File Transfer Protocol) is the secure, modern version of FTP, it encrypts the transfer. FTPS is FTP with SSL/TLS added.

**Use cases:** Uploading files to a web server, transferring large datasets, deploying website files.

---

## Summary Table

| Protocol | Based On | Reliable? | Encrypted? | Connection Type | Key Use Case |
|----------|----------|-----------|------------|-----------------|--------------|
| **TCP** | — | ✅ Yes | ❌ No | Connection-oriented | Foundation for HTTP/HTTPS |
| **UDP** | — | ❌ No | ❌ No | Connectionless | Video calls, gaming |
| **HTTP** | TCP | ✅ Yes | ❌ No | Request/response | Web browsing |
| **HTTPS** | TCP + TLS | ✅ Yes | ✅ Yes | Request/response | Secure web browsing |
| **HTTP/3** | UDP (QUIC) | ✅ Per stream | ✅ Yes | Multiplexed | Streaming, mobile |
| **WebSocket** | HTTP → WS | ✅ Yes | Optional | Persistent, full-duplex | Live chat, real-time |
| **SMTP** | TCP | ✅ Yes | Optional | Push (one-way) | Sending emails |
| **FTP** | TCP | ✅ Yes | ❌ No | Two-channel | File uploads/downloads |

- ![communication-protocols](./images/communication-protocols.png)