1-distributed web infrastructure
![SHXYonm](https://github.com/nadisan/alx-system_engineering-devops/assets/76504146/7ad47db7-d588-4614-bde9-f09f92a8109d)



	Load Balancer: A load balancer like HAProxy can be used to distribute incoming traffic across multiple servers,
	       ensuring that no single server is overloaded. It will be installed on one server.
	The load balancer will be configured with a round-robin distribution algorithm, which distributes incoming traffic evenly across all		   servers. This ensures that no single server is overloaded and that all servers are utilized efficiently.

	The load-balancer will enable an Active-Active setup, which means that all servers are actively serving traffic at all times. In an 		   Active-Passive setup, one server is designated as the primary server and serves traffic while the other servers remain idle
               until the primary server fails. This setup can result in wasted resources and slower response times.

	In a database Primary-Replica (Master-Slave) cluster, the primary node is the main database server that receives all write requests 		   and updates. The replica nodes are secondary servers that receive copies of the data from the primary node
	       and can be used for read requests. The primary node is responsible for ensuring data consistency across all nodes.
	
	The primary node is responsible for handling all write requests and ensuring data consistency. The replica nodes are used for read
		 requests and do not have the same level of responsibility as the primary node.

The issues are with this infrastructure
	1. Single Point of Failure (SPOF): The load balancer and database server are both SPOFs. If either of these servers fails, the entire infrastructure will be affected.

	2. Security issues: There is no firewall or HTTPS configured, leaving the infrastructure vulnerable to attacks.

	3. No monitoring: Without monitoring tools in place, it will be difficult to identify and address issues with the infrastructure in a timely manner.
