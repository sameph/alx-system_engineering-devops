  
		Database administration
	0x14. MySQL - DevOps - SysAdmin - MySQL
Intro.

A database is a structured collection of data that is organized and stored for efficient retrieval and manipulation.

Types of databases:
- Relational databases use tables to organize data and are accessed using SQL or NoSQL queries.

- Distributed databases store records in multiple locations and can be homogeneous or heterogeneous.

- Cloud databases are built in a public, private or hybrid cloud environment.

- NoSQL databases are good for dealing with large collections of distributed data.

- Object-oriented databases organize data using object-oriented programming languages.

- Graph databases store, map, and query relationships using concepts from graph theory.

- Database challenges include data security, data integrity, database performance, and database integration.

- A database management system (DBMS) enables users to create and manage a database, - DBMS helps users manipulate data, control access, and provide different views of the database.

A database replica
often referred to as a database replica set, is a copy of a database that is kept synchronized with the primary database. Replicas are typically used in database systems to achieve specific goals, such as improving performance, ensuring high availability, and enhancing disaster recovery capabilities.

The purposes and benefits of having database replicas are as follows:

High Availability: Database replicas help ensure high availability by allowing for failover. If the primary database server goes down, one of the replicas can be promoted to take its place, minimizing downtime and ensuring continuous access to the data.

Load Balancing: Replicas can distribute read operations, such as SELECT queries, to share the load and improve overall database performance. This is known as load balancing and helps prevent the primary server from becoming a performance bottleneck.

Disaster Recovery: Database replicas act as a safety net in case of catastrophic failures or data corruption. If the primary database is compromised or lost, replicas can be used to restore the data to a previous state.

Backup and Reporting: Replicas can be used for backup purposes without affecting the performance of the primary database. They are also valuable for running analytical or reporting queries, as these operations can be offloaded to replicas.

Storing database backups in different physical locations: the primary reason is disaster recovery and data protection. Storing backups in multiple physical locations provides redundancy and helps mitigate various risks, such as:

Upgrade to paid

Primary-replica cluster: “master-slave”:
A primary-replica cluster, also known as a master-slave cluster or primary-secondary cluster, is a type of architecture used in various distributed computing and database systems. It consists of two or more servers, where one server acts as the primary (or master) and the others as replicas (or slaves). This architecture is commonly used for achieving specific goals such as high availability, load balancing, and fault tolerance. Here's how it works:

Primary Server (Master):

The primary server is considered the authoritative source of data.

It handles write operations and is responsible for managing the primary copy of the data.

Any updates or changes to the data are made on the primary server.

Replica Servers (Slaves):

Replica servers maintain a copy of the data from the primary server.

They handle read operations, such as SELECT queries, and serve as backup or standby systems.

Data on replica servers is synchronized with the primary server to ensure that it stays up-to-date.

https://www.researchgate.net/figure/Master-slave-architecture_fig1_317299391
