# Synthetic Candidate Generation Notes

## Purpose

This project uses synthetic candidates to simulate how personality-based hiring algorithms may produce compounding workforce disparities over time.

The goal is not to perfectly model real people. The goal is to create a controllable, reproducible simulation population for experimentation.

## Candidate Attributes

Each generated candidate includes:

- candidate ID
- gender
- race/ethnicity
- Big Five personality traits:
  - openness
  - conscientiousness
  - extraversion
  - agreeableness
  - neuroticism
- optional metadata:
  - education level
  - years of experience

## Big Five Trait Generation

For the MVP, each Big Five trait is generated from a normal distribution centered around `0.50` with a standard deviation of `0.15`, then clipped to remain between `0.0` and `1.0`.

This creates candidates whose traits mostly cluster around the middle of the scale, while still allowing lower and higher trait scores.

## Why Normal Distributions?

The Big Five model is commonly represented as five broad personality dimensions: openness, conscientiousness, extraversion, agreeableness, and neuroticism. Big Five inventories are designed to measure those broad trait domains. 

Personality research often treats trait scores as continuous individual differences rather than fixed categories. For simulation purposes, drawing from normal distributions creates a simple, explainable approximation of population variation.

## Current MVP Assumption

The current MVP uses the same mean and standard deviation for all five traits:

| Trait | Mean | Standard Deviation |
|---|---:|---:|
| openness | 0.50 | 0.15 |
| conscientiousness | 0.50 | 0.15 |
| extraversion | 0.50 | 0.15 |
| agreeableness | 0.50 | 0.15 |
| neuroticism | 0.50 | 0.15 |

This is intentionally simple. Later versions can use trait-specific means and standard deviations from published datasets.

## Sources to Cite

- Big Five Inventory overview from the University of Wisconsin–Madison: explains that the BFI measures extraversion, agreeableness, conscientiousness, neuroticism, and openness.
- Fleeson (2009), available through PubMed Central, discusses Big Five standing and trait/state distributions.
- Soto & John’s Big Five Inventory work can be used later if this project adds more precise trait norms.

## Important Limitation

These generated traits should not be interpreted as real psychological assessments. They are synthetic simulation variables used to test how scoring rules behave over repeated hiring rounds.