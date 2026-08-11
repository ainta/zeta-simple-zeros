# Proof sketch with exact constants

This note records the mathematical deduction checked by the accompanying
finite certificates, taking Anthropic's Theorem D and its setup as cited
input.

## 1. Imported Montgomery-Taylor input

Let

$$
N=N(T,2T),\qquad S=N_0^s(T,2T),
$$

where zeros are counted with multiplicity in $N$, while $S$ counts simple
zeros on the critical line. Anthropic proves

$$
H_0:=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=0.6725007036794116\ldots
$$

and, in the notation of its Proposition 4.4,

$$
S\ge H_0N-o(N).
$$

The optimized window has limiting normalized overlap kernel

$$
k(x)=\frac{K(x)}{K(0)},\qquad
K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2t)\cos(2\pi xt)dt,
$$

with

$$
K(x)=
\frac{\sin(\pi x-1/\sqrt2)}{2\pi x-\sqrt2}
+\frac{\sin(\pi x+1/\sqrt2)}{2\pi x+\sqrt2},
\quad K(0)=\sqrt2\sin(1/\sqrt2).
$$

The displayed singularities are removable. The code evaluates the equivalent
entire sinc expression.

For bounded normalized separations, the inner products of the simple-zero
atoms satisfy

$$
\langle v_\gamma,v_{\gamma'}\rangle
=k(x_\gamma-x_{\gamma'})+o(1)
$$

uniformly after the same central truncation used in the paper.

## 2. Stability-enhanced rank-inertia inequality

Define the convex nonnegative function

$$
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
$$

Let $V$ be a matrix with $r$ columns of norm at most one, put
$P=VV^*$, $M=V^*V$, and let $Q$ be Hermitian with at most $b$
positive eigenvalues. Then

$$
\|P+Q\|_F^2
\ge 4\mathrm{tr}(P+Q)-3r-4b+\mathrm{tr}(\Psi(M)). \qquad (2.1)
$$

To prove it, write $Q=Q_+-Q_-$. The positive part satisfies

$$
\|Q_+\|_F^2\ge4\mathrm{tr}(Q_+)-4b.
$$

If $p_i,n_i$ are the decreasing eigenvalues of $P,Q_-$, von Neumann's
trace inequality reduces the other part to

$$
\min_{n\ge0}\big((p-n)^2+4n\big)
=2p-1+\Psi(p).
$$

The nonzero spectra of $VV^*$ and $V^*V$ agree. Summing and using
$\mathrm{tr}(P)\le r$ gives (2.1).

Applying (2.1) to the simple-zero part of Anthropic's decomposition preserves
the defect

$$
\Delta(M):=\mathrm{tr}(\Psi(M))
$$

that the original two-trace argument drops. The counting step becomes

$$
S\ge H_0N+\Delta(M)-o(N). \qquad (2.2)
$$

## 3. The 3-point certificate

Set

$$
\epsilon_4=\min_{u,v\ge0,u+v\le4}
\big(k(u)^2+k(v)^2+k(u+v)^2\big). \qquad (3.1)
$$

### Why $\epsilon_4>0$ without computation

A positive zero $x$ of $K$ obeys

$$
x\tan(\pi x)=c,qquad
c=\frac{\tan(1/\sqrt2)}{\sqrt2\pi}>0. \qquad (3.2)
$$

If $x,y,x+y$ were all positive zeros, the tangent addition formula and
(3.2) would imply

$$
x^2+xy+y^2+c^2=0,
$$

which is impossible. Thus the positive zero set of $K$ is sum-free. On the
compact triangle in (3.1), the three summands cannot vanish simultaneously;
at a boundary with $u=0$ or $v=0$, one summand is $k(0)^2=1$. Hence
$\epsilon_4>0$.

The finite verifier strengthens this to

$$
\epsilon_4\ge\frac{221}{10^6}=0.000221. \qquad (3.3)
$$

### Converting triangles into global defect

For any graph $E$ of maximum degree two on the columns of $V$, a dual
form of $\Psi$ gives

$$
\Delta(V^*V)\ge\frac32\sum_{\{i,j\}\in E}
|\langle V_i,V_j\rangle|^2. \qquad (3.4)
$$

Partition the normalized zero interval into cells of length four, and split
the zeros in each cell into disjoint triples. The number $q$ of triples is

$$
q\ge\frac13\left(S-\frac N2\right)-o(N).
$$

Joining each triple into a triangle and using (3.1), (3.4) yields

$$
\Delta(M)\ge\frac{\epsilon_4}{2}
\left(S-\frac N2\right)-o(N). \qquad (3.5)
$$

Combining (2.2) and (3.5),

$$
\frac SN\ge
\frac{H_0-\epsilon_4/4}{1-\epsilon_4/2}. \qquad (3.6)
$$

With the certified value (3.3), this is $67.2519767\%$. The analytic
positivity proof alone already gives a strict improvement over $H_0$.

## 4. The 7-point certificate

Write $w(x)=k(x)^2$. For six nonnegative consecutive gaps define

$$
F_6(g_1,\ldots,g_6)
=\frac1{3000}\sum_{i=1}^6g_i
+\sum_{s=1}^6\frac{2}{7-s}
  \sum_{i=1}^{7-s}w(g_i+\cdots+g_{i+s-1}). \qquad (4.1)
$$

There are 21 pair distances in (4.1). The verifier proves

$$
F_6(g_1,\ldots,g_6)\ge\frac{19}{5000}
\quad\text{for every }g_i\ge0. \qquad (4.2)
$$

For $m$ ordered points $y_1\lt\cdots\lt y_m$, let

$$
E_m=2\sum_{1\le i\lt j\le m}w(y_j-y_i).
$$

Sum (4.2) over all consecutive 7-point windows. A pair spanning $s$ gaps
occurs in at most $7-s$ windows and its coefficient is $2/(7-s)$.
Each gap occurs in at most six windows. Consequently

$$
E_m+\frac1{500}(y_m-y_1)
\ge\frac{19}{5000}(m-6). \qquad (4.3)
$$

For every corresponding principal block $G$, convex pinching and the definition of $\Psi$
give

$$
\mathrm{tr}(\Psi(G))\ge\min\left(1,
2\sum_{i\lt j}|G_{ij}|^2\right). \qquad (4.4)
$$

Choose $m=269$. Then

$$
A=\frac{19}{5000}(269-6)=\frac{4997}{5000}\lt1.
$$

Equations (4.3)-(4.4) imply for every consecutive 269-point block $B$,

$$
\Delta(G_B)+\frac1{500}\mathrm{span}(B)
\ge\frac{4997}{5000}-o(1). \qquad (4.5)
$$

Average (4.5) over all 269 offsets of consecutive block partitions. Each
interior gap is charged by at most 268 offsets and the total normalized length
is $N+o(N)$. Therefore

$$
\Delta(M)\ge
\frac{4997}{1{,}345{,}000}S
-\frac{268}{134{,}500}N-o(N). \qquad (4.6)
$$

Substituting (4.6) into (2.2) and rearranging gives

$$
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{1{,}345{,}000H_0-2{,}680}{1{,}340{,}003}
=0.673008527927\ldots. \qquad (4.7)
$$

## 5. Proof dependencies

The finite certificates prove (3.3) and (4.2). Sections 2–4 give the deductions
from those inequalities to (3.6) and (4.7). The zero-counting, tail, trace, and
test-family inputs come from the cited Anthropic paper and Lean artifact.
