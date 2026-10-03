# {{S0001}}

:::{note} {{S0002}}


- {{S0003}}
- {{S0004}}
- {{S0005}}
- {{S0006}}
- {{S0007}}
- {{S0008}}
- {{S0009}}

:::

### {{S0010}}


$${\hat{A}\psi_n = A_n\psi_n}$$

- {{S0011}}

:::{note} {{S0012}}

{{S0013}}
:::

:::{admonition} {{S0014}}
:class: dropdown solution

$$\hat{p} f = p f $$

$$-i\hbar \frac{df}{dx} = p$$

{{S0015}}

$$-i\hbar k = p\rightarrow k=\frac{ip}{\hbar}$$

$$f = e^{ipx/\hbar}$$

- {{S0016}}

:::

{{S0017}}

- {{S0018}}
- {{S0019}}

$$Av = \lambda v$$

:::{note} {{S0020}}

$$\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix} = \lambda \begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}$$
::: 

````{admonition} **Solving eigenfunction-eigenvalue problems numerically**
:class: note, dropdown

```python
import numpy as np

# Define the matrix
matrix = np.array([ [1, 2], 
                    [2, 4]   ] )

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Display the eigenvalues and eigenvectors
eigenvalues, eigenvectors
```

````



### {{S0021}}


::::{grid}
:gutter: 2

:::{grid-item-card} {{S0022}}

{{S0023}}

:::

:::{grid-item-card} {{S0024}}

{{S0025}}

:::

::::

{{S0026}}

- {{S0027}}

$$\hat{H} \mid \psi_n \rangle=E_n \mid \psi_n \rangle$$

$$E_n=E^*_n$$

- {{S0028}}

$$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- {{S0029}}

$$\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$$

- {{S0030}}
- {{S0031}}

### {{S0032}}

- {{S0033}}

$$\hat{A}\mid \phi_n \rangle = A_n \mid \phi_n \rangle$$

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- {{S0034}}

::::{grid}
:gutter: 2

:::{grid-item-card} {{S0035}}

$$\psi=\sum_n c_n \mid n\rangle$$

$$c_n = \braket{n \mid \psi}$$

:::

:::{grid-item-card} {{S0036}}

$$\psi(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$$

$$c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )\psi(x) dx$$
:::

::::


### {{S0037}}

- {{S0038}}

$$|\psi\rangle  = \sum_n c_n |\phi_n\rangle $$

- {{S0039}}

$$p_n=\mid c_n \mid^2$$

$$\sum_n \mid c_n \mid^2 =\sum_n p_n=1$$


### {{S0040}}

- {{S0041}}

- {{S0042}}

$$\mid \psi \rangle=c_1 \mid 1 \rangle+c_2 \mid 2\rangle$$ 

$$\langle \psi \mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\mid 1\rangle + c_2 \mid 2\rangle\Big] =\\ = \mid c_1 \mid^2 \langle 1 \mid 1 \rangle+(c^*_1 c_2\langle 1 \mid 2 \rangle+c_1 c^*_2\langle 2 \mid 1 \rangle)+\mid c_2\mid^2   = c_1^2+c^2_2=p_1+p_2=1$$

- {{S0043}}

 $$\langle E\rangle= \langle \psi \mid \hat{H}\mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\hat{H}\mid 1\rangle + c_2 \hat{H}\mid 2\rangle\Big] =\Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1E_1\mid 1\rangle + c_2 E_2\mid 2\rangle\Big] = \\ = c_1^2E_1+c^2_2 E_2=p_1E_1+p_2 E_2$$


:::{note} {{S0044}}

{{S0045}}
- {{S0046}}
- {{S0047}}
:::

:::{admonition} {{S0048}}
:class: dropdown solution

$$\psi(x)=\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{\pi x}{L}+\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{5\pi x}{L}$$ 

- {{S0049}}

$$\langle E \rangle =p_1 E_1+p_2 E_2 = \frac{1}{2}\frac{1^2 h^2}{8mL^2}+\frac{1}{2}\frac{5^2 h^2}{8mL^2}$$
:::



:::{note} {{S0050}}

{{S0051}}

$$\psi = c_1\phi_1 + c_2\phi_2$$

- {{S0052}}
- {{S0053}}
:::

:::{admonition} {{S0054}}
:class: dropdown solution

{{S0055}}


$$\left<\hat{H}\right> = \left<\psi\left|\hat{H}\right|\psi\right> = \left|c_1\right|^2\left<\phi_1\left|\hat{H}\right|\phi_1\right> + c_1^*c_2\left<\phi_1\left|\hat{H}\right|\phi_2\right> + c_2^*c_1\left<\phi_2\left|\hat{H}\right|\phi_1\right>$$
$$ + \left|c_2\right|^2\left<\phi_2\left|\hat{H}\right|\phi_2\right> = \left|c_1\right|^2E_1 + c_1^*c_2E_2\underbrace{\left<\phi_1\left|\phi_2\right.\right>}_{= 0} + c_2^*c_1E_1\underbrace{\left<\phi_2\left|\phi_1\right.\right>}_{= 0} + \left|c_2\right|^2E_2$$
$$= \left|c_1\right|^2E_1 + \left|c_2\right|^2E_2$$


{{S0056}}

$$\left<\hat{H}^2\right> = \left<\psi\left|\hat{H}^2\right|\psi\right> = \left<\psi\left|\hat{H}\right|E_1c_1\phi_1 + E_2c_2\phi_2\right> = \left<c_1\phi_1 + c_2\phi_2\left|E_1^2c_1\phi_1 + E_2^2c_2\phi_2\right.\right>$$
$$ = \left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 \Rightarrow \sigma_{\hat{H}} = \sqrt{\left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 - \left(\left|c_1\right|^2E_1 + \left|c_2\right|^2E_2\right)^2}$$

:::



```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "sympy",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import sympy as sp
```

{{S0057}}

```{marimo} python
x, L, n, hbar = sp.symbols("x L n hbar", positive=True)
psi_n = sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / L)
psi_n
```

```{marimo} python
p2_psi = -hbar**2 * sp.diff(psi_n, x, 2)
p2_psi
```

```{marimo} python
p2_avg = sp.simplify(sp.integrate(psi_n * p2_psi, (x, 0, L)))
p2_avg
```

{{S0058}}

### {{S0059}}

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- {{S0060}}

- {{S0061}}

  $$\mid \psi \rangle \rightarrow \mid \phi_n \rangle$$

- {{S0062}}

- {{S0063}}

- {{S0064}}

  $$\langle \phi_1 \mid \phi_2 \rangle=0$$


### {{S0065}}

- {{S0066}}

- {{S0067}}
- {{S0068}}



### {{S0069}}

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/7B1llCxVdkE" frameborder="0" allowfullscreen>
</iframe>
</html>


### {{S0070}}

- {{S0071}}

- {{S0072}}

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UjaAxUO6-Uw" frameborder="0" allowfullscreen>
</iframe>
</html>




