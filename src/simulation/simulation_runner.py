import pandas as pd

from src.experiment_config import ExperimentScenario, TRAIT_COLUMNS
from src.scoring import score_for_scenario
from src.simulation.candidate_generator import CandidateGenerator
from src.simulation.screening import select_top_candidates


def run_screening_simulation(
    scoring_function,
    n_rounds: int = 10,
    candidates_per_round: int = 100,
    selected_per_round: int = 20,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Run a multi-round algorithmic screening simulation.

    Each round:
    - generates a fresh candidate pool
    - scores candidates
    - selects the top candidates
    - records selected candidates with round number
    """
    generator = CandidateGenerator(seed=seed)
    all_selected = []

    for round_number in range(1, n_rounds + 1):
        candidates = generator.generate_population(candidates_per_round)

        selected = select_top_candidates(
            candidates=candidates,
            scoring_function=scoring_function,
            n_selected=selected_per_round,
        )

        selected["round"] = round_number
        all_selected.append(selected)

    return pd.concat(all_selected, ignore_index=True)


def _workforce_trait_profile(
    selected_rounds: list[pd.DataFrame],
) -> dict[str, float] | None:
    """
    Calculate the selected workforce's average Big Five profile so far.
    """
    if not selected_rounds:
        return None

    selected_to_date = pd.concat(selected_rounds, ignore_index=True)
    return selected_to_date[TRAIT_COLUMNS].mean().to_dict()


def run_scenario_simulation(
    scenario: ExperimentScenario,
    n_rounds: int = 10,
    candidates_per_round: int = 100,
    selected_per_round: int = 20,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Run one configured Phase 2 experiment scenario.

    Each scenario uses the same candidate generation and top-N screening path.
    If culture_fit_strength is enabled, scores from round 2 onward are blended
    with similarity to the workforce selected in earlier rounds.
    """
    generator = CandidateGenerator(seed=seed)
    all_selected = []

    for round_number in range(1, n_rounds + 1):
        workforce_profile = _workforce_trait_profile(all_selected)
        candidates = generator.generate_population(candidates_per_round)

        selected = select_top_candidates(
            candidates=candidates,
            scoring_function=lambda candidate: score_for_scenario(
                candidate=candidate,
                scenario=scenario,
                workforce_profile=workforce_profile,
            ),
            n_selected=selected_per_round,
        )

        selected["round"] = round_number
        selected["scenario"] = scenario.key
        all_selected.append(selected)

    return pd.concat(all_selected, ignore_index=True)


def run_scenario_simulation_with_applicant_pool(
    scenario: ExperimentScenario,
    n_rounds: int = 10,
    candidates_per_round: int = 100,
    selected_per_round: int = 20,
    seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Run one Phase 2 scenario and keep both applicant and selected records.

    Applicant records capture the generated candidate pools before screening.
    Selected records capture the hired workforce after scoring and top-N
    selection. Both use the same generated candidates for the same run.
    """
    generator = CandidateGenerator(seed=seed)
    all_applicants = []
    all_selected = []

    for round_number in range(1, n_rounds + 1):
        workforce_profile = _workforce_trait_profile(all_selected)
        candidates = generator.generate_population(candidates_per_round)

        applicants = pd.DataFrame([candidate.to_dict() for candidate in candidates])
        applicants["round"] = round_number
        applicants["scenario"] = scenario.key
        all_applicants.append(applicants)

        selected = select_top_candidates(
            candidates=candidates,
            scoring_function=lambda candidate: score_for_scenario(
                candidate=candidate,
                scenario=scenario,
                workforce_profile=workforce_profile,
            ),
            n_selected=selected_per_round,
        )

        selected["round"] = round_number
        selected["scenario"] = scenario.key
        all_selected.append(selected)

    return (
        pd.concat(all_selected, ignore_index=True),
        pd.concat(all_applicants, ignore_index=True),
    )
