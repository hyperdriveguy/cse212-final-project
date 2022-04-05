# Queues

## Introduction

Queues are distinguished by their *first in, first out* or "FIFO" data access.
We see examples of FIFO in real life, most commonly in the forms of lines of people.
Another way to think of it is "first come, first served".
In the realm of computing, queues are using to preserve the order of data.
For example, when a computer is requesting data from an external device, it can't process
it all at once; keeping bytes in their proper order is important so that data isn't
corrupted.

## Diagram

Let's first look at a more abstract example of a queue using a line at an amusement park:

![Amusement park example](pictures/queue-abstract-example.drawio.svg)

As we see, when a ride is ready for new riders, it *dequeues* that many riders out
of the front of the line to get on the ride. When a new rider enters the back of the
line, the rider is *enqueued*.

Let's see a second, less abstract abstract example of using a queue to preserve the
order of the alphabet:

![Alphabet example](pictures/queue-alpha-example.drawio.svg)

Notice how the queue preserves the order when enqueuing and dequeuing.

## Performance

| Common Queue Operation |                        Description                       |    Performance   |
|:----------------------:|:--------------------------------------------------------:|:----------------:|
| enqueue(value)         | Adds "value" to the back of the queue                    | O(1)             |
| dequeue()              | Removes and returns the item from the front of the queue | O(n) or O(1)[^1] |
| size()                 | Returns the size of the queue                            | O(1)             |
| empty()                | Returns true if the length of the queue is zero.         | O(1)             |

[^1]: Performance is only O(n) time if the backing data structure is an array.
Other backing structures, such as linked lists, can return values more efficiently.
