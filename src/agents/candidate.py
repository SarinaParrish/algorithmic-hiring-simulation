from dataclasses import dataclass
from typing import Optional


@dataclass
class Candidate:
    """
    Represents one synthetic job candidate in the hiring simulation.

    Big Five traits are stored as normalized floats between 0.0 and 1.0.
    Demographic attributes are stored as strings so they can be grouped,
    counted, and visualized later.
    """

    candidate_id: int

    # Demographic attributes
    gender: str
    race_ethnicity: str

    # Big Five personality traits
    openness: float
    conscientiousness: float
    extraversion: float
    agreeableness: float
    neuroticism: float

    # Optional metadata for future experiments
    education_level: Optional[str] = None
    years_experience: Optional[int] = None

    def to_dict(self) -> dict:
        """
        Convert a Candidate object into a flat dictionary.

        This makes it easy to create a Pandas DataFrame later:
        pd.DataFrame([candidate.to_dict() for candidate in candidates])
        """
        return {
            "candidate_id": self.candidate_id,
            "gender": self.gender,
            "race_ethnicity": self.race_ethnicity,
            "openness": self.openness,
            "conscientiousness": self.conscientiousness,
            "extraversion": self.extraversion,
            "agreeableness": self.agreeableness,
            "neuroticism": self.neuroticism,
            "education_level": self.education_level,
            "years_experience": self.years_experience,
        }

    def trait_vector(self) -> list[float]:
        """
        Return the Big Five traits as a list in a consistent order.

        This will be useful later for scoring functions.
        """
        return [
            self.openness,
            self.conscientiousness,
            self.extraversion,
            self.agreeableness,
            self.neuroticism,
        ]