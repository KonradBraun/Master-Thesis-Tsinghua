"""Virtual Bruce-Vincent evaluation of COMSOL model 04 (1D Zn//Zn, ND layer at x = 0).

Inputs: point evaluations exported from COMSOL (columns i0, X_ND, t, phil, cZn) at
point 1 (x = 0, ES1) and point 3 (x = L, ES2). The current is reconstructed from the
model's own Butler-Volmer / mass-action kinetics at both electrodes; their mismatch
is printed as a consistency check.

Usage: py -P tools/analyse_bv04.py <point1.txt> <point3.txt> [out.png] [s6_dir]
"""
import sys
from pathlib import Path

import numpy as np

F, R = 96485.33212, 8.31446261815324
T = 293.15          # COMSOL default model input (no other T set in model 04)
f = F / (R * T)
c0, dV, n = 2000.0, 10e-3, 2
D_salt, t_plus = 3.27e-10, 0.51                      # model 02-04 parameters
D_Zn, D_SO4 = D_salt / (2 * (1 - t_plus)), D_salt / (2 * t_plus)


def load(path):
    return np.loadtxt(path, comments="%")


p1, p3 = load(sys.argv[1]), load(sys.argv[2])
assert np.allclose(p1[:, :3], p3[:, :3]), "rows of the two tables do not match"
i0, X, t = p1[:, 0], p1[:, 1], p1[:, 2]
phil1, c1, phil3, c3 = p1[:, 3], p1[:, 4], p3[:, 3], p3[:, 4]


def i_loc(i0ref, phis, phil, c):
    eta_ref = phis - phil                     # E_eq,ref = 0
    return i0ref * (np.exp(f * eta_ref) - (c / c0) * np.exp(-f * eta_ref))


i_es1 = i_loc(i0, 0.0, phil1, c1)             # cathodic (plating at the ND side), < 0
i_es2 = i_loc(i0, dV, phil3, c3)              # anodic, > 0
cur = 0.5 * (i_es2 - i_es1)
mismatch = np.abs(i_es1 + i_es2) / np.abs(cur)
# Delta = dV - (|eta1| + |eta2|) = electrolyte drop + Nernst term (exact identity)
delta = (phil3 - phil1) + (R * T / (n * F)) * np.log(c3 / c1)

print(f"T = {T} K; max relative mismatch |i_ES1 + i_ES2| / i = {mismatch.max():.2e}\n")
hdr = (f"{'i0':>6} {'X':>6} | {'I0':>9} {'I600':>9} {'Iss':>9} | {'ss chk':>7} | "
       f"{'Iss/I0':>6} {'D0/mV':>7} {'Dss/mV':>7} | {'t+ ss':>6} {'t+ 600':>6} | "
       f"{'cZn(0) ss':>9} {'t+loc':>5}")
print(hdr)
print("-" * len(hdr))
rows = []
for a in np.unique(i0):
    for x in np.unique(X):
        m = (i0 == a) & (X == x)
        tt, I, Dl = t[m], cur[m], delta[m]
        k0, kss = 0, np.argmax(tt)
        k600 = int(np.argmin(np.abs(tt - 600)))
        kprev = int(np.argsort(tt)[-2])
        tss = I[kss] * Dl[k0] / (I[k0] * Dl[kss])
        t600 = I[k600] * Dl[k0] / (I[k0] * Dl[k600])
        cz = c1[m][kss]
        cs = cz - x / 2                           # electroneutrality in the layer
        tloc = D_Zn * cz / (D_Zn * cz + D_SO4 * cs)
        chk = abs(I[kss] - I[kprev]) / I[kss]
        rows.append((a, x, tt, I / I[k0]))
        print(f"{a:6g} {x:6g} | {I[k0]:9.4g} {I[k600]:9.4g} {I[kss]:9.4g} | {chk:7.1e} | "
              f"{I[kss]/I[k0]:6.3f} {Dl[k0]*1e3:7.4f} {Dl[kss]*1e3:7.4f} | {tss:6.3f} {t600:6.3f} | "
              f"{cz:9.1f} {tloc:5.2f}")

if len(sys.argv) > 3:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for a, x, tt, norm in rows:
        if x in (0, 3100):                    # X = 10000 is a mesh artefact (see progress.md)
            ax.semilogx(tt[1:], norm[1:], lw=1.2,
                        label=f"model i0 = {a:g} A/m², X = {x:g}")
    if len(sys.argv) > 4:
        import xlrd
        s6 = Path(sys.argv[4])
        for name, ls in (("GF", "k--"), ("ND@GF", "k:")):
            sh = xlrd.open_workbook(s6 / name / "it.xls").sheet_by_index(0)
            d = np.array([[float(v) for v in sh.row_values(r)] for r in range(sh.nrows)])
            ax.semilogx(d[:, 0], d[:, 1] / d[0, 1], ls, lw=1.5, label=f"measured {name} (S6)")
    ax.set(xlabel="t / s", ylabel="I(t) / I(t→0)", ylim=(0.4, 1.02),
           title="Bruce–Vincent current decay: model 04 vs. measurement")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(sys.argv[3], dpi=130)
    print(f"\nplot: {sys.argv[3]}")
