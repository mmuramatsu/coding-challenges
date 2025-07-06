# Problem: 1865 - Finding Pairs With a Certain Sum (MEDIUM)

## Problem statement

Given two integer array `nums1` and `nums2`, our task is to implement a class `FindSumPairs` with two methods:

- `add(index, val)`: add `val` to `nums2[index]`;
- `count(tot)`: find the number of pairs `(i, j)`, where `nums1[i] + nums2[j] == tot`.

## Intuition:

The bottleneck of this class is the `count` function. The simplest way to make this function is by use two nested loops, but given the constraints, this will lead us to a TLE.

An optimization for this simple solution is apply the same concept used in the **Two Sum** problem. Instead of iterate through all elements of `nums1` and `nums2` we can create two Hash Map that store the frequency of each integer in `nums1` and `nums2`.

Example: `nums1 = [1,1,1,2,2]` -> `freq1 = {1: 3, 2: 2}`.

We can define this Hash Maps during the initialization of the class, and this Maps will be atributes of the class. One change needed is on the method `add()`, in which we also need to update the frequency of the old value and the new values on the Maps.

On the method `count()`, we can loop through all keys of `freq1` that are less than `tot` (this is due to `key1 + key2 == tot`, we also have in the constraints that `nums1[i]` and `nums2[i]` are in the interval $[1, 10^5]$, so `key1 <= tot`.) and check if `tot - key1` exists in `freq2`, if exists, then `count += freq1[key1] * freq2[tot - key1]`. Otherwise, there's no `key2` that satify `key1 + key2 == tot`.

One last optimization that we can do is based on the fact that we only consider `key1` that are less than `tot`. We know that `nums1` don't suffer any changes, so we can create a sorted list that will store the keys of `freq1`. We `count()` is called we going to loop through this sorted keys and return when find a `key1 >= tot`, processing only the possible keys of `freq1`.

### Complexity:

Let $N1$ and $N2$ be the length of `nums1` and `nums2`, respectively. Let $U1$ and $U2$ be the number of unique values of `nums1` and `nums2`, respectively.

- Time complexity:
    - `_init_`: $O(N1 \ + \ N2 \ + \ log \; U1)$. $O(N1 + N2)$ to initialize the Hash Maps. $O(log \; U1)$ to sort the keys array;
    - `add()`: $O(1)$;
    - `count()`: $O(U1)$. We iterate through all the keys of `freq1` in the worst case.

- Space complexity:
    - `_init_`: $O(N1 \ + \ N2)$. The Hash Maps in the worst case is $O(N)$;
    - `add()`: $O(1)$;
    - `count()`: $O(1)$.

### Elixir trick

This problem is not designed to be solve by functional language like Elixir, or better, Elixir is not designed to work in a Object-Oriented approach. We can simulate that pattern but it's not its natural or most performant idiom for this kind of problem.

Elixir don't have classes, instead, we use modules to group functions and structs to define the "shape" of our data (our "object's state"). Data is immutable, so functions take state and return *new* state.

LeetCode's test infrastructure for "class-based" problems (where you're given a Class Solution) assumes an implicit `this` or `self` context that holds the state. Elixir, being immutable and functional, requires explicit state passing. But we can't change the signature of the method to pass the state through the calls.

The strategy is to try to mimic the "global" or "instance" state assumed by the test runner, even though it's not truly global or instance-based in Elixir. The idea is to store the "object" (FindSumPairs struct) in a place that `add()` and `count()` can implicitly access.

The most common way to do this on LeetCode for Elixir/Haskell/F# etc., is to use an `Agent`. When we use an `Agent`, Elixir spawns a new, separete, Erlang process that will store the data that we need to be "global". Each process in the Erlang VM (on which Elixir runs) has a "mailbox". When we interact with an Agent (or any process), you're not directly calling a function on its data; you're sending it a message.

Sending a message is inherently an asynchronous operation. You put a message in the target process's mailbox, and your process continues executing. The target process will eventually pick up the message from its mailbox when it's ready. That's why we have a lack of performance on Elixir solution.

Using this approach it feels like we have the data globally, and that's because we can refer to the `Agent` by its registered name `(:find_sum_pairs_state)` from anywhere in our code within the same Elixir/Erlang VM, it effectively acts like a shared, globally accessible variable. However, it's not truly global memory; it's a dedicated process responsible for managing and mediating access to its own private state.