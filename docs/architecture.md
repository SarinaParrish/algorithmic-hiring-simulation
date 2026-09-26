# Architecture Overview

## Algorithmic Hiring Simulation

### Purpose

This project simulates how personality-based hiring algorithms can influence workforce outcomes over repeated screening rounds.

The system generates synthetic candidates, applies configurable scoring functions, selects top candidates, and records how selection patterns change under different scoring approaches.

---

## High-Level System Flow

```text
Candidate Generator
        ↓
Candidate Population
        ↓
Scoring Function
        ↓
Screening Selection
        ↓
Selected Candidates
        ↓
Metrics & Logging
        ↓
Visualization & Analysis
```

---

## Core Components

### Candidate Generation

Location:

```text
src/simulation/candidate_generator.py
```

Generates synthetic candidate populations using:

* Big Five personality traits
* Demographic attributes
* Education levels
* Years of experience

The generator uses seeded randomness to support reproducible experiments.

---

### Candidate Model

Location:

```text
src/agents/candidate.py
```

Each candidate is represented as an agent containing:

* Candidate ID
* Gender
* Race/Ethnicity
* Big Five trait values
* Education level
* Years of experience

This structure provides a consistent representation for all simulation experiments.

---

### Scoring System

Location:

```text
src/scoring.py
```

The scoring system evaluates candidates according to configurable rules.

Current implementations include:

* Neutral scoring
* Personality-weighted scoring

Different scoring configurations allow comparison of how algorithmic preferences affect selected candidate populations.

---

### Screening Pipeline

Location:

```text
src/simulation/screening.py
```

The screening pipeline:

1. Receives a candidate population
2. Scores each candidate
3. Ranks candidates
4. Selects top performers

This process models a simplified algorithmic screening stage in a hiring workflow.

---

### Multi-Round Simulation

Location:

```text
src/simulation/simulation_runner.py
```

The simulation executes repeated screening rounds.

Each round:

1. Generates a candidate pool
2. Applies scoring rules
3. Selects candidates
4. Records outcomes

Repeated rounds allow observation of long-term selection patterns.

---

### Metrics and Logging

Locations:

```text
src/metrics.py
outputs/
outputs/logs/
```

The system records:

* Selected candidate counts
* Demographic composition
* Average personality traits
* Experiment outputs

Results are saved as CSV files for analysis and reproducibility.

---

### Visualization

Locations:

```text
src/visualization.py
src/radar_chart_demo.py
```

Visualization components generate charts used to compare simulation outcomes across scoring approaches.

Current visual outputs include trait comparison visualizations and radar charts.

---

## Design Principles

The project emphasizes:

* Reproducibility
* Explainability
* Modular design
* Experiment-driven analysis

The goal is not to predict real hiring outcomes, but to provide a transparent framework for exploring how algorithmic design choices can influence workforce-level patterns.
