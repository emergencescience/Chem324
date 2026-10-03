---
kernelspec:
  name: python3
  display_name: Python 3
---

# {{S0001}}

 :::{note} {{S0002}}

{{S0003}}

   - {{S0004}}
   
   - {{S0005}}
   
   - {{S0006}}
   
   - {{S0007}}
   
   - {{S0008}}

   - {{S0009}}
:::

### {{S0010}}

- {{S0011}}
- {{S0012}}
- {{S0013}}
- {{S0014}}
- {{S0015}}

```{code-cell} python
:tags: [hide-input]
# synced: box_bounce
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(5)
xc = rng.random(4000)                                       # classical: snapshots at random times
cand = rng.random(16000)
xq = cand[rng.random(16000) < np.sin(3 * np.pi * cand) ** 2][:4000]   # quantum: samples of |psi_3|^2
yj = rng.random(4000)
counts = np.unique(np.round(np.geomspace(1, 4000, 44)).astype(int))
counts = np.concatenate([counts, np.full(8, counts[-1])])
edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
xs = np.linspace(0, 1, 300)
fig, axes = plt.subplots(2, 2, figsize=(8, 3.9), sharex=True,
                         gridspec_kw={"height_ratios": [1, 2.2], "hspace": 0.12, "wspace": 0.1})
(ta, tb), (ha, hb) = axes
for ax in (ta, tb):
    ax.axvline(0, color="k", lw=3); ax.axvline(1, color="k", lw=3)
    ax.set_ylim(0, 1); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.tick_params(bottom=False)
ta.set_title("classical: a ball bouncing at constant speed", loc="left", fontsize=10.5)
tb.set_title(r"quantum, $n = 3$: each dot is one detection", loc="left", fontsize=10.5)
(trail,) = ta.plot([], [], "o", color=ORANGE, ms=9, alpha=0.25)
(ball,) = ta.plot([], [], "o", color=ORANGE, ms=12)
scat = tb.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
bars_c = ha.bar(mid, 0 * mid, width=0.92 * dx, color=ORANGE, alpha=0.5)
bars_q = hb.bar(mid, 0 * mid, width=0.92 * dx, color=TEAL, alpha=0.5)
(pc,) = ha.plot([], [], color=GRAY, lw=2.4, ls="--", label=r"flat: $1/L$")
(pq,) = hb.plot([], [], color=CARDINAL, lw=2.4, label=r"$|\psi_3(x)|^2$")
for ax in (ha, hb):
    ax.set_xlim(-0.02, 1.02); ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("position x")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
ha.set_ylabel("times caught here")
fig.subplots_adjust(left=0.05, right=0.99, top=0.84, bottom=0.13)
sup = fig.suptitle("", fontsize=11.5)
tri = lambda s: 0.04 + 0.92 * (1 - np.abs(2 * (s % 1) - 1))  # bounce between the walls

def update(i):
    N = counts[i]
    pos = tri(np.arange(i - 3, i + 1) / 11.0)
    trail.set_data(pos[:-1], np.full(3, 0.5)); ball.set_data(pos[-1:], [0.5])
    scat.set_offsets(np.column_stack([xq[:N], yj[:N]]))
    hc = np.histogram(xc[:N], bins=edges)[0]; hq = np.histogram(xq[:N], bins=edges)[0]
    for b, c in zip(bars_c, hc):
        b.set_height(c)
    for b, c in zip(bars_q, hq):
        b.set_height(c)
    pc.set_data(xs, np.full_like(xs, N * dx)); pq.set_data(xs, N * dx * 2 * np.sin(3 * np.pi * xs) ** 2)
    top = 1.3 * max(1.0, hc.max(), hq.max(), 2 * N * dx)
    ha.set_ylim(0, top); hb.set_ylim(0, top)
    sup.set_text(f"N = {N} position measurement" + ("" if N == 1 else "s"))

ani = FuncAnimation(fig, update, frames=len(counts), interval=150, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

{{S0016}}

### {{S0017}}


:::{figure} {{S0018}}
:label: fig-particle-in-a-box-2
:alt: Particle in a box
:width: 300px

{{S0019}}
:::

{{S0020}}

- {{S0021}}

$$
V(x) =
\begin{cases} 
\infty & x \le 0 \text{ or } x \ge L \\ 
0 & 0 < x < L
\end{cases}
$$

- {{S0022}}

$$
\psi(0) = \psi(L) = 0
$$

- {{S0023}}

$$
\hat{H} = \hat{K} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}
$$

- {{S0024}}

$$
\hat{H} \psi(x) = E \psi(x)
$$

- {{S0025}}

$$
-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x) = E \psi(x)
$$

$$
\psi''(x) = -k^2 \psi(x)
$$

- {{S0026}}

$$
k^2 = \frac{2mE}{\hbar^2}
$$

### {{S0027}}

- {{S0028}}

$$
\psi''(x) = -k^2 \psi(x)
$$

- {{S0029}}

$$
\psi(x) = c_1 e^{ikx} + c_2 e^{-ikx} = A \cos(kx) + B \sin(kx)
$$

- {{S0030}}

$$
\psi(x) = B \sin(kx)
$$

- {{S0031}}

$$
B \sin(kL) = 0
$$

- {{S0032}}

$$
kL = n\pi \quad \text{or} \quad k = \frac{n\pi}{L}
$$

- {{S0033}}

$$
\psi(x) = B \sin\left(\frac{n\pi}{L}x\right)
$$

- {{S0034}}

$$
E_n = \frac{n^2 h^2}{8mL^2}
$$

- {{S0035}}
- {{S0036}}

### {{S0037}}

- {{S0038}}

$$
\int_0^L \psi_n(x)^2 \, dx = 1
$$

- {{S0039}}

$$
B_n^2 \int_0^L \sin^2\left(\frac{n\pi x}{L}\right) dx = \frac{B_n^2}{2} \int_0^L \left[ 1 - \cos\left(\frac{2n\pi x}{L}\right) \right] dx =1
$$

- {{S0040}}

$$
\frac{B_n^2}{2} \cdot L = 1
$$

- {{S0041}}

$$
B_n = \sqrt{\frac{2}{L}}
$$

### {{S0042}}

:::{important} {{S0043}}

$${\psi_n(x) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}$$

$${E_n=\frac{n^2 h^2}{8mL^2}}$$

:::

:::{important} {{S0044}}

$${\psi_n(x, t) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}\cdot e^{-i\frac{E_n t}{\hbar}}$$

$$\Psi(x,t) = \sum_n c_n \psi_n(x, t)$$

- {{S0045}}

:::

```{code-cell} python
:tags: [hide-input]
# synced: pib_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.4), sharey=True, gridspec_kw={"wspace": 0.08})
for ax in (ax1, ax2):
    ax.plot([0, 0, 1, 1], [18.3, 0, 0, 18.3], color="k", lw=2.6)
    ax.set_xlim(-0.04, 1.04); ax.set_ylim(-0.4, 18.3)
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("x")
    ax.spines["left"].set_visible(False)
for n in range(1, 5):
    E, s = n * n, np.sin(n * np.pi * x)
    for ax in (ax1, ax2):
        ax.hlines(E, 0, 1, color=GRAY, lw=0.8, ls="--")
    ax1.plot(x, E + 1.25 * s, color=TEAL, lw=2.4)
    ax2.fill_between(x, E, E + 1.6 * s**2, color=CARDINAL, alpha=0.18, lw=0)
    ax2.plot(x, E + 1.6 * s**2, color=CARDINAL, lw=2.2)
    ax2.plot(np.arange(1, n) / n, np.full(n - 1, E), "o", color="k", ms=5, zorder=5)
    ax2.text(1.06, E, rf"$n = {n}$,  " + (r"$E_1$" if n == 1 else rf"${E}E_1$"), va="center", fontsize=11.5)
ax1.set_yticks([]); ax1.set_ylabel("energy")
ax1.set_title(r"$\psi_n(x)$, drawn on its level $E_n$", loc="left", fontsize=11)
ax2.set_title(r"$|\psi_n(x)|^2$: dots mark the $n-1$ nodes", loc="left", fontsize=11)
fig.subplots_adjust(left=0.05, right=0.83, top=0.92, bottom=0.12)
plt.show()
```

{{S0046}}

### {{S0047}}

{{S0048}}

- {{S0049}}

$$E_1 = h^2/8mL^2$$

- {{S0050}}

- {{S0051}}

- {{S0052}}

$$E_{n+1} - E_n = (2n+1)\frac{h^2}{8mL^2}$$

{{S0053}}

- {{S0054}}
- {{S0055}}

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "plotly",
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
import plotly.graph_objects as go
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
```

```{marimo} python
:hide-code: true

box_L = mo.ui.slider(0.5, 1.0, step=0.05, value=1.0, show_value=True, label="box length L (units of L₀)")
box_L
```

```{marimo} python
:hide-code: true

_L = box_L.value
_x = np.linspace(0, _L, 300)
_fig, (_ax, _axl) = plt.subplots(1, 2, figsize=(7.5, 3.4), gridspec_kw={"width_ratios": [1.4, 1]})
_ax.plot([0, 0, _L, _L], [38, 0, 0, 38], color="k", lw=2.6)
for _n, _c in zip((1, 2, 3), (TEAL, ORANGE, PURPLE)):
    _E = _n**2 / _L**2
    _ax.hlines(_E, 0, _L, color=_c, lw=0.9, ls="--")
    _ax.plot(_x, _E + 1.2 * np.sin(_n * np.pi * _x / _L), color=_c, lw=2.4)
    _ax.text(_L + 0.05, _E, rf"$E_{_n} = {_E:.1f}$", color=_c, va="center", fontsize=11)
_ax.text(0, -1.5, "0", ha="center", va="top", fontsize=11)
_ax.text(_L, -1.5, "L", ha="center", va="top", fontsize=11)
_ax.set_xlim(-0.05, 1.42); _ax.set_ylim(-4.5, 38); _ax.set_xticks([]); _ax.set_yticks([])
_ax.spines["left"].set_visible(False); _ax.spines["bottom"].set_visible(False)
_ax.set_title(rf"$L = {_L:.2f}\,L_0$", loc="left", fontsize=11)
_Lg = np.linspace(0.45, 3, 300)
_axl.plot(_Lg, 1 / _Lg**2, color=TEAL, lw=2.2)
_axl.plot([_L], [1 / _L**2], "o", color=TEAL, ms=9)
_axl.set_xlim(0.4, 3); _axl.set_ylim(0, 5)
_axl.set_xlabel(r"$L / L_0$"); _axl.set_ylabel(r"$E_1$")
_axl.set_title(r"$E_1 \propto 1/L^2$: never zero", loc="left", fontsize=11)
_fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.17, wspace=0.22)
_fig
```

{{S0056}}

### {{S0057}}

1. {{S0058}}
    - {{S0059}}
    - {{S0060}}
    - {{S0061}}

2. {{S0062}}

- {{S0063}}
- {{S0064}}
- {{S0065}}
    - {{S0066}}
    - {{S0067}}

- {{S0068}}

### {{S0069}}

- {{S0070}}
- {{S0071}}

$$
P_n = \frac{1}{3} + \frac{\sin(2n\pi/3) - \sin(4n\pi/3)}{2n\pi}
$$

- {{S0072}}

```{marimo} python
:hide-code: true

n_c = mo.ui.slider(1, 40, step=1, value=1, show_value=True, label="quantum number n")
n_c
```

```{marimo} python
:hide-code: true

_n = n_c.value
_x = np.linspace(0, 1, 3000)
_p = 2 * np.sin(_n * np.pi * _x) ** 2
_P = 1 / 3 + (np.sin(2 * _n * np.pi / 3) - np.sin(4 * _n * np.pi / 3)) / (2 * _n * np.pi)
_fig, _ax = plt.subplots(figsize=(7, 3.0))
_ax.axvspan(1 / 3, 2 / 3, color=PURPLE, alpha=0.09, lw=0)
_ax.fill_between(_x, _p, color=CARDINAL, alpha=0.2, lw=0)
_ax.plot(_x, _p, color=CARDINAL, lw=1.4 if _n < 12 else 0.8, label=r"$|\psi_n|^2$")
_ax.axhline(1, color="k", lw=2, ls="--", label=r"classical: $1/L$")
_ax.plot([0, 0, 1, 1], [2.6, 0, 0, 2.6], color="k", lw=2.6)
_ax.set_xlim(-0.02, 1.02); _ax.set_ylim(0, 2.6)
_ax.set_yticks([0, 1, 2]); _ax.set_yticklabels(["0", "1/L", "2/L"])
_ax.set_xticks([0, 1 / 3, 2 / 3, 1]); _ax.set_xticklabels(["0", "L/3", "2L/3", "L"])
_ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=2, bbox_to_anchor=(1.0, 1.18))
_ax.set_title(f"n = {_n}:  P(middle third) = {_P:.3f}", loc="left", fontsize=11, color=PURPLE)
_fig.tight_layout()
_fig
```

{{S0073}}

### {{S0074}}

- {{S0075}}
- {{S0076}}

$$
\Psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1t/\hbar} + \psi_2(x)\,e^{-iE_2t/\hbar}\right]
$$

- {{S0077}}

$$
|\Psi(x,t)|^2 = \frac{1}{2}\left[\psi_1^2(x) + \psi_2^2(x)\right] + \psi_1(x)\,\psi_2(x)\cos\omega t
$$

```{code-cell} python
:tags: [hide-input]
# synced: box_slosh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
fixed, cross = 0.5 * (p1**2 + p2**2), p1 * p2               # |Psi|^2 = fixed + cross cos(wt): even + odd about L/2
nf = 60
ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # E1 = 1, E2 = 4, hbar = 1: w = 3, three sloshes
xbar = lambda t: 0.5 - 16 / (9 * np.pi**2) * np.cos(3 * t)  # <x>(t) = L/2 + x12 cos(wt), x12 = -16L/9pi^2
th = np.linspace(0, 2 * np.pi, 200)
fig = plt.figure(figsize=(7.2, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], height_ratios=[2, 1], hspace=0.42, wspace=0.08)
ax, axx = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])
axc, axl = fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])
ax.plot(x, fixed, color=GRAY, lw=1.8, ls="--", label=r"$\frac{1}{2}(\psi_1^2 + \psi_2^2)$")
(dens,) = ax.plot([], [], color=CARDINAL, lw=2.8, label=r"$|\Psi|^2$")
band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.18, lw=0)]
(mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=14, zorder=6, ls="none", label=r"$\langle x\rangle$")
ax.plot([0, 0, 1, 1], [3.35, 0, 0, 3.35], color="k", lw=2.6)          # peak of |Psi|^2 is 3.10
ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 3.35); ax.set_xticks([]); ax.set_yticks([])
ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.legend(loc="lower left", bbox_to_anchor=(0, 0.97), ncol=3, frameon=False, fontsize=13,
          handlelength=1.6, columnspacing=1.4)
axx.axhline(0, color=GRAY, lw=0.8)
(crs,) = axx.plot([], [], color=PURPLE, lw=2.6)
cband = [axx.fill_between(x, 0 * x, color=PURPLE, alpha=0.18, lw=0)]
axx.set_xlim(-0.02, 1.02); axx.set_ylim(-1.7, 1.7); axx.set_yticks([])
axx.set_xticks([0, 0.5, 1]); axx.set_xticklabels(["0", "L/2", "L"], fontsize=13)
axx.spines["left"].set_visible(False)
axx.set_title(r"cross term $\psi_1\psi_2\cos\omega t$", loc="left", fontsize=13, color=PURPLE)
for a in (ax, axx):
    a.axvline(0.5, color=GRAY, lw=0.8, ls=":")
axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
(arc,) = axc.plot([], [], color=PURPLE, lw=3.2, label=r"$\omega t$")
(h1,) = axc.plot([], [], color=TEAL, lw=3.2, label=r"$E_1$")
(h2,) = axc.plot([], [], color=ORANGE, lw=3.2, label=r"$E_2 = 4E_1$")
axc.set_aspect("equal"); axc.set_xlim(-1.15, 1.15); axc.set_ylim(-1.15, 1.15); axc.set_axis_off()
axc.set_title("phase clocks", fontsize=13)
axl.set_axis_off()
axl.legend(handles=[h1, h2, arc], loc="center", frameon=False, fontsize=13, handlelength=1.2)
fig.subplots_adjust(left=0.02, right=0.99, top=0.87, bottom=0.1)

def update(i):
    t = ts[i]
    c = cross * np.cos(3 * t)
    dens.set_data(x, fixed + c)
    band[0].remove(); band[0] = ax.fill_between(x, fixed + c, color=CARDINAL, alpha=0.18, lw=0)
    mark.set_data([xbar(t)], [0.14])
    crs.set_data(x, c)
    cband[0].remove(); cband[0] = axx.fill_between(x, c, color=PURPLE, alpha=0.18, lw=0)
    a1, a2 = -t, -4 * t                                     # clock hands: e^{-iE1 t}, e^{-iE2 t}
    d = (a1 - a2) % (2 * np.pi)                             # angle between the hands, w t
    s = np.linspace(a2, a2 + d, 40) if d <= np.pi else np.linspace(a1, a1 + 2 * np.pi - d, 40)
    arc.set_data(0.42 * np.cos(s), 0.42 * np.sin(s))
    h1.set_data([0, np.cos(a1)], [0, np.sin(a1)]); h2.set_data([0, np.cos(a2)], [0, np.sin(a2)])

ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

{{S0078}}

- {{S0079}}

$$
\langle x \rangle(t) = \frac{L}{2} + \cos\omega t \int_0^L x\,\psi_1\psi_2\,dx = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\omega t
$$

- {{S0080}}

### {{S0081}}

:::{figure} {{S0082}}
:label: fig-particle-in-a-box-3
:alt: pib1
:width: 300px

{{S0083}}
:::

$$\hat{H}\psi(x,y,z) = E\psi(x,y,z)$$


$${-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) = E\psi}$$

- {{S0084}}

$${\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\left|\psi(x,y,z)\right|^2dxdydz = 1}$$

- {{S0085}}

$${-\frac{\hbar^2}{2m}\Delta\psi = E\psi} \\
{\textnormal{with }\psi(a,y,z) = \psi(x,b,z) = \psi(x,y,c) = 0} \\
{\textnormal{and }\psi(0,y,z) = \psi(x,0,z) = \psi(x,y,0) = 0}$$

- {{S0086}}
- {{S0087}}

$${\psi(x,y,z) = X(x)Y(y)Z(z)}$$

- {{S0088}}

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2} + \frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2} + \frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E}$$

- {{S0089}}

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}\right] = E_x\textnormal{ with }X(0) = X(a) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}\right] = E_y\textnormal{ with }Y(0) = Y(b) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E_z\textnormal{ with }Z(0) = Z(c) = 0}$$

- {{S0090}}

$${X(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n_x\pi x}{a}\right)}\\
{Y(y) = \sqrt{\frac{2}{b}}\sin\left(\frac{n_y\pi y}{b}\right)}\\
{Z(z) = \sqrt{\frac{2}{c}}\sin\left(\frac{n_z\pi z}{c}\right)}$$

:::{important} {{S0091}}

{{S0092}}

$${\psi(x,y,z) = X(x)Y(y)Z(z) = \sqrt{\frac{8}{abc}}\sin\left(\frac{n_x\pi x}{a}\right)\sin\left(\frac{n_y\pi y}{b}\right)\sin\left(\frac{n_z\pi z}{c}\right)}$$

$${E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)}$$

{{S0093}}

$$
\psi_{n_x, n_y, n_z}(x, y, z) = \frac{2}{L^{3/2}} \sin\left( \frac{n_x \pi x}{L} \right) \sin\left( \frac{n_y \pi y}{L} \right) \sin\left( \frac{n_z \pi z}{L} \right)
$$


$$
E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)
$$


:::


- {{S0094}}

- {{S0095}}


:::{admonition} {{S0096}}
:class: dropdown

{{S0097}}

{{S0098}}

{{S0099}}
:::


```{marimo} python
:hide-code: true

nx3 = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="nx")
ny3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="ny")
nz3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="nz")
mo.hstack([nx3, ny3, nz3], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

side3 = 10.0
g3 = np.linspace(0, side3, 48)
X3, Y3, Z3 = np.meshgrid(g3, g3, g3, indexing="ij")

def psi1d_m(q, n_q):
    return np.sqrt(2 / side3) * np.sin(n_q * np.pi * q / side3)

psi_3d = psi1d_m(X3, nx3.value) * psi1d_m(Y3, ny3.value) * psi1d_m(Z3, nz3.value)
amp3 = 0.5 * np.abs(psi_3d).max()

fig3d = go.Figure(data=go.Isosurface(
    x=X3.flatten(), y=Y3.flatten(), z=Z3.flatten(), value=psi_3d.flatten(),
    colorscale="RdBu", isomin=-amp3, isomax=amp3, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig3d.update_layout(
    scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z", aspectmode="data"),
    width=680, height=460,
    title_text=f"wavefunction isosurfaces, state ({nx3.value}, {ny3.value}, {nz3.value})",
)
fig3d
```

{{S0100}}

- {{S0101}}

```{marimo} python
:hide-code: true

side_a = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side a (units of L)")
side_b = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side b")
side_c = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side c")
mo.hstack([side_a, side_b, side_c], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_s = (side_a.value, side_b.value, side_c.value)
_E = {}
for _i in range(1, 9):
    for _j in range(1, 9):
        for _k in range(1, 9):
            _E[(_i, _j, _k)] = _i**2 / _s[0]**2 + _j**2 / _s[1]**2 + _k**2 / _s[2]**2
_levels = []
for _st in sorted(_E, key=_E.get):
    if _levels and abs(_E[_st] - _levels[-1][0]) < 1e-6:
        _levels[-1][1].append(_st)
    else:
        _levels.append([_E[_st], [_st]])
_levels = _levels[:7]
_top = _levels[-1][0] * 1.08
_fig, _ax = plt.subplots(figsize=(7, 4.2))
_ylab = -1.0
for _Eg, _ss in _levels:
    _g = len(_ss)
    _col = PURPLE if _g > 1 else TEAL
    for _q in range(_g):
        _ax.hlines(_Eg, 0.1 + 0.34 * _q, 0.38 + 0.34 * _q, color=_col, lw=3.2)
    _ylab = max(_Eg, _ylab + 0.055 * _top)                  # keep labels of close levels apart
    _lab = f"g = {_g}:  " + ", ".join(f"({_a},{_b},{_c})" for _a, _b, _c in _ss) if _g <= 3 else f"g = {_g}"
    _ax.text(2.2, _ylab, _lab, va="center", fontsize=10, color=_col)
_ax.set_xlim(0, 5.4); _ax.set_ylim(0, _top)
_ax.set_xticks([]); _ax.set_yticks([]); _ax.spines["bottom"].set_visible(False)
_ax.set_ylabel(r"energy (units of $h^2/8mL^2$)")
_ax.set_title(f"sides a, b, c = {_s[0]:.2f}, {_s[1]:.2f}, {_s[2]:.2f}: the seven lowest levels", loc="left", fontsize=11)
_fig.tight_layout()
_fig
```

{{S0102}}

### {{S0103}}

{{S0104}}

$$
\langle A \rangle = \int \psi^*(x)\hat{A}\psi(x)dx
$$

{{S0105}}

{{S0106}}

:::{note} {{S0107}}
:class: dropdown

{{S0108}}

{{S0109}}

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
$$

{{S0110}}
- {{S0111}}
- {{S0112}}
- {{S0113}}

{{S0114}}

{{S0115}}

$$
\langle x \rangle = \int_0^L x |\psi_n(x)|^2 \, dx
$$

{{S0116}}

$$
|\psi_n(x)|^2 = \left( \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) \right)^2 = \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right)
$$

{{S0117}}

{{S0118}}

$$
\langle x \rangle = \int_0^L x \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right) \, dx
$$

{{S0119}}

{{S0120}}

{{S0121}}

$$
\sin^2 \theta = \frac{1}{2} \left(1 - \cos(2\theta)\right)
$$

{{S0122}}

$$
\langle x \rangle = \frac{2}{L} \int_0^L x \left( \frac{1}{2} \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) \right) dx
$$

{{S0123}}

$$
\langle x \rangle = \frac{1}{L} \int_0^L x \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) dx
$$

{{S0124}}

$$
\langle x \rangle = \frac{1}{L} \left( \int_0^L x \, dx - \int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx \right)
$$

{{S0125}}

- {{S0126}}

$$
\int_0^L x \, dx = \frac{L^2}{2}
$$

- {{S0127}}

$$
\int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx = 0
$$

{{S0128}}

{{S0129}}

$$
\langle x \rangle = \frac{1}{L} \times \frac{L^2}{2} = \frac{L}{2}
$$

{{S0130}}

{{S0131}}

$$
\langle x \rangle = \frac{L}{2}
$$

{{S0132}}

{{S0133}}

{{S0134}}
- {{S0135}}
- {{S0136}}
- {{S0137}}

{{S0138}}
:::


### {{S0139}}

{{S0140}}

:::{figure} {{S0141}}
:width: 70%

{{S0142}}
:::

- {{S0143}}
- {{S0144}}

:::{figure} {{S0145}}
:width: 70%

{{S0146}}
:::

#### {{S0147}}

{{S0148}}

{{S0149}}

$$
L = 1.35\,\text{Å} + 1.54\,\text{Å} + 1.35\,\text{Å} = 4.24\,\text{Å}.
$$

{{S0150}}

{{S0151}}

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{hc}{\lambda}.
$$

```{code-cell} python
:tags: [hide-input]
import numpy as np

h = 6.626e-34    # Planck constant (J s)
m = 9.109e-31    # electron mass (kg)
c = 3.0e8        # speed of light (m/s)
# box ending at the end carbons, then one carbon radius (0.77 A) past each end
for label, L in [("L = 4.24 A", 4.24e-10), ("L = 5.78 A", 5.78e-10)]:
    E = lambda n: n**2 * h**2 / (8 * m * L**2)
    dE = E(3) - E(2)             # HOMO (n=2) -> LUMO (n=3)
    lam = h * c / dE
    print(f"{label}:  Delta E (2 -> 3) = {dE:.3e} J,  absorption wavelength = {lam * 1e9:.0f} nm")
```

{{S0152}}

### {{S0153}}

#### {{S0154}}

{{S0155}}

:::{admonition} {{S0156}}
:class: dropdown solution

{{S0157}}

$$\begin{equation}
\text{Prob}(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2}P(x)dx = \int_{x_1}^{x_2} \psi^*(x)\psi(x)dx
\end{equation}$$

{{S0158}}

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) = \frac{2}{a}\int_{\frac{a}{3}}^{\frac{2a}{3}} \sin^2\frac{n\pi x}{a}dx
\end{align}$$

{{S0159}}

$$\begin{equation}
\int\sin^2axdx = \frac{x}{2} - \frac{\sin2ax}{4a}
\end{equation}$$

{{S0160}}

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) &= \frac{2}{a}\left[ \frac{x}{2} - \frac{\sin\frac{2n\pi x}{a}}{\frac{4n\pi}{a}}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{x}{2} - \frac{a\sin\frac{2n\pi x}{a}}{4n\pi}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{a}{3} - \frac{a\sin\frac{4n\pi}{3}}{4n\pi} - \frac{a}{6} + \frac{a\sin\frac{2n\pi }{3}}{4n\pi}\right] \\
&= 2\left[ \frac{1}{6}  + \frac{\sin\frac{2n\pi }{3} - \sin\frac{4n\pi}{3}}{4n\pi}\right]
\end{align}$$
:::

#### {{S0161}}

{{S0162}}

:::{admonition} {{S0163}}
:class: dropdown solution

{{S0164}}

$$\begin{equation}
\langle x^2 \rangle = \int \psi^*(x) x^2 \psi(x)dx
\end{equation}$$

{{S0165}}

{{S0166}}

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx
\end{align}$$

{{S0167}}

$$\begin{equation}
\int x^2\sin^2\alpha xdx = \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2} + C
\end{equation}$$

{{S0168}}

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx \\
&= \frac{2}{a}\left[ \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2}\right]_0^a \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha a - \frac{a\cos 2\alpha a}{4\alpha^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\frac{n\pi}{a}} - \frac{1}{8\left(\frac{n\pi}{a}\right)^3}\right)\sin2\frac{n\pi}{a} a - \frac{a\cos 2\frac{n\pi}{a} a}{4\left(\frac{n\pi}{a}\right)^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \frac{a^3}{\left(2n\pi\right)^2} \right] \\
&=  \frac{a^2}{3} - \frac{a^2}{2\left(n\pi\right)^2} 
\end{align}$$

{{S0169}}

$$\begin{equation}
\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \frac{a}{2\pi n}\sqrt{\frac{\pi^2n^2}{3} -2}
\end{equation}$$
:::

#### {{S0170}}

{{S0171}}

:::{admonition} {{S0172}}
:class: dropdown solution

{{S0173}}

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{E}\psi_n(x)dx
\end{equation}$$

{{S0174}}

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx.
\end{equation}$$

{{S0175}}

$$\begin{equation}
\hat{H}\psi_n(x)  = E_n\psi_n(x)
\end{equation}$$

{{S0176}}

$$\begin{align}
\langle E \rangle &= \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx \\
&=\int_0^a \psi_n^*(x)E_n\psi_n(x)dx \\
&=E_n\int_0^a \psi_n^*(x)\psi_n(x)dx \\
&= E_n
\end{align}$$

{{S0177}}
:::

#### {{S0178}}

{{S0179}}

:::{admonition} {{S0180}}
:class: dropdown solution

{{S0181}}

$$\begin{equation}
\langle p \rangle = \int_0^a \psi_n^*(x)\hat{p}\psi_n(x)dx
\end{equation}$$

{{S0182}}

$$\begin{equation}
\hat{p}_x = -i\hbar\frac{d}{dx}
\end{equation}$$

{{S0183}}

$$\begin{align}
\langle p \rangle &= \int_0^a \psi_n^*(x)\left(-i\hbar\frac{d}{dx}\right)\psi_n(x)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{d}{dx}\left(\sin\left(\frac{n\pi x}{a}\right)\right)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{n\pi}{a}\cos\left(\frac{n\pi x}{a}\right)dx \\
&= -\frac{2in\pi\hbar}{a^2}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\cos\left(\frac{n\pi x}{a}\right)dx \\
&= 0
\end{align}$$

{{S0184}}

{{S0185}}
:::

#### {{S0186}}

{{S0187}}


:::{admonition} {{S0188}}
:class: dropdown solution

{{S0189}}

$$E_{111} = \frac{h^2}{8m_e}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)$$
$$= \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}\left(\frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 1.39\times10^{-20}\textnormal{ J} = 87.0\textnormal{ meV}$$


$$E_{211} = E_{121} = E_{112} = \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}$$
$$\times\left(\frac{2^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 2.79\times 10^{-20}\textnormal{ J} = 174\textnormal{ meV} \Rightarrow \Delta E = 87\textnormal{ meV}$$
{{S0190}}

:::

#### {{S0191}}

{{S0192}}

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

{{S0193}}

{{S0194}}

:::{admonition} {{S0195}}
:class: dropdown solution

{{S0196}}

$$E_{1,1,2} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 2^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (1 + 1 + 4) = \frac{\hbar^2 \pi^2}{2mL^2} \times 6$$

{{S0197}}

$$E_{2,2,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 2^2 + 2^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (4 + 4 + 1) = \frac{\hbar^2 \pi^2}{2mL^2} \times 9$$

{{S0198}}

:::

#### {{S0199}}

{{S0200}}

- {{S0201}}
- {{S0202}}

:::{admonition} {{S0203}}
:class: dropdown solution

{{S0204}}

{{S0205}}

{{S0206}}

- {{S0207}}

$$3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14$$

- {{S0208}}
  
  - {{S0209}}
  - {{S0210}}
  - {{S0211}}
  - {{S0212}}
  - {{S0213}}
  - {{S0214}}

{{S0215}}

:::

#### {{S0216}}

- {{S0217}}
- {{S0218}}

:::{admonition} {{S0219}}
:class: dropdown solution

{{S0220}}

$$E_{1,1,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} \times 3$$

{{S0221}}

{{S0222}}

:::

#### {{S0223}}

{{S0224}}

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

- {{S0225}}
- {{S0226}}

:::{admonition} {{S0227}}
:class: dropdown solution

{{S0228}}

{{S0229}}

{{S0230}}

- {{S0231}}
- {{S0232}}
  - {{S0233}}
  - {{S0234}}
  - {{S0235}}
- {{S0236}}

{{S0237}}

:::

#### {{S0238}}

{{S0239}}

:::{admonition} {{S0240}}
:class: dropdown solution

{{S0241}}

$$
\Delta E = \frac{(2^2 - 1^2)h^2}{8mL^2} = \frac{3h^2}{8mL^2},
$$

{{S0242}}
:::

#### {{S0243}}

{{S0244}}

:::{admonition} {{S0245}}
:class: dropdown solution

$$
L = 4 \times 1.35\,\text{Å} + 3 \times 1.45\,\text{Å} = 10.55\,\text{Å} = 10.55 \times 10^{-10}\,\text{m}.
$$

{{S0246}}
:::

#### {{S0247}}

{{S0248}}

:::{admonition} {{S0249}}
:class: dropdown solution

{{S0250}}

$$
L = 4 \times 1.35\,\text{Å} + 4 \times 1.40\,\text{Å} = 11.0\,\text{Å}.
$$

{{S0251}}

$$
\Delta E = E_3 - E_1 = \frac{(3^2 - 1^2)h^2}{8mL^2} = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

{{S0252}}
:::

#### {{S0253}}

{{S0254}}

:::{admonition} {{S0255}}
:class: dropdown solution

{{S0256}}

$$
\Delta E = E_3 - E_1 = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

{{S0257}}
:::

#### {{S0258}}

{{S0259}}

:::{admonition} {{S0260}}
:class: dropdown solution

$$
L = 5 \times 1.34\,\text{Å} + 4 \times 1.54\,\text{Å} = 12.86\,\text{Å}.
$$

{{S0261}}

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{5h^2}{8mL^2},
$$

{{S0262}}
:::

#### {{S0263}}

{{S0264}}

:::{admonition} {{S0265}}
:class: dropdown solution

{{S0266}}

$$
E_{n_x, n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right).
$$

{{S0267}}

$$
\frac{1^2}{L_x^2} + \frac{2^2}{L_y^2} = 2.5 \times 10^{17} + 4.0 \times 10^{18} = 4.25 \times 10^{18}\,\text{m}^{-2},
$$

{{S0268}}

$$
E_{1,2} \approx 2.56 \times 10^{-19}\,\text{J} \approx 1.60\,\text{eV}.
$$
:::
