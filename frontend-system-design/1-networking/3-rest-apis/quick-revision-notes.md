## REST APIs — Quick Revision

---

**What Is REST?**
- **API** — A contract that lets two services communicate without knowing each other's internals
- **REST** — Rules for how to structure that communication over HTTP
- Built on HTTP, stateless, language agnostic, uses JSON mostly

---

**Benefits (one-liner each)**

| Benefit | What It Means |
|---------|--------------|
| **Ease of Use** | Built on HTTP — familiar rules, easy to pick up |
| **Stateless** | No session memory on server — every request is self-contained |
| **Scalable** | Statelessness makes horizontal scaling easy |
| **Flexible Data** | Supports JSON, XML, plain text etc. |
| **Uniform Interface** | Consistent conventions across all REST APIs |
| **Caching** | Free HTTP-level caching built in |
| **Separation of Concerns** | Frontend and backend are independent |
| **Language Agnostic** | Python backend, React frontend — REST doesn't care |
| **Easy Testing** | Test with Postman, Insomnia, or curl |
| **Security** | HTTPS + Auth headers = secure by default |

---

**1. URL Structure**
```
https://api.example.com:5000/api/users/42?page=1
  │          │             │     │       │
protocol    host          port  path   query params
```

REST path conventions:
- `GET /api/users` → all users
- `GET /api/users/42` → single user
- `POST /api/users` → create user
- `PATCH /api/users/42` → partial update
- `DELETE /api/users/42` → delete user

---

**2. HTTP Methods**

| Method | Use | Changes Data? |
|--------|-----|---------------|
| **GET** | Read data | ❌ No |
| **POST** | Create new resource | ✅ Yes |
| **PUT** | Replace full resource | ✅ Yes |
| **PATCH** | Partial update only | ✅ Yes |
| **DELETE** | Remove resource | ✅ Yes |
| **HEAD** | Get headers only, no body | ❌ No |
| **OPTIONS** | CORS preflight check | ❌ No |
| **TRACE** | Debug only — disabled in prod | ❌ No |

> **PUT vs PATCH:** PUT replaces everything. PATCH updates only what you send.

---

**3. Key Headers**

**Request:**

| Header | Purpose |
|--------|---------|
| `Host` | Target server |
| `Authorization` | `Bearer <token>` for auth |
| `Accept` | Expected response format (`application/json`) |
| `Content-Type` | Format of request body (`application/json`) |
| `Cookie` | Send stored cookies |
| `Origin` | Where request comes from (CORS) |

**Response:**

| Header | Purpose |
|--------|---------|
| `Content-Type` | Format of response (`application/json`) |
| `Set-Cookie` | Tell client to store a cookie |
| `Content-Length` | Size of response body |
| `Server` | Server software info |

---

**4. Status Codes**

| Range | Category | Key Codes |
|-------|----------|-----------|
| **1xx** | Informational | 101 Switching Protocols (HTTP → WS) |
| **2xx** | Success | 200 OK, 201 Created, 202 Accepted (async), 204 No Content, 206 Partial |
| **3xx** | Redirect | 301 Permanent, 302 Temporary, 307 Temp (keeps method), 308 Perm (keeps method) |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthenticated, 403 Forbidden, 404 Not Found, 429 Rate Limited |
| **5xx** | Server Error | 500 Crash, 502 Bad Gateway, 503 Down, 504 Timeout, 507 No Storage |

**Quick memory aids:**
- `401` = "Who are you?" (not logged in)
- `403` = "I know you, but no." (not authorized)
- `503` → worth retrying (server was temporarily down)
- `400` → don't retry (your request is wrong)

---

**Status Code Decision Tree for Frontend**
```
Response received
      │
   2xx? ──▶ ✅ Show success
      │
   4xx?
   ├── 401 ──▶ Redirect to login
   ├── 403 ──▶ Show "Access Denied"
   ├── 404 ──▶ Show "Not Found"
   └── 400 ──▶ Show validation error (don't retry)
      │
   5xx?
   ├── 503 ──▶ Retry after delay
   └── 500 ──▶ Show generic error
```

- Practical example of rest api at - /practical
