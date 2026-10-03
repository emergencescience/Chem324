---
kernelspec:
  name: python3
  display_name: Python 3
---

# {{S0001}}

:::{note} {{S0002}}

- {{S0003}}
- {{S0004}}
- {{S0005}}
- {{S0006}}
- {{S0007}}

:::

### {{S0008}}

- {{S0009}}
  - {{S0010}}
  - {{S0011}}
- {{S0012}}
- {{S0013}}

:::{figure} {{S0014}}
:label: fig-schrodinger-equation-1
:alt: A person stepping through a door into a space filled with crossing lines
:width: 300px

{{S0015}}
:::

### {{S0016}}

{{S0017}}

#### {{S0018}}

- {{S0019}}

$$
\Psi(x,t) = A\,e^{i(kx-\omega t)}
$$

- {{S0020}}

$$
p = \frac{h}{\lambda} = \hbar k, \qquad E = h\nu = \hbar\omega
$$

:::{important} {{S0021}}

$$
\Psi(x,t) = A\,e^{\frac{i}{\hbar}(px - Et)}
$$

:::

- {{S0022}}

```{code-cell} python
:tags: [hide-input]
# synced: complex_plane_wave
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
k, w = 2 * np.pi / 4.0, 2 * np.pi            # lambda = 4, one period per loop
x = np.linspace(0, 12, 600)
ts = np.linspace(0, 1, 36, endpoint=False)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.0), sharex=True,
                               gridspec_kw={"height_ratios": [1.25, 1]})
(re,) = ax1.plot([], [], color=TEAL, lw=2.4, label=r"Re $\Psi = \cos(kx-\omega t)$")
(im,) = ax1.plot([], [], color=ORANGE, lw=2.0, ls="--", label=r"Im $\Psi = \sin(kx-\omega t)$")
ax1.axhline(0, color=GRAY, lw=0.6)
ax1.set_ylim(-1.3, 1.95); ax1.set_yticks([-1, 0, 1]); ax1.set_ylabel(r"$\Psi$")
ax1.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
ax1.set_title(r"free particle $\Psi = e^{i(kx-\omega t)}$: two real waves, a quarter cycle apart",
              loc="left", fontsize=11)

real2 = ax2.fill_between(x, 0 * x, color=GRAY, alpha=0.25, lw=0)
(real2_line,) = ax2.plot([], [], color=GRAY, lw=1.4, label=r"a real wave, $\cos^2(kx-\omega t)$: moving dead spots")
ax2.plot(x, np.ones_like(x), color=CARDINAL, lw=2.8, label=r"$|\Psi|^2 = \mathrm{Re}^2 + \mathrm{Im}^2 = 1$ everywhere")
ax2.set_xlim(0, 12); ax2.set_ylim(0, 1.75); ax2.set_yticks([0, 1])
ax2.set_xlabel("x"); ax2.set_ylabel("probability density")
ax2.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=1)
fig.tight_layout()

def update(i):
    ph = k * x - w * ts[i]
    re.set_data(x, np.cos(ph)); im.set_data(x, np.sin(ph))
    real2_line.set_data(x, np.cos(ph) ** 2)
    real2.set_data(x, 0 * x, np.cos(ph) ** 2)

ani = FuncAnimation(fig, update, frames=len(ts), interval=85, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

{{S0023}}

#### {{S0024}}

- {{S0025}}

$$
i\hbar\,\frac{\partial \Psi}{\partial t} = E\,\Psi
$$

- {{S0026}}

$$
-i\hbar\,\frac{\partial \Psi}{\partial x} = p\,\Psi, \qquad\qquad -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} = \frac{p^2}{2m}\,\Psi
$$

- {{S0027}}

#### {{S0028}}

- {{S0029}}

$$
E = \frac{p^2}{2m} + V
$$

- {{S0030}}

$$
E\,\Psi = \frac{p^2}{2m}\,\Psi + V\,\Psi
\qquad\Longrightarrow\qquad
i\hbar\,\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\,\Psi
$$

:::{important} {{S0031}}

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} + V(x)\, \Psi = i \hbar \frac{\partial \Psi}{\partial t}
$$

:::

- {{S0032}}

$$
\underbrace{-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2}}_{\substack{\text{kinetic energy:} \\ \text{curvature of } \Psi \text{ in space}}}
\;+\;
\underbrace{V(x)\,\Psi\vphantom{\frac{\partial^2}{\partial x^2}}}_{\substack{\text{potential energy:} \\ \text{defines the system}}}
\;=\;
\underbrace{i \hbar \frac{\partial \Psi}{\partial t}\vphantom{\frac{\partial^2}{\partial x^2}}}_{\substack{\text{total energy:} \\ \text{rate of change of } \Psi \text{ in time}}}
$$

- {{S0033}}
- {{S0034}}

:::{tip} {{S0035}}
:class: dropdown

{{S0036}}

{{S0037}}

$$
\omega = \frac{\hbar k^2}{2m}
$$

{{S0038}}

:::

### {{S0039}}

{{S0040}}

### {{S0041}}

{{S0042}}

#### {{S0043}}

- {{S0044}}

$$
i\hbar\,\psi(x)\,\frac{dT}{dt} = T(t)\left[-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\,\psi\right]
$$

- {{S0045}}

$$
i\hbar\,\frac{1}{T}\frac{dT}{dt} = \frac{1}{\psi}\left[-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\,\psi\right]
$$

- {{S0046}}

#### {{S0047}}

- {{S0048}}

$$
T(t) = e^{-iEt/\hbar}
$$

- {{S0049}}

#### {{S0050}}

:::{important} {{S0051}}

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi}{d x^2} + V(x)\, \psi = E\, \psi
$$

:::

- {{S0052}}

:::{important} {{S0053}}

$$
\Psi(x,t) = \psi(x)\, e^{-iEt/\hbar}
$$

:::

### {{S0054}}

- {{S0055}}

$$
|\Psi(x,t)|^2 = |\psi(x)|^2\,\left|e^{-iEt/\hbar}\right|^2 = |\psi(x)|^2
$$

- {{S0056}}
- {{S0057}}

```{code-cell} python
:tags: [hide-input]
# synced: phase_clock
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 300)
ts = np.linspace(0, 1, 36, endpoint=False)    # one full turn of the n = 1 clock
th = np.linspace(0, 2 * np.pi, 200)
fig = plt.figure(figsize=(8, 4.3))
gs = fig.add_gridspec(2, 2, width_ratios=[3.4, 1], hspace=0.5, wspace=0.08)
rows = []
for r, n in enumerate((1, 2)):
    ax, axc = fig.add_subplot(gs[r, 0]), fig.add_subplot(gs[r, 1])
    psi = np.sqrt(2) * np.sin(n * np.pi * x)
    ax.fill_between(x, psi**2, color=CARDINAL, alpha=0.12, lw=0)
    ax.plot(x, psi**2, color=CARDINAL, lw=1.8, label=r"$|\Psi|^2$ (does not move)")
    (re,) = ax.plot([], [], color=TEAL, lw=2.4, label=r"Re $\Psi$")
    (im,) = ax.plot([], [], color=ORANGE, lw=2.0, ls="--", label=r"Im $\Psi$")
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(0, 1); ax.set_ylim(-1.7, 2.3); ax.set_yticks([-1, 0, 1, 2])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"])
    ax.set_title(rf"$\Psi_{n}(x,t) = \psi_{n}(x)\,e^{{-iE_{n}t/\hbar}}$" + ("" if n == 1 else r",  $E_2 = 4E_1$"),
                 loc="left", fontsize=11)
    if r == 0:
        ax.legend(loc="upper right", frameon=False, fontsize=9, ncol=3, bbox_to_anchor=(1.0, 1.32))
    axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
    axc.axhline(0, color=GRAY, lw=0.6); axc.axvline(0, color=GRAY, lw=0.6)
    (hand,) = axc.plot([], [], color=PURPLE, lw=2.8)
    (tip,) = axc.plot([], [], "o", color=PURPLE, ms=7)
    axc.set_aspect("equal"); axc.set_xlim(-1.25, 1.25); axc.set_ylim(-1.25, 1.25); axc.set_axis_off()
    axc.set_title("phase clock" if r == 0 else "4 times faster", fontsize=10, color=PURPLE)
    rows.append((n, psi, re, im, hand, tip))
fig.subplots_adjust(left=0.06, right=0.99, top=0.86, bottom=0.08)

def update(i):
    for n, psi, re, im, hand, tip in rows:
        z = np.exp(-2j * np.pi * n**2 * ts[i])
        re.set_data(x, psi * z.real); im.set_data(x, psi * z.imag)
        hand.set_data([0, z.real], [0, z.imag]); tip.set_data([z.real], [z.imag])

ani = FuncAnimation(fig, update, frames=len(ts), interval=110, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

{{S0058}}

### {{S0059}}

- {{S0060}}

$$
\frac{d^2\psi}{dx^2} = -\frac{2m}{\hbar^2}\,\big[E - V(x)\big]\,\psi
$$

- {{S0061}}
  - {{S0062}}
  - {{S0063}}

```{code-cell} python
:tags: [hide-input]
# synced: allowed_forbidden
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
a, V0, N = 1.2, 30.0, 700                     # half width, depth (units hbar^2/2m = 1)
x = np.linspace(-3.4, 3.4, N); h = x[1] - x[0]
V = np.where(np.abs(x) < a, 0.0, V0)
H = (np.diag(2.0 / h**2 + V) - np.diag(np.ones(N - 1) / h**2, 1)
     - np.diag(np.ones(N - 1) / h**2, -1))
En, vec = np.linalg.eigh(H)
n = 3                                         # fourth level: three nodes, long tails
E, psi = En[n], vec[:, n] / np.abs(vec[:, n]).max()
psi = psi * np.sign(psi[np.argmax(np.abs(psi))])

fig, ax = plt.subplots(figsize=(8, 3.4))
ax.axvspan(-a, a, color=TEAL, alpha=0.08, lw=0)
ax.axvspan(-3.4, -a, color=CARDINAL, alpha=0.06, lw=0)
ax.axvspan(a, 3.4, color=CARDINAL, alpha=0.06, lw=0)
ax.plot(x, V, color="k", lw=2.0)
ax.axhline(E, color=GRAY, lw=1.2, ls="--")
ax.plot(x, E + 7.5 * psi, color=TEAL, lw=2.6)
ax.text(3.35, E + 0.9, "E", color=GRAY, fontsize=11, ha="right")
ax.text(3.35, V0 + 0.9, "V(x)", color="k", fontsize=11, ha="right")
ax.text(0, 38.5, r"allowed, $E > V$" + "\n" + r"$\psi$ curves toward the axis: oscillates",
        ha="center", va="top", fontsize=10, color=TEAL)
for xc in (-2.35, 2.35):
    ax.text(xc, 38.5, r"forbidden, $E < V$" + "\n" + "curves away: decays",
            ha="center", va="top", fontsize=10, color=CARDINAL)
ax.set_xlim(-3.4, 3.4); ax.set_ylim(-2, 39.5)
ax.set_xlabel("x"); ax.set_ylabel("energy"); ax.set_yticks([])
fig.tight_layout()
plt.show()
```

{{S0064}}

### {{S0065}}

- {{S0066}}
- {{S0067}}
- {{S0068}}

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
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
```

```{marimo} python
:hide-code: true

E1 = mo.ui.slider(0.10, 3.00, step=0.01, value=0.80, show_value=True, label="trial energy E (units of ħω)")
E1
```

```{marimo} python
:hide-code: true

x1 = np.linspace(-4.6, 4.6, 1400)
h1 = x1[1] - x1[0]
V1 = 0.5 * x1**2
f1 = (1.0 + h1 * h1 * 2.0 * (E1.value - V1) / 12.0).tolist()
psi1 = [0.0, 1e-8]
for _j in range(1, len(f1) - 1):          # Numerov integration from left to right
    psi1.append(((12.0 - 10.0 * f1[_j]) * psi1[_j] - f1[_j - 1] * psi1[_j - 1]) / f1[_j + 1])
psi1 = np.array(psi1)
psi1 = psi1 / np.abs(psi1[np.abs(x1) < 2.6]).max()
ok1 = abs(psi1[-1]) < 0.05
col1 = "#107895" if ok1 else "#C8102E"

fig1, ax1 = plt.subplots(figsize=(7, 3.3))
ax1.plot(x1, V1, color="k", lw=1.8)
ax1.axhline(E1.value, color="#6c757d", lw=1.1, ls="--")
ax1.plot(x1, E1.value + 0.85 * np.clip(psi1, -9, 9), color=col1, lw=2.6)
ax1.text(0, 4.55, r"$V(x) = \frac{1}{2}kx^2$", fontsize=11, ha="center")
ax1.set_xlim(-4.6, 4.6); ax1.set_ylim(-1.2, 5.2); ax1.set_yticks([])
ax1.set_xlabel("x"); ax1.set_ylabel("energy")
ax1.set_title(f"E = {E1.value:.2f}: " + ("the tail returns to the axis" if ok1 else "the tail blows up"),
              loc="left", fontsize=11, color=col1)
fig1.tight_layout()
fig1
```

```{marimo} python
:hide-code: true

nodes1 = int(np.sum(np.diff(np.sign(psi1[np.abs(x1) < 3.5])) != 0))
mo.md(f"Trial energy **{E1.value:.2f} ħω**: " + (f"**allowed**. The solution decays on both sides and has **{nodes1}** node(s)." if ok1 else "**not allowed**. The solution cannot decay on both sides, so no particle can have this energy."))
```

{{S0069}}

- {{S0070}}
- {{S0071}}

### {{S0072}}

{{S0073}}

- {{S0074}}
- {{S0075}}

:::{important} {{S0076}}

$$
p(x) = \psi^{*}(x)\,\psi(x) = |\psi(x)|^2
$$

- {{S0077}}

:::

- {{S0078}}

```{code-cell} python
:tags: [hide-input]
# synced: born_buildup
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(7)
cand = rng.random(14000)
hits = cand[rng.random(14000) < np.sin(2 * np.pi * cand) ** 2][:3000]   # samples of 2 sin^2(2 pi x)
yj = rng.random(3000)
counts = np.unique(np.round(np.geomspace(1, 3000, 40)).astype(int))
edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
xs = np.linspace(0, 1, 300)

fig, (ax_s, ax_h) = plt.subplots(2, 1, figsize=(8, 4.0), sharex=True,
                                 gridspec_kw={"height_ratios": [1, 2.3]})
scat = ax_s.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
ax_s.set_ylim(0, 1); ax_s.set_yticks([])
for sp in ("left", "bottom"):
    ax_s.spines[sp].set_visible(False)
ax_s.tick_params(bottom=False)
bars = ax_h.bar(mid, np.zeros_like(mid), width=0.92 * dx, color=TEAL, alpha=0.5, label="detections per bin")
(curve,) = ax_h.plot([], [], color=CARDINAL, lw=2.6, label=r"prediction $N\,|\psi(x)|^2\,\Delta x$")
ax_h.set_xlim(0, 1); ax_h.set_yticks([])
ax_h.set_xticks([0, 0.5, 1]); ax_h.set_xticklabels(["0", "L/2", "L"])
ax_h.set_xlabel("position x"); ax_h.set_ylabel("detections")
ax_h.legend(loc="upper center", frameon=False, fontsize=9.5, ncol=2, bbox_to_anchor=(0.5, 1.17))
ax_s.set_title("N = 1 detection, one dot each", loc="left", fontsize=11)
fig.tight_layout()

def update(i):
    N = counts[i]
    scat.set_offsets(np.column_stack([hits[:N], yj[:N]]))
    hist = np.histogram(hits[:N], bins=edges)[0]
    for b, c in zip(bars, hist):
        b.set_height(c)
    curve.set_data(xs, N * dx * 2 * np.sin(2 * np.pi * xs) ** 2)
    ax_h.set_ylim(0, 1.3 * max(1.0, hist.max(), 2 * N * dx))
    ax_s.set_title(f"N = {N} detection" + ("" if N == 1 else "s") + ", one dot each", loc="left", fontsize=11)

ani = FuncAnimation(fig, update, frames=len(counts), interval=160, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

{{S0079}}

- {{S0080}}

```{code-cell} python
:tags: [hide-input]
# synced: h1s_cloud
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(11)
N = 5000
r = 0.5 * rng.gamma(shape=3.0, scale=1.0, size=N)       # P(r) = 4 r^2 exp(-2r), r in units of a0
cos_t = 1 - 2 * rng.random(N); phi = 2 * np.pi * rng.random(N)
xx, zz = r * np.sqrt(1 - cos_t**2) * np.cos(phi), r * cos_t
rr = np.linspace(0, 6, 300)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5), gridspec_kw={"width_ratios": [1, 1.35]})
ax1.scatter(xx, zz, s=2, color=TEAL, alpha=0.45, lw=0)
ax1.plot([0], [0], "+", color=CARDINAL, ms=9, mew=1.8)
ax1.set_aspect("equal"); ax1.set_xlim(-5, 5); ax1.set_ylim(-5, 5)
ax1.set_xlabel(r"x / $a_0$"); ax1.set_ylabel(r"z / $a_0$")
ax1.set_title(f"{N} position measurements", loc="left", fontsize=11)
ax2.hist(r, bins=np.linspace(0, 6, 49), density=True, color=TEAL, alpha=0.45, label="measured distances")
ax2.plot(rr, 4 * rr**2 * np.exp(-2 * rr), color=CARDINAL, lw=2.6, label=r"$4\pi r^2\,|\psi_{1s}|^2$")
ax2.set_xlim(0, 6); ax2.set_xlabel(r"distance from the nucleus r / $a_0$"); ax2.set_ylabel("probability density")
ax2.legend(frameon=False, fontsize=10)
ax2.set_title("the dots follow the wavefunction", loc="left", fontsize=11)
fig.tight_layout()
plt.show()
```

{{S0081}}

:::{tip} {{S0082}}
:class: dropdown

{{S0083}}

- {{S0084}}
- {{S0085}}
- {{S0086}}
- {{S0087}}

{{S0088}}

{{S0089}}

{{S0090}}

{{S0091}}

{{S0092}}

:::

### {{S0093}}

- {{S0094}}

:::{important} {{S0095}}

$$
\int_{-\infty}^{+\infty} |\psi(x)|^2\, dx = 1
$$

:::

- {{S0096}}
- {{S0097}}
- {{S0098}}

:::{note} {{S0099}}

{{S0100}}

$$
\int_0^1 (N x)^2\, dx = N^2 \int_0^1 x^2\,dx = \frac{N^2}{3} = 1 \quad\Rightarrow\quad N = \sqrt{3}
$$

{{S0101}}

:::

```{code-cell} python
:tags: [hide-input]
# synced: normalization_area
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 300)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 2.9), sharey=True)
for ax, c, col, lab, area in ((ax1, 1.0, GRAY, r"$\psi' = x$", "area = 1/3"),
                              (ax2, 3.0, TEAL, r"$\psi = \sqrt{3}\,x$", "area = 1")):
    ax.fill_between(x, c * x**2, color=col, alpha=0.25, lw=0)
    ax.plot(x, c * x**2, color=col, lw=2.6)
    ax.text(0.06, 2.55, lab, fontsize=12, color=col)
    ax.text(0.80, 0.18 * c + 0.05, area, fontsize=11, ha="center", color="k")
    ax.set_xlim(0, 1); ax.set_ylim(0, 3.1); ax.set_xlabel("x")
ax1.set_ylabel(r"$|\psi(x)|^2$")
ax1.set_title("not normalized", loc="left", fontsize=11)
ax2.set_title("normalized: a probability density", loc="left", fontsize=11)
fig.tight_layout()
plt.show()
```

{{S0102}}

### {{S0103}}

- {{S0104}}

:::{important} {{S0105}}

$$
P(a < x < b) = \int_a^b |\psi(x)|^2\,dx
$$

:::

- {{S0106}}

:::{note} {{S0107}}

{{S0108}}

$$
P(a<x<b) = \int_a^b 3x^2\,dx = b^3 - a^3
$$

{{S0109}}

:::

{{S0110}}

```{marimo} python
:hide-code: true

a2 = mo.ui.slider(0.0, 1.0, step=0.05, value=0.30, show_value=True, label="left edge a")
b2 = mo.ui.slider(0.0, 1.0, step=0.05, value=0.60, show_value=True, label="right edge b")
mo.hstack([a2, b2], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

lo2, hi2 = min(a2.value, b2.value), max(a2.value, b2.value)
P2 = hi2**3 - lo2**3
x2 = np.linspace(0, 1, 400)
m2 = (x2 >= lo2) & (x2 <= hi2)
fig2, ax2 = plt.subplots(figsize=(7, 3.0))
ax2.plot(x2, 3 * x2**2, color="#107895", lw=2.6)
ax2.fill_between(x2[m2], 3 * x2[m2] ** 2, color="#107895", alpha=0.3, lw=0)
ax2.axvline(lo2, color="#6c757d", lw=1, ls="--"); ax2.axvline(hi2, color="#6c757d", lw=1, ls="--")
ax2.set_xlim(0, 1); ax2.set_ylim(0, 3.1)
ax2.set_xlabel("x"); ax2.set_ylabel(r"$|\psi(x)|^2 = 3x^2$")
ax2.set_title(f"P({lo2:.2f} < x < {hi2:.2f}) = {P2:.3f}", loc="left", fontsize=11)
fig2.tight_layout()
fig2
```

```{marimo} python
:hide-code: true

mo.md(f"Shaded area: $b^3 - a^3 = {hi2:.2f}^3 - {lo2:.2f}^3 =$ **{P2:.3f}**, so the particle is found in this region in about **{1000 * P2:.0f}** of every 1000 measurements.")
```

{{S0111}}

### {{S0112}}

- {{S0113}}

:::{important} {{S0114}}

$$
\langle x \rangle = \int x\,|\psi(x)|^2\,dx, \qquad \langle x^2 \rangle = \int x^2\,|\psi(x)|^2\,dx, \qquad \sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}
$$

:::

- {{S0115}}

:::{note} {{S0116}}

{{S0117}}

$$
\langle x\rangle = \int_0^1 x \cdot 3x^2\,dx = \frac{3}{4}, \qquad
\langle x^2\rangle = \int_0^1 x^2 \cdot 3x^2\,dx = \frac{3}{5}
$$

$$
\sigma_x = \sqrt{\frac{3}{5} - \left(\frac{3}{4}\right)^2} = \sqrt{\frac{3}{80}} \approx 0.19
$$

:::

```{code-cell} python
:tags: [hide-input]
# synced: mean_and_spread
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 2001)
fig, axes = plt.subplots(1, 2, figsize=(8, 3.0), sharey=True)
for ax, p, col, lab in ((axes[0], 3 * x**2, TEAL, r"$|\psi|^2 = 3x^2$"),
                        (axes[1], 2 * np.sin(np.pi * x) ** 2, ORANGE, r"$|\psi_1|^2 = 2\sin^2(\pi x)$")):
    mu = np.trapezoid(x * p, x)
    sig = np.sqrt(np.trapezoid(x**2 * p, x) - mu**2)
    ax.fill_between(x, p, color=col, alpha=0.2, lw=0); ax.plot(x, p, color=col, lw=2.6)
    ax.axvspan(mu - sig, mu + sig, color=PURPLE, alpha=0.12, lw=0)
    ax.axvline(mu, color=PURPLE, lw=1.6)
    ax.plot([mu], [-0.16], marker="^", color=PURPLE, ms=11, clip_on=False, zorder=6)
    ax.set_title(lab + rf":  $\langle x\rangle = {mu:.2f}$,  $\sigma_x = {sig:.2f}$", loc="left", fontsize=10.5)
    ax.set_xlim(0, 1); ax.set_ylim(0, 3.2); ax.set_xlabel("x")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1]); ax.tick_params(axis="x", pad=9)
axes[0].set_ylabel("probability density")
axes[0].text(0.75 - 0.21, 2.75, r"$\pm\sigma_x$", color=PURPLE, fontsize=11, ha="right")
fig.tight_layout()
plt.show()
```

{{S0118}}

### {{S0119}}

{{S0120}}

- {{S0121}}

{{S0122}}

- {{S0123}}

:::{important} {{S0124}}

$$
\hat{H} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x)
$$

$$
\hat{H}\,\Psi = i\hbar \frac{\partial \Psi}{\partial t} \qquad\qquad \hat{H}\,\psi = E\,\psi
$$

:::

- {{S0125}}

#### {{S0126}}

- {{S0127}}

$$
\hat{A} f(x) = a\, f(x)
$$

```{code-cell} python
:tags: [hide-input]
# synced: eigen_test
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(-3, 3, 500); a = 1.5
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.0))
ax1.plot(x, np.sin(a * x), color=TEAL, lw=2.6, label=r"$f = \sin(ax)$")
ax1.plot(x, -a**2 * np.sin(a * x), color=CARDINAL, lw=2.2, ls="--", label=r"$f'' = -a^2 \sin(ax)$")
ax1.set_title(r"same shape, rescaled: eigenfunction of $d^2/dx^2$", loc="left", fontsize=10.5)
ax2.plot(x, np.exp(-x**2), color=TEAL, lw=2.6, label=r"$f = e^{-x^2}$")
ax2.plot(x, (4 * x**2 - 2) * np.exp(-x**2), color=CARDINAL, lw=2.2, ls="--", label=r"$f'' = (4x^2-2)\,e^{-x^2}$")
ax2.set_title("new shape: not an eigenfunction", loc="left", fontsize=10.5)
for ax in (ax1, ax2):
    ax.axhline(0, color=GRAY, lw=0.6); ax.set_xlim(-3, 3); ax.set_ylim(-2.6, 3.6); ax.set_xlabel("x")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
fig.tight_layout()
plt.show()
```

{{S0128}}

- {{S0129}}

:::{important} {{S0130}}

$$
\hat{H}\, \psi_n = E_n\, \psi_n
$$

- {{S0131}}
- {{S0132}}

:::

#### {{S0133}}

- {{S0134}}

:::{important} {{S0135}}

$$
\langle A \rangle = \int \psi^{*}(x)\, \hat{A}\, \psi(x)\, dx
$$

:::

{{S0136}}

:::{note} {{S0137}}

{{S0138}}

{{S0139}}

$$
\langle p\rangle = \int_0^1 \psi_n\,(-i\hbar)\,\frac{d\psi_n}{dx}\,dx = -2i\hbar\, n\pi \int_0^1 \sin(n\pi x)\cos(n\pi x)\,dx = 0
$$

{{S0140}}

{{S0141}}

$$
\langle p^2\rangle = -\hbar^2\int_0^1 \psi_n\,\psi_n''\,dx = (n\pi\hbar)^2, \qquad
\langle E\rangle = \frac{\langle p^2\rangle}{2m} = \frac{(n\pi\hbar)^2}{2m}
$$

{{S0142}}

:::

#### {{S0143}}

- {{S0144}}

$$
\Psi(x,t) = \sum_n c_n\, \psi_n(x)\, e^{-iE_n t/\hbar}
$$

- {{S0145}}

### {{S0146}}

{{S0147}}

### {{S0148}}

#### {{S0149}}

{{S0150}}

:::{admonition} {{S0151}}
:class: dropdown solution

{{S0152}}

$$
-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} = \frac{p^2}{2m}\,\Psi
$$

{{S0153}}

$$
i\hbar\frac{\partial \Psi}{\partial t} = i\hbar\left(-\frac{iE}{\hbar}\right)\Psi = E\,\Psi
$$

{{S0154}}

:::

#### {{S0155}}

{{S0156}}

$$
\Psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1t/\hbar} + \psi_2(x)\,e^{-iE_2t/\hbar}\right]
$$

{{S0157}}

:::{admonition} {{S0158}}
:class: dropdown solution

{{S0159}}

$$
|\Psi|^2 = \frac{1}{2}\left[\psi_1^2 + \psi_2^2 + \psi_1\psi_2\left(e^{i(E_2-E_1)t/\hbar} + e^{-i(E_2-E_1)t/\hbar}\right)\right]
$$

$$
|\Psi|^2 = \frac{1}{2}\left[\psi_1^2 + \psi_2^2\right] + \psi_1\psi_2\cos\left(\frac{(E_2-E_1)\,t}{\hbar}\right)
$$

{{S0160}}

:::

#### {{S0161}}

{{S0162}}

:::{admonition} {{S0163}}
:class: dropdown solution

{{S0164}}

$$
\int_{-1}^{1} N^2\cos^2\left(\frac{\pi x}{2}\right)dx = \frac{N^2}{2}\int_{-1}^{1}\left[1 + \cos(\pi x)\right]dx = \frac{N^2}{2}\left[2 + 0\right] = N^2
$$

{{S0165}}

$$
P\left(0 < x < \tfrac{1}{2}\right) = \frac{1}{2}\int_0^{1/2}\left[1 + \cos(\pi x)\right]dx = \frac{1}{2}\left[\frac{1}{2} + \frac{1}{\pi}\right] \approx 0.41
$$

{{S0166}}

:::

#### {{S0167}}

{{S0168}}

- {{S0169}}
- {{S0170}}

:::{admonition} {{S0171}}
:class: dropdown solution

{{S0172}}

$$
-i \hbar \dfrac{\partial}{\partial x} A \sin(ax) = -i \hbar A a \cos(ax)
$$

{{S0173}}

$$
-\dfrac{\hbar^2}{2m} \dfrac{\partial^2}{\partial x^2} A \sin(ax) = \dfrac{\hbar^2 a^2}{2m}\, A \sin(ax)
$$

{{S0174}}

{{S0175}}

$$
-i\hbar \dfrac{\partial}{\partial x} N e^{-ikx} = -i\hbar(-ik)\,N e^{-ikx} = -\hbar k\, N e^{-ikx}
$$

{{S0176}}

{{S0177}}

:::

#### {{S0178}}

{{S0179}}

:::{admonition} {{S0180}}
:class: dropdown solution

$$
\frac{d}{dx} e^{-\alpha x^2} = -2\alpha x\, e^{-\alpha x^2}
$$

$$
\frac{d^2}{dx^2} e^{-\alpha x^2} = \left( 4\alpha^2 x^2 - 2\alpha \right) e^{-\alpha x^2}
$$

{{S0181}}

:::

#### {{S0182}}

{{S0183}}

#### {{S0184}}

{{S0185}}

#### {{S0186}}

{{S0187}}

#### {{S0188}}

{{S0189}}

#### {{S0190}}

{{S0191}}
