import pandas as pd

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