# MVP Scope

## Algorithmic Hiring Simulation

### MVP Goal

Build a complete end-to-end simulation that demonstrates how personality-based scoring systems can influence candidate selection outcomes over repeated hiring rounds.

The MVP focuses on creating a reproducible and explainable simulation rather than a production hiring system.

---

# In Scope (Completed)

The following components are included in the Phase 1 MVP:

## Candidate Generation

* Synthetic candidate creation
* Big Five personality traits
* Demographic attributes
* Education levels
* Experience levels

## Candidate Representation

* Candidate agent model
* Structured candidate attributes
* Reproducible population generation

## Scoring Systems

* Neutral scoring approach
* Personality-weighted scoring approach
* Configurable candidate evaluation logic

## Screening Pipeline

* Candidate scoring
* Candidate ranking
* Top-candidate selection

## Simulation

* Multi-round screening process
* Repeated experiment execution
* Workforce outcome tracking

## Metrics and Analysis

* Personality trait summaries
* Demographic composition summaries
* Comparative experiment analysis

## Outputs

* CSV logging
* Experiment result storage
* Radar chart visualizations
* Trait comparison charts

## Testing

* Candidate generation tests
* Basic smoke tests

---

# Out of Scope

The following items are intentionally excluded from the MVP:

* Real applicant data
* Production hiring systems
* Machine learning models
* Live deployment
* Web applications
* Real-world hiring recommendations
* Automated decision-making systems
* Predictive workforce forecasting

---

# Assumptions

The MVP makes several simplifying assumptions:

* Candidate data is synthetic.
* Personality traits are represented using Big Five scores.
* Scoring systems are simplified representations of screening rules.
* Screening outcomes are not equivalent to actual hiring outcomes.
* Simulation results are exploratory rather than predictive.

---

# Success Criteria

The MVP is considered successful if it can:

1. Generate synthetic candidate populations.
2. Apply configurable scoring systems.
3. Execute repeated screening rounds.
4. Log experiment results.
5. Produce comparative visualizations.
6. Demonstrate measurable differences between scoring approaches.

---

# Phase 2 Opportunities

Potential future extensions include:

* Feedback loops where workforce composition influences future scoring
* Intervention testing
* Additional scoring approaches
* Sensitivity analysis
* Expanded visualization suite
* Comparison to published hiring audit studies
* Deeper fairness analysis

These enhancements are intentionally deferred until after MVP completion.

---

# Current MVP Status

Phase 1 MVP is complete.

The system successfully:

* Generates synthetic candidates
* Applies configurable scoring systems
* Runs multi-round simulations
* Produces reproducible outputs
* Logs experiment results
* Generates comparative visualizations

Initial findings indicate that personality-weighted scoring can significantly alter the personality profile of selected candidates, particularly increasing conscientiousness and decreasing neuroticism compared to a neutral scoring baseline.
