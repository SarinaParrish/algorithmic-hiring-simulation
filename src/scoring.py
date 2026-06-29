from src.agents.candidate import Candidate
from src.experiment_config import ExperimentScenario, TRAIT_COLUMNS


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


def weighted_trait_score(
    candidate: Candidate,
    trait_weights: dict[str, float],
    invert_neuroticism: bool = False,
) -> float:
    """
    Score a candidate from configurable Big Five trait weights.

    For personality-weighted hiring, lower neuroticism is often treated as
    preferred, so invert_neuroticism converts that trait to 1 - neuroticism.
    """
    score = 0.0

    for trait_name, weight in trait_weights.items():
        trait_value = getattr(candidate, trait_name)

        if trait_name == "neuroticism" and invert_neuroticism:
            trait_value = 1 - trait_value

        score += weight * trait_value

    return round(score, 3)


def culture_fit_score(
    candidate: Candidate,
    workforce_profile: dict[str, float] | None,
) -> float:
    """
    Measure how similar a candidate is to the current selected workforce.

    Similarity is 1 minus the mean absolute distance across Big Five traits.
    A missing workforce profile returns a neutral value so round 1 is driven
    by the base hiring rule.
    """
    if not workforce_profile:
        return 0.5

    distances = [
        abs(getattr(candidate, trait_name) - workforce_profile[trait_name])
        for trait_name in TRAIT_COLUMNS
    ]

    return round(1 - (sum(distances) / len(distances)), 3)


def score_for_scenario(
    candidate: Candidate,
    scenario: ExperimentScenario,
    workforce_profile: dict[str, float] | None = None,
) -> float:
    """
    Score a candidate using a Phase 2 experiment scenario.

    Baseline and personality-weighted scenarios use only trait weights.
    Culture-fit scenarios blend that base score with similarity to the
    previously selected workforce profile.
    """
    base_score = weighted_trait_score(
        candidate=candidate,
        trait_weights=scenario.trait_weights,
        invert_neuroticism=scenario.invert_neuroticism,
    )

    if scenario.culture_fit_strength == 0:
        return base_score

    fit_score = culture_fit_score(candidate, workforce_profile)
    base_weight = 1 - scenario.culture_fit_strength
    score = (base_weight * base_score) + (
        scenario.culture_fit_strength * fit_score
    )

    return round(score, 3)
