# {{S0001}}

:::{admonition} {{S0002}}

- {{S0003}}
- {{S0004}}
- {{S0005}}
- {{S0006}}

- {{S0007}}
- {{S0008}}

:::



### {{S0009}}

- {{S0010}}

$$\psi_n(x,t) = \psi_n(x) e^{-\frac{i}{\hbar}E_n t}$$

- {{S0011}}

$$\mid \psi_n(x,t) \mid^2 = \psi_n^*(x)\psi_n(x) e^{-\frac{i}{\hbar}E_n t} e^{+\frac{i}{\hbar}E_n t} = \mid \psi_n(x) \mid^2$$

- {{S0012}}

$$\langle A \rangle = \int \psi_n^*(x) e^{+\frac{i}{\hbar}E_n t} \hat{A} \psi_n(x) e^{-\frac{i}{\hbar}E_n t} dx = \int \psi_n^*(x) \hat{A} \psi_n(x) dx$$

- {{S0013}}


### {{S0014}}

- {{S0015}}

$$\mid \psi(0) \rangle =c_1\mid 1 \rangle + c_2 \mid 2 \rangle$$

- {{S0016}}

$$\mid \psi(t) \rangle =c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2 \rangle= c_1(t)\mid 1\rangle+c_2(t) \mid 2 \rangle$$

- {{S0017}}

:::{admonition} {{S0018}}
:class: dropdown

$$  i\hbar\frac{\partial}{\partial t}\mid \psi \rangle =\hat{H}\psi(t)\rangle $$

{{S0019}}

$$i\hbar \Big( -\frac{i}{\hbar}E_1 c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1\rangle-\frac{i}{\hbar}E_2 c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2\rangle \Big) = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle$$

{{S0020}}

$$c_1 e^{-\frac{i}{\hbar}E_1 t}\hat{H}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\hat{H} \mid 2 \rangle = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle $$

:::



```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
```

```{marimo} python
def psi_n(x, n):
    """Time-independent wavefunction for a particle in a box."""
    L = 1 # set box length

    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def T_n(t, n):
    """Time dependence factor for the wavefunction."""
    L = 1 # set box length
    m, hbar = 1, 1 # set atomic units
    En = n**2 * np.pi**2 * hbar**2 / (2 * m * L**2)

    return np.exp(-1j * En * t / hbar)

def psi_combined(x, t, c1=1, c2=1, n1=1, n2=2):
    """Time-dependent wavefunction for a normalized superposition of two PIB states."""

    norm = np.sqrt(c1**2 + c2**2)

    return (c1 * psi_n(x, n1) * T_n(t, n1) + c2 * psi_n(x, n2) * T_n(t, n2)) / norm
```

```{marimo} python
def plot_wavefunction(t=0, c1=1, c2=1, n1=1, n2=2):

    L = 1.0
    x = np.linspace(0, L, 1000)

    psi_squared_x = np.abs(psi_combined(x, t, c1=c1, c2=c2, n1=n1, n2=n2))**2

    plt.plot(x, psi_squared_x, color="#3d81f6", lw=2)
    plt.fill_between(x, psi_squared_x, alpha=0.2, color="#3d81f6")

    plt.title(f"$|\\Psi(x,t)|^2$ for states n={n1} and n={n2} at t={t:.2f}")
    plt.xlabel('x')
    plt.ylabel(r'$|\Psi(x, t)|^2$')
    plt.grid(True, alpha=0.4)
    plt.ylim([0, 4.5])
    plt.gcf()
```

```{marimo} python
:hide-code: true

t_qw = mo.ui.slider(0, 10.0, step=0.1, value=0.0, show_value=True, label="time t")
n2_qw = mo.ui.slider(2, 6, step=1, value=2, show_value=True, label="second state n2")
mo.hstack([t_qw, n2_qw], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

plot_wavefunction(t=t_qw.value, c1=1, c2=1, n1=1, n2=n2_qw.value)
plt.gcf()
```

- {{S0021}}
### {{S0022}}

- {{S0023}}

$$\mid \psi(t)\rangle = \sum_n c_n e^{-\frac{i}{\hbar}E_n t} \mid n\rangle$$

- {{S0024}}

$$\langle \psi(t) \mid \psi(t)\rangle = \sum_n \sum_k \langle n \mid c^*_n e^{\frac{i}{\hbar}E_n t} \cdot c_k e^{-\frac{i}{\hbar}E_k t} \mid k\rangle = \sum_n \sum_k c^*_n c_k e^{-\frac{i}{\hbar}(E_k - E_n)t} \delta_{kn} = \sum_n \mid c_n \mid^2 = 1$$

- {{S0025}}


### {{S0026}}

- {{S0027}}

- {{S0028}}

  $$\langle A \rangle = \langle \psi \mid \hat{A} \mid \psi \rangle$$

{{S0029}}

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \langle \frac{\partial \psi}{\partial t} \mid \hat{A} \mid \psi \rangle + \langle \psi \mid \hat{A} \mid \frac{\partial \psi}{\partial t} \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle
  $$

- {{S0030}}

  $$
  i\hbar \frac{\partial}{\partial t} \mid \psi \rangle = \hat{H} \mid \psi \rangle
  $$  

{{S0031}}

  $$\langle \frac{\partial \psi}{\partial t} \mid = -\frac{1}{i\hbar} \langle \psi \mid \hat{H},$$
  $$\mid \frac{\partial \psi}{\partial t} \rangle = \frac{1}{i\hbar} \hat{H} \mid \psi \rangle.$$

- {{S0032}}

  $$\frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid \hat{A}\hat{H} \mid \psi \rangle - \frac{1}{i\hbar} \langle \psi \mid \hat{H}\hat{A} \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle$$
  
:::{important} {{S0033}}

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid [\hat{A}, \hat{H}] \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle.
  $$

:::

- {{S0034}}

- {{S0035}}

  $$
  \frac{\partial}{\partial t}\langle E \rangle = 0
  $$  
 

### {{S0036}}

:::{figure} {{S0037}}
:label: fig-time-dependence-1
:alt: pib1
:width: 300px

{{S0038}}
:::

:::{figure} {{S0039}}
:label: fig-time-dependence-2
:alt: pib1
:width: 300px

{{S0040}}
:::

:::{seealso} {{S0041}}
{{S0042}}
:::
