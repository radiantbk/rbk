import pickle
import os
import random

class robot():
  def __init__(self,name,data):
    self.name =name
    self.data = data
    
  def __getstate__(self):
    return self.data
		
  def __setstate__(self,data):
    self.data = data
  
  def search_name(self,name):
    for i,d in enumerate(self.data):
      if d['name']==name:
        return i,d
  def update_data(self,name,dic):
    for x,ea in enumerate(self.data):
        if ea['name']==name:
          self.data[x]=dic
          return
    
  def main_loop(self):
    rbt = self.name
    print('—-欢迎来找%s—-'%rbt)
    name = input('请输入你的名字:')
    if not self.search_name(name):
      print('%s: %s,很高兴认识你！'%(rbt,name))
      d={'name':name,'pool':[],'history':[]}
      self.data.append(d)
    else:
      print('%s: %s，很高兴又遇见你！'%(rbt,name))
      k,d= self.search_name(name)
    while True:
      md= input('请输入模式:1.训练；2.聊天[退出输入q]')
      if md in  ['q','Q','Quit','quit']:
        print('%s:再见！'%rbt)
        break
      elif md in [1,'1',1.]:
        print('欢迎进入训练模式')
        self.update_data(name,self.train(d,rbt))
      elif md in [2,'2','2.']:
        print('欢迎进入聊天模式!')
        self.update_data(name,self.chat(d,rbt))
      else:
        print('输入有误，请重新选择！')
        
  def chat(self,dic,rbt):
    while True:
      q=input('请输入内容:[退出输入q]')
      if q in ['q','Q','Quit','quit']:
        print('%s: 再见！'%rbt)
        break
      fb=dic['pool']
      ans_list=[]
      for ea in fb:
        if ea[0] in q:
          ans_list.append(ea[2])
      if ans_list ==[]:
        print('%s: 我还不懂，请主人多教教我！'%rbt)
      else:
        answer = random.choice(ans_list)
        print(answer)
        dic['history'].append([q,answer])
    return dic
  def train(self,dic,rbt):
    while True:
      print('--训练中--')
      qizz=input('请输入一句话:')
      sbj=input('请输入这句话的主题:[多个主题用逗号隔开]')
      sbj=sbj.replace('，',',')
      sbj_list = sbj.split(',')
      answer = input('请输入答案')
      for ea in sbj_list:
        dic['pool'].append([ea,qizz,answer])
      conti = input('是否继续？[y/n]')
      if conti in ['y','Y','Yes','yes']:
        print('%s: 好的，我们再来@@'%rbt)
      elif conti in ['n','no','No','N']:
        print('%s: 太好了，可以休息一下咯。'%rbt)
        return dic
      else:
        print('%s: 不说就是继续咯喽...'%rbt)
try:
  fo=open('rbk_robot.pkl','rb')
  data = pickle.load(fo)
  fo.close()
except:
  data =[]
obj=robot('小R',data)
obj.main_loop()
fw = open('rbk_robot.pkl','wb')
pickle.dump(obj.data,fw)
fw.close()
