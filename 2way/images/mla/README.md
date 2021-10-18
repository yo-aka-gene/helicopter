
            feature set:
            Index(['(size-2.49)', '(n_clip-2.0)', '(size-2.49)*(size-2.49)',
       '(n_clip-2.0)*(n_clip-2.0)', '(size-2.49)*(n_clip-2.0)'],
      dtype='object')
            
            optimal model:
                                        OLS Regression Results                            
==============================================================================
Dep. Variable:                   time   R-squared:                       0.800
Model:                            OLS   Adj. R-squared:                  0.780
Method:                 Least Squares   F-statistic:                     40.00
Date:                Mon, 18 Oct 2021   Prob (F-statistic):           1.78e-13
Time:                        17:54:52   Log-Likelihood:                -34.600
No. Observations:                  45   AIC:                             79.20
Df Residuals:                      40   BIC:                             88.23
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         4.5262      0.185     24.510      0.000       4.153       4.899
(size-2.49)                  -1.3031      0.209     -6.244      0.000      -1.725      -0.881
(n_clip-2.0)                 -0.5160      0.051    -10.209      0.000      -0.618      -0.414
(size-2.49)*(size-2.49)      -2.5425      0.745     -3.412      0.001      -4.049      -1.036
(n_clip-2.0)*(n_clip-2.0)     0.1182      0.044      2.700      0.010       0.030       0.207
==============================================================================
Omnibus:                        0.492   Durbin-Watson:                   2.088
Prob(Omnibus):                  0.782   Jarque-Bera (JB):                0.634
Skew:                          -0.189   Prob(JB):                        0.728
Kurtosis:                       2.558   Cond. No.                         30.8
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            
            