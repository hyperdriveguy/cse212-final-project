"""Implement a queue for PS5 backorders.
"""

# This example uses the deque structure to provide O(1) for both
# enqueue and dequeue operations.
from collections import deque

class Queue:
    """Implementation of a queue using a "deque".

    By the time all the challenges are completed, all functions
    that exist in the reading should be available and have output
    that corresponds to the test below.
    """

    def __init__(self, elements=None):
        if elements is None:
            self.queue = deque()
        else:
            self.queue = deque(elements)

    # Challenge: add items to the end of the queue
    def enqueue(self, value):
        """Adds a value to the end of the queue.

        Args:
            value (any): added value
        """
        self.queue.append(value)

    def dequeue(self):
        """Removes and returns the value at the end of the queue.

        Returns:
            any: value
        """
        if len(self.queue) >= 1:
            return self.queue.popleft()
        return None

    def __str__(self):
        return self.queue.__str__()[6:-1]

    def __len__(self):
        """Length of the queue

        Returns:
            int: queue length
        """
        return len(self.queue)

    @property
    def empty(self):
        """Check if queue is empty

        Returns:
            bool: True if empty, False otherwise
        """
        return len(self.queue) == 0

# Amusement park line example

# Make a queue for a line with people in it
ride_line = \
    Queue(['Rider 1', 'Rider 2', 'Rider 3', 'Rider 4', 'Rider 5', 'Rider 6', 'Rider 7', 'Rider 8'])

# A new rider entered the end of the line
ride_line.enqueue('Rider 9')

# ['Rider 1', 'Rider 2', 'Rider 3', 'Rider 4', 'Rider 5', 'Rider 6', 'Rider 7', 'Rider 8', 'Rider 9']
print(ride_line)

# The ride finished a cycle and has 5 open seats
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()

# ['Rider 6', 'Rider 7', 'Rider 8', 'Rider 9']
print(ride_line)

# A new rider entered the end of the line
ride_line.enqueue('Rider 10')

# The ride finished a cycle and has 5 open seats
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()

# []
print(ride_line)

# True
print('Line empty:', ride_line.empty)

# Two new riders at the end of the line
ride_line.enqueue('Rider 11')
ride_line.enqueue('Rider 12')

# ['Rider 11', 'Rider 12']
print(ride_line)

# The ride finished a cycle and has 5 open seats
ride_line.dequeue()
ride_line.dequeue()
# These should not return anything but still successfully run
ride_line.dequeue()
ride_line.dequeue()
ride_line.dequeue()

# []
print(ride_line)

class TieredQueue:
    """The Playstation 5 is a widely sought after game console.
    As such, many companies have started paid memberships that
    give priority to members over others. In this challenge,
    you will use multiple "tiered" queues that supersede others
    whenever there are any customers in that queue.
    """

    def __init__(self):
        self.platinum_members = Queue()
        self.gold_members = Queue()
        self.bronze_members = Queue()
        self.non_members = Queue()

    # Challenge: enqueue customers based on priority
    def enqueue(self, customer:str, priority:int=0):
        """Add customer to a queue based on membership.

        Priority 1: Platinum Members
        Priority 2: Gold Members
        Priority 3: Bronze Members
        Any other: Non-Member

        Args:
            customer (str): customer name
            priority (int): customer membership level
        """
        if priority == 1:
            self.platinum_members.enqueue(customer)
        elif priority == 2:
            self.gold_members.enqueue(customer)
        elif priority == 3:
            self.bronze_members.enqueue(customer)
        else:
            self.non_members.enqueue(customer)

    # Challenge: dequeue customers based on priority
    def dequeue(self):
        """Remove customer from queue based on priority.

        Priority 1: Platinum Members
        Priority 2: Gold Members
        Priority 3: Bronze Members
        Any other: Non-Member

        If any higher priority queue is populated, it should
        always take precedence over the lower priorities.

        Returns:
            str: customer from respective queue
        """
        if not self.platinum_members.empty:
            return self.platinum_members.dequeue()
        if not self.gold_members.empty:
            return self.gold_members.dequeue()
        if not self.bronze_members.empty:
            return self.bronze_members.dequeue()
        return self.non_members.dequeue()

    def __str__(self):
        """All combined queues represented in order.
        """
        plat = self.platinum_members.__str__()[1:-1] + ', '
        if plat == ', ':
            plat = ''
        gold = self.gold_members.__str__()[1:-1] + ', '
        if gold == ', ':
            gold = ''
        bronze = self.bronze_members.__str__()[1:-1] + ', '
        if bronze == ', ':
            bronze = ''
        others = self.non_members.__str__()[1:-1]

        return f'[{plat}{gold}{bronze}{others}]'

    def __len__(self):
        """Combined length of all queues
        """
        return len(self.platinum_members) + len(self.gold_members) + \
            len(self.bronze_members) + len(self.non_members)

    @property
    def empty(self):
        """Check if queue is empty

        Returns:
            bool: True if empty, False otherwise
        """
        return self.__len__() == 0

# Tests

playstation_backorders = TieredQueue()
# This is just to see who has at least one Playstation 5.
# Sets are covered more in depth in the next lesson.
have_playstations = set()

playstation_backorders.enqueue('Jeremy', 2)
playstation_backorders.enqueue('Bode', 1)
playstation_backorders.enqueue('Charles', 1)
playstation_backorders.enqueue('Felica', 2)
playstation_backorders.enqueue('Dilly', 2)
playstation_backorders.enqueue('Jacobo')
playstation_backorders.enqueue('Carcinogen')
playstation_backorders.enqueue('Leety', 3)
playstation_backorders.enqueue('Lilee', 3)
playstation_backorders.enqueue('Kentisha', 2)
playstation_backorders.enqueue('Robbalobbadoo', 1)

# ['Bode', 'Charles', 'Robbalobbadoo', 'Jeremy', 'Felica', 'Dilly', 'Kentisha', 'Leety', 'Lilee', 'Jacobo', 'Carcinogen']
print(playstation_backorders)
assert playstation_backorders.__str__() == \
    "['Bode', 'Charles', 'Robbalobbadoo', 'Jeremy', 'Felica', 'Dilly', 'Kentisha', 'Leety', 'Lilee', 'Jacobo', 'Carcinogen']"

# Orders became available
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())

# Order doesn't matter
# {'Charles', 'Robbalobbadoo', 'Bode'}
print(have_playstations)

# Bode's back for another
playstation_backorders.enqueue('Bode', 1)

# ['Bode', 'Jeremy', 'Felica', 'Dilly', 'Kentisha', 'Leety', 'Lilee', 'Jacobo', 'Carcinogen']
print(playstation_backorders)
assert playstation_backorders.__str__() == \
    "['Bode', 'Jeremy', 'Felica', 'Dilly', 'Kentisha', 'Leety', 'Lilee', 'Jacobo', 'Carcinogen']"

# Large batch of orders became available
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())

# ['Jacobo', 'Carcinogen']
print(playstation_backorders)
assert playstation_backorders.__str__() == "['Jacobo', 'Carcinogen']"

# Order doesn't matter
# {'Charles', 'Kentisha', 'Bode', 'Felica', 'Lilee', 'Dilly', 'Jeremy', 'Leety', 'Robbalobbadoo'}
print(have_playstations)

# Bode's back for yet another
playstation_backorders.enqueue('Bode', 1)

# Only one available
have_playstations.add(playstation_backorders.dequeue())

# ['Jacobo', 'Carcinogen']
print(playstation_backorders)
assert playstation_backorders.__str__() == "['Jacobo', 'Carcinogen']"

# Large batch of orders became available
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())
have_playstations.add(playstation_backorders.dequeue())

# []
print(playstation_backorders)
print('No backorders:', playstation_backorders.empty)
assert playstation_backorders.empty
