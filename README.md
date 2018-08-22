# Quickfix-Tradeclient-Django
Django Web User Interface that take required inputs and sends it to a quickfix tradeclient thorough the RabbitMQ messaging broker.

Installation
------------
Make sure latest Python and Django are installed.
Navigate to the `quickfix-tradeclient-django` repository directory, and run command

```
python3 ./manage.py runserver 8080
```

Example
-------
Run the web application, and got to page:`localhost:8080/form`

Make sure the RabbitMQ-server is running, fill the form and sumbit.
The order will be sent to exchange="" and queue="orders"

To see the message in queue from terminal, use rabbitmqadmin as follows:

`>>>rabbitmqadmin get queue="orders" requeue=false`

(Another page :8080/form/plot shows a scatter plot with dummy variable used for testing)

Other rabbitmqadmin useful commands:

To list available exchanges:
`rabbitmqadmin -V test list exchanges`

To list details of available queues:
`rabbitmqadmin -f long -d 3 list queues`

See other commands:
```
rabbitmqadmin --bash-completion
rabbitmqadmin --help
rabbitmqadmin help subcommands
```

Screenshots
-----------
url `../form/` gives a form for users to input desired information for a trade with our quickfix tradeclient:

![/form](https://user-images.githubusercontent.com/40487507/43889986-39d01654-9bce-11e8-8515-2bb320bfa563.png)


url `../form/plotly` is a scatterplot with dummy data, used for testing:

![/plotly](https://user-images.githubusercontent.com/40487507/43890022-4ea04b8a-9bce-11e8-9f8a-f6b5ea065152.png)
