import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scoring import neutral_score, personality_weighted_score
from src.simulation.simulation_runner import run_screening_simulation


def summarize_results(df, label):
    print(f"\n--- {label} ---")
    print("\nSelected candidates by round:")
    print(df.groupby("round").size())

    print("\nGender composition:")
    print(df["gender"].value_counts())

    print("\nRace/Ethnicity composition:")
    print(df["race_ethnicity"].value_counts())

    print("\nAverage selected traits:")
    print(df[[
        "openness",
        "conscientiousness",
        "extraversion",
        "agreeableness",
        "neuroticism",
    ]].mean())


def main():
    neutral_results = run_screening_simulation(neutral_score)
    weighted_results = run_screening_simulation(personality_weighted_score)

    summarize_results(neutral_results, "Neutral Scoring - 10 Rounds")
    summarize_results(weighted_results, "Personality Weighted Scoring - 10 Rounds")

    neutral_results.to_csv("outputs/neutral_scoring_results.csv", index=False)
    weighted_results.to_csv("outputs/personality_weighted_results.csv", index=False)

    print("\nSaved outputs:")
    print("outputs/neutral_scoring_results.csv")
    print("outputs/personality_weighted_results.csv")

if __name__ == "__main__":
    main()