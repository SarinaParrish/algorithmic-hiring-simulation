# Evidence Package B
# Algorithmic Hiring and AI-Assisted Recruitment

## Purpose

This evidence package examines how algorithmic and AI-assisted systems are used in hiring and recruitment. It supports all three experiments by providing real-world context for automated scoring, screening, ranking, and candidate selection.

This package does not claim that all AI hiring tools are biased or that all algorithmic hiring systems operate the same way. Its purpose is to explain why automated hiring systems matter, what risks researchers have identified, and how this connects to a simulation that tests different scoring strategies over repeated hiring rounds.

Supports:
- Experiment 1 – Baseline
- Experiment 2 – Personality-Weighted Hiring
- Experiment 3 – Culture-Fit Feedback Loop

---

## Executive Summary

Algorithmic hiring refers to the use of computational tools to assist with recruitment, screening, assessment, ranking, or selection of job candidates. These systems may be used to process large applicant pools, apply scoring rules consistently, identify candidates who match employer-defined criteria, or support human decision-making.

Research shows that algorithmic hiring is not one single technology. It can include resume screening systems, pre-employment assessments, personality or behavioral assessments, video interview analysis, ranking tools, chatbots, and predictive analytics. This matters for the capstone because the simulation models a simplified version of one part of this pipeline: candidates are scored according to configurable rules, selected over multiple rounds, and then analyzed for changes in workforce composition.

Raghavan et al. (2020) is one of the most important sources for this package because it examines commercial vendors offering algorithmic pre-employment assessments. The paper argues that there has been growing interest in using algorithms in hiring, especially as a way to address or mitigate bias, but that limited public information exists about how these tools are built, validated, and audited. This directly supports the need for cautious modeling: the simulation can explore possible mechanisms, but it cannot claim to reproduce a real vendor system.

Recent multidisciplinary reviews also emphasize that algorithmic hiring sits at the intersection of computer science, law, organizational psychology, and fairness research. Researchers continue to debate whether algorithmic hiring can reduce bias, reproduce existing discrimination, or introduce new forms of unfairness. This is why the capstone should frame the simulation as an exploratory model rather than a proof that AI hiring systems behave in a specific way.

This package supports the overall project by showing that automated hiring systems are real, consequential, and contested. It justifies why a simulation of repeated scoring decisions is relevant, while also clarifying that real-world hiring tools are more complex than the model.

---

## Key Takeaways

- Algorithmic hiring systems are used in recruitment, screening, assessment, ranking, and candidate selection.
- These systems can improve speed, consistency, and scalability in high-volume hiring.
- Algorithmic hiring tools may also introduce or reproduce bias depending on data, features, scoring rules, validation, and deployment context.
- Commercial hiring tools are often difficult to evaluate because their internal models and validation practices may not be fully transparent.
- Human oversight does not automatically eliminate algorithmic risk.
- The simulation can model one simplified mechanism of algorithmic hiring, but it cannot represent the full complexity of real hiring software.

---

## Current Research Consensus

### Strong Evidence

- AI-assisted hiring systems are increasingly used across the recruitment and selection pipeline.
- Automated systems can apply scoring or ranking rules across large applicant pools.
- Algorithmic hiring systems require validation, monitoring, and evaluation.
- Bias can enter through data choices, prediction targets, feature selection, model design, and deployment context.
- Transparency and accountability are major concerns in commercial hiring tools.

### Mixed / Ongoing Debate

- Whether algorithmic hiring reduces bias compared to human hiring.
- Which fairness metrics are most appropriate for employment decisions.
- Whether human oversight is enough to correct algorithmic bias.
- How much transparency vendors should provide.
- Whether AI hiring systems improve workforce diversity.
- How algorithmic hiring tools should be governed or audited.

---

## Major Sources

### Raghavan et al. (2020)

**Why it Matters**  
Foundational paper on commercial algorithmic hiring vendors. This source is central because it examines how vendors describe, validate, and evaluate algorithmic pre-employment assessments.

**Key Findings**
- Algorithmic hiring tools are often promoted as ways to improve or debias hiring.
- Vendor claims and validation practices vary.
- Data choices, prediction targets, and bias mitigation methods create technical and legal challenges.
- Limited transparency makes external evaluation difficult.

**Supports**  
Experiments 1, 2, and 3

**Limitations**  
Does not provide direct experimental data from the capstone’s simulation model.

---

### Fabris et al. (2025)

**Why it Matters**  
Recent multidisciplinary survey on fairness and bias in algorithmic hiring. Useful for connecting the capstone to current research across computer science, law, and social science.

**Key Findings**
- Algorithmic hiring fairness remains an unsettled research problem.
- Bias can arise at multiple points in the hiring pipeline.
- Fairness definitions, datasets, mitigation methods, and legal standards vary.
- The field still lacks clear agreement on whether and when algorithmic hiring is less biased than traditional hiring.

**Supports**  
Experiments 1, 2, and 3

**Limitations**  
Broad survey; not focused specifically on personality-weighted hiring.

---

### Bogen & Rieke (2018)

**Why it Matters**  
Influential report on hiring algorithms, equity, and bias. Useful for explaining the practical risks of automated hiring systems.

**Key Findings**
- Hiring algorithms can affect who sees job opportunities, who is screened out, and who advances.
- Bias can enter through training data, proxies, and design choices.
- Automated systems may create barriers for applicants even before human review.
- Transparency and accountability are important for responsible deployment.

**Supports**  
Experiments 1, 2, and 3

**Limitations**  
Policy/report source rather than peer-reviewed empirical study.

---

### Rigotti & Fosch-Villaronga (2024)

**Why it Matters**  
Recent scoping review focused specifically on fairness in AI recruitment and selection.

**Key Findings**
- Fairness in AI recruitment is difficult to define and operationalize.
- AI hiring tools must be evaluated not only for accuracy but also for fairness and social impact.
- Practical implementation of fairness remains challenging.
- Recruitment systems require attention to both technical and legal concerns.

**Supports**  
Experiments 1, 2, and 3

**Limitations**  
Scoping review; does not test a specific hiring simulation.

---

### Dadaboyev et al. (2025)

**Why it Matters**  
Recent systematic review on the role of AI in employee recruitment.

**Key Findings**
- AI may improve efficiency in recruitment and screening.
- AI recruitment tools also raise concerns about fairness, algorithmic bias, and ethics.
- Ethical frameworks and future research are needed to support fair use of AI in recruitment.
- AI hiring should not be evaluated only by speed or automation benefits.

**Supports**  
Experiments 1, 2, and 3

**Limitations**  
Recent review; should be used for context rather than as the main theoretical foundation.

---

### NIST AI Risk Management Framework (2023)

**Why it Matters**  
Authoritative framework for thinking about trustworthy and responsible AI systems. Useful for framing why hiring algorithms should be evaluated and documented.

**Key Findings**
- AI systems should be governed, mapped, measured, and managed.
- Trustworthy AI involves validity, reliability, safety, security, accountability, transparency, explainability, privacy, and fairness.
- Risk management is an ongoing process rather than a one-time check.
- High-impact AI systems require careful monitoring and evaluation.

**Supports**  
All experiments, especially final discussion and limitations

**Limitations**  
Not specific to hiring; should be used as a responsible AI framing source.

---

## Connection to the Simulation

### Research Supports

- Modeling hiring as a scoring and selection pipeline.
- Comparing different algorithmic scoring strategies.
- Studying repeated hiring decisions over multiple rounds.
- Treating automated hiring as a system that can produce different outcomes depending on design choices.
- Evaluating outputs rather than assuming the algorithm is neutral.

### Research Does Not Support

- Claiming that all AI hiring tools work like the simulation.
- Claiming that algorithmic hiring is always more biased than human hiring.
- Claiming that algorithmic hiring is always fairer than human hiring.
- Claiming that the simulation reproduces a real vendor’s internal model.
- Treating automation as automatically objective.

---

## Living Claim Map

### Supported Claims

- Algorithmic hiring systems are used in modern recruitment and selection.
- Automated hiring tools can score, rank, screen, or recommend candidates.
- Algorithmic hiring systems can scale decision rules across large applicant pools.
- Bias may enter through data, features, labels, prediction targets, scoring rules, or deployment context.
- Algorithmic hiring requires validation, monitoring, and responsible evaluation.

### Mixed Claims

- AI hiring systems reduce human bias.
- AI hiring systems improve workforce diversity.
- Human oversight is sufficient to prevent algorithmic harm.
- Bias audits fully capture fairness risks.
- Algorithmic systems are more objective than human decision-makers.

### Claims the Literature Cannot Make

- Algorithmic hiring is always discriminatory.
- Algorithmic hiring is always more fair than traditional hiring.
- All AI hiring tools use the same methods.
- Vendor claims about fairness are always reliable.
- One fairness metric can fully determine whether a hiring system is fair.

### Claims My Simulation Cannot Make

- The simulation cannot prove how real AI hiring vendors operate.
- The simulation cannot prove that real companies use the modeled scoring rules.
- The simulation cannot determine whether a specific commercial hiring tool is biased.
- The simulation cannot prove that algorithmic hiring causes real-world discrimination.
- The simulation cannot capture the full complexity of real recruitment pipelines.

The defensible claim is: this simulation models one simplified mechanism by which automated scoring rules may influence workforce composition over repeated hiring rounds.