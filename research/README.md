# Research Evidence Packages

## Overview

This directory contains the research supporting the capstone project:

**Modeling Personality-Based Bias in Algorithmic Hiring**

Rather than organizing the literature as a traditional literature review, the research is structured into independent **Evidence Packages**. Each package investigates a specific research domain that informs the simulation, experiment design, interpretation of results, or discussion of limitations.

The objective of this research is **not** to prove that the simulation is correct. Instead, the evidence packages provide real-world context, identify where existing research supports or challenges the simulation's assumptions, and help ensure that the project's conclusions remain academically rigorous.

---

## Repository Structure

```text
research/
│
├── README.md
│
├── package-a-big-five-personality/
├── package-b-algorithmic-hiring/
├── package-c-bias-amplification/
├── package-d-culture-fit/
├── package-e-agent-based-modeling/
├── package-f-governance-and-auditing/
│
└── final-claim-map.md
```

Each evidence package contains two files:

* **research-summary.md** — A research synthesis, evidence summary, and living claim map for that topic.
* **bibliography.md** — A concise bibliography containing core references, DOIs, publisher links, and publicly available resources where appropriate.

---

## Evidence Packages

### Package A — Big Five Personality in Hiring

Examines the use of Big Five personality traits in employment selection, with particular attention to conscientiousness and extraversion. This package provides the research foundation for the project's personality-weighted hiring experiment.

### Package B — Algorithmic Hiring and AI-Assisted Recruitment

Provides background on AI-assisted hiring systems, automated candidate screening, recruitment technologies, and current research surrounding their use in employment.

### Package C — Bias Amplification and Feedback Loops

Explores how repeated algorithmic decisions can reinforce existing patterns over time, providing theoretical support for studying long-term workforce composition rather than isolated hiring decisions.

### Package D — Culture Fit, Homophily, and Organizational Similarity

Examines organizational behavior research related to culture fit, homophily, and similarity-based hiring, supporting the simulation's culture-fit feedback mechanism.

### Package E — Agent-Based Modeling and Simulation

Justifies the use of agent-based modeling as the research methodology for the capstone, explaining why simulation is an appropriate approach for studying complex adaptive systems and emergent behavior.

### Package F — Governance, Auditing, and Responsible AI

Reviews governance frameworks, bias auditing, responsible AI principles, and employment-related AI regulation to place the simulation within the broader context of trustworthy AI.

---

## Final Claim Map

The `final-claim-map.md` document combines the findings from all evidence packages into a single reference. It distinguishes:

* Claims well supported by existing research
* Claims that remain debated or context-dependent
* Claims the current literature cannot support
* Claims the simulation itself cannot make

This document serves as a guide when interpreting simulation results and writing the final capstone report.

---

## Relationship to the Capstone

These evidence packages support the capstone's central research question:

> **How do different personality-weighting strategies in AI hiring algorithms affect workforce composition over time, and under what conditions do small individual biases become larger systemic disparities?**

The research and simulation are designed to complement one another. The literature provides theoretical and empirical context, while the simulation explores one plausible mechanism through which different hiring strategies may influence organizational outcomes over repeated hiring rounds.

Together, they provide a structured, research-informed framework for analyzing personality-based bias in algorithmic hiring while acknowledging the limitations of simulation-based research.
