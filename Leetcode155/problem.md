155. Min Stack
     Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

#Optimization

A few hints, roughly in order of "easy win" → "clever trick":

Do you need a custom Node class at all?
A stack is exactly what Python's list already is. You can push/pop/peek from a list in O(1) — no need to hand-roll a linked list with previousNode pointers. That removes a layer of object overhead.
Do you need to store the min in every node?
Right now every single element carries its own minValue, even when the min hasn't changed in ages. Think about using two separate stacks: one for the actual values, and one that only tracks minimums. Ask yourself — when pushing a new value, do you always need to add something to the min-stack, or only when the new value is a new minimum (or ties it)? Same question for popping: when do you need to pop from the min-stack?
Can you avoid a second stack entirely?
This is the more advanced trick: instead of storing the min separately, you can keep a single stack and just track the current minimum as one variable. When you push a value smaller than the current min, you store an encoded value in the stack (something based on the difference between the new value and the old min) instead of the raw value, then update your min variable. On pop, if you read back one of these "encoded" markers, you know how to reconstruct the previous min from it. This gets you down to essentially O(1) extra space beyond the stack itself (no parallel min array/stack at all).

What we need: when pushing a new value v that's smaller than the current min m, we need to store something in the stack that:

Is guaranteed to be less than the new min (so on pop/getMin we can tell "this is an encoded marker, not a real value")
Lets us recover the old min m later, using only that stored number and the new min (which we'll keep in self.min_val)

The formula: push 2\*v - m instead of v.

Let's check both properties.

Property 1 — is it always less than the new min?
The new min is v (since v < m). We need 2\*v - m < v.

2v−m<v⟺v<m

That's exactly the condition we're already in (v < m), so it always holds. Good — any encoded value we ever push is guaranteed smaller than self.min_val at that point, which is exactly the signal we use to detect "this is a marker."

Property 2 — can we recover the old min?
Say we stored encoded = 2\*v - m. Later, when we pop it, self.min_val currently equals v (the min we set at push time). We want to recover m. Rearranging:

encoded=2v−m⟹m=2v−encoded

Since we know v (it's the current self.min_val at pop time) and encoded (it's the value on the stack), we can solve for m directly.

Putting it together:

push(v):
if stack is empty, set self.min_val = v, push v.
else if v >= self.min_val, just push v (no change to min).
else (v < self.min_val): push 2*v - self.min_val, then update self.min_val = v.
pop():
top = stack.pop()
if top < self.min_val → it was an encoded marker. The real value that was pushed was actually self.min_val (the old min at that time!), and the old-old min is 2*self.min_val - top. So: recover old min via old_min = 2\*self.min_val - top, set self.min_val = old_min, and treat the returned top-of-stack value as self.min_val-before-update...
Wait — one subtlety worth noticing yourself: when top is an encoded marker, what was the actual value the user pushed at that time? (Hint: it's not top, and it's not the new self.min_val either — think about what v equaled when you did the encoding.)
