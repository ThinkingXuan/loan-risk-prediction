# loan-risk-prediction
💖基于机器学习的贷中风险预测模型--江苏银行“随e融”杯--二等奖💖

- 项目背景

  网贷业务中，一个客户的工作或者生活情况的变化往往会对客户产生较大影响，一些负面因素可能导致一个优质客户转变为高风险客户，准确的在贷中场景中识别风险概率变化较大的客户，可以有效的进行防范并降低损失。在实际中，描述一个客户的数据维度复杂且多元，我们需要从万千数据中挖掘，寻找那些可以体现客户风险的特征维度，因此需要引入机器学习模型，通过不同的算法进行大量的运算以确定客户的风险变化情况。

- 赛题理解

  题目中的贷中客户分为三种情况：普通贷款，授信，贷中再申请贷款。这是一个贷中风险控制的评分卡建模过程（二分类问题）,数据分为五张表，由cust_id进行关联，但并不是每个客户都存在五张表，例如贷款中客户授信信息表，贷中客户申请表，贷中客户申请的缺失值考虑直接补0，授信这种缺失值有其实际意义，考虑进行分箱。 

  由于该二分类中存在类不平衡问题，我们考虑建立以XGBoost、LightGBM、CatBoost为第一层基模型,逻辑回归为第二模型的Stacking融合模型，为此期待达到更高的模型效果。

- 核心技术
	数据预处理，决策树分箱，XGBoost、LightGBM、CatBoost算法，模型融合Stacking
	
- 方案步骤

  1. 赛题理解

     ![图片1](C:\Users\youxuan\Pictures\图片1.png)

  2. 数据探索性分析

  3. 数据清洗（数据预处理）

  4. 特征工程

  5. 模型训练

  6. 模型验证

  7. 模型预测

