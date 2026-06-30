from src.agents.candidate import Candidate
from src.experiment_config import (
    BASELINE_SCENARIO,
    CULTURE_FIT_SCENARIO,
    PERSONALITY_WEIGHTED_SCENARIO,
)
from src.scoring import culture_fit_score, score_for_scenario
from src.simulation.simulation_runner import run_scenario_simulation
from src.simulation.simulation_runner import run_scenario_simulation_with_applicant_pool


def _candidate(**overrides):
    values = {
        "candidate_id": 1,
        "gender": "female",
        "race_ethnicity": "Black",
        "openness": 0.5,
        "conscientiousness": 0.8,
        "extraversion": 0.7,
        "agreeableness": 0.4,
        "neuroticism": 0.2,
    }
    values.update(overrides)
    return Candidate(**values)


def test_baseline_scenario_matches_equal_trait_average():
    candidate = _candidate()

    assert score_for_scenario(candidate, BASELINE_SCENARIO) == 0.52


def test_personality_weighted_scenario_inverts_neuroticism():
    candidate = _candidate()

    assert score_for_scenario(candidate, PERSONALITY_WEIGHTED_SCENARIO) == 0.67


def test_culture_fit_score_rewards_similarity_to_workforce_profile():
    similar_candidate = _candidate(openness=0.5)
    different_candidate = _candidate(openness=0.0)
    workforce_profile = {
        "openness": 0.5,
        "conscientiousness": 0.8,
        "extraversion": 0.7,
        "agreeableness": 0.4,
        "neuroticism": 0.2,
    }

    assert culture_fit_score(similar_candidate, workforce_profile) == 1.0
    assert culture_fit_score(different_candidate, workforce_profile) < 1.0


def test_culture_fit_simulation_adds_scenario_column():
    results = run_scenario_simulation(
        scenario=CULTURE_FIT_SCENARIO,
        n_rounds=2,
        candidates_per_round=10,
        selected_per_round=3,
        seed=42,
    )

    assert len(results) == 6
    assert set(results["scenario"]) == {CULTURE_FIT_SCENARIO.key}


def test_scenario_simulation_can_return_applicant_pool():
    selected, applicants = run_scenario_simulation_with_applicant_pool(
        scenario=BASELINE_SCENARIO,
        n_rounds=2,
        candidates_per_round=10,
        selected_per_round=3,
        seed=42,
    )

    assert len(selected) == 6
    assert len(applicants) == 20
    assert set(selected["scenario"]) == {BASELINE_SCENARIO.key}
    assert set(applicants["scenario"]) == {BASELINE_SCENARIO.key}
