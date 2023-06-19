import math

class NB():
 def __init__(self):
  self.cla_all_num = 0
  self.cla_num = {}
  self.cla_tag_num = {}
  self.landa = 1  # 拉普拉斯修正值

 def train(self, taglist, cla):  # 训练，每次插入一条数据
  # 插入分类
  self.cla_all_num += 1
  if cla in self.cla_num:  # 是否已存在该分类
   self.cla_num[cla] += 1
  else:
   self.cla_num[cla] = 1
  if cla not in self.cla_tag_num:
   self.cla_tag_num[cla] = {}  # 创建每个分类的标签字典
  # 插入标签
  tmp_tags = self.cla_tag_num[cla]  # 浅拷贝，用作别名
  for tag in taglist:
   if tag in tmp_tags:
    tmp_tags[tag] += 1
   else:
    tmp_tags[tag] = 1

 def P_C(self, cla):  # 计算分类 cla 的先验概率
  return self.cla_num[cla] / self.cla_all_num

 def P_all_C(self):  # 计算所有分类的先验概率
  tmpdict = {}
  for key in self.cla_num.keys():
   tmpdict[key] = self.cla_num[key] / self.cla_all_num
  return tmpdict

 def P_W_C(self, tag, cla):  # 计算分类 cla 中标签 tag 的后验概率
  tmp_tags = self.cla_tag_num[cla]  # 浅拷贝，用作别名
  if tag not in self.cla_tag_num[cla]:
   return self.landa / (self.cla_num[cla] + len(tmp_tags) * self.landa)  # 拉普拉斯修正
  return (tmp_tags[tag] + self.landa) / (self.cla_num[cla] + len(tmp_tags) * self.landa)

 def test(self, test_tags):  # 测试
  res = ''
  res_P = None
  for cla in self.cla_num.keys():
   log_P_W_C = 0
  for tag in test_tags:
   log_P_W_C += math.log(self.P_W_C(tag, cla))
   tmp_P = log_P_W_C + math.log(self.P_C(cla))  # P(w|Ci) * P(Ci)
  if res_P is None:
   res = cla
  res_P = tmp_P
  if tmp_P > res_P:
   res = cla
   res_P = tmp_P
  return res

 def set_landa(self, landa):
  self.landa = landa
 def clear(self):  # 重置模型
  self.cla_all_num = 0
  self.cla_num.clear()
  self.cla_tag_num.clear()

if __name__ == '__main__':
    nb = NB()  # 生成模型
    # 训练模型
    # 年龄，收入，是否学生，信用等级  --->  是否买了电脑
    nb.train(['<=30', 'high', 'no', 'fair'], 'no')
    nb.train(['<=30', 'high', 'no', 'excellent'], 'no')
    nb.train(['31…40', 'high', 'no', 'fair'], 'yes')
    nb.train(['>40', 'medium', 'no', 'fair'], 'yes')
    nb.train(['>40', 'low', 'yes', 'fair'], 'yes')
    nb.train(['>40', 'low', 'yes', 'excellent'], 'no')
    nb.train(['31…40', 'low', 'yes', 'excellent'], 'yes')
    nb.train(['<=30', 'medium', 'no', 'fair'], 'no')
    nb.train(['<=30', 'low', 'yes', 'fair'], 'yes')
    nb.train(['>40', 'medium', 'yes', 'fair'], 'yes')
    nb.train(['<=30', 'medium', 'yes', 'excellent'], 'yes')
    nb.train(['31…40', 'medium', 'no', 'excellent '], 'yes')
    nb.train(['31…40', 'high', 'yes', 'fair'], 'yes')
    nb.train(['>40', 'medium', 'no', 'excellent'], 'no')


testdata = ['<=30', 'medium', 'yes', 'fair']
print('测试结果：', nb.test(testdata))