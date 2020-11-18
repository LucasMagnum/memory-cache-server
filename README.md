Memory Cache Server
==========================

This is an extremely simple implementation of a memory cache server using a hash table.

It will instantiated a dictionary in Python and keep its values in memory until the server is closed.

Python 3.8+


How to connect
==============

Start the server, running the following command:

    $ python server.py
    Serving on ('127.0.0.1', 5000)

Open a connection to the server. Ex:

    $ telnet 127.0.0.1 5000
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.

Execute commands:

    SET key value
    OK
    GET key
    value
    DELETE key
    OK
    GET key
    NOT_FOUND
    EXIT
    Connection closed by foreign host.


How to test
===========

To run the tests, run the following commands:

    pip install -r requirements.txt
    pytest tests.py


API
===

The communication with the server is through the set of commands available:

    SET, GET, DELETE

SET
---
Use the SET command to add a value to a key. Ex:

    SET key value


GET
---
Use the GET command to retrieve a value added to a key. Ex:

    GET key


DELETE
------
Use the DELETE a key. Ex:

    DELETE KEY