#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


a=pd.read_excel(r'C:\Users\HP\Downloads\Attribute DataSet (1).xlsx')


# In[6]:


a[5:20]


# In[7]:


a


# In[12]:


b=pd.read_excel(r'C:\Users\HP\Downloads\Attribute DataSet (1).xlsx',sheet_name='pavan')


# In[13]:


b


# In[14]:


type(a)


# In[15]:


type(b)


# In[16]:


c=pd.read_excel(r'C:\Users\HP\Downloads\Attribute DataSet (1).xlsx',sheet_name='pavan',header=None,names=['A','B','C'])


# In[17]:


c


# In[18]:


a.head()


# In[19]:


a.tail()


# In[21]:


a.head(10)


# In[22]:


a.tail(10)


# In[40]:


d=pd.read_csv(r'C:\Users\HP\Downloads\haberman.csv',header=None,names=['A','B','C','D'])


# In[ ]:





# In[42]:


d


# In[45]:


e=pd.read_csv(r'C:\Users\HP\Downloads\haberman.csv',sep='@')


# In[46]:


e


# In[47]:


d


# In[48]:


f=pd.read_csv(r'C:\Users\HP\Downloads\haberman.csv',sep=",")


# In[49]:


f


# In[51]:


g=pd.read_csv(r'https://raw.githubusercontent.com/selva86/datasets/master/HouseVotes84.csv')


# In[52]:


g


# In[53]:


# the above is how to view github repositery data set in my system with out downloading#


# In[56]:


h=pd.read_html(r'https://www.basketball-reference.com/leagues/NBA_2015_totals.html')


# In[57]:


h


# In[55]:


# how to read html page data without dowNloading#


# In[58]:


type(h)


# In[59]:


len(h)


# In[62]:


h[0]


# In[64]:


js=pd.read_json('https://api.github.com/repos/pandas-dev/pandas/issues')


# In[74]:


js


# In[66]:


js.columns


# In[70]:


js['user']


# In[71]:


a


# In[72]:


a.to_json('test.json')


# In[73]:


pwd


# In[75]:


# in pandas we can convert any file to another type of file#


# In[80]:


a.to_csv('T1.csv',sep='#')


# In[81]:


pwd


# In[82]:


ysql:
    1.Create a table attribute daset and dress dataset
    2.Do a bulk load for these two table for respective dataset
    3.read these dataset in pandas as a dataframe
    4.convert attribute dataset in json format
    5.Store this dataset into mongodb
    6.in sql task try to perform left join operation with attribute and dress data sets on clumns
    7.Write a sql query to fcind out how many unique dress based on drtess id
    8.try to find out how many dresses having recomendation zero
    9.try to find out third highest most selling dress id
    10.
    


# In[83]:


a


# In[84]:


type(a['Style'])


# In[85]:


a.dtypes


# In[86]:


a['Dress_ID','Price']


# In[92]:


l1=a[['Dress_ID','Price']]


# In[93]:


l1


# In[94]:


type(l1)


# In[95]:


l2=a[['Price']]


# In[96]:


l2


# In[97]:


type(l2)


# In[98]:


a.describe()


# In[99]:


type(a)


# In[110]:


p=a[a.dtypes[a.dtypes=='float64'].index]


# In[111]:


p


# In[113]:


p.describe()


# In[115]:


q=a[a.dtypes[a.dtypes=='object'].index]


# In[116]:


q


# In[117]:


q.describe()


# In[120]:


a['Style'][1:5]


# In[122]:


a['pavan']='kumar'


# In[124]:


a['pavan']


# In[125]:


a.columns


# In[128]:


a['Style'].isnull()


# In[129]:


a['pavan'][1:10].isnull()


# In[134]:


d['A'][1:5].isnull()


# In[136]:


ds=pd.read_excel(r'C:\Users\HP\Downloads\Dress sales.xlsx')


# In[137]:


ds


# In[143]:


ds.columns


# In[144]:


a.columns


# In[152]:


a[a['Rating']<4.0][0:10]


# In[154]:


a[a['Rating']<3.0]['Style'][0:10]


# In[159]:


a[(a['Style']=='Casual')&(a['Rating']<3)&(a['Season']=='Summer')]['Size']


# In[160]:


ds


# In[161]:


gh=pd.read_csv(r'https://raw.githubusercontent.com/selva86/datasets/master/df_final.csv')


# In[162]:


gh


# In[163]:


gh.columns


# In[164]:


gh.dtypes


# In[165]:


# convert date from 'object' to 'datetime64'#


# In[166]:


pd.to_datetime(gh['Date'])


# In[167]:


gh['converted date order']=pd.to_datetime(gh['Date'])


# In[168]:


gh.columns


# In[169]:


gh


# In[170]:


gh['order date year']=gh['converted date order'].dt.year


# In[172]:


gh.head()


# In[176]:


gh['order date week']=gh['converted date order'].dt.weekofyear


# In[177]:


gh.head()


# In[191]:


gh[(gh['order date year']==2019)&(gh['order date week']>25)].head()


# In[193]:


gh[gh['Annual.GDP.Growth']==max(gh['Annual.GDP.Growth'])]['order date week']


# In[197]:


gh[122:127]


# In[198]:


gh['order date week'].value_counts()


# In[200]:


# the above is to get the groups#


# In[202]:


gh.head()


# In[204]:


gh['new addition']=gh['Annual.GDP.Growth']+gh['Last_inflation']


# In[205]:


gh.head()


# In[206]:


a.columns


# In[208]:


a.drop('pavan')


# In[210]:


a.drop('pavan',axis=1).head()


# In[211]:


# for deleting perticular column use axis=1 and for a row axis=0)


# In[222]:


a=a.drop('Style',axis=1,inplace=True)


# In[214]:


# to save all changes again assign that to same name  #
           #or#
    # use following method#


# In[228]:


a.drop('Season',axis=1,inplace=True)


# In[230]:


a.columns


# In[234]:


a.loc[[2,3]]


# In[232]:


a[2:4]


# In[240]:


a.loc[1:10:1]


# In[242]:


gh.loc[1:10:2]


# In[244]:


gh.loc[5:10]


# In[246]:


gh.loc[0:4,['Country','Date']]


# In[258]:


gh.iloc[0:5,0:6:2]


# In[250]:


# iloc is similar to slicing#


# In[257]:


gh.iloc[0:4,0:3:2]


# In[259]:


gh.head()


# In[260]:


gh[gh['Last_inflation']>50.0]


# In[265]:


gh1=gh[(gh['Last_inflation']<1.0)|(gh['Last_inflation']>50.0)]


# In[266]:


gh1


# In[275]:


gh1.dropna(axis=0)


# In[276]:


gh1.dropna(axis=1)


# In[277]:


gh.head()


# In[278]:


gh.drop('Country',axis=1)


# In[279]:


gh.drop(1,axis=0)


# In[281]:


a.dropna(thresh=5)


# In[282]:


## the above meaning of thresh is if u have less than 5 nan values it will drop those rows


# In[284]:


gh.fillna(value=4)


# In[285]:


a.fillna(value=4)


# In[290]:


a.fillna(value=10)


# In[293]:


gh.groupby('order date week')['Last_inflation'].mean()


# In[299]:


# above is group by average of last_inflation weekly$$


# In[300]:


gh.groupby('order date week')['Annual.GDP.Growth'].mean()


# In[306]:


gh.Last_inflation.astype('float64')[1:16]


# In[313]:


gh.Last_inflation.float64.replace('.','2').astype(int)


# In[314]:


gh.groupby['order date week']['Last_inflation'].sum()


# In[316]:


data={'name':['sudh','krish','hitesh','telusko'],
     'salary':[100,200,300,400],
     'mail_id':['sudh@ineuron.ai','krish@ineuron.ai','hitesh@ineuron.ai','telusko@ineuron.ai'],
      'addr':['blr','blr','blr','mum']}


# In[322]:


cp=pd.DataFrame(data)


# In[328]:


cp1=pd.DataFrame(data,index=[30,31,32,34])


# In[325]:


cp


# In[329]:


cp1.iloc[0:3]


# In[335]:


cp1.loc[[0,3]]


# In[332]:


cp1.loc[31:34]


# In[333]:


cp1.loc[[31,32]]


# In[340]:


data1={'pf_no':[234,25,252,345],
       'income_tax':[245,56,458,5554],
       'mobile_no':[756546465,546546454,5246566785,7585465456],
       'courses':['ds','fs','ms','dd']}


# In[343]:


cps=pd.DataFrame(data1)


# In[344]:


cps


# In[345]:


cp


# In[346]:


pd.concat([cp,cps])


# In[347]:


# the above is for horizontal addition of data(when column names are different#


# In[367]:


df=pd.concat([cp,cps],axis=1)


# In[368]:


df


# In[352]:


# vertical addition of data (when column names are different)#


# In[353]:


data2={'0':[234,25,252,345],
       '1':[245,56,458,5554],
       '2':[756546465,546546454,5246566785,7585465456],
       '3':['ds','fs','ms','dd']}


# In[355]:


data3={'0':['sudh','krish','hitesh','telusko'],
     '1':[100,200,300,400],
     '2':['sudh@ineuron.ai','krish@ineuron.ai','hitesh@ineuron.ai','telusko@ineuron.ai'],
      '3':['blr','blr','blr','mum']}


# In[358]:


cpd=pd.DataFrame(data2)


# In[359]:


cpd


# In[360]:


cpd1=pd.DataFrame(data3)


# In[361]:


cpd1


# In[362]:


pd.concat([cpd,cpd1])


# In[364]:


# in the above it is row addition which columns index are same in both dataframes#


# In[365]:


pd.concat([cpd,cpd1],axis=1)


# In[366]:


# inthe above case it is column addition and also row index are same#


# In[369]:


df


# In[373]:


df[['name','mail_id']]


# In[374]:


df[df['name']=='sudh']['mail_id']


# In[375]:


cp


# In[377]:


df


# In[378]:


pd.merge(cp,df)


# In[379]:


pd.merge(cp,cps)


# In[380]:


data5={'pf_no':[234,25,252,444],
       'income_tax':[245,56,458,5554],
       'mobile_no':[756546465,546546454,5246566785,7585465456],
       'courses':['ds','fs','ms','df']}


# In[381]:


df1=pd.DataFrame(data5)


# In[382]:


pd.merge(df,df1)


# In[383]:


# merge operation will give the common rows with all columns  from the both of the dataframes#


# In[384]:


pd.merge(df,df1,'left')


# In[385]:


pd.merge(df,df1,'right')


# In[386]:


pd.merge(df,df1,'inner')


# In[387]:


## inner merge and merge both are same#


# In[388]:


pd.merge(df,df1,'outer')


# In[389]:


# outer merge gives common plus distinct data#


# In[390]:


data6={'pf_no1':[234,25,252,444],
       'income_tax1':[245,56,458,5554]}
data7={'pf_no2':[234,25,252,444],
       'mobile_no':[756546465,546546454,5246566785,7585465456],
       'courses':['ds','fs','ms','df']}


# In[391]:


df3=pd.DataFrame(data6)


# In[392]:


df3


# In[395]:


df4=pd.DataFrame(data7)


# In[396]:


df4


# In[414]:


pd.merge(df3,df4,left_on='pf_no1',right_on='pf_no2',how='inner')


# In[415]:


## the above is simillar to column addition##


# In[400]:


data8={'pf_no':[234,25,2534,444],
       'income_tax':[245,56,458,5554],
       'mobile_no':[756546465,546546454,5246566785,7585465456],
       'courses':['ds','fs','ms','df']}
data9={'pf_no':[234,25,2522,444],
       'income_tax':[245,562,458,5554],
       'mobile_no':[756546465,5456546454,5246566785,7585465456],
       'courses':['ds','fs','ms','df']}


# In[402]:


df6=pd.DataFrame(data8)


# In[404]:


df6


# In[405]:


df7=pd.DataFrame(data9)


# In[406]:


df7


# In[412]:


pd.merge(df6,df7,on=['pf_no','income_tax','mobile_no'])


# In[413]:


# above is to merge those data when 3 of the conditions are satisfied"


# In[436]:


def mobnumber(a):
    b=str(a)
    if len(b)==10:
        return 'correct'
    else:
        return 'wrong number'
  


# In[437]:


mobnumber(10000)


# In[438]:


df7['mob number verify']=df7['mobile_no'].apply(mobnumber)


# In[439]:


df7


# In[440]:


## in the above we did the operation using user defined function##


# In[441]:


a


# In[442]:


def fashion(a):
    if a=='o-neck':
        return 'old-fashion'
    else:
        return 'new-fashion'


# In[444]:


a['Neck_line_fashion']=a['NeckLine'].apply(fashion)


# In[446]:


a.tail()


# In[456]:


## numpy class###


# In[457]:


import numpy as np


# In[458]:


np.array([2,3,4,5])


# In[459]:


fh=np.array([1,2,3,40],ndmin=5)


# In[460]:


fh


# In[461]:


fh1=np.array([[[1,2,3],[2,3,4]]])


# In[462]:


fh1.ndim


# In[ ]:




