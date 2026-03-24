# Exercise 4.1: Design a Verifiable Prediction

## Background
Maxwell's greatest hit: He derived `v = 1/√(μ₀ε₀)` from his equations, computed the number (~3×10⁸ m/s), and **predicted** that light is an electromagnetic wave. Hertz later confirmed.

Your turn. In business/product contexts, we often have hypotheses. But NOT all hypotheses are **verifiable predictions**.

**Good prediction**:
✅ Quantified (specific number or range)
✅ Novel (not used to build the model)
✅ Testable (experiment feasible with reasonable resources)
✅ Binary outcome (pass/fail, or exceed threshold)

**Bad hypothesis**:
❌ "The new feature will improve user experience." (vague)
❌ "Our model will be better." (better than what? by how much?)

---

## Exercise: Design 3 Predictions for Your Project

Pick **one** of these scenarios (or your own real project):

A. **Growth team**: You're increasing weekly active users (WAU)
B. **Pricing**: You're testing a new pricing model
C. **AI feature**: You're adding LLM-powered chat support
D. **Your actual project**: define your own

For the chosen scenario, write **3 predictions**, each must satisfy:

```
Prediction i: "If we [intervention], then [metric] will [change] by [amount] within [time], with confidence [level]."
```

Example (from Maxwell's style):
> "If displacement current term is correct, then electromagnetic waves should propagate at speed v = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s. This can be tested by generating oscillating currents and measuring wavelength/frequency."

---

## Exercise A (Growth): Increasing WAU

**Intervention ideas**:
- Send push notifications at optimal time
- Add social sharing feature
- Reduce signup friction
- Improve onboarding flow

### Write your predictions:

1. **Prediction 1**:
   - Intervention: [specific change]
   - Metric: [e.g., WAU, DAU, retention]
   - Expected change: [e.g., +15%]
   - Time horizon: [e.g., 4 weeks]
   - Confidence: [e.g., 95%]
   - Minimum detectable effect (MDE): [e.g., 5%]

2. **Prediction 2**:

3. **Prediction 3**:

---

## Exercise B (Pricing): New Pricing Model

Example current: $20/user/month flat
New: Tiered pricing $10 (starter), $30 (pro), $100 (enterprise) per user

### Predictions:

1. **Revenue impact**: "Switching to tiered pricing will increase average revenue per user (ARPU) by ≥20% within 3 months, without losing >5% of existing customers."

2. **Segment response**:
   - Starter tier will attract 100 new small customers in first month (vs baseline 20)
   - Enterprise tier conversion rate from free trial will increase from 10% to 25%

---

## Exercise C (AI Feature): LLM Chat Support

Intervention: Replace rule-based FAQ with GPT-4 chatbot

### Predictions:

1. **Efficiency**: "AI chatbot will resolve 40% of inquiries without human agent, reducing average handle time from 5 min to 2 min (60% reduction)."

2. **Quality**: "Customer satisfaction (CSAT) will remain ≥85% (current human-only is 88%)."

3. **Cost**: "Support labor cost per ticket will drop from $5 to $1.50 (70% reduction)."

---

## Exercise D (Your Project)

Use this template:

```
Context:
  Current state: [baseline metrics]
  Intervention: [what you'll change]
  Target metric: [what you'll measure]

Predictions:
1. [prediction statement]
2. [prediction statement]
3. [prediction statement]

For each:
- Success threshold (quantitative)
- Experiment design (control vs treatment, sample size)
- Test duration
- Decision rule (if p<0.05 and effect>threshold → launch)
```

---

## Deliverables

Submit a markdown file with:

1. Scenario choice and brief description
2. 3 prediction statements (properly formatted)
3. For **one** prediction, write the **experiment design**:
   - Null hypothesis H₀
   - Alternative hypothesis H₁
   - Primary metric
   - Sample size calculation (use eff=0.05, power=0.8, expected lift=?)
   - Duration
   - Stopping criteria (early success/failure)
   - Potential confounders & how to control

---

## Example Answer (Growth Scenario)

```markdown
### Prediction 1
"If we send push notifications at 7 PM instead of 3 PM, daily active users (DAU) will increase by 12% within 2 weeks, with 95% confidence."

Experiment:
- H₀: Δ_DAU = 0
- H₁: Δ_DAU > 0
- Metric: DAU (7-day rolling average)
- Sample: 50% users get 7 PM (treatment), 50% get 3 PM (control)
- Duration: 14 days
- MDE: 8% (detect with 80% power given σ=0.15 from historical)
- Decision: if p<0.05 and lift≥8% → switch to 7 PM for all
```

---

## Scoring Rubric

Your predictions will be evaluated on:

| Criterion | Points |
|-----------|--------|
| Quantified (specific number, not "improve") | 2 |
| Novel (not used in model building) | 2 |
| Testable (experiment feasible) | 2 |
| Binary outcome (clear pass/fail) | 2 |
| Realistic time horizon | 1 |
| Appropriate confidence level | 1 |
| **Total per prediction** | **10** |

**Total**: 30 points (3 predictions)

---

🦞 龙虾: "好理论不是解释过去，而是预告未来。你的实验，就是那个'赫兹'。"
