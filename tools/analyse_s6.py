"""Bruce-Vincent re-analysis of the group's SI Fig. S6 raw data (GF and ND@GF)."""
import sys
from pathlib import Path

import numpy as np
import xlrd

base = Path(sys.argv[1])
out_png = Path(sys.argv[2])
files = {
    "GF": ("GF/it.xls", "GF/initialEIS.xls", "GF/EIS_after_run_it.xls"),
    "ND@GF": ("ND@GF/it.xls", "ND@GF/initial_EIS.xls", "ND@GF/EIS_after_it.xls"),
}
dV = 10e-3  # V, stated in SI


def read(path):
    sh = xlrd.open_workbook(base / path).sheet_by_index(0)
    return np.array([[float(v) for v in sh.row_values(r)] for r in range(sh.nrows)])


def eis_resistances(z):
    zr, zi = z[:, 0], z[:, 1]  # second column = -Z'' (capacitive arc positive)
    # bulk resistance: high-frequency crossing of -Z'' through zero (first sign change - to +)
    k = np.where((zi[:-1] < 0) & (zi[1:] >= 0))[0][0]
    rb = zr[k] + (zr[k + 1] - zr[k]) * (0 - zi[k]) / (zi[k + 1] - zi[k])
    return rb, zr[-1], zr[-5:].mean(), zr.max()


def bv(i0, iss, r0, rs):
    return iss * (dV - i0 * r0) / (i0 * (dV - iss * rs))


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for name, (f_it, f_e0, f_e1) in files.items():
    it = read(f_it)
    t, i = it[:, 0], it[:, 1]
    rb0, rl0, rm0, rx0 = eis_resistances(read(f_e0))
    rb1, rl1, rm1, rx1 = eis_resistances(read(f_e1))
    i0, iss = i[0], i[-1]
    print(f"===== {name}")
    print(f"I(0.1 s) = {i0*1e6:.2f} uA, I(600 s) = {iss*1e6:.2f} uA, ratio {iss/i0:.3f}")
    for tt in (1, 10, 100, 300, 500, 590):
        print(f"   I({tt:>3} s) = {np.interp(tt, t, i)*1e6:.2f} uA")
    slope = np.polyfit(t[t > 500], i[t > 500], 1)[0]
    print(f"slope 500-600 s: {slope*1e9*100:.3f} nA per 100 s ({slope*100/iss*100:.2f} % of I_s per 100 s)")
    # exponential fit I = Iinf + A exp(-t/tau), grid over tau, t >= 1 s
    m = t >= 1
    best = None
    for tau in np.logspace(0, 4, 400):
        X = np.c_[np.ones(m.sum()), np.exp(-t[m] / tau)]
        coef, res, *_ = np.linalg.lstsq(X, i[m], rcond=None)
        r = ((X @ coef - i[m]) ** 2).sum()
        if best is None or r < best[0]:
            best = (r, tau, coef)
    _, tau, (iinf, amp) = best
    print(f"fit (t>=1 s): tau = {tau:.0f} s, I_inf = {iinf*1e6:.2f} uA, A = {amp*1e6:.2f} uA")
    print(f"EIS initial: R_b = {rb0:.2f} Ohm, Z'_lowf last/mean5/max = {rl0:.1f} / {rm0:.1f} / {rx0:.1f} Ohm")
    print(f"EIS after:   R_b = {rb1:.2f} Ohm, Z'_lowf last/mean5/max = {rl1:.1f} / {rm1:.1f} / {rx1:.1f} Ohm")
    print(f"Ohm check: I0*Rtot0 = {i0*rl0*1e3:.1f} mV, Is*Rtot_s = {iss*rl1*1e3:.1f} mV (SI: dV = 10 mV)")
    print("t+ (interfacial R = Z'_lowf - R_b):")
    for lab, a, b in (("last", rl0, rl1), ("mean5", rm0, rm1), ("max", rx0, rx1)):
        r0, rs = a - rb0, b - rb1
        print(f"   {lab:5s}: R0 = {r0:.1f}, Rs = {rs:.1f} -> I0R0 = {i0*r0*1e3:.1f} mV, IsRs = {iss*rs*1e3:.1f} mV, t+ = {bv(i0, iss, r0, rs):.3f}")
    # transport-only decay estimate with the measured bulk resistance and bulk t+ 0.197 / 0.51
    for tp in (0.197, 0.51):
        extra = rb0 * (1 / tp - 1)
        print(f"   transport-only decay (R_b {rb0:.1f} Ohm, t+ {tp}): {extra/(rl0+extra)*100:.1f} %")
    ax[0].plot(t, i * 1e6, label=name)
    z0, z1 = read(f_e0), read(f_e1)
    ax[1].plot(z0[:, 0], z0[:, 1], ".-", ms=3, label=f"{name} initial")
    ax[1].plot(z1[:, 0], z1[:, 1], ".-", ms=3, label=f"{name} after")
ax[0].set(xlabel="t / s", ylabel="I / uA", title="Chronoamperometry (S6 raw)")
ax[1].set(xlabel="Z' / Ohm", ylabel="-Z'' / Ohm", title="EIS before/after (S6 raw)")
ax[0].legend(); ax[1].legend(fontsize=7)
fig.tight_layout()
fig.savefig(out_png, dpi=120)
print(f"plot: {out_png}")
