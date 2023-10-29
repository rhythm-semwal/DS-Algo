This problem is a perfect one to be solved with a heap, also known as a priority queue. If you don't know what a heap is, then this article should help get you up to speed. In this article, we'll discuss the basics of what a heap does and how to use one. If you're interested in the theory behind the implementation of a heap, here is a resource for that.

In short, a heap is a data structure that is capable of giving you the smallest (or largest) element (by some criteria) in constant time, while also being able to add elements and remove the smallest (or largest) element in only logarithmic time. Imagine if you wanted to replicate this functionality naively with an array. To make sure we can find the smallest element in constant time, let's just keep our array sorted, so that the last element is always the largest (or smallest, depending on if we're sorting in ascending or descending order). Removing the largest/smallest element will take O(1) time as we are popping from the end of the array. However, to add a new element, we first need to find where the element should be inserted and then insert it by shifting the array, which requires O(n) time. Now, there are potential improvements to this approach, like using a deque for removals and insertions and binary searching to find insertion points, but the point is that a heap makes it so we don't need to worry about any of that.

In summary, a heap:

Stores elements, and can find the smallest (min-heap) or largest (max-heap) element stored in O(1)O(1)O(1).
Can add elements and remove the smallest (min-heap) or largest (max-heap) element in O(log⁡(n))O(\log(n))O(log(n)).
Can perform insertions and removals while always maintaining the first property.
The capability to remove and insert elements in log⁡(n)\log(n)log(n) time makes heaps extremely useful. For example, many problems that can be naively solved in O(n2)O(n^2)O(n 
2
 ) time, can be solved in O(n⋅log⁡(n))O(n \cdot \log(n))O(n⋅log(n)) time by using a heap. To put this in perspective, for an input size of n=105n = 10^5n=10 
5
  elements, n⋅log⁡(n)n \cdot \log(n)n⋅log(n) is over 6000 times smaller than n2n^2n 
2
 .