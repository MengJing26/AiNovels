# Exercise 3.1: Pricing Boundary Innovation

## Problem Statement
Your SaaS product faces a classic trade-off:

- **Small businesses** demand low price (p → 0) but expect full features.
- **Enterprise** customers want premium features but resist high per-seat prices.

The naive pricing model: `price = base + per_user × n` fails at boundaries:
- n → 0 (solopreneur): price must be near 0 → base can't cover costs ❌
- n → ∞ (large corp): price should grow slower than n (economies of scale) → linear per_user fee fails ❌

---

## Task: Find the Missing Δ Term

### Step 1: Current Equation
```
Revenue = n (number of users) × p (price per user) + base_fee
```

Boundary conditions:
1. When n → 0, Revenue should approach a minimum viable fee (e.g., $10/month) to cover costs
2. When n → ∞, price per user should decrease (bulk discount), e.g., p ∝ 1/√n

Current linear model: **violates both boundaries**.

### Step 2: Propose a Δ Term

Add a function f(n) that modifies price per user:

```
p_effective(n) = p_base × f(n)
```

with f(1) ≈ 1 (for mid-size), f(n) → ∞? no, **Re-read**:
- n→0: we need minimum fee, so `Revenue(n) = min_fee + (n×p×f(n))`
- n→∞: we need p_eff↓, so f(n)↓

**Better approach**: Use a **network effect multiplier** (similar to Maxwell's displacement current):

```
Revenue = n × p_base × (1 + γ × log(n))  # OR
Revenue = base_fee × (1 + β·n^α) where α<1
```

But also consider **value-based pricing**: Value ≈ usage × network_size

### Step 3: Design Your Boundary-Enhanced Pricing

Propose a formula with parameters that satisfy:
- For n=1: price ≈ $10-30 (MVP)
- For n=1000: price per user ≈ $5-10 (bulk)
- For n=10,000: price per user ≈ $2-5 (enterprise)

Plot Revenue vs n on log-log scale.

---

## Exercise 4: Quality-Cost Trade-off

Product managers constantly say:
- Low cost → quality ↓
- High quality → cost ↑

Is this **inevitable** or can innovation break the trade-off?

Current model: `quality = a - b·cost` (negative correlation)

**Boundary conditions**:
- cost → 0 (free product): quality should approach 0? But some free products have high quality (Freemium) → **contradiction**
- cost → ∞ (unlimited budget): quality approaches asymptote (perfect quality) → **maybe true**

But the real boundary is **switching point** between manual vs automated production.

### Task
Identify a **boundary variable** (like "manufacturing method" or "technology stack") that, if changed, makes the equation change form entirely.

Example: Traditional manufacturing: quality ∝ 1/cost
Digital product (zero marginal cost): quality ↑, cost → 0

**Your challenge**: Find another boundary that shifts the trade-off curve.

---

## Deliverables

For each exercise:

1. **Original equation**: Write the naive model
2. **Boundary violations**: Show which condition fails at which extreme
3. **Δ term proposal**: Your added term with formula
4. **Verification**: Show new equation satisfies boundaries (analytically or with plot)
5. **Business impact**: Estimate revenue increase or cost reduction

---

## Template Answer (Pricing Example)

```yaml
Original: Revenue = 20*n  # $20/user/month

Boundary violations:
- n=1 → Revenue=$20 (maybe okay)
- n=1000 → Revenue=$20,000 (enterprise might pay $5/user instead)
- n=10,000 → Revenue=$200,000 (too expensive, churn)

Proposed Δ: f(n) = n^{-0.3}  (diminishing multiplier)

New formula: Revenue = n × $20 × n^{-0.3} = $20 × n^{0.7}

Check:
- n=1: $20 ✓
- n=1000: $20 × 1000^{0.7} = $20 × 251 ≈ $5,020 ($5/user) ✓
- n=10,000: $20 × 10k^{0.7} = $20 × 1585 ≈ $31,700 ($3/user) ✓

Impact: Enterprise deal 10,000 users → saves $168,300/year vs flat pricing
```

---

🦞 龙虾: "边界上的矛盾，往往是创新的最后藏宝图。顺着它，找到 Δ。"
