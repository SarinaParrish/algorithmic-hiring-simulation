import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.simulation.candidate_generator import CandidateGenerator
from src.simulation.screening import select_top_candidates
from src.scoring import (
    neutral_score,
    personality_weighted_score,
)


def run_experiment(scoring_function, label):
    print(f"\n--- {label} ---")

    generator = CandidateGenerator(seed=42)

    candidates = generator.generate_population(100)

    selected = select_top_candidates(
        candidates=candidates,
        scoring_function=scoring_function,
        n_selected=20,
    )

    print("\nTop Candidates:")
    print(selected.head())

    print("\nGender Distribution:")
    print(selected["gender"].value_counts())

    print("\nRace/Ethnicity Distribution:")
    print(selected["race_ethnicity"].value_counts())

    print("\nAverage Trait Scores:")
    print(
        selected[
            [
                "openness",
                "conscientiousness",
                "extraversion",
                "agreeableness",
                "neuroticism",
            ]
        ].mean()
    )


def main():
    run_experiment(neutral_score, "Neutral Scoring")

    run_experiment(
        personality_weighted_score,
        "Personality Weighted Scoring",
    )


if __name__ == "__main__":
    main()