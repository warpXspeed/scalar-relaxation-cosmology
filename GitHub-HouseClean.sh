#!/bin/bash
cd /home/merlin/scalar-relaxation-cosmology

# --- Safety backup first (takes 10 seconds, saves everything) ---
mkdir -p _backup_before_reorg
cp -r . _backup_before_reorg/
echo "✅ Backup complete: _backup_before_reorg/"

# --- Create archive directories ---
mkdir -p archive/early_theories
mkdir -p archive/speculative
mkdir -p archive/superseded
mkdir -p archive/generated_outputs
mkdir -p archive/personal
mkdir -p archive/code

# --- Move early/superseded theories ---
mv "Gravity Circuit Universe.md" archive/early_theories/ 2>/dev/null
mv "SolarFurnaceModel_Archival_v1.0.pdf" archive/early_theories/ 2>/dev/null

# --- Move speculative / consciousness / exotic stuff ---
mv "UnderstandingTime-GravityUnity" archive/speculative/ 2>/dev/null
mv "From Quantum Butterfly to Cosmic Intelligence-R2.md" archive/speculative/ 2>/dev/null
mv "The Evidence-Locked Story of the 12 ka Global Cataclysm" archive/speculative/ 2>/dev/null
mv "Why the Sun Has Not Burnt Out" archive/speculative/ 2>/dev/null
mv "Excitonic Floquet Engineering" archive/speculative/ 2>/dev/null

# --- Move old / superseded docs ---
mv "theory_overview.md" archive/superseded/ 2>/dev/null
mv "ReadMe.md" archive/superseded/ 2>/dev/null

# --- Move generated outputs / figures (not source of truth) ---
mv "outputs" archive/generated_outputs/ 2>/dev/null
mv "run_output" archive/generated_outputs/ 2>/dev/null
mv "figs" archive/generated_outputs/ 2>/dev/null
mv "figures" archive/generated_outputs/ 2>/dev/null
mv "kg_damping_plot.png" archive/generated_outputs/ 2>/dev/null

# --- Move personal / life stuff ---
mv "life" archive/personal/ 2>/dev/null

# --- Move standalone .py files (they belong in scripts/) ---
mv "Regeneration Code.py" scripts/ 2>/dev/null
mv "make_figures.py" scripts/ 2>/dev/null
mv "simulation_example.py" scripts/ 2>/dev/null
mv "srec_clockwork.py" scripts/ 2>/dev/null

# --- Check what remote the submodules point to ---
echo "--- src remote ---"
cd src && git remote -v && cd ..
echo "--- scalar-relaxation-cosmology remote ---"
cd scalar-relaxation-cosmology && git remote -v && cd ..

echo ""
echo "✅ Reorganization complete."
echo ""
echo "Top-level should now be:"
ls -la

