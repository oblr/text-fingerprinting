# text-fingerprinting

## Rabin fingerprint

```
f(x) = m_0 + m_1 * x + ... + m_{n-1} * (x**{n-1})
```

## shingling

see "https://nlp.stanford.edu/IR-book/html/htmledition/near-duplicates-and-shingling-1.html":

Given a positive integer $k$ and a sequence of terms in a document $d$, define the $k$-shingles of $d$ to be the set of all consecutive sequences of $k$ terms in $d$.

Let $S(d_j)$ denote the set of shingles of document $d_j$.

The Jaccard coefficient measures the degree of overlap between the sets $S(d_1)$ and $S(d_2)$ as $\vert S(d_1) \cap S(d_2)\vert/\vert S(d_1) \cup S(d_2)\vert$. [denoted by $J(S(d_1),S(d_2))$].