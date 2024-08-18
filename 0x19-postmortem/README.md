Issue Summary

13/10/2023 from 11:15 AM to 12:00 AM UTC+1 all requests for our homepage to the servers got a 404 error response

Timeline

· 11:10 AM : Updates push

· 11:15 AM : Observing the problem

· 11:15 AM : Informing the front end and backend handlers

· 11:20 AM : Rollback change executed

· 11:24 AM : Restarting server begin

· 11:27 AM : Traffic fully back online (100%)

· 11:30 AM : Began debugging and push further with the problem

· 11:50 AM : Issue fixed and changes pushed

· 11:55 AM : Began restart of the server

· 11:00 AM : Traffic back 100% online plus the new updates.

Root cause and resolution

After rolling back changes we knew that the changes were made by the front end team so we took the broken changes and run them on a test server which replicated same problem, our server uses apache2 and apache2 error logs didn't give enough information about the problem so we traced the apache2 process using strace and when a request is sent strace tool catches a lot of error and after some scanning for these errors we found the error which is a typo in page file extension. After fixing the error we pushed back the changes and restarted the servers at 11:00 AM, traffic came back online 100% with the 00000 new updates.

Corrective and preventative measures

In order to prevent the occurrence of similar problems from happening again there is a need to:

· Create an automated test pipeline for every update push

· Add a monitoring software to our servers which will monitor lot of things and one of them Network Traffic requests’ and responses and configure it to make an alert to the teams when too much non desired responses were sent like 404

· Create a test for every new update and the teams should not push until those tests pass.







