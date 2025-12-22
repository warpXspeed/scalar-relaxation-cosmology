#!/bin/bash
# Run the full 256³ production
python3 src_klein_gordon_256_slab.py --N 256 --steps 12000 --output_int 1200
# Regenerate GW (add your synthetic_gw function here or separate script)
echo "Production complete. Check run_output_256/diagnostics.csv"
