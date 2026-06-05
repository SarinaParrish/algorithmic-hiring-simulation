# Algorithmic Hiring Simulation

## AISE 26 Solo Capstone Project

**Sarina Parrish**

---

## Project Overview

This project is a Python-based simulation exploring how personality-based hiring algorithms can create compounding workforce disparities over time.

Modern hiring platforms increasingly use algorithmic screening tools and personality assessments to evaluate candidates. These systems are often presented as objective, but small differences in how candidate traits are weighted can influence who is selected across repeated hiring rounds.

This capstone models that process using synthetic candidates, Big Five personality traits, demographic attributes, configurable scoring systems, and multi-round screening simulations.

The goal is not to predict real hiring outcomes, but to demonstrate how simple algorithmic rules can produce measurable differences in selected candidate populations over time.

---

## Research Question

How do trait-weighting choices in AI hiring algorithms affect selected candidate populations over repeated screening rounds?

More specifically:

* Do personality-weighted scoring systems change the traits of selected candidates?
* Do repeated screening rounds amplify those differences?
* How can small scoring choices lead to larger systemic patterns?

---

## MVP Features

The current MVP includes:

* Synthetic candidate generation
* Big Five personality vectors
* Demographic attributes
* Configurable scoring systems
* Deterministic screening pipeline
* Multi-round simulation runner
* CSV experiment logging
* Radar chart visualizations
* Comparative scoring experiments
* Reproducible seeded simulations

---

## Current Findings

The MVP compares a neutral scoring approach against a personality-weighted scoring approach.

In the weighted scoring condition, selected candidates showed:

* Higher average conscientiousness
* Lower average neuroticism
* Measurable changes in selected personality profiles
* Repeated selection patterns across 10 screening rounds

Example 10-round results:

| Trait             | Neutral Scoring | Personality Weighted Scoring |
| ----------------- | --------------: | ---------------------------: |
| Openness          |        0.588965 |                     0.572800 |
| Conscientiousness |        0.593010 |                     0.651225 |
| Extraversion      |        0.610660 |                     0.615670 |
| Agreeableness     |        0.566700 |                     0.536325 |
| Neuroticism       |        0.596475 |                     0.464245 |

These results show that even a simple trait-weighted screening rule can meaningfully change the personality profile of selected candidates over repeated hiring rounds.

---

## Repository Structure

```text
algorithmic-hiring-simulation/
├── README.md
├── requirements.txt
├── data/
├── docs/
│   ├── architecture.md
│   ├── candidate_generation_notes.md
│   ├── mvp_scope.md
│   └── images/
│       └── output (1).png
├── experiments/
│   ├── generate_candidates_demo.py
│   ├── generate_trait_comparison_chart.py
│   ├── run_baseline.py
│   ├── run_comparison.py
│   ├── run_multi_round_simulation.py
│   └── run_screening_experiment.py
├── outputs/
│   ├── figures/
│   ├── logs/
│   ├── neutral_scoring_results.csv
│   └── personality_weighted_results.csv
├── src/
│   ├── agents/
│   │   └── candidate.py
│   ├── simulation/
│   │   ├── candidate_generator.py
│   │   ├── screening.py
│   │   └── simulation_runner.py
│   ├── data_generation.py
│   ├── metrics.py
│   ├── radar_chart_demo.py
│   ├── scoring.py
│   └── visualization.py
└── tests/
    ├── test_candidate_generation.py
    └── test_smoke.py
```

---

## How the Simulation Works

The simulation follows a simple pipeline:

1. Generate synthetic candidates.
2. Assign each candidate demographic attributes.
3. Assign each candidate Big Five personality trait values.
4. Apply a scoring function to each candidate.
5. Select the top candidates for each round.
6. Repeat the process across multiple screening rounds.
7. Compare selected candidate traits and demographic composition across scoring systems.
8. Save results as CSV logs and visual outputs.

---

## Main Demo Script

The main MVP demo script is:

```bash
python3 experiments/run_multi_round_simulation.py
```

This runs a 10-round comparison between:

1. Neutral scoring
2. Personality-weighted scoring

The script prints summary results to the terminal and saves CSV output files.

---

## Example Output Files

Running the main simulation creates:

```text
outputs/neutral_scoring_results.csv
outputs/personality_weighted_results.csv
```

Additional logged versions may also appear in:

```text
outputs/logs/
```

Visualization outputs include:

```text
docs/images/output (1).png
outputs/figures/selected_trait_comparison.png
```

---

## Installation and Setup

Clone the repository:

```bash
git clone <repo-url>
cd algorithmic-hiring-simulation
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run the main simulation:

```bash
python3 experiments/run_multi_round_simulation.py
```

---

## Technical Stack

* Python
* NumPy
* pandas
* matplotlib
* pytest

---

## Methodology

This project uses synthetic data rather than real applicant data. Each candidate is represented as an agent with demographic attributes and Big Five personality trait values.

The simulation compares how different scoring rules affect who is selected. The neutral scoring condition provides a baseline, while the personality-weighted condition applies stronger preference to certain traits.

By running the process across multiple rounds, the project demonstrates how repeated algorithmic decisions can produce measurable differences in selected candidate populations.

---

## Limitations

This simulation is intentionally simplified for an MVP.

Current limitations include:

* Candidate data is synthetic.
* Scoring rules are illustrative, not production hiring models.
* The MVP models screening outcomes, not full real-world hiring decisions.
* Demographic results should not be interpreted as real-world predictions.
* The current version does not yet include feedback loops where selected candidates influence future scoring criteria.
* The model is designed to support exploration and explanation, not to make hiring recommendations.

---

## Phase 2 Roadmap

Planned Phase 2 improvements may include:

* Feedback loops where selected workers influence future culture-fit criteria
* Intervention testing, such as blind screening or trait re-weighting
* Additional scoring scenarios
* Sensitivity analysis across scoring parameters
* Stronger written analysis connecting simulation findings to real-world hiring algorithm debates

The priority for Phase 2 is to improve analytical depth while keeping the project explainable and reproducible.

---

## Showcase Summary

This project demonstrates how personality-based algorithmic screening can shift selected candidate profiles over time.

The MVP successfully generates synthetic candidates, applies configurable scoring systems, runs repeated screening simulations, logs results, and produces comparative visualizations.

The main finding is that personality-weighted scoring increased conscientiousness and decreased neuroticism among selected candidates compared to neutral scoring. This supports the broader argument that small algorithmic design choices can compound into larger workforce-level patterns.

---

## Author

**Sarina Parrish**
AISE 26 Solo Capstone Project
