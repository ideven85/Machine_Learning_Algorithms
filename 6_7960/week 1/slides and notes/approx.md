### Weierstrass Approximation Theorem

One of the foundational results behind neural network approximation theory.

**Statement**

If (f(x)) is a **continuous function** on a closed interval ([a,b]), then for every (\epsilon > 0), there exists a polynomial (p(x)) such that

[
|f(x)-p(x)| < \epsilon
]

for **all** (x \in [a,b]).

In other words:

> Any continuous function on a bounded interval can be approximated arbitrarily well by a polynomial.

---

### Intuition

Imagine drawing any smooth curve:

* (x^2)
* (\sin(x))
* (e^x)
* weird wiggly continuous curves

The theorem says that if you're willing to use a high enough degree polynomial,

[
a_0 + a_1x + a_2x^2 + \cdots + a_nx^n
]

you can get as close as you want everywhere on the interval.

📈 The polynomial becomes a flexible "shape machine" that can mimic the target function.

---

### Example

Suppose

[
f(x)=|x|
]

on ([-1,1]).

Although (|x|) is not itself a polynomial, Weierstrass guarantees a sequence of polynomials

[
p_1(x), p_2(x), p_3(x), \ldots
]

that converges uniformly to (|x|).

As degree increases:

[
p_n(x) \to |x|
]

everywhere on ([-1,1]).

---

### Why it Matters for Deep Learning

Historically, this theorem inspired the question:

> If polynomials can approximate any continuous function, can neural networks do the same?

This led to the **Universal Approximation Theorem**.

For a neural network with enough hidden units:

[
f(x) \approx \sum_i a_i \sigma(w_i^T x + b_i)
]

where (\sigma) is an activation function (sigmoid, ReLU, etc.).

So:

| Classical Analysis                           | Deep Learning                                    |
| -------------------------------------------- | ------------------------------------------------ |
| Polynomials approximate continuous functions | Neural networks approximate continuous functions |
| Basis functions: (1,x,x^2,\dots)             | Basis functions: (\sigma(w^Tx+b))                |
| Weierstrass theorem                          | Universal Approximation theorem                  |

---

### What Weierstrass Does *Not* Say

It does **not** tell us:

* How large the polynomial degree must be.
* Whether the approximation is computationally efficient.
* How to find the polynomial.

Similarly, the Universal Approximation Theorem says a network **exists**, not that SGD can easily find it.

---

### Connection to Barron's Theorem (from your 6.7960 notes)

The progression is roughly:

1. **Weierstrass (1885)**
   "A continuous function can be approximated."

2. **Universal Approximation (1980s)**
   "A neural network can approximate a continuous function."

3. **Barron's Theorem (1993)**
   "For certain function classes, a neural network can approximate efficiently, with error decreasing roughly as (O(1/\sqrt{m})) where (m) is the number of hidden units."

The key advance from Weierstrass → Barron is moving from **existence** to **efficiency**.

### Exam-sized takeaway

> **Weierstrass Approximation Theorem:** Every continuous function on a compact interval can be uniformly approximated arbitrarily well by polynomials.

This is the mathematical ancestor of the neural network **Universal Approximation Theorem**. 🧠📚

Sure. The **Weierstrass function** in LaTeX is:

```latex
W(x)=\sum_{n=0}^{\infty} a^n \cos\!\left(b^n \pi x\right)
```

which renders as

[
W(x)=\sum_{n=0}^{\infty} a^n \cos!\left(b^n \pi x\right)
]

with conditions



$$[
0<a<1,\qquad b\in\mathbb{N}\ \text{odd},\qquad ab>1
]$$

---

The **Weierstrass Approximation Theorem** can be written as:



$$[
\forall \varepsilon>0,\ \exists p(x)
\text{ polynomial such that }
\sup_{x\in[a,b]}
|f(x)-p(x)|<\varepsilon
]$$

where (f) is continuous on ([a,b]).

---

The **Universal Approximation Theorem** is often expressed informally as



$$[
f(x)\approx
\sum_{i=1}^{m}
a_i,\sigma(w_i^\top x+b_i)$$
]

This is the neural-network analogue of Weierstrass that appears in deep learning theory. 🧠📚

\[W(x)=\sum_{n=0}^{\infty} a^n \cos\!\left(b^n \pi x\right)\]