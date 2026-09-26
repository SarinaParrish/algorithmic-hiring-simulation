import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.experiment_config import PHASE_2_SCENARIOS, TRAIT_COLUMNS
from src.simulation.simulation_runner import (
    run_scenario_simulation_with_applicant_pool,
)


OUTPUT_DIR = Path("outputs/logs")


def summarize_results(df, label):
    print(f"\n--- {label} ---")

    print("\nSelected candidates by round:")
    print(df.groupby("round").size())

    print("\nGender composition:")
    print(df["gender"].value_counts())

    print("\nRace/Ethnicity composition:")
    print(df["race_ethnicity"].value_counts())

    print("\nAverage selected traits:")
    print(df[TRAIT_COLUMNS].mean())


def applicant_pool_filename(scenario_key: str) -> str:
    return f"{scenario_key}_applicant_pool.csv"


def run_phase2_experiments(
    n_rounds: int = 10,
    candidates_per_round: int = 100,
    selected_per_round: int = 20,
    seed: int = 42,
):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    for scenario in PHASE_2_SCENARIOS:
        selected_df, applicant_df = run_scenario_simulation_with_applicant_pool(
            scenario=scenario,
            n_rounds=n_rounds,
            candidates_per_round=candidates_per_round,
            selected_per_round=selected_per_round,
            seed=seed,
        )

        output_path = OUTPUT_DIR / scenario.output_filename
        applicant_output_path = OUTPUT_DIR / applicant_pool_filename(scenario.key)

        selected_df.to_csv(output_path, index=False)
        applicant_df.to_csv(applicant_output_path, index=False)

        summarize_results(selected_df, f"{scenario.label} - {n_rounds} Rounds")
        print(f"\nSaved output: {output_path}")
        print(f"Saved applicant pool: {applicant_output_path}")

        results[scenario.key] = selected_df

    return results


def main():
    run_phase2_experiments()


if __name__ == "__main__":
    main()
