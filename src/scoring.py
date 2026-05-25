from src.agents.candidate import Candidate


def neutral_score(candidate: Candidate) -> float:
    """
    Score a candidate by averaging all Big Five traits equally.
    """
    return round(sum(candidate.trait_vector()) / 5, 3)


def personality_weighted_score(candidate: Candidate) -> float:
    """
    Score a candidate using a simple personality-weighted hiring rule.

    This MVP version places extra weight on conscientiousness and extraversion
    to simulate a hiring system that favors traits often associated with
    workplace performance or culture-fit assumptions.
    """
    score = (
        0.15 * candidate.openness
        + 0.35 * candidate.conscientiousness
        + 0.25 * candidate.extraversion
        + 0.15 * candidate.agreeableness
        + 0.10 * (1 - candidate.neuroticism)
    )

    return round(score, 3)