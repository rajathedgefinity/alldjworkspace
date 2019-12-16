# Extending Existing User Model with a Proxy.

## Using a Proxy Model

### What is a Proxy Model ?

It is a model inheritance without creating a new table in the database. It is used to change the behaviour of an existing model (e.g. default ordering, add new methods, etc.) without affecting the existing database schema.

### When should I use a Proxy Model?

You should use a Proxy Model to extend the existing User model when you don’t need to store extra information in the database, but simply add extra methods or change the model’s query Manager.
