import numpy as np
import pandas as pd

np.random.seed(42)

n_users = 5000

data = pd.DataFrame({
    "user_id": range(n_users),
    "income_mean": np.random.gamma(5, 200, n_users),
    "income_std": np.random.gamma(2, 50, n_users),
    "current_debt": np.random.gamma(3, 300, n_users),
    "past_defaults": np.random.binomial(3, 0.2, n_users),
    "tx_volume": np.random.poisson(30, n_users),
    "acceptance_history": np.random.beta(2, 5, n_users),
    "repayment_history": np.random.beta(5, 2, n_users),
})

data.to_csv("synthetic_users.csv", index=False)
print("Generated synthetic_users.csv")
