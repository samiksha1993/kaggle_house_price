def clean(train_in):
	median_LotFrontage = train_in['LotFrontage'].dropna().mean()
	if len(train_in.LotFrontage[train_in.LotFrontage.isnull()])>0:
		train_in.LotFrontage[train_in.LotFrontage.isnull()] = median_LotFrontage

	#MasVnrArea
	median_MasVnrArea = train_in['MasVnrArea'].dropna().mean()
	if len(train_in.MasVnrArea[train_in.MasVnrArea.isnull()])>0:
		train_in.MasVnrArea[train_in.MasVnrArea.isnull()]  = median_MasVnrArea
	#Alley
	if len(train_in.Alley[train_in.Alley.isnull()])>0:
		train_in.Alley[train_in.Alley.isnull()] = 'no'

	#Fence
	if len(train_in.Fence[train_in.Fence.isnull()])>0:
		train_in.Fence[train_in.Fence.isnull()] = 'no'

	#MiscFeature
	if len(train_in.MiscFeature[train_in.MiscFeature.isnull()])>0:
		train_in.MiscFeature[train_in.MiscFeature.isnull()] = 'unknown'

	#PoolQC
	if len(train_in.PoolQC[train_in.PoolQC.isnull()])>0:
		train_in.PoolQC[train_in.PoolQC.isnull()] = 'no'

	#GarageQual
	if len(train_in.GarageQual[train_in.GarageQual.isnull()])>0:
		train_in.GarageQual[train_in.GarageQual.isnull()] = 'no'

	#GarageCond
	if len(train_in.GarageCond[train_in.GarageCond.isnull()])>0:
		train_in.GarageCond[train_in.GarageCond.isnull()] = 'no'

	#GarageFinish
	if len(train_in.GarageFinish[train_in.GarageFinish.isnull()])>0:
		train_in.GarageFinish[train_in.GarageFinish.isnull()] = 'no'

	#FireplaceQu
	if len(train_in.FireplaceQu[train_in.FireplaceQu.isnull()])>0:
		train_in.FireplaceQu[train_in.FireplaceQu.isnull()] = 'no'

	#GarageType
	if len(train_in.GarageType[train_in.GarageType.isnull()])>0:
		train_in.GarageType[train_in.GarageType.isnull()] = 'no'

	#GarageCars
	if len(train_in.GarageCars[train_in.GarageCars.isnull()])>0:
		train_in.GarageCars[train_in.GarageCars.isnull()] = 0

	#GarageYrBlt
	if len(train_in.GarageYrBlt[train_in.GarageYrBlt.isnull()])>0:
		train_in.GarageYrBlt[train_in.GarageYrBlt.isnull()] = train_in.YearBuilt

	#BsmtQual
	if len(train_in.BsmtQual[train_in.BsmtQual.isnull()])>0:
		train_in.BsmtQual[train_in.BsmtQual.isnull()] = "no"

	#BsmtCond
	if len(train_in.BsmtCond[train_in.BsmtCond.isnull()])>0:
		train_in.BsmtCond[train_in.BsmtCond.isnull()] = "no"

	#BsmtExposure
	if len(train_in.BsmtExposure[train_in.BsmtExposure.isnull()])>0:
		train_in.BsmtExposure[train_in.BsmtExposure.isnull()] = "no"
		
	#BsmtFinType1
	if len(train_in.BsmtFinType1[train_in.BsmtFinType1.isnull()])>0:
		train_in.BsmtFinType1[train_in.BsmtFinType1.isnull()] = "no"
		
	#BsmtFinType2
	if len(train_in.BsmtFinType2[train_in.BsmtFinType2.isnull()])>0:
		train_in.BsmtFinType2[train_in.BsmtFinType2.isnull()] = "no"

	#Electrical
	if len(train_in.Electrical[train_in.Electrical.isnull()])>0:
		train_in.Electrical[train_in.Electrical.isnull()] = train_in.Electrical.dropna().mode().values

	#SaleType
	if len(train_in.SaleType[train_in.SaleType.isnull()])>0:
		train_in.SaleType[train_in.SaleType.isnull()] = 'Oth'

	#GarageArea
	if len(train_in.GarageArea[train_in.GarageArea.isnull()])>0:
		train_in.GarageArea[train_in.GarageArea.isnull()] = 0

	#KitchenQual
	if len(train_in.KitchenQual[train_in.KitchenQual.isnull()])>0:
		train_in.KitchenQual[train_in.KitchenQual.isnull()] = train_in.KitchenQual.dropna().mode().values

	#BsmtHalfBath
	if len(train_in.BsmtHalfBath[train_in.BsmtHalfBath.isnull()])>0:
		train_in.BsmtHalfBath[train_in.BsmtHalfBath.isnull()] = train_in.BsmtHalfBath.dropna().mode().values

	#BsmtFullBath
	if len(train_in.BsmtFullBath[train_in.BsmtFullBath.isnull()])>0:
		train_in.BsmtFullBath[train_in.BsmtFullBath.isnull()] = train_in.BsmtFullBath.dropna().mode().values

	#Functional
	if len(train_in.Functional[train_in.Functional.isnull()])>0:
		train_in.Functional[train_in.Functional.isnull()] = train_in.Functional.dropna().mode().values

	#MasVnrType
	if len(train_in.MasVnrType[train_in.MasVnrType.isnull()])>0:
		train_in.MasVnrType[train_in.MasVnrType.isnull()] = 'None'

	#Exterior2nd
	if len(train_in.Exterior2nd[train_in.Exterior2nd.isnull()])>0:
		train_in.Exterior2nd[train_in.Exterior2nd.isnull()] = 'Other'

	#Exterior1st
	if len(train_in.Exterior1st[train_in.Exterior1st.isnull()])>0:
		train_in.Exterior1st[train_in.Exterior1st.isnull()] = 'Other'

	#Utilities
	if len(train_in.Utilities[train_in.Utilities.isnull()])>0:
		train_in.Utilities[train_in.Utilities.isnull()] = train_in.Utilities.dropna().mode().values

	#MSZoning
	if len(train_in.MSZoning[train_in.MSZoning.isnull()])>0:
		train_in.MSZoning[train_in.MSZoning.isnull()] = train_in.MSZoning.dropna().mode().values

	#BsmtFinSF2
	if len(train_in.BsmtFinSF2[train_in.BsmtFinSF2.isnull()])>0:
		train_in.BsmtFinSF2[train_in.BsmtFinSF2.isnull()] = train_in.BsmtFinSF2.dropna().median()

	#TotalBsmtSF
	if len(train_in.TotalBsmtSF[train_in.TotalBsmtSF.isnull()])>0:
		train_in.TotalBsmtSF[train_in.TotalBsmtSF.isnull()] = train_in.TotalBsmtSF.dropna().median()

	#BsmtFinSF1
	if len(train_in.BsmtFinSF1[train_in.BsmtFinSF1.isnull()])>0:
		train_in.BsmtFinSF1[train_in.BsmtFinSF1.isnull()] = train_in.BsmtFinSF1.dropna().median()

	#BsmtUnfSF
	if len(train_in.BsmtUnfSF[train_in.BsmtUnfSF.isnull()])>0:
		train_in.BsmtUnfSF[train_in.BsmtUnfSF.isnull()] = train_in.BsmtUnfSF.dropna().median()
	
	return train_in

