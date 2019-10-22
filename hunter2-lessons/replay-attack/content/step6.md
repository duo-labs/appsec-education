# Breaking the Cycle

### The Importance of Other Controls

While the changes we introduced to the signature generation can help reduce the potential overall risk, there are problems with it. One of the most outstanding is that we're only locking it down to a one-second limit. An attacker could make a lot of requests in one second using some pretty simple automation. 

We could always update the logic to lock it down to an even smaller time frame (say milliseconds) but then you start running into real world limitations such as network latency. Some requests just can't happen sub-second like that and, in our case, would cause pain on the user's side in the form of frequent signature validation failures.

### So what else?

Fortunately, there are other controls that can be put in place to help prevent replay attacks besides just adding in this randomness. These other controls usually rely more on the logic of the system rather than a more standardized control. They do, however, relate back to one concept: actions taken by certain users in the context of the system.

As an example lets go back to our "money transfer" example at the beginning of the lesson. When a legitimate user makes the request, you can gather information about it such as:

- Amount of the transfer
- Accounts to transfer from and to
- IP address

Then you could use this information when another request comes through to see how similar it is and to check for irregularities. In the context of a replay attack coming from an attacker rather than the valid user, the IP address might be different. Or you could take it a step further and look at the frequency of the requests so see if anything's amiss.

Adding these checks is tightly bound to the logic of your application but they can go a long way towards preventing issues not caught by simpler controls.

### No solution is perfect

A determined attacker will almost always find a way around whatever controls you have in place. This is why a multi-layered approach is favorable over a single control. Our time-based replay prevention shouldn't be the only tool in your arsenal to thwart attackers but one of many in a "defense in depth approach".
