#!/bin/bash
cd /home/merlin/scalar-relaxation-cosmology

mkdir -p _backup_before_reorg
cp -r . _backup_before_reorg/
echo "Backup complete: _backup_before_reorg/"

mkdir -p archive/early_theories
mkdir -p archive/speculative
mkdir -p archive/superseded
mkdir -p archive/generated_outputs
mkdir -p archive/personal
mkdir -p archive/code

mv "Gravity Circuit Universe.md" archive/early_theories/ 2>/dev/null
mv "SolarFurnaceModel_Archival_v1.0.pdf" archive/early_theories/ 2>/dev/null

mv "UnderstandingTime-GravityUnity" archive/speculative/ 2>/dev/null
mv "From Quantum Butterfly to Cosmic Intelligence-R2.md" archive/speculative/ 2>/dev/null
mv "The Evidence-Locked Story of the 12 ka Global Cataclysm" archive/speculative/ 2>/dev/null
mv "Why the Sun Has Not Burnt Out" archive/speculative/ 2>/dev/null
mv "Excitonic Floquet Engineering" archive/speculative/ 2>/dev/null

mv "theory_overview.md" archive/superseded/ 2>/dev/null
mv "ReadMe.md" archive/superseded/ 2>/dev/null

mv "outputs" archive/generated_outputs/ 2>/dev/null
mv "run_output" archive/generated_outputs/ 2>/dev/null
mv "figs" archive/generated_outputs/ 2>/dev/null
mv "figures" archive/generated_outputs/ 2>/dev/null
mv "kg_damping_plot.png" archive/generated_outputs/ 2>/dev/null

mv "life" archive/personal/ 2>/dev/null

mv "Regeneration Code.py" scripts/ 2>/dev/null
mv "make_figures.py" scripts/ 2>/dev/null
mv "simulation_example.py" scripts/ 2>/dev/null
mv "srec_clockwork.py" scripts/ 2>/dev/null

echo "Done. Top-level:"
ls -la
