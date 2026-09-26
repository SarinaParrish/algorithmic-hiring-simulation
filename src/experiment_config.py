from dataclasses import dataclass


TRAIT_COLUMNS = [
    "openness",
    "conscientiousness",
    "extraversion",
    "agreeableness",
    "neuroticism",
]


@dataclass(frozen=True)
class ExperimentScenario:
    """
    Configuration for one hiring simulation experiment.

    culture_fit_strength controls how much previous selected workforce traits
    influence current-round scores. A value of 0 disables feedback.
    """

    key: str
    label: str
    trait_weights: dict[str, float]
    output_filename: str
    invert_neuroticism: bool = False
    culture_fit_strength: float = 0.0


BASELINE_SCENARIO = ExperimentScenario(
    key="baseline",
    label="Baseline",
    trait_weights={
        "openness": 0.20,
        "conscientiousness": 0.20,
        "extraversion": 0.20,
        "agreeableness": 0.20,
        "neuroticism": 0.20,
    },
    output_filename="baseline_results.csv",
)


PERSONALITY_WEIGHTED_SCENARIO = ExperimentScenario(
    key="personality_weighted",
    label="Personality Weighted Hiring",
    trait_weights={
        "openness": 0.15,
        "conscientiousness": 0.35,
        "extraversion": 0.25,
        "agreeableness": 0.15,
        "neuroticism": 0.10,
    },
    output_filename="personality_weighted_results.csv",
    invert_neuroticism=True,
)


CULTURE_FIT_SCENARIO = ExperimentScenario(
    key="culture_fit_feedback",
    label="Culture-Fit Feedback Loop",
    trait_weights={
        "openness": 0.15,
        "conscientiousness": 0.35,
        "extraversion": 0.25,
        "agreeableness": 0.15,
        "neuroticism": 0.10,
    },
    output_filename="culture_fit_feedback_results.csv",
    invert_neuroticism=True,
    culture_fit_strength=0.30,
)


PHASE_2_SCENARIOS = [
    BASELINE_SCENARIO,
    PERSONALITY_WEIGHTED_SCENARIO,
    CULTURE_FIT_SCENARIO,
]
