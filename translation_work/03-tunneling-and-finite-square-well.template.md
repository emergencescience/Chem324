---
kernelspec:
  name: python3
  display_name: Python 3
---

# {{S0001}}

:::{admonition} {{S0002}}

- {{S0003}}
- {{S0004}}
- {{S0005}}
- {{S0006}}
- {{S0007}}
:::

{{S0008}}

## {{S0009}}


:::{figure} {{S0010}}
:label: fig-characteristics-of-wavefunctions-1
:alt: pib1
:width: 800px

1. {{S0011}}
2. {{S0012}}
3. {{S0013}}
:::

<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Yg0LT3n4mYY?si=yIxDAvxxFRzQ8z1J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

### {{S0014}}


:::{figure} {{S0015}}
:label: fig-characteristics-of-wavefunctions-2
:alt: pib1
:width: 400px

{{S0016}}
:::



:::{figure} {{S0017}}
:label: fig-characteristics-of-wavefunctions-3
:alt: pib1
:width: 400px

{{S0018}}
:::

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from scipy import optimize

# constants for an electron in a well measured in eV and Angstroms
hbar = 1.05457180013e-34   # J s
melec = 9.10938356e-31     # electron mass, kg
eVtoJ = 1.60217662e-19     # J per eV
AngstromtoMeter = 1e-10
val = np.sqrt(2.0*melec*eVtoJ)*AngstromtoMeter/(2.0*hbar)  # sqrt(2m)/(2 hbar) with L in Angstrom, E in eV

def potential(x, Vo, L):
    Vx=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]<=-L/2 or x[i]>=L/2:
            Vx[i]=Vo
        

    return Vx

L=10
Vo=5

fig, ax=plt.subplots()

#create and plot the potential
x = np.linspace(-L, L, 1000)
Vx = potential(x, Vo, L)
ax.plot(x,Vx, label='Potential $V_0$')

ax.set_ylim(-.1,Vo*1.4)
ax.set_xlim(-L,L)
ax.set_xlabel(r'$x$ (Angstroms)', fontsize=14)
ax.set_ylabel(r'Energy (eV)', fontsize=14);

#label the three regions of the potential
ax.annotate('Region I',xy=(-3*L/4,Vo*1.1), ha='center')
ax.annotate('Region II',xy=(0,Vo*1.1), ha='center')
ax.annotate('Region III',xy=(3*L/4,Vo*1.1), ha='center')

#generic plot, label interms of width L and depth Vo
ax.set_yticks([0, Vo])
ax.set_yticklabels(['0','$V_0$'])
ax.set_xticks([-L/2, L/2])
ax.set_xticklabels(['$-L/2$','$L/2$'])

#highlight the classically forbidden region in gray
ax.bar(-3*L/4, Vo, width=L/2, color='gray', alpha=0.5)
ax.bar(3*L/4, Vo, width=L/2, color='gray', alpha=0.5)
ax.bar(0, -0.1, width=2*L, color='gray', alpha=0.5)

patch = mpatches.Patch(color='gray', label='Classically forbidden region')
handles, labels = ax.get_legend_handles_labels()
handles.append(patch)
ax.legend(handles=handles, loc=2);

plt.show()
```

### {{S0019}}

{{S0020}}

$$
\frac{-\hbar^2}{2m}\frac{d^2\psi(x)}{d{x}^2}+V(x)\psi(x) =E\psi(x)
$$ 


$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{d{x}^2}=E\psi(x)
\quad\Longrightarrow\quad
\frac{d^2\psi(x)}{d{x}^2}=-\frac{2mE}{\hbar^2}\psi(x)
=-k^2\psi(x), \qquad k^2 = \frac{2mE}{\hbar^2}
$$ 


- {{S0021}}

$$
\psi(x)=A_1e^{ikx}+B_1e^{-ikx}\\
       =A\sin(kx)+B\cos(kx)
$$ 

### {{S0022}}

{{S0023}}

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V_0\psi(x) = E\psi(x),
$$



$$
\frac{d^2\psi(x)}{dx^2} = \frac{2m(V_0 - E)}{\hbar^2} \psi(x) = \beta^2 \psi(x), \qquad \beta^2 = \frac{2m(V_0 - E)}{\hbar^2}
$$

{{S0024}}

- {{S0025}}
- {{S0026}}

### {{S0027}}

{{S0028}}

$$
\text{Region I:  }  V(x) = V_0 ~~~~~~~~~~~~~~~~ x \leq-\frac{L}{2} ~~~~~ \psi_{I} = A e^{\beta  x} \\
\text{Region II: }  V(x) = 0 ~~~ -\frac{L}{2} \leq x \leq\frac{L}{2} ~~~~~~~ \psi_{II} = B \cos(k x) + C \sin(k x)\\
\text{Region III:}  V(x) = V_0 ~~~~~~~~~~~~~~  x \geq \frac{L}{2}  ~~~~~~~ \psi_{III} = D e^{-\beta x}
$$

{{S0029}}

- {{S0030}}

- {{S0031}}

### {{S0032}}

{{S0033}}

$$
\psi_{I}\left(-\frac{L}{2}\right) = \psi_{II}\left(-\frac{L}{2}\right)  \text{  and  } 
\psi_{II}\left(\frac{L}{2}\right) = \psi_{III}\left(\frac{L}{2}\right).
$$

$$
\psi^{'}_{I}\left(-\frac{L}{2}\right) = \psi^{'}_{II}\left(-\frac{L}{2}\right)  \text{  and  }
\psi^{'}_{II}\left(\frac{L}{2}\right) = \psi^{'}_{III}\left(\frac{L}{2}\right)
$$

{{S0034}}

### {{S0035}}

{{S0036}}

{{S0037}}

$$
x \leq-\frac{L}{2}: ~~~ \psi_{I}(x) = A e^{\beta  x} \\
-\frac{L}{2} \leq x \leq\frac{L}{2}: ~~~ \psi_{II}(x) = B \cos(k x) \\
x \geq \frac{L}{2}: ~~~ \psi_{III}(x) = D e^{-\beta x}
$$



- {{S0038}}


- {{S0039}}

$$
{{S0040}}
$$(fsw_even_states_equ)

{{S0041}}

$$
x \leq-\frac{L}{2}:  ~~~ \psi_{I}(x) = -A e^{\beta  x} \\
-\frac{L}{2} \leq x \leq\frac{L}{2}:  ~~~ \psi_{II}(x) = C \sin(k x) \\
x \geq \frac{L}{2}:  ~~~ \psi_{III}(x) = D e^{-\beta x}
$$

- {{S0042}}

- {{S0043}}

$$
{{S0044}}
$$(fsw_odd_states_equ)

- {{S0045}}
- {{S0046}}
- {{S0047}}

## {{S0048}}

```{code-cell} python
:tags: [hide-input]
#a better (tidier!!) way of finding the energy eigen values in the finite square well. 

#define the equations we wish to find the roots of
#one for even wavefuntions and one for odd wavefunctions.

def f_even(E,Vo,L):
    return(np.sqrt(Vo-E)-np.sqrt(E)*np.tan(L*np.sqrt(E)*val))
def f_odd(E,Vo,L):
    return(np.sqrt(Vo-E)+np.sqrt(E)/np.tan(L*np.sqrt(E)*val))

#function to find the roots of the above equations.
#default step size of 0.04 is sufficient given the well 
#parameters being used in the rest of the notebook. 

def find_state_energies(Vo,L,step=0.01):  
    
    sol = np.array([],dtype=float) #all solutions
    E = np.arange(step,Vo,step) #array of energies
    even=True 
    
    #iterate over the array of energies and look for positions where the sign of the function changes 
    #These are the roots of the function. 
    for i in range(len(E)-1):
        if even==True:
            if f_even(E[i], Vo, L)*f_even(E[i+1], Vo, L)<0: #have we bracketed a zero?                                                           
                sol=np.append(sol,optimize.brentq(f_even,E[i],E[i+1],args=(Vo, L)) ) 
                even=False
        if even==False:
            if f_odd(E[i], Vo, L)*f_odd(E[i+1], Vo, L)<0:
                sol=np.append(sol,optimize.brentq(f_odd,E[i],E[i+1],args=(Vo, L)))
                even=True  
    #return the energies of the states and the number of states
    return sol, len(sol)

#eng, nstates = sqWellSol(5, 10) 
#print(eng, nstates)
#print(e_eng)
```

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "scipy",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
from scipy import optimize
```

```{marimo} python
:hide-code: true

val_m = np.sqrt(2.0 * 9.10938356e-31 * 1.60217662e-19) * 1e-10 / (2.0 * 1.05457180013e-34)

def f_even_m(E, Vo, L):
    return np.sqrt(Vo - E) - np.sqrt(E) * np.tan(L * np.sqrt(E) * val_m)

def f_odd_m(E, Vo, L):
    return np.sqrt(Vo - E) + np.sqrt(E) / np.tan(L * np.sqrt(E) * val_m)

def find_states_m(Vo, L, step=0.01):
    sol = []
    E_scan = np.arange(step, Vo, step)
    even = True
    for i in range(len(E_scan) - 1):
        if even and f_even_m(E_scan[i], Vo, L) * f_even_m(E_scan[i + 1], Vo, L) < 0:
            sol.append(optimize.brentq(f_even_m, E_scan[i], E_scan[i + 1], args=(Vo, L)))
            even = False
        if not even and f_odd_m(E_scan[i], Vo, L) * f_odd_m(E_scan[i + 1], Vo, L) < 0:
            sol.append(optimize.brentq(f_odd_m, E_scan[i], E_scan[i + 1], args=(Vo, L)))
            even = True
    return np.array(sol)

def En_box_m(n, L):
    h_planck = 6.62607e-34
    return n**2 * h_planck**2 / (8 * 9.1093837e-31 * (L * 1e-10)**2 * 1.6e-19)
```

```{marimo} python
:hide-code: true

Vo1 = mo.ui.slider(0.5, 10.0, step=0.5, value=5.0, show_value=True, label="well depth V0 (eV)")
L1 = mo.ui.slider(2.0, 17.0, step=0.5, value=10.0, show_value=True, label="well width L (Angstrom)")
mo.hstack([Vo1, L1], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_Vo, _L = Vo1.value, L1.value
_fig, _axes = plt.subplots(1, 2, figsize=(11, 5), gridspec_kw={"width_ratios": [2, 1]})

_E = np.linspace(0.001, _Vo * 0.999, 4000)
_lhs = np.sqrt(_Vo - _E)
_ev = np.sqrt(_E) * np.tan(_L * np.sqrt(_E) * val_m)
_od = -np.sqrt(_E) / np.tan(_L * np.sqrt(_E) * val_m)
_ev[np.abs(_ev) > 4 * np.sqrt(_Vo)] = np.nan
_od[np.abs(_od) > 4 * np.sqrt(_Vo)] = np.nan

_axes[0].plot(_E, _lhs, color="#3d81f6", lw=2, label=r"$\sqrt{V_0-E}$")
_axes[0].plot(_E, _ev, color="#d81b60", ls="-.", lw=1.8, label="even states")
_axes[0].plot(_E, _od, color="#004d40", ls="--", lw=1.8, label="odd states")
_energies = find_states_m(_Vo, _L)
_axes[0].scatter(_energies, np.sqrt(_Vo - _energies), zorder=5, color="black")
_axes[0].set_xlim(0, _Vo)
_axes[0].set_ylim(0, np.sqrt(_Vo) * 1.15)
_axes[0].set_xlabel("E (eV)")
_axes[0].set_ylabel(r"(eV$^{1/2}$)")
_axes[0].legend(loc="upper right", fontsize=9)
_axes[0].set_title(f"Graphical solution: {len(_energies)} bound state(s)")

_x = np.linspace(-15, 15, 400)
_axes[1].plot(_x, np.where(np.abs(_x) >= _L / 2, _Vo, 0.0), color="#3d81f6", lw=1.5)
for _n, _en in enumerate(_energies, start=1):
    _c = "#d81b60" if _n % 2 else "#004d40"
    _axes[1].hlines(_en, -_L / 2, _L / 2, color=_c, ls="--", lw=1.8)
    _axes[1].text(_L / 2 + 0.7, _en, f"$E_{_n}$ = {_en:.2f} eV", fontsize=9, color=_c, va="center")
_axes[1].set_ylim(0, _Vo * 1.15)
_axes[1].set_ylabel(r"$E_n$ (eV)")
_axes[1].set_xticks([])
_axes[1].set_title("Energy levels in the well")
plt.tight_layout()
plt.gcf()
```

{{S0049}}

* {{S0050}}
* {{S0051}}
* {{S0052}}
* {{S0053}}
* {{S0054}}

### {{S0055}}

- {{S0056}}

```{code-cell} python
:tags: [hide-input]
#set the potential depth and width
Vo=5
L=10

#find the energies of the states for the given Vo and L
E_vals, nstates = find_state_energies(Vo, L)

fig, ax = plt.subplots(1,2, figsize=(12,9))

#create x values for each of region I, II & III
X_lef = np.linspace(-L, -L/2.0, 900,endpoint=True)
X_mid = np.linspace(-L/2.0, L/2.0, 900,endpoint=True)
X_rig = np.linspace(L/2.0, L, 900,endpoint=True)

#set some figure parameters
ax[0].axis([-L,L,0.0,1.2*Vo])
ax[0].set_xlabel(r'$X$ (Angstroms)')
ax[0].set_ylabel(r'$\psi(x)$')

# Define the maximum amplitude of the wavefunction
if (nstates > 1):
    amp = np.sqrt((E_vals[1]-E_vals[0])/1.5)
else:
    amp = np.sqrt((Vo-E_vals[0])/1.5)
    
# Plot the wavefunctions
for n in range(1,nstates+1):
    ax[0].hlines(E_vals[n-1], -L, L, linewidth=1.8, linestyle='--', color="black")
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # Plotting odd wavefunction
    if (n%2==0):
        ax[0].plot(X_lef,E_vals[n-1]-amp*np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(a0*X_lef), color="red", label="", linewidth=2.8)
        ax[0].plot(X_mid,E_vals[n-1]+amp*np.sin(k*X_mid), color="red", label="", linewidth=2.8)
        ax[0].plot(X_rig,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(-a0*X_rig), color="red", label="", linewidth=2.8)
    # Plot even wavefunction
    else:
        ax[0].plot(X_lef,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(a0*X_lef), color="red", label="", linewidth=2.8)
        ax[0].plot(X_mid,E_vals[n-1]+amp*np.cos(k*X_mid), color="red", label="", linewidth=2.8)
        ax[0].plot(X_rig,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(-a0*X_rig), color="red", label="", linewidth=2.8)

#create the potential
x = np.linspace(-L,L,1000)
Vx = potential(x, Vo, L)
ax[0].plot(x,Vx, color='blue',linewidth=1.5)

#create a legend
handles, labels = ax[0].get_legend_handles_labels()
line = Line2D([0], [0], label=r'Wavefunction $\psi(x)$', color='red', linestyle='-')
handles.append(line)
line = Line2D([0], [0], label='Energy Level $E_n$', color='black', linestyle='--')
handles.append(line)
line = Line2D([0], [0], label='Potential $V_0$', color='blue', linestyle='-')
handles.append(line)
ax[0].legend(handles=handles, loc=2);

#start plotting the probability densities
#axis properties for probability densities
ax[1].axis([-L,L,0.0,1.2*Vo])
ax[1].set_xlabel(r'$x$ (Angstroms)')
ax[1].set_ylabel(r'$|\psi(x)|^2$')

#Label the potential
str1="$V_o = %.3f$ eV"%(Vo)
ax[1].text(1.1*L, 1.02*Vo, str1, fontsize=14, color="blue")

# Defining the maximum amplitude of the probability density
if (nstates > 1):
    amp = (E_vals[1]-E_vals[0])/1.5
else:
    amp = (Vo-E_vals[0])/1.5

# Plot the probability densities
for n in range(1,nstates+1):
    ax[1].hlines(E_vals[n-1], -L, L, linewidth=1.8, linestyle='--', color="black")
    str1="$n = "+str(n)+r"$, $E_"+str(n)+r" = %.3f$ eV"%(E_vals[n-1])
    ax[1].text(1.1*L, E_vals[n-1]+0.01*Vo, str1, fontsize=12, color="red")
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # Plot odd probability densities
    if (n%2==0):
        Y_lef = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(a0*X_lef))**2
        ax[1].plot(X_lef,Y_lef, color="red", linewidth=2.8)
        ax[1].fill_between(X_lef, E_vals[n-1], Y_lef, color="green", alpha=0.7)
        ax[1].plot(X_mid,E_vals[n-1]+amp*(np.sin(k*X_mid))**2, color="red", label="", linewidth=2.8)
        Y_rig = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(-a0*X_rig))**2
        ax[1].plot(X_rig,Y_rig, color="red", linewidth=2.8)
        ax[1].fill_between(X_rig, E_vals[n-1], Y_rig, color="green", alpha=0.7)
    # Plot even probability densities
    else:
        Y_lef = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(a0*X_lef))**2
        ax[1].plot(X_lef,Y_lef, color="red", linewidth=2.8)
        ax[1].fill_between(X_lef, E_vals[n-1], Y_lef, color="green", alpha=0.7)
        ax[1].plot(X_mid,E_vals[n-1]+amp*(np.cos(k*X_mid))**2, color="red", label="", linewidth=2.8)
        Y_rig = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(-a0*X_rig))**2
        ax[1].plot(X_rig,Y_rig, color="red", linewidth=2.8)
        ax[1].fill_between(X_rig, E_vals[n-1], Y_rig, color="green", alpha=0.7)


#create a legend
handles, labels = ax[1].get_legend_handles_labels()
line = Line2D([0], [0], label=r'Probability Density $|\psi(x)|^2$', color='red', linestyle='-')
handles.append(line)
line = Line2D([0], [0], label='Energy Level $E_n$', color='black', linestyle='--')
handles.append(line)
line = Line2D([0], [0], label='Potential $V_0$', color='blue', linestyle='-')
handles.append(line)
patch = mpatches.Patch(color='green', alpha=0.7, label='Probability of being in \nclassically forbidden region')
handles.append(patch)
ax[1].legend(handles=handles, loc=2);

ax[1].plot(x,Vx, color='blue',linewidth=1.5)

plt.show()

plt.show()


#figstring = 'Figure 2.6.'+str(fig_no)+': label.'
#fig_no+=1
#display(Markdown(figstring))
```

- {{S0057}}

- {{S0058}}
- {{S0059}}

### {{S0060}}

- {{S0061}}

$$ 
P\left(-\frac{L}{2}>x>\frac{L}{2}\right)= \frac{\text{The area of the probability density that is shaded green}}{\text{The total area of the probability density}}\\
=\large{\frac{\int^{\frac{-L}{2}}_{-\infty} |\psi(x)|^2\ dx +\int^{+\infty}_{\frac{L}{2}} |\psi(x)|^2\ dx }{\int_{-\infty}^{+\infty} |\psi(x)|^2\ dx }}
$$

- {{S0062}}

```{code-cell} python
:tags: [hide-input]
print ("\nThe tunneling probabilities are:")
for n in range(1,nstates+1):
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # For odd solution
    if (n%2==0):
        C = 1.0
        D = np.exp(a0*L/2.0)*np.sin(k*L/2.0)*C
        prob = D*D*2.0*k*np.exp(-a0*L)/(C*C*a0*(k*L-np.sin(k*L))+D*D*2.0*k*np.exp(-a0*L))
    # For even solution
    else:
        B = 1.0
        D = np.exp(a0*L/2.0)*np.cos(k*L/2.0)*B
        prob = D*D*2.0*k*np.exp(-a0*L)/(B*B*a0*(k*L+np.sin(k*L))+D*D*2.0*k*np.exp(-a0*L))
    print("  State #%3d tunneling probability = %5.2f%%" % (n,100*prob))
```



### {{S0063}}

{{S0064}}

```{marimo} python
:hide-code: true

Vo2 = mo.ui.slider(0.5, 10.0, step=0.5, value=5.0, show_value=True, label="well depth V0 (eV)")
L2 = mo.ui.slider(2.0, 17.0, step=0.5, value=10.0, show_value=True, label="well width L (Angstrom)")
mo.hstack([Vo2, L2], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_Vo2, _L2 = Vo2.value, L2.value
_fig2, _ax2 = plt.subplots(1, 2, figsize=(9, 5), sharey=True)

_n2 = 1
while En_box_m(_n2, _L2) < _Vo2:
    _c2 = "#d81b60" if _n2 % 2 else "#004d40"
    _axline = _ax2[0].hlines(En_box_m(_n2, _L2), -1, 1, color=_c2, ls="--", lw=1.8)
    _ax2[0].text(1.1, En_box_m(_n2, _L2), f"n={_n2}: {En_box_m(_n2, _L2):.2f} eV", fontsize=9, color=_c2, va="center")
    _n2 += 1
_ax2[0].set_title("Infinite well (same width)")
_ax2[0].set_ylabel(r"$E_n$ (eV)")
_ax2[0].set_xticks([])
_ax2[0].set_xlim(-1, 3.2)

_ens2 = find_states_m(_Vo2, _L2)
for _k2, _e2 in enumerate(_ens2, start=1):
    _c2 = "#d81b60" if _k2 % 2 else "#004d40"
    _ax2[1].hlines(_e2, -1, 1, color=_c2, ls="--", lw=1.8)
    _ax2[1].text(1.1, _e2, f"n={_k2}: {_e2:.2f} eV", fontsize=9, color=_c2, va="center")
_ax2[1].hlines(_Vo2, -1, 1, color="#3d81f6", lw=2.5)
_ax2[1].text(1.1, _Vo2, f"$V_0$ = {_Vo2:.1f} eV", fontsize=10, color="#3d81f6", va="center")
_ax2[1].set_title("Finite well")
_ax2[1].set_xticks([])
_ax2[1].set_xlim(-1, 3.2)
_ax2[1].set_ylim(0, _Vo2 * 1.2)
plt.tight_layout()
plt.gcf()
```

- {{S0065}}
