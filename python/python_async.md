# mutli + (thread, task, process)

## short introduction:

Only multiprocessing actually runs these trains of thought at literally the same time.

Threading and asyncio both run on a single processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process.

### multiprocessing:
Parallelism consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

### multi-tasks:
Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

### multi-threading:
Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.


## difference between threading and asyncio

The way the threads or tasks take turns is the big difference between threading and asyncio. In threading, the operating system actually knows about each thread and can interrupt it at any time to start running a different thread. This is called pre-emptive multitasking since the operating system can pre-empt your thread to make the switch.

Pre-emptive multitasking is handy in that the code in the thread doesn’t need to do anything to make the switch. It can also be difficult because of that “at any time” phrase. This switch can happen in the middle of a single Python statement, even a trivial one like x = x + 1.

Asyncio, on the other hand, uses cooperative multitasking. The tasks must cooperate by announcing when they are ready to be switched out. That means that the code in the task has to change slightly to make this happen.

The benefit of doing this extra work up front is that you always know where your task will be swapped out. It will not be swapped out in the middle of a Python statement unless that statement is marked. You’ll see later how this can simplify parts of your design.


| Concurrency Type | Switching Decision | Number of Processors |
| ---------------- | ------------------ | -------------------- |
| Pre-emptive multitasking (threading) | The operating system decides when to switch tasks external to Python. | 1 |
| Cooperative multitasking (asyncio) | The tasks decide when to give up control. | 1 |
| Multiprocessing (multiprocessing) | The processes all run at the same time on different processors. | Many |

## when is what useful

### CPU-bound and I/O-bound

- I/O-bound:

  I/O-bound: problems cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource. They arise frequently when your program is working with things that are much slower than your CPU.

  requests on the internet can take several orders of magnitude longer than CPU instructions, so your program can end up spending most of its time waiting. This is what your browser is doing most of the time.

- CPU-bound:

  On the flip side, there are classes of programs that do significant computation without talking to the network or accessing a file. These are the CPU-bound programs, because the resource limiting the speed of your program is the CPU, not the network or the file system.


## Summary on who suitable for what:

To recap the above, concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.
