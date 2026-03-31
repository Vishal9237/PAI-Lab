from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Income_Stability': ['Stable', 'Stable', 'Unstable', 'Stable', 'Unstable', 'Unstable', 'Stable', 'Stable'],
    'Credit_History': ['Good', 'Poor', 'Good', 'Average', 'Poor', 'Poor', 'Good', 'Average'],
    'Employment_Type': ['Salaried', 'Self-employed', 'Salaried', 'Self-employed', 'Unemployed', 'Salaried', 'Salaried', 'Self-employed'],
    'Default_Risk': ['Low', 'High', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Medium']
})

model = DiscreteBayesianNetwork([
    ('Income_Stability', 'Default_Risk'),
    ('Credit_History', 'Default_Risk'),
    ('Employment_Type', 'Default_Risk')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)
inference = VariableElimination(model)

result = inference.query(
    variables=['Default_Risk'],
    evidence={'Credit_History': 'Poor', 'Employment_Type': 'Self-employed'}
)
print(result)
