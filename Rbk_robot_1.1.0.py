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
      md= input('请选择模式:1.训练；2.聊天[退出输入q]')
      if md in  ['q','Q','Quit','quit']:
        print('%s:再见！'%rbt)
        break
      elif md in [1,'1',1.]:
        print('欢迎进入训练模式')
        self.update_data(name,self.train(d,rbt,name))
      elif md in [2,'2','2.']:
        print('欢迎进入聊天模式!')
        self.update_data(name,self.chat(d,rbt,name))
      else:
        print('输入有误，请重新选择！')
        
  def chat(self,dic,rbt,name):
    while True:
      q=input('%s:[退出输入q]'%name)
      if q in ['q','Q','Quit','quit']:
        print('%s: 再见！'%rbt)
        break
      fb_pool=dic['pool']
      answer=self.find_answer(fb_pool,q)
      print('%s: %s'%(rbt,answer))
      dic['history'].append([q,answer])
    return dic
    
  def find_answer(self,fb_pool,qizz):
    ans_list=[] # minimum 1 subject matched
    ans_dic={} #>=2 subjects mathced 
    for ea in fb_pool:
        if (ea[0] in qizz):
          ans_list.append(ea[2])
    if ans_list ==[]:
      answer='我还不懂，请主人多教教我！'
    else:
      for ea in ans_list:
        if ea in ans_dic.keys():
          ans_dic[ea] += 1
        else:
          ans_dic[ea]=1
      i=0
      dic_li=[]
      ans_dic2=ans_dic.copy()
      while ans_dic2 !={} and i<3:
        ans=max(ans_dic2,key=ans_dic2.get)
        if i >=1 and ans_dic[dic_li[i-1]] > ans_dic[ans]:
        #when 2nd largest item got, make comparison
          break
        dic_li.append(ans)
        ans_dic2.pop(ans)
        i+=1
      answer=random.choice(dic_li)
      print('answer related to %s subjects'%ans_dic[answer])
    return answer
      
  def train(self,dic,rbt,name):
    while True:
      print('--训练中--')
      qizz=input('%s:请输入一句话:\n%s:'%(rbt,name))
      sbj=input('%s:这句话的主题:[多个主题用逗号隔开]\n%s:'%(rbt,name))
      sbj=sbj.strip()
      sbj=sbj.replace('，',',')
      sbj_list = sbj.split(',')
      answer = input('%s: 请输入答案:\n%s:'%(rbt,name))
      for ea in sbj_list:
        dic['pool'].append([ea,qizz,answer])
      conti = input('%s:是否继续？[y/n]\n%s:'%(rbt,name))
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
fo = open('rbk_robot.pkl','rb')
data2 = pickle.load(fo)
fo.close()
