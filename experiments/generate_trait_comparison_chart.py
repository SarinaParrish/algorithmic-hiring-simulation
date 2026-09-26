import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.experiment_config import PHASE_2_SCENARIOS
from src.radar_chart_demo import save_radar_chart_from_csvs


CHART_TITLES = {
    "baseline": "Baseline: Selected Workforce Trait Profile",
    "personality_weighted": "Personality-Weighted Hiring: Selected Workforce Trait Profile",
    "culture_fit_feedback": "Culture-Fit Feedback Loop: Selected Workforce Trait Profile",
}


def radar_chart_filename(scenario_key: str) -> str:
    return f"{scenario_key}_radar_chart.png"


def applicant_pool_filename(scenario_key: str) -> str:
    return f"{scenario_key}_applicant_pool.csv"


def main():
    output_dir = Path("outputs/figures")
    log_dir = Path("outputs/logs")

    for scenario in PHASE_2_SCENARIOS:
        applicant_pool_csv_path = log_dir / applicant_pool_filename(scenario.key)
        hired_workforce_csv_path = log_dir / scenario.output_filename

        if not applicant_pool_csv_path.exists():
            raise FileNotFoundError(
                f"Missing {applicant_pool_csv_path}. "
                "Run experiments/run_phase2_experiments.py first."
            )

        if not hired_workforce_csv_path.exists():
            raise FileNotFoundError(
                f"Missing {hired_workforce_csv_path}. "
                "Run experiments/run_phase2_experiments.py first."
            )

        output_path = output_dir / radar_chart_filename(scenario.key)
        save_radar_chart_from_csvs(
            applicant_pool_csv_path=applicant_pool_csv_path,
            hired_workforce_csv_path=hired_workforce_csv_path,
            title=CHART_TITLES[scenario.key],
            output_path=output_path,
            hired_label=f"{scenario.label} Hired Workforce",
        )

        print(f"Saved chart: {output_path}")


if __name__ == "__main__":
    main()
