import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt


def main():
    neutral_df = pd.read_csv(
        "outputs/logs/neutral_scoring_results.csv"
    )

    weighted_df = pd.read_csv(
        "outputs/logs/personality_weighted_results.csv"
    )

    traits = [
        "openness",
        "conscientiousness",
        "extraversion",
        "agreeableness",
        "neuroticism",
    ]

    neutral_means = neutral_df[traits].mean()
    weighted_means = weighted_df[traits].mean()

    plt.figure(figsize=(10, 6))

    x = range(len(traits))

    plt.plot(
        x,
        neutral_means,
        marker="o",
        label="Neutral Scoring",
    )

    plt.plot(
        x,
        weighted_means,
        marker="o",
        label="Personality Weighted",
    )

    plt.xticks(x, traits)
    plt.ylabel("Average Selected Trait Score")
    plt.xlabel("Big Five Traits")

    plt.title(
        "Selected Candidate Trait Comparison"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/selected_trait_comparison.png"
    )

    print(
        "Saved chart: outputs/figures/selected_trait_comparison.png"
    )


if __name__ == "__main__":
    main()