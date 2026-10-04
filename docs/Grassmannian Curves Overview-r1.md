The measured threshold is the milestone result: the engine's first falsifiable validity condition, extracted from a sweep rather than asserted in prose. Before moving to the 3-D lift, three points of scrutiny on the sweep itself, then the chart spec.

1. Read the shape of the curve—it's telling you the right thing

The counterintuitive part is that mean $|\Delta S|$ rises as drift slows (0.378 → 0.689). That's actually the correct signature, and it's worth stating explicitly in the README because a reviewer will flag it: fast drift scrambles phase coherence, so the pulse train's observable response dephases almost immediately and the residual against the twin is small. Slow drift preserves the coherent response longer, so the residual grows toward its adiabatic limit. The plateau is the point where the pulse response stops depending on the drift rate—memory retention saturates. So the knee isn't measuring "where residual vanishes"; it's measuring where the observable becomes drift-rate-independent, which is the operational definition of adiabaticity for this engine. Say it in exactly those terms.

2. Two honesty caveats before this goes in the README

- The plateau creeps. 0.675 → 0.689 between $\varepsilon = 0.045$ and 0.022 is a +2% change, not zero. One more point at $\varepsilon \approx 0.01$ (another half-decade) would confirm the flattening is real rather than an inflection before continued growth. If it keeps creeping at ~2% per halving, the threshold should be quoted as "$\varepsilon \lesssim 0.05$ with residual converging at $\sim$2% per halving," not as a hard knee.
- Define the residual precisely. "Mean $|\Delta S|$" needs its exact definition in the README—injected state vs. counterfactual twin, path-dependent $\Omega(t)$ on both, integrated over which window. The threshold number is only reproducible if the metric is pinned down.

Also note what the path-dependent fix did to the interference numbers: memory ratio dropped from +29% to +14%, and the $\gamma$ values were substantially revised (Joule 0 → 1.193, tidal now 0.639 vs. 0.382). That's honest accounting—the old figures were artifacts of replaying the final $\Omega$ over the whole history, and they should be superseded in the README rather than left standing. The qualitative conclusions survived (memory protected, $\gamma$ path-dependent, ratio enhanced); the quantities didn't. That's the difference between a number you can defend and a number you have to walk back.

3. The projection result deserves its own line

Zero projection activations across the entire sweep is a genuine finding, not a null result: it says the physically motivated solar-driven schedules never push $\operatorname{Im}\Omega$ toward the positive-definite boundary. The cone constraint is satisfied by the dynamics you actually model, not enforced by clipping. That's one sentence in the README, but it's the kind of sentence that distinguishes a constrained model from a free one.

Next: the 3-D chart lift

Spec, with the toroidal chart as the default:

1. The chart interface.

class ToroidalChart:
    """Maps 1-D hierarchy output onto a genus-1 laboratory slice."""
    def __init__(self, R_major, r_minor): ...
    def gradient(self, v, x):   # d/dx lifted to the toroidal frame
        ...

The chart owns the mapping convention and nothing else—the engine stays chart-agnostic, so a Cartesian laboratory chart can be added later without touching the core.

2. The lift.

def shear_tensor_3d(x, t, state, chart):
    v      = current_density(x, t, state.omega_at(t), state.U, state.Z(t))
    grad_v = chart.gradient(v, x)
    S      = 0.5 * (grad_v + grad_v.T) - (np.trace(grad_v) / 3.0) * np.eye(3)
    return S

3. The payoff: eigenvalue decomposition of $S$. On the toroidal chart, the eigenvalues of $S$ separate into the poloidal and toroidal shear components—the exact split your double-toroid atomic models already use. Run the capture train and plot the two eigenvalue tracks through time: the induction → Joule → tidal sequence should show as a specific, sequenced pattern in the poloidal/toroidal decomposition, and that figure is the visualization of the Terminal Capture Analysis the whole engine was built to support.

4. Consistency check: the trace of $S$ must vanish to machine precision at every sample (same tolerance class as the cnoidal test, $\sim10^{-15}$). If it doesn't, the chart gradient lift has an error.

That closes the roadmap. After that, the natural genus-2 extension—where the period matrix becomes genuinely $2\times2$ and the adiabatic threshold becomes a surface over two drift directions—is the first step out of the demo regime and toward the multi-phase substrate your SRC models actually describe.
