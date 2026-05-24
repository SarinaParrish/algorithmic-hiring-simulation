import numpy as np
import pandas as pd

from src.agents.candidate import Candidate


class CandidateGenerator:
    """
    Generates synthetic candidates for the hiring simulation.

    This generator creates:
    - Big Five personality traits using normal distributions
    - demographic attributes using configurable category probabilities
    - optional education and experience metadata

    Random generation is controlled by a seed for reproducibility.
    """

    def __init__(self, seed: int = 42):
        self.rng = np.random.default_rng(seed)

        self.big_five_means = {
            "openness": 0.50,
            "conscientiousness": 0.50,
            "extraversion": 0.50,
            "agreeableness": 0.50,
            "neuroticism": 0.50,
        }

        self.big_five_std = 0.15

        self.gender_categories = ["female", "male", "nonbinary"]
        self.gender_probabilities = [0.49, 0.49, 0.02]

        self.race_ethnicity_categories = [
            "Black",
            "Latine",
            "White",
            "Asian",
            "Multiracial",
        ]
        self.race_ethnicity_probabilities = [0.20, 0.25, 0.35, 0.15, 0.05]

        self.education_levels = [
            "high_school",
            "associate",
            "bachelor",
            "master",
        ]

    def generate_trait(self, trait_name: str) -> float:
        """
        Generate one Big Five trait score as a clipped normal value.
        """
        mean = self.big_five_means[trait_name]
        value = self.rng.normal(loc=mean, scale=self.big_five_std)
        return round(float(np.clip(value, 0.0, 1.0)), 3)

    def generate_candidate(self, candidate_id: int) -> Candidate:
        """
        Generate one synthetic Candidate object.
        """
        gender = str(
            self.rng.choice(
                self.gender_categories,
                p=self.gender_probabilities,
            )
        )

        race_ethnicity = str(
            self.rng.choice(
                self.race_ethnicity_categories,
                p=self.race_ethnicity_probabilities,
            )
        )

        education_level = str(
            self.rng.choice(self.education_levels)  
        )
        years_experience = int(self.rng.integers(0, 16))

        return Candidate(
            candidate_id=candidate_id,
            gender=gender,
            race_ethnicity=race_ethnicity,
            openness=self.generate_trait("openness"),
            conscientiousness=self.generate_trait("conscientiousness"),
            extraversion=self.generate_trait("extraversion"),
            agreeableness=self.generate_trait("agreeableness"),
            neuroticism=self.generate_trait("neuroticism"),
            education_level=education_level,
            years_experience=years_experience,
        )

    def generate_population(self, n_candidates: int) -> list[Candidate]:
        """
        Generate a list of synthetic candidates.
        """
        return [
            self.generate_candidate(candidate_id=i + 1)
            for i in range(n_candidates)
        ]

    def generate_dataframe(self, n_candidates: int) -> pd.DataFrame:
        """
        Generate synthetic candidates and return them as a Pandas DataFrame.
        """
        candidates = self.generate_population(n_candidates)
        return pd.DataFrame([candidate.to_dict() for candidate in candidates])