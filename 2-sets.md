# Sets

## Introduction

Sets have two major distinctive characteristics:

1. They do not preserve any item order
2. Every item in them must be unique

Taking advantage of these characteristics, a set implementation will *hash*
an object given to it. A hash is a puesdo-unique value that can be thought
of as a distinct signiature. Because the signiatures are generally unique enough,
the hash can be manipulated to determine a static location under the hood.
When all is said and done, common operations such as adding, removing, and
checking for membership can be done in O(1) time.

### A note on Maps

A data structure that expands on sets is a Map or Dictionary. These types store
unique keys, just like a set would, and associates these keys with different data.
Maps are very common; in fact it is the basis of some general data storage formats,
such as the JSON format.

