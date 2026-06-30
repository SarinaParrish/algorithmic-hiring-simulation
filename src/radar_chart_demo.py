import os
from pathlib import Path

MATPLOTLIB_CACHE_DIR = Path(".matplotlib_cache")
MATPLOTLIB_CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MATPLOTLIB_CACHE_DIR))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.experiment_config import TRAIT_COLUMNS


TRAIT_LABELS = [
    "Openness",
    "Conscientiousness",
    "Extraversion",
    "Agreeableness",
    "Neuroticism",
]

APPLICANT_BLUE = "#1f77b4"
HIRED_PASTEL_PINK = "#f4a7b9"


def _to_big_five_display_scale(values: list[float]) -> list[float]:
    """
    Convert normalized simulation traits from 0-1 to the demo chart's 1-5 scale.
    """
    return [1 + (value * 4) for value in values]


def load_trait_means_from_csv(csv_path: Path) -> list[float]:
    """
    Load Big Five averages from one simulation output CSV.
    """
    df = pd.read_csv(csv_path)
    return df[TRAIT_COLUMNS].mean().tolist()


def save_radar_chart(
    applicant_pool_means: list[float],
    hired_workforce_means: list[float],
    title: str,
    output_path: Path,
    applicant_label: str = "Applicant Pool / Initial Profile",
    hired_label: str = "Hired Workforce After Simulation",
) -> None:
    """
    Save a two-profile radar chart using the original demo style.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    applicant_values = _to_big_five_display_scale(applicant_pool_means)
    hired_values = _to_big_five_display_scale(hired_workforce_means)
    applicant_values = applicant_values + applicant_values[:1]
    hired_values = hired_values + hired_values[:1]
    angles = np.linspace(0, 2 * np.pi, len(TRAIT_LABELS), endpoint=False).tolist()
    angles += angles[:1]

    fig = plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    ax.plot(
        angles,
        applicant_values,
        linewidth=2,
        label=applicant_label,
        color=APPLICANT_BLUE,
    )
    ax.fill(angles, applicant_values, alpha=0.18, color=APPLICANT_BLUE)

    ax.plot(
        angles,
        hired_values,
        linewidth=2,
        label=hired_label,
        color=HIRED_PASTEL_PINK,
    )
    ax.fill(angles, hired_values, alpha=0.18, color=HIRED_PASTEL_PINK)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(TRAIT_LABELS, fontsize=11)
    ax.set_ylim(1, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=9)

    plt.title(title, fontsize=14, pad=25)
    ax.legend(loc="upper right", bbox_to_anchor=(1.28, 1.12))

    fig.text(
        0.5,
        0.04,
        "Compares initial applicant pool traits to hired workforce traits after multiple hiring rounds.",
        ha="center",
        fontsize=10,
    )

    plt.tight_layout(rect=[0, 0.07, 1, 1])
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_radar_chart_from_csvs(
    applicant_pool_csv_path: Path,
    hired_workforce_csv_path: Path,
    title: str,
    output_path: Path,
    applicant_label: str = "Applicant Pool / Initial Profile",
    hired_label: str = "Hired Workforce After Simulation",
) -> None:
    """
    Load applicant and selected-workforce CSVs and save a radar chart.
    """
    applicant_pool_means = load_trait_means_from_csv(applicant_pool_csv_path)
    hired_workforce_means = load_trait_means_from_csv(hired_workforce_csv_path)
    save_radar_chart(
        applicant_pool_means=applicant_pool_means,
        hired_workforce_means=hired_workforce_means,
        title=title,
        output_path=output_path,
        applicant_label=applicant_label,
        hired_label=hired_label,
    )
