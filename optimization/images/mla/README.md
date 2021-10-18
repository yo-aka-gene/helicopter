
            feature set:
            Index(['(width-6.0)', '(length-10.0)', '(width-6.0)*(width-6.0)',
       '(length-10.0)*(length-10.0)', '(width-6.0)*(length-10.0)'],
      dtype='object')
            
            optimal model:
                                        OLS Regression Results                            
==============================================================================
Dep. Variable:                   time   R-squared:                       0.781
Model:                            OLS   Adj. R-squared:                  0.752
Method:                 Least Squares   F-statistic:                     27.29
Date:                Mon, 18 Oct 2021   Prob (F-statistic):           9.33e-08
Time:                        17:58:50   Log-Likelihood:                -12.041
No. Observations:                  27   AIC:                             32.08
Df Residuals:                      23   BIC:                             37.27
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===============================================================================================
                                  coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------------
const                           9.0957      0.253     35.960      0.000       8.572       9.619
(width-6.0)*(width-6.0)        -0.1497      0.042     -3.582      0.002      -0.236      -0.063
(length-10.0)*(length-10.0)     0.0176      0.010      1.681      0.106      -0.004       0.039
(width-6.0)*(length-10.0)      -0.0246      0.003     -8.137      0.000      -0.031      -0.018
==============================================================================
Omnibus:                        0.218   Durbin-Watson:                   2.553
Prob(Omnibus):                  0.897   Jarque-Bera (JB):                0.391
Skew:                          -0.161   Prob(JB):                        0.823
Kurtosis:                       2.506   Cond. No.                         213.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            
            