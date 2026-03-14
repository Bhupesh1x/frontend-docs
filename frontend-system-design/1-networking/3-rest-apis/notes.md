## Rest API's

- **API (Application Programming Interface)**: If we have two different programming services and we want to connect them or have communication between them then we can use api's for it.

- **REST**: Representational State Transfer it defines how the data transferred in communication between two services should be structured.

- Rest is build on top of HTTP protocol and it provides foundation how the data and be delivered or transferred on the web.

**Benefits of REST Api's**

- **1. Ease of use**: It is easy to use as it is build on top of HTTP and follows the predefined set of rules.
- **2. Stateless**: Rest apis don't maintain the state between the request. Each individual request is on it's own and take the relevant information for the current request.
- **3. Scalability**: Scaling REST Api's is easy as the load increases we can do the horizontal or vertical scaling.
- **4. Flexibility of data**: Based on the use case we can choose the data format suits our need in REST Api's like JSON or XML.
- **5. Uniform interface**: As REST is built on top of HTTP there are set of rules and standard which is followed while communication so the request and response follow a particular convention.
- **6. Caching**: We can also cache the data which doesn't change much often to reduce the load on the server. And as REST uses HTTP we get default HTTP level caching with it.
- **7. Separation of concern**: The two services connected doesn't have to be on the same language and they don't need to be depended on each other.
- **8. Language agnostic**: The two services connected doesn't have to be on the same language they can be written on the different languages and can be connected with each other with the help of REST api's.
- **9. Ease of Testing**: Testing REST Api's is very easy and efficiently using different services like REST.
- **10. Security**: We can use REST with Https which provides out of the box security to the api's and also we can leverage Auth headers to include security in the api's services.

**Building blocks of the rest api's**

**1. URL**

- URL is used to reach to the method which needs to be executed. It consist of different parts which help us to get to and execute the correct method.

- Eg. http://localhost:5000/api/users | http://localhost:5000/api/todos

- In this /api/path and /api/todos are the path. Which help us determine which method to execute in the server route.

- ![url parts](./images/url-parts.png)

**2. Methods**

- We have few different methods available for different operations:

- Get: Get method is used for getting/receiving some data from the server
- Post: Post method is used for sending some data to the server for saving or creating some entry on the server.
- PUT/PATCH: We use PUT/PATCH to update the existing data using server. PUT method is used when we want to update the full record and if we want to make the partial update then we use PATCH method.
- DELETE: Delete method is used for deleting some data from the server.
- HEAD: Head method is used for getting data related to some Headers from the server.
- OPTIONS: Options method is used for some security checks made before actual request to check if the requested server allows the client request or not.
- CONNECT: Connect method is used for establish the connection between the client and server. So the next time we make the request the extra hop of handshake is not needed in the next set of requests.
- TRACE: Trace method is used for tracing some information on the server to check if everything is going correctly and diagnose any issue. It is mostly used in the DEV mode as we don't want to leak any info on the prod.

**3. Headers**

- In each request there are some headers are set which defines the things about the request and response.

- Some of the important request headers:

- Request Headers: 

| Header   | Use case | Example     |
|--------|-----|----------|
| Host  | Target Host  | https://www.1.cdn.example.com |
| Origin  | Origin Host  | https://www.example.com |
| Referrer  | Indicate the previous page making the request  | https://www.example.com/123 |
| User Agent  | Indicate the client User agent string - OS, Browser  | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 |
| Accept  | Indicate which all content type is accepted in response  | application/json |
| Accept-Language  | Preferred response content language  | en-US,en;q=0.9 |
| Accept-encoding  | Encoding algorithm  | gzip, deflate, br, zstd |
| Connection  | Keep TCP connection open/close configuration  | keep-alive/close |
| Authorization  | Send auth credentials  | Authorization: Bearer {token} |
| Cookie  | Previous server token can be resend | key=value; |

- Response Headers:

| Header   | Use case | Example     |
|--------|-----|----------|
| Date  | Generated response Date and time  | Sat, 14 Mar 2026 12:12:11 GMT |
| server | Provides server info  | cloudflare/nginx |
| Content-Type | Type of response content  | application/json text/html |
| Content-Length | Original body response length  | 73 |
| Set-cookie | Informs about cookie  | Set-cookie: token=ey123ytre |
| Content-Encoding | Response content encoding  | br |

**4. Status Code**

- When we make the request when it get's resolved we get some status code with it. It helps us identify what happened with the request. Did it get successful or failed.

- Different Status Codes:

| Status Code range | range Use Case | Status Code | Use Case |
|----------|----------|----------|----------|
| 1xx  | Information  | 100 <br/> 101  | 100 - Continue <br/> 101 - Switching (HTTP - ws)  |
| 2xx  | Success  | 200<br/>201<br/>202<br/>204<br/>206  | 200 - OK (Work is done) <br/> 201 - Created <br/> 202 - Accepted (Request accepted successfully used when doing some async work) <br/> 204 - No Content (Work done but no content to sent eg. Delete data) <br/> 206 - Partial Content (Sent or received partial data successfully can be used when there is chunk of data saved successfully from the big chunk)  |
| 3xx  | Redirection  | 301 <br/> 302  | 301: Moved permanently <br/> 302: Moved temporary <br/> 307: Moved temporary but persist the method <br/> 308: Moved permanently but persist the method |
| 4xx  | Client side error  | 400 <br/> 401 <br/> 403 <br/> 404 <br/> 405  | 400: Bad Request (Got the incorrect data) <br/> 401: Unauthorized (not logged in) <br/> 403: Authorization (Logged in but not authorized to access this resource) <br/> 404: Not found <br/> 405: Method not allowed  |
| 5xx  | Server side error  | 500 <br/> 502 <br/> 503 <br/> 504 <br/> 507  | 500: Internal server error <br/> 502: Bad gateway <br/> 503: Service Unavailable (Server is down) <br/> 504: Gateway timeout (Server was processing something but it took server more time then expected)<br/> 507: Insufficient storage (Mostly with file upload/download requests)   |

- We can also handle frontend based on this status codes. And also can apply retry logic like if we are getting 503 we can retry as the server was down and might get up in sometime. But with status code 400 there is no point in retrying as we will get the same error again and again as the request is faulty.
