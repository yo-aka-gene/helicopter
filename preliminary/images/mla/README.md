
            feature set:
            Index(['(size-1.99)', '(size-1.99)*(size-1.99)',
       '(size-1.99)*(size-1.99)*(size-1.99)'],
      dtype='object')
            
            optimal model:
                                        OLS Regression Results                            
==============================================================================
Dep. Variable:                   time   R-squared:                       0.339
Model:                            OLS   Adj. R-squared:                  0.279
Method:                 Least Squares   F-statistic:                     5.635
Date:                Mon, 18 Oct 2021   Prob (F-statistic):             0.0106
Time:                        18:15:56   Log-Likelihood:                -25.421
No. Observations:                  25   AIC:                             56.84
Df Residuals:                      22   BIC:                             60.50
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       6.2709      0.224     28.040      0.000       5.807       6.735
(size-1.99)                 0.3965      0.204      1.942      0.065      -0.027       0.820
(size-1.99)*(size-1.99)    -0.9450      0.353     -2.678      0.014      -1.677      -0.213
==============================================================================
Omnibus:                        5.001   Durbin-Watson:                   1.759
Prob(Omnibus):                  0.082   Jarque-Bera (JB):                3.442
Skew:                           0.478   Prob(JB):                        0.179
Kurtosis:                       4.546   Cond. No.                         3.15
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            
            