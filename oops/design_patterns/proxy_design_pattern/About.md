#  [Structural Design Patterns]([https://www.geeksforgeeks.org/structural-design-patterns/] )
that allows you to provide the replacement for an another object. Here, we use different classes to represent the functionalities of another class. The most important part is that here we create an object having original object functionality to provide to the outer world. The meaning of word

#### Proxy

is “in place of” or “on behalf of” that directly explains the

### Proxy Method
The Proxy Design Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it.

This pattern is useful when you want to add an extra layer of control over access to an object. 

The **proxy** acts as an intermediary, controlling access to the real object.
￼

A real-world example can be a cheque or credit card as a proxy for what is in our bank account. It can be used in place of cash and provides a means of accessing that cash when required. 

* And that’s exactly what the Proxy pattern does – ” Controls and manages access to the object they are protecting”.
* As in the decorator pattern, proxies can be chained together. The client, and each proxy, believe it is delegating messages to the real server:
