
            feature set:
            Index(['(pod-8.0)', '(body-2.0)', '(wing-10.0)', '(width-6.0)',
       '(thickness-3.0)', '(fixation-0.0)', '(thread-0.0)', '(shape-0.0)',
       '(pod-8.0)*(pod-8.0)', '(body-2.0)*(body-2.0)',
       '(wing-10.0)*(wing-10.0)', '(width-6.0)*(width-6.0)',
       '(thickness-3.0)*(thickness-3.0)'],
      dtype='object')
            
            optimal model:
                                        OLS Regression Results                            
==============================================================================
Dep. Variable:                   time   R-squared:                       0.577
Model:                            OLS   Adj. R-squared:                  0.478
Method:                 Least Squares   F-statistic:                     5.808
Date:                Mon, 18 Oct 2021   Prob (F-statistic):            0.00390
Time:                        17:51:10   Log-Likelihood:                -32.245
No. Observations:                  22   AIC:                             74.49
Df Residuals:                      17   BIC:                             79.94
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       6.5540      0.596     10.996      0.000       5.297       7.811
(wing-10.0)                -0.1044      0.057     -1.837      0.084      -0.224       0.016
(thread-0.0)                0.4918      0.257      1.915      0.072      -0.050       1.034
(shape-0.0)                -0.6160      0.257     -2.399      0.028      -1.158      -0.074
(wing-10.0)*(wing-10.0)    -0.0937      0.026     -3.556      0.002      -0.149      -0.038
==============================================================================
Omnibus:                        7.436   Durbin-Watson:                   1.385
Prob(Omnibus):                  0.024   Jarque-Bera (JB):                5.040
Skew:                           0.974   Prob(JB):                       0.0804
Kurtosis:                       4.304   Cond. No.                         53.1
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            
            