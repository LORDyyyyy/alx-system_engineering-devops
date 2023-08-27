# Simple web stack

## Specifics about this Infrastructure:
1. What is a Server:
A server in this context refers to a physical or virtual machine that stores and manages resources, services, and data. In this infrastructure, it's the central unit responsible for hosting the web application and database.

2. Role of the Domain Name:
The domain name (www.foobar.com) is the user-friendly address that people use to access websites. It's used to translate human-readable domain names into IP addresses that computers use to locate each other on the internet.

3. DNS Record for www:
The DNS record for www in www.foobar.com is a CNAME (Canonical Name) record. It points to the main domain record, effectively making it an alias for the base domain.

4. Role of the Web Server (Nginx):
The web server (Nginx) handles incoming HTTP requests from users' browsers. It can serve static content directly to users, manage SSL encryption, and also act as a reverse proxy by forwarding requests to the application server for dynamic content.

5. Role of the Application Server:
The application server executes the business logic of the web application. It processes requests, interacts with the database to retrieve or store data, generates dynamic content, and sends responses back to the web server for delivery to users.

6. Role of the Database (MySQL):
The database stores and manages structured data that the application requires. In this case, MySQL is used to hold website data like user accounts, posts, comments, etc. The application server communicates with the database to perform read and write operations.

7. Server Communication with Users:
The server communicates with the user's computer using the HTTP protocol. When a user accesses the website, their browser sends an HTTP request to the server. The server processes the request and sends back an HTTP response, which the browser then renders as a webpage.

## Issues with the Infrastructure:

1. Single Point of Failure (SPOF):
This infrastructure has a single server hosting all components. If the server goes down due to hardware failure, software issues, or other reasons, the entire website becomes inaccessible. There's no redundancy to ensure continued service.

2. Downtime During Maintenance:
Whenever maintenance or updates are needed, such as deploying new code, the web server needs to be restarted. During this time, the website might experience downtime, leading to a poor user experience.

3. Limited Scalability:
The infrastructure lacks scalability. If the website experiences a surge in traffic, a single server might struggle to handle the load. Scaling up to accommodate more users would be challenging without adding more servers and distributing the load.
