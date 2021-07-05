Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:




| Azure Resource           | Service Tier   | Monthly Cost |
| ------------             | ------------   | ------------ |
| *Azure Postgres Database*| *Basic*        | *$30.30*     |
| *Azure Service Bus*      | *Basic*        |  *$0.01*     |
| *Azure App service plan* | *Free tier*    | *$0*         |
| *Azure storage*          |    *Basic*     | *$0.10*      |


The app service includes the web app and the function app.

**Explanation**
The azure web app was already available, all I had to was to change the environment variables within config.py. The web app provides better performance and user experience. It's cost effective to share one app service plan and scale independently in the future.The costs of the services are reasonable, outside of the PostgreSQL database, which is by far the most expensive part of the architecture.

Other than the database, everthing else is available at a reasonable cost.
