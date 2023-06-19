import pandas as pd
from sklearn import preprocessing
# 导入数据
data=pd.read_csv("normalization_data.csv",header=None)

# min-max标准化
#feature_range设置最大最小变换值，默认（0,1）
min_max_normalizer=preprocessing.MinMaxScaler(feature_range=(60,100))
#将数据缩放(映射)到设置固定区间
scaled_data=min_max_normalizer.fit_transform(data)
#将变换后的数据转换为dataframe对象
data_normalized=pd.DataFrame(scaled_data)
print(data_normalized)
# z_score标准化
df=pd.DataFrame(data)
normalizer=preprocessing.scale(df)
normalized=pd.DataFrame(normalizer)
print(normalized)
# sigmod标准化

