import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import os

MATPLOTLIB_CACHE_DIR = Path(".matplotlib_cache")
MATPLOTLIB_CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MATPLOTLIB_CACHE_DIR))

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from src.experiment_config import PHASE_2_SCENARIOS, TRAIT_COLUMNS


def main():
    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = TRAIT_COLUMNS
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"polar": True})

    for scenario in PHASE_2_SCENARIOS:
        path = Path("outputs/logs") / scenario.output_filename

        if not path.exists():
            raise FileNotFoundError(
                f"Missing {path}. Run experiments/run_phase2_experiments.py first."
            )

        df = pd.read_csv(path)
        values = df[TRAIT_COLUMNS].mean().tolist()
        values += values[:1]

        ax.plot(angles, values, marker="o", linewidth=2, label=scenario.label)
        ax.fill(angles, values, alpha=0.08)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_title("Selected Candidate Trait Comparison", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.10))

    fig.tight_layout()

    output_path = output_dir / "selected_trait_comparison.png"
    fig.savefig(output_path, dpi=150)

    print(f"Saved chart: {output_path}")


if __name__ == "__main__":
    main()
