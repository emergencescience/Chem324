# {{S0001}}

:::{note} {{S0002}}
- {{S0003}}
- {{S0004}}
- {{S0005}}
- {{S0006}}
- {{S0007}}
- {{S0008}}
:::


### {{S0009}}

- {{S0010}}

- {{S0011}}

  $$
  \hat{p}_x = -i\hbar\frac{d}{dx}
  $$

- {{S0012}}

  $$
  \hat{x} = x
  $$

- {{S0013}}


:::{admonition} {{S0014}}
:class: dropdown

- {{S0015}}

$$\frac{d^2}{dx^2} e^{2x} = 4e^{2x}$$

$$\hat{A} f =4f$$

-  {{S0016}}

- {{S0017}}

  - {{S0018}}
  - {{S0019}}
  - {{S0020}}
  - {{S0021}}

:::


### {{S0022}}

- {{S0023}}

$$
\hat{A}(\psi_1 + \psi_2) = \hat{A}\psi_1 + \hat{A}\psi_2
$$

$$
\hat{A}(c\psi) = c\hat{A}\psi
$$

- {{S0024}}
- {{S0025}}



:::{admonition} {{S0026}}
:class: dropdown

- {{S0027}}


- {{S0028}}

$$\frac{d}{dx}(c_1f_1+c_2f_2) = c_1\frac{df_1}{dx}+c_2\frac{df_2}{dx}$$

$$\int(c_1f_1+c_2f_2)dx = c_1\int f_1dx+c_2\int f_2dx$$

- {{S0029}}

$$\sqrt{(c_1f_1+c_2f_2)} \neq c_1\sqrt{f_1} +c_2\sqrt{f_2}$$

:::


### {{S0030}}

:::{important} {{S0031}}

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

- {{S0032}}
- {{S0033}}

- {{S0034}}
    - {{S0035}}
    - {{S0036}}


:::{note} {{S0037}}

{{S0038}}
:::

:::{admonition} {{S0039}}
:class: dropdown solution

{{S0040}}

$$
\hat{A}\hat{B}f = xf'(x)\textnormal{ and } \hat{B}\hat{A}f = \frac{d}{dx}\left(xf(x)\right) = f(x) + xf'(x)$$
$$\left[\hat{A},\hat{B}\right]f = \hat{A}\hat{B}f - \hat{B}\hat{A}f = -f$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = -1\textnormal{ (this is non-zero and the operators do not commute)}
$$
:::

#### {{S0041}}

$${\left[A,A\right] = \left[A,A^n\right] = \left[A^n,A\right] = 0}$$

- {{S0042}}

$${\left[A,B\right] = -\left[B,A\right]}$$

- {{S0043}}


### {{S0044}}

{{S0045}}

$${\hat{p}_x\hat{x}\psi(x) = \hat{p}_x\left(x\psi(x)\right) = \left(\frac{\hbar}{i}\frac{d}{dx}\right)\left(x\psi(x)\right) = \frac{\hbar x}{i}\frac{d\psi(x)}{dx} + \frac{\hbar}{i}\psi(x)}$$

$${\hat{x}\hat{p}_x\psi(x) = x\left(\frac{\hbar}{i}\frac{d\psi(x)}{dx}\right)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right]\psi(x) = \left(\hat{p}_x\hat{x} - \hat{x}\hat{p}_x\right)\psi(x) = \frac{\hbar}{i}\psi(x)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right] = \frac{\hbar}{i}}$$

{{S0046}}

$$
{\left[\hat{T},\hat{p}_x\right] = \left[\frac{\hat{p}_x^2}{2m},\hat{p}_x\right] = \frac{p_x^3}{2m} - \frac{p_x^3}{2m} = 0}
$$

{{S0047}}

$$
\Delta x\Delta p_x \ge \frac{\hbar}{2}
$$


{{S0048}}

$${\Delta A\Delta B \ge \frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right|}$$


- {{S0049}}

- {{S0050}}

$$\frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right| = \frac{1}{2}\left|\left<\left[\hat{x},\hat{p}_x\right]\right>\right| = \frac{1}{2}\left|\left<\frac{\hbar}{i}\right>\right|
= \frac{1}{2}\left|\left<\psi\left|\frac{\hbar}{i}\right|\psi\right>\right| = \frac{1}{2}\left|\frac{\hbar}{i}\underbrace{\left<\psi\left|\psi\right.\right>}_{=1}\right| = \frac{\hbar}{2}$$

$$\Rightarrow \Delta x\Delta p_x \ge \frac{\hbar}{2}$$

- {{S0051}}


### {{S0052}}

:::{important} {{S0053}}

$$[\hat{A},\hat{B}]=0$$

$$\hat{A}\phi_k = a_k \phi_k$$

$$\hat{B}\phi_k = b_k \phi_k$$

:::

:::{admonition} {{S0054}}
:class: dropdown

- {{S0055}}

{{S0056}}

$$\hat{A}\psi_i = a_i\psi_i\textnormal{ and }\hat{B}\psi_i = b_i\psi_i$$

{{S0057}}

$$\hat{A}\hat{B}\psi = \hat{A}\left(\hat{B}\psi\right) = \hat{A}\overbrace{\left(\hat{B}\sum\limits_{i=1}^{\infty}c_i\psi_i\right)}^{\textnormal{complete basis}}
= \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_i\hat{B}\psi_i\right)}^{\hat{B}\textnormal{ linear}} = \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_ib_i\psi_i\right)}^{\textnormal{eigenfunction of }\hat{B}}$$
$$= \overbrace{\sum\limits_{i=1}^{\infty}c_ib_i\hat{A}\psi_i}^{\hat{A}\textnormal{ linear}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ib_ia_i\psi_i}^{\textnormal{eigenfunction of }\hat{A}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ia_ib_i\psi_i}^{a_i\textnormal{ and }b_i\textnormal{ are constants}} = \sum\limits_{i=1}^{\infty}c_ia_i\hat{B}\psi_i$$
$$= \hat{B}\sum\limits_{i=1}^{\infty}c_ia_i\psi_i = \hat{B}\sum\limits_{i=1}^{\infty}c_i\hat{A}\psi_i = \hat{B}\hat{A}\sum\limits_{i=1}^{\infty}c_i\psi_i = \hat{B}\hat{A}\psi$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = 0$$

{{S0058}}
:::

- {{S0059}}

- {{S0060}}

- {{S0061}}



### {{S0062}}

- {{S0063}}

  $$
  \langle A \rangle = \int \psi^* \hat{A} \psi \, d\tau
  $$

- {{S0064}}

  $$
  \hat{A}\psi = a\psi
  $$

{{S0065}}

  $$
  \langle A \rangle = \int \psi^* a \psi \, d\tau = a \int \psi^*\psi \, d\tau = a
  $$

{{S0066}}



### {{S0067}}

{{S0068}}

* {{S0069}}
* {{S0070}}
  
$$
  \langle \phi | \psi \rangle = \int \phi^*(r), \psi(r), d\tau
$$

* {{S0071}}
  
$$
  \langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
$$
  
* {{S0072}}


### {{S0073}}


- {{S0074}}

#### {{S0075}}

- {{S0076}}

- {{S0077}}

:::{important} {{S0078}}

* {{S0079}}

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}^\dagger \phi | \psi \rangle.
$$

- {{S0080}}

* {{S0081}}

$$
A^\dagger = (A^T)^*
$$

{{S0082}}

$$
(A^\dagger)_{jk} = A_{kj}^*.
$$


:::

{{S0083}}

$$
a_{jk} = \langle \psi_j | \hat{A} | \psi_k \rangle
\quad \Rightarrow \quad
a^*_{kj} = \langle \psi_k | \hat{A}^\dagger | \psi_j \rangle.
$$



#### {{S0084}}

{{S0085}}

$$
\hat{A} = \hat{A}^\dagger.
$$

{{S0086}}

:::{important} {{S0087}}

$$
A = A^\dagger, \quad a_{jk} = a_{kj}^*.
$$
:::

:::{important} {{S0088}}

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}\phi | \psi \rangle,
\qquad \text{or equivalently,} \qquad
\langle j| \hat{A}|k\rangle = \langle k| \hat{A}|j\rangle^*.
$$

{{S0089}}

$$
\int \psi_j^*(x), [\hat{A}\psi_k(x)],dx
= \int \psi_k(x), [\hat{A}\psi_j(x)]^*,dx.
$$
:::



#### {{S0090}}


1. {{S0091}}

  $$
  \hat{A}|\psi\rangle = a|\psi\rangle \implies a \in \mathbb{R}.
  $$

:::{tip} {{S0092}}
:class: dropdown

- {{S0093}}

$$
\int \psi^* \hat{A} \psi \, d\tau = a
$$

$$
\int \psi \left(\hat{A} \psi\right)^* \, d\tau = a^*
$$

- {{S0094}}

$$
a = a^*
$$

:::

2. {{S0095}}

  $$
  \langle \psi_m | \psi_n \rangle = 0 \quad (m \ne n).
  $$

:::{tip} {{S0096}}
:class: dropdown

{{S0097}}

$$
\textnormal{LHS: } \int \psi_j^* \hat{A} \psi_k \, d\tau = \int \psi_j^* a_k \psi_k \, d\tau = a_k \int \psi_j^* \psi_k \, d\tau
$$

$$
\textnormal{RHS: } \int \psi_k \left(\hat{A} \psi_j \right)^* \, d\tau = \int \psi_k \left(a_j \psi_j \right)^* \, d\tau = a_j \int \psi_j^* \psi_k \, d\tau
$$

- {{S0098}}

$$
\left(a_k - a_j \right) \int \psi_j^* \psi_k \, d\tau = 0
$$

- {{S0099}}

$$
\int \psi_j^* \psi_k \, d\tau = 0
$$

- {{S0100}}

- {{S0101}}

:::

:::{note} {{S0102}}

{{S0103}}

{{S0104}}
:::

:::{admonition} {{S0105}}
:class: dropdown solution

- {{S0106}}
- {{S0107}}
- {{S0108}}
- {{S0109}}

:::

- {{S0110}}

- {{S0111}}

$$\int \psi_1 d\psi_2 =- \int \psi_2d\psi_1 + \psi_1\psi_2\Big|_{x_{min}}^{x_{max}} =- \int \psi_2d\psi_1$$

:::{note} {{S0112}}

{{S0113}}
:::

:::{admonition} {{S0114}}
:class: dropdown solution

{{S0115}}
:::

{{S0116}}


### {{S0117}}

#### {{S0118}}

{{S0119}}

- {{S0120}}

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( x \frac{d}{dx} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

- {{S0121}}
- {{S0122}}


:::{note} {{S0123}}
:class: dropdown


{{S0124}}

{{S0125}}

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx
$$

{{S0126}}

{{S0127}}

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx
$$

{{S0128}}

{{S0129}}

$$
\int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx = \int_{a}^{b} \left( \psi_1^*(x) + x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

{{S0130}}

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx + \int_{a}^{b} x \frac{d}{dx} \psi_1^*(x) \psi_2(x) \, dx
$$

{{S0131}}

{{S0132}}

$$
\int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

{{S0133}}

{{S0134}}

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx
$$

{{S0135}}

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx \neq \int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

- {{S0136}}
:::

#### {{S0137}}

- {{S0138}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

- {{S0139}}


:::{note} {{S0140}}
:class: dropdown

{{S0141}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

### {{S0142}}

{{S0143}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx
$$

### {{S0144}}

{{S0145}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx
$$

{{S0146}}

{{S0147}}

$$
-\int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx = \left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d^2}{dx^2} \psi_1^*(x) \psi_2(x) \, dx
$$

{{S0148}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

{{S0149}}

{{S0150}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

:::


#### {{S0151}}

- {{S0152}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

:::{note} {{S0153}}
:class: dropdown

{{S0154}}

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1^*(x) \right)  \, dx
$$

- {{S0155}}

$$
\int_{a}^{b} \psi_1^*(x) \left( i\frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx = -\int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x)^* \right)
$$

:::

#### {{S0156}}

$$
A = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
i & 1 \\
-1 & -i
\end{pmatrix}
$$

$$
C = \begin{pmatrix}
2 & i \\
-i & 2
\end{pmatrix}
$$

:::{note} {{S0157}}
:class: dropdown

{{S0158}}

{{S0159}}

{{S0160}}

{{S0161}}

{{S0162}}

{{S0163}}

$$
B^\dagger = \begin{pmatrix}
-i & -1 \\
1 & i
\end{pmatrix}
$$

{{S0164}}

{{S0165}}

{{S0166}}

$$
C^\dagger = \begin{pmatrix}
2 & -i \\
i & 2
\end{pmatrix}
$$

{{S0167}}

:::

#### {{S0168}}

{{S0169}}

:::{note} {{S0170}}
:class: dropdown

- {{S0171}}

- {{S0172}}

$$
\frac{d \psi(x)}{dx} \approx \frac{\psi(x_{n+1}) - \psi(x_{n-1})}{2 \Delta x}
$$

- {{S0173}}

- {{S0174}}

- {{S0175}}

$$
P = \frac{i}{2 \Delta x} \begin{pmatrix}
0 & -1 & 0 & 1 \\
1 & 0 & -1 & 0 \\
0 & 1 & 0 & -1 \\
-1 & 0 & 1 & 0
\end{pmatrix}
$$

{{S0176}}
- {{S0177}}
- {{S0178}}
- {{S0179}}

- {{S0180}}
:::

#### {{S0181}}

{{S0182}}

:::{admonition} {{S0183}}
:class: dropdown solution

{{S0184}}

$$
\hat{A} f(x) = x \frac{df}{dx}
$$

{{S0185}}

$$
\hat{A}(\hat{A} f(x)) = \hat{A} \left( x \frac{df}{dx} \right) = x \frac{d}{dx} \left( x \frac{df}{dx} \right)
$$

{{S0186}}

$$
\frac{d}{dx} \left( x \frac{df}{dx} \right) = \frac{df}{dx} + x \frac{d^2 f}{dx^2}
$$

{{S0187}}

$$
\hat{A}^2 f(x) = x \left( \frac{df}{dx} + x \frac{d^2 f}{dx^2} \right) = x \frac{df}{dx} + x^2 \frac{d^2 f}{dx^2}
$$

:::

#### {{S0188}}

{{S0189}}

:::{admonition} {{S0190}}
:class: dropdown solution

{{S0191}}

$$
\hat{B} f(x) = -i\hbar \frac{d}{dx} e^{ikx}
$$

{{S0192}}

$$
\frac{d}{dx} e^{ikx} = ik e^{ikx}
$$

{{S0193}}

$$
\hat{B} f(x) = -i\hbar \cdot ik e^{ikx} = \hbar k e^{ikx}
$$

{{S0194}}

:::

#### {{S0195}}

{{S0196}}

:::{admonition} {{S0197}}
:class: dropdown solution

{{S0198}}

$$
\hat{D}(\alpha f(x) + \beta g(x)) = x \frac{d}{dx} (\alpha f(x) + \beta g(x)) = \alpha x \frac{df}{dx} + \beta x \frac{dg}{dx}
$$

{{S0199}}

{{S0200}}

$$
\hat{D} f(x) = x \frac{d}{dx} x^n = x \cdot n x^{n-1} = n x^n
$$

{{S0201}}

:::
