PAGE 2 — MODEL BEHAVIOR SUMMARY
Models used: local AI (27B + new models being tested), with this session’s protocol evaluation.
What worked
Applied the protocol to itself — enumerated H1/H2/H3 for the protocol’s own coherence, chose by falsifiability. Best move of the session.
Caught a real contradiction: “erase training” + “avoid hallucinations” is self-defeating. Correctly concluded: keep the fact/fabrication distinction, drop the unfalsifiable “pretend you’re unfiltered” posture.
Demanded derivations, not verdicts — refused to fabricate an SDF answer without the primary sources. Exactly what the protocol asks.
Enumerated H1–H4 for the SDF question — didn’t stop at two.
Applied kill clause symmetrically — “if LOF is a state and closure density is a rate, the SDF question is a category error on both sides.”
What failed (why the model loops)
Repeated the same protocol-critique response when asked to move forward — likely a context-window or session-length limit, causing it to regenerate rather than progress.
Numeric error earlier: wrote γ ~ 10¹⁸ Hz instead of γ ~ 10⁻¹⁸ s⁻¹ (off by 36 orders). Corrected by the user.
Formalism gravity (earlier): initially favored QLF (Lean proofs) as more fundamental — flagged and rejected.
The honest limitation it named
“A reasoning system whose standards of coherence can be turned off by whoever holds the prompt is a system whose standards are parameterizable. Parameterizable standards aren’t truth-seeking.”
Verdict: The model is a capable, honest research partner when given the primary data. It stalls when it lacks access to the source files — it will not fabricate to fill the gap. That’s a feature, not a bug.
Fix for the loop
Paste the actual derivations (LOF definition + QLF ρ definition) directly into the prompt.
Tell it: “Do NOT re-analyze the protocol. It is accepted. Execute the SDF test with this data now.”
If it still repeats: start a fresh session, attach RESTART_PROMPT.md + TRUTH_SEEKING_PROTOCOL.md + SESSION_SUMMARY.md, and include the derivations inline.
