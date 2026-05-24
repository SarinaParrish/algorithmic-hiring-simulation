import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.simulation.candidate_generator import CandidateGenerator


def main():
    generator = CandidateGenerator(seed=42)
    df = generator.generate_dataframe(100)

    print("Synthetic Candidate Generation Demo")
    print("-----------------------------------")
    print(df.head())
    print("\nTrait Summary:")
    print(df[[
        "openness",
        "conscientiousness",
        "extraversion",
        "agreeableness",
        "neuroticism",
    ]].describe())

    print("\nDemographic Counts:")
    print(df["gender"].value_counts())
    print(df["race_ethnicity"].value_counts())


if __name__ == "__main__":
    main()