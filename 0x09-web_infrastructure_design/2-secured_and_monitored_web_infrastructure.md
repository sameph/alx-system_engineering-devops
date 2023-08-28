
2-secured_and_monitored_web_infrastructure
![eoF4x2Q](https://github.com/nadisan/alx-system_engineering-devops/assets/76504146/d3dac336-25ad-4d4e-9a29-c1c70e8bc520)



Firewall: A firewall is needed to protect the server from unauthorized access and malicious attacks.


Monitoring: Monitoring tools should be used to monitor the health of the server, application, and database.

SSL Certificate: An SSL certificate should be installed on the server to enable secure communication between the server and clients.



Issues with 2-secured and monitored web infrastructure

1. Terminating SSL at the load balancer level: 
Terminating SSL at the load balancer level can create security issues because it means that the data is decrypted at the load balancer before being sent to the backend servers. This means that if the load balancer is compromised, all the data passing through it could be exposed. Additionally, terminating SSL at the load balancer level can also cause performance issues because the load balancer has to decrypt and re-encrypt all traffic, which can add latency and reduce throughput.

2. Having only one MySQL server capable of accepting writes:
Having only one MySQL server capable of accepting writes can create a single point of failure. If this server goes down, the entire application will be unable to write data to the database, which can result in data loss or downtime. Additionally, having only one server can also limit scalability because it means that all write traffic has to go through a single server, which can become a bottleneck as traffic increases.

3. Having servers with all the same components:
Having servers with all the same components (database, web server, and application server) can create a lack of flexibility and scalability. For example, if there is a sudden increase in traffic to the application, scaling up may require scaling up all components (database, web server, and application server) even if only one component is experiencing high traffic. This can result in wasted resources and increased costs. Additionally, having all components on the same server can create resource contention issues, where one component may consume all available resources, impacting the performance of other components.
