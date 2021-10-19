
            feature set:
            Index(['(size-1.99)', '(batch-3.0)', '(size-1.99)*(size-1.99)',
       '(batch-3.0)*(batch-3.0)', '(size-1.99)*(size-1.99)*(size-1.99)',
       '(batch-3.0)*(batch-3.0)*(batch-3.0)', '(size-1.99)*(batch-3.0)'],
      dtype='object')
            
            optimal model:
                                        OLS Regression Results                            
==============================================================================
Dep. Variable:                   time   R-squared:                       0.460
Model:                            OLS   Adj. R-squared:                  0.411
Method:                 Least Squares   F-statistic:                     9.372
Date:                Tue, 19 Oct 2021   Prob (F-statistic):            0.00114
Time:                        04:07:20   Log-Likelihood:                -22.888
No. Observations:                  25   AIC:                             51.78
Df Residuals:                      22   BIC:                             55.43
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       5.6196      0.294     19.095      0.000       5.009       6.230
(size-1.99)*(size-1.99)    -0.9487      0.319     -2.976      0.007      -1.610      -0.288
(size-1.99)*(batch-3.0)     0.1092      0.035      3.092      0.005       0.036       0.182
==============================================================================
Omnibus:                        0.438   Durbin-Watson:                   2.168
Prob(Omnibus):                  0.803   Jarque-Bera (JB):                0.184
Skew:                           0.205   Prob(JB):                        0.912
Kurtosis:                       2.911   Cond. No.                         20.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            
            