# Regression with the Ames Housing Data

---

## Premise: 
I have just joined a new "full stack" real estate company in Ames, Iowa. The strategy of the firm is two-fold:
- Own the entire process from the purchase of the land all the way to sale of the house, and anything in between.
- Use statistical analysis to optimize investment and maximize return.

The company is still small, and though investment is substantial the short-term goals of the company are more oriented towards purchasing existing houses and flipping them as opposed to constructing entirely new houses. That being said, the company has access to a large construction workforce operating at rock-bottom prices.

This project uses the [Ames housing data recently made available on kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

## Data:
The full description of the data features can be found in a separate file:

    housing.csv
    data_description.txt

## Objective:
1. Develop an algorithm to estimate the value of the residential homes based on fixed characteristics (those that are not considered easy to renovate).
2. Identify characteristics of homes that the company can cost-effectively change/renovate with their construction team.
3. Evaluate the mean dollar value impact on SalePrice of different renovations.

Use the information to buy homes that are likely to sell for more than the initial purchase.

## Process:
1. Perform any cleaning, feature engineering, and EDA you deem necessary.
- Be sure to remove any houses that are not residential from the dataset.
- Identify **fixed** features that can predict price.
- Train a model on pre-2010 data and evaluate its performance on the 2010 houses.
- Characterize and evaluate the model. (How does it perform and what are the best estimates of price?)

## Citations:
- http://www.remodeling.hw.net/cost-vs-value/2010/west-north-central/des-moines-ia/
- http://cdnassets.hw.net/b6/3d/047accdd4174a4965051631d7900/cvv-2010-2011-professional-desmoinesia.pdf

## Findings:
**Fixed Features that were better predictors of SalePrice:**
While there were a total of 47 final features, I decided to look only at feature importances of > 0.0125, which is summarized in the table at the end of in Part03A. Based on the output, and ignoring the dummies aspect of certain categorical features, the following appear to be the best predictors of price:
    - Whether the home has a 2nd floor (`2ndFlrSF`, `1stFlrSF`)
    - The residential zoning (`MSZoning_RM`, which indicates medium density)
    - Basements (BsmtUnfSF, BsmtFinSF1, TotalBsmtSF),
    - Year Built (how old the construction is)
    - Lot Frontage and Lot Area,
    - Above grade living area (GrLivArea)
    
**Renovatable Features that were better predictors of SalePrice (ipynb Part03-B):**
- Room improvements 
- Kitchen Quality improvements
- Basement renovations
- Heating renovations
- Garage features
