import pandas as pd

from src.agents.candidate import Candidate


def select_top_candidates(
    candidates: list[Candidate],
    scoring_function,
    n_selected: int,
) -> pd.DataFrame:
    """
    Score candidates and return the top-ranked candidates as a DataFrame.

    This represents the algorithmic screening stage:
    candidates are ranked by score, and the top candidates advance.
    """
    scored_candidates = []

    for candidate in candidates:
        row = candidate.to_dict()
        row["score"] = scoring_function(candidate)
        scored_candidates.append(row)

    df = pd.DataFrame(scored_candidates)
    df = df.sort_values(by="score", ascending=False)

    return df.head(n_selected).reset_index(drop=True)