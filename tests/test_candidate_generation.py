from src.simulation.candidate_generator import CandidateGenerator


def test_generate_single_candidate():
    generator = CandidateGenerator(seed=42)

    candidate = generator.generate_candidate(candidate_id=1)

    assert candidate.candidate_id == 1

    assert 0.0 <= candidate.openness <= 1.0
    assert 0.0 <= candidate.conscientiousness <= 1.0
    assert 0.0 <= candidate.extraversion <= 1.0
    assert 0.0 <= candidate.agreeableness <= 1.0
    assert 0.0 <= candidate.neuroticism <= 1.0


def test_population_size():
    generator = CandidateGenerator(seed=42)

    population = generator.generate_population(100)

    assert len(population) == 100


def test_reproducibility():
    generator_a = CandidateGenerator(seed=42)
    generator_b = CandidateGenerator(seed=42)

    candidate_a = generator_a.generate_candidate(1)
    candidate_b = generator_b.generate_candidate(1)

    assert candidate_a.to_dict() == candidate_b.to_dict()