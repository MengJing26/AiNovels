# Exercise 2.1: Logistic Growth Fitting

## Background
Many adoption curves follow Logistic growth:

dU/dt = α · U · (1 - U/K)

where:
- U(t) = number of users at time t
- α = intrinsic growth rate
- K = carrying capacity (market saturation)
- Analytical solution: U(t) = K / (1 + ((K - U₀)/U₀) · e^{-αt})

---

## Exercise

Given monthly active user (MAU) data for a SaaS product:

| Month (t) | MAU (U) |
|-----------|---------|
| 0 (launch) | 1,200   |
| 3         | 4,500   |
| 6         | 12,000  |
| 9         | 22,000  |
| 12        | 32,000  |

### Task 1: Parameter Estimation
Use nonlinear least squares to estimate α and K.

**Hints**:
- Python: `scipy.optimize.curve_fit`
- Provide initial guesses: α=0.1, K=50000, U0=1200

### Task 2: Forecast
Predict MAU at:
- t = 18 months (1.5 years)
- t = 24 months (2 years)
- t = 36 months (3 years)

### Task 3: Balance Point
What is the theoretical saturation point K? Is it stable?

### Task 4: Growth Strategy
If you want to reach 50,000 MAU faster, what levers can you adjust in the equation?
- Increase α (growth rate) → how?
- Increase K (market size) → how?

---

## Deliverables

1. Print fitted parameters: α = ?, K = ?, U₀ = ?
2. Forecast table
3. Stability analysis (why K is stable equilibrium)
4. 2-3 actionable growth strategies based on model

---

## Template Code (Python)

```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def logistic(t, alpha, K, U0):
    return K / (1 + (K/U0 - 1) * np.exp(-alpha * t))

# Data
t_data = np.array([0, 3, 6, 9, 12])
U_data = np.array([1200, 4500, 12000, 22000, 32000])

# Fit
popt, _ = curve_fit(logistic, t_data, U_data, p0=[0.1, 50000, 1200])
alpha, K, U0 = popt
print(f"α={alpha:.4f}, K={K:.0f}, U0={U0:.0f}")

# Forecast
t_future = np.array([18, 24, 36])
U_pred = logistic(t_future, *popt)
for t, u in zip(t_future, U_pred):
    print(f"Month {t}: {u:,.0f} MAU")

# Plot
t_all = np.linspace(0, 36, 100)
U_all = logistic(t_all, *popt)
plt.plot(t_all, U_all, label='Logistic Fit')
plt.scatter(t_data, U_data, color='red', label='Actual')
plt.xlabel('Month')
plt.ylabel('MAU')
plt.legend()
plt.show()
```

---

## Bonus: Multi-product System

If you have 2 products A and B with coupled growth:

dA/dt = α_A · A · (1 - (A+βB)/K_A)
dB/dt = α_B · B · (1 - (B+γA)/K_B)

where β,γ are cross-competition coefficients.

Interpret: if A and B compete for same users (β,γ > 0), how does equilibrium change?

---

🦞 龙虾: "增长不是指数爆炸，而是S型曲线。知道饱和点 K，才有清晰战略。"
