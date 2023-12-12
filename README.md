When you type "https://www.google.com" in your browser and press Enter. This is a fundamental process that occurs when a user requests a web page. I'll break it down step by step:

DNS Request (Domain Name System):**
DNS, or Domain Name System, is a critical component of the internet that acts as a directory service for translating human-friendly domain names (like www.google.com) into IP addresses (like 192.168.1.1) that computers and networking equipment use to locate each other on the internet.

- When you type the URL "https://www.google.com" in your browser and press Enter, the first thing that happens is a DNS request.

Your computer will first check its local DNS cache to see if it has recently resolved that domain. If it finds a match, it uses the cached IP address and doesn't need to go further.

If the IP address isn't in the local cache, your computer sends a query to a DNS resolver server. This resolver can be provided by your Internet Service Provider (ISP) or a third-party DNS service like Google DNS or Cloudflare DNS.

How to check DNS caching | UNBLOG Tutorialshttps://think.unblog.ch/en/how-to-check-and-query-dns-caching/
Resource https://think.unblog.ch/en/how-to-check-and-query-dns-caching/
Once the browser has the IP address of "www.google.com," it establishes a TCP (Transmission Control Protocol) connection to the web server.

TCP/IP Connection:
TCP is one of the core protocols in the TCP/IP suite, It is responsible for establishing and maintaining a connection between two devices, ensuring the reliable and ordered delivery of data packets.

Key features of TCP include error checking, data sequencing, flow control, and acknowledgment of received data.

IP is another essential component of TCP/IP. IP is another essential component of TCP/IP, It handles the addressing and routing of data packets across a network.

IP assigns unique IP addresses to devices on a network, allowing them to find each other. There are two main versions of IP in use today: IPv4 (32-bit addresses) and IPv6 (128-bit addresses).

Process:
Connection Establishment (TCP)
When two devices wish to communicate using TCP, they go through a three-way handshake process to establish a connection.

The sender (client) sends a SYN (synchronize) packet to the receiver (server). The receiver responds with a SYN-ACK (synchronize-acknowledge) packet. Finally, the sender acknowledges the response with an ACK packet. This handshake ensures both parties are ready to communicate

Three-Way Handshake - an overview | ScienceDirect Topics
Resource https://www.scaler.com/topics/computer-network/tcp-3-way-handshake/
Data Transfer (TCP):
Once the connection is established, data can be transmitted, Data is divided into packets, each with a sequence number, The receiver acknowledges receipt of each packet.

If a packet is lost or corrupted, it is retransmitted. This ensures data reliability and integrity.

Firewalls may inspect individual packets of data as they pass between your computer and the internet, here it comes:
Firewalls
play a crucial role in the context of browsing request sending by acting as a barrier between your computer and the internet. They are designed to enhance the security and control of your network traffic, including web browsing requests. Here's how firewalls work in this context:

1. Packet Filtering:

Firewalls inspect individual packets of data as they pass between your computer and the internet. Each packet contains information about its source, destination, and the type of data it carries.

Firewalls use a set of predefined rules to decide which packets are allowed to pass through and which should be blocked.

In the context of browsing, firewalls can filter out potentially harmful or malicious packets, helping to protect your computer from threats.

2. Port-Based Filtering:

Firewalls can also filter traffic based on the network ports used. Ports are like designated doors for specific types of traffic.

Web browsing typically uses ports 80 (HTTP) and 443 (HTTPS). Firewalls can be configured to allow or block traffic on these ports.

For instance, they can block access to certain websites by blocking traffic on these ports, effectively preventing browsing requests to those sites.

TCP ensures that the SSL/TLS handshake messages are delivered reliably between the client (browser) and the server.

HTTPS/SSL
The HTTPS/SSL handshake is a crucial process that occurs when your web browser sends a request to a secure website (one that uses HTTPS) to establish a secure encrypted connection. It ensures that the data transmitted between your browser and the web server remains confidential and cannot be intercepted or tampered with during transmission. Here's how the HTTPS/SSL handshake works in the context of a browser request:

**1. Initiating the Connection:**

- When you enter a URL with "https://" into your browser's address bar (e.g., https://www.example.com), your browser knows that it needs to establish a secure connection.

- It sends a request to the web server, indicating its intention to establish a secure connection.

**2. Server Authentication (Server Hello):**

- The web server responds with a message that includes its SSL/TLS certificate. This certificate contains the server's public key and is signed by a trusted Certificate Authority (CA).

- Your browser checks if the certificate is valid, not expired, and signed by a trusted CA. If everything checks out, it proceeds to the next step.

**3. Client Key Exchange:**

- Your browser generates a symmetric encryption key, called the "pre-master secret."

- It encrypts this pre-master secret with the server's public key (from the certificate) and sends it back to the server.

**4. Server Key Exchange:**

- The web server decrypts the pre-master secret using its private key, which only the server knows.

- Both the client (your browser) and server now have the same pre-master secret, which will be used for symmetric encryption and decryption of data.

**5. Session Key Creation:**

- The client and server independently derive a session key from the pre-master secret. This session key will be used for encrypting and decrypting data during the current session.

**6. Secure Data Transfer:**

- With the session key established, the browser and server switch to using symmetric encryption for data transfer. This is much faster and efficient than asymmetric encryption used in the initial handshake.

- All data exchanged between your browser and the server is encrypted and can only be decrypted by parties with the session key.

**7. Secure Connection Established:**

- Once the handshake is complete, your browser displays a padlock icon or other indicators to show that the connection is secure.

- You can now safely send your request (such as loading a webpage) over this encrypted connection.

The HTTPS/SSL handshake ensures that the data sent between your browser and the web server is secure and private. It provides encryption, server authentication, and data integrity, making it a fundamental component of secure web browsing.

When a client (such as a web browser) makes an HTTPS request to a web application, it first reaches a load balancer.

a load balancer is a critical component in the architecture after HTTPS/SSL encryption.

The load balancer is typically configured to listen on the HTTPS port (usually 443) to accept secure connections.

Load Balancer:
SSL Termination (Optional):

In some cases, the load balancer can perform SSL termination. This means it decrypts the incoming SSL traffic from clients before forwarding it to backend servers.

Decrypting at the load balancer allows it to inspect and manipulate the traffic, apply security policies, and offload the CPU-intensive SSL decryption from the backend servers.

The load balancer then re-encrypts the traffic before sending it to the backend servers if SSL termination is not performed.

The load balancer uses load-balancing algorithms to distribute incoming requests among multiple backend servers.

This ensures that each server receives a balanced share of the incoming traffic, improving performance and fault tolerance.

Request Forwarding:

The load balancer forwards the client's HTTPS request to one of the backend servers based on the load-balancing algorithm's decision.

It establishes a new SSL connection to the chosen backend server if SSL termination was performed, or it forwards the encrypted request if SSL termination was not done.

Backend Processing:

The selected backend server receives the request, which is typically still encrypted if SSL termination was not performed at the load balancer.

The backend server processes the request, which may involve executing application logic, querying databases, and generating responses.

Web Server:

The web server (e.g., Apache, Nginx) receives the request from the load balancer.

A web server is a software application responsible for handling HTTP requests from clients (usually web browsers) and sending back HTTP responses, which typically include web pages and associated resources.

Static Content Delivery: Web servers are excellent at serving static content such as HTML files, CSS stylesheets, JavaScript files, images, and other assets. These resources are pre-existing files that don't change in response to user interactions.

In many cases, especially for high-traffic websites, web servers work in conjunction with load balancers to distribute incoming requests across multiple backend servers. This ensures even distribution of the workload and improved performance and availability.

Application Server (Optional):

An application server is a software component that specializes in executing server-side code and handling dynamic content generation. It works closely with the web server to deliver interactive and data-driven web applications.

In some cases, there is an application server (e.g., Tomcat, Node.js) that processes dynamic content or executes server-side code (e.g., handling user logins).

Key Functions of an Application Server:

Dynamic Content Generation: Unlike static resources served by the web server, dynamic content varies based on user input, database queries, or other factors. Application servers generate this content on-the-fly. For example, when you log in to a web application, the application server handles the authentication process and retrieves personalized data.

Server-Side Code Execution: Application servers execute server-side scripts or code written in languages like Python, Ruby, Node.js, or Java. This code performs business logic, processes forms, and communicates with databases.

Database Interaction: If an application requires data storage and retrieval, the application server communicates with databases. It can send SQL queries to retrieve or update information in a structured manner.

Session Management: Application servers often manage user sessions, maintaining state information between different HTTP requests. This is crucial for user authentication and maintaining user-specific data.

Database (Optional):

Databases are specialized software systems designed for storing, organizing, and retrieving structured data efficiently.

Key Functions of a Database:

Data Storage: Databases store data in structured tables, ensuring data integrity and consistency. Examples include user profiles, product details, and transaction records.

Data Retrieval: Application servers interact with databases through queries to fetch specific data as requested by users. Databases use query languages like SQL (Structured Query Language) for this purpose.

Data Manipulation: Databases support operations like inserting, updating, and deleting data records. This ensures that data remains accurate and up-to-date.

Data Security: Databases implement security features such as user authentication, authorization, and encryption to protect sensitive data.

Scalability: Databases can be designed to scale horizontally (adding more servers) or vertically (increasing server resources) to handle growing data loads.

https://medium.com/@kenneth.ca95/what-happens-when-you-type-a-url-in-your-browser-and-press-enter-97e74d2a802
