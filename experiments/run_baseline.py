import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.experiment_config import BASELINE_SCENARIO, TRAIT_COLUMNS
from src.simulation.simulation_runner import run_scenario_simulation


def main():
    output_dir = Path("outputs/logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    results = run_scenario_simulation(BASELINE_SCENARIO)
    output_path = output_dir / BASELINE_SCENARIO.output_filename
    results.to_csv(output_path, index=False)

    print("\n--- Baseline - 10 Rounds ---")
    print("\nAverage selected traits:")
    print(results[TRAIT_COLUMNS].mean())
    print(f"\nSaved output: {output_path}")


if __name__ == "__main__":
    main()
