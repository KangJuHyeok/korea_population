import pandas as pd
import numpy as np
import webbrowser
import folium
import csv
import matplotlib.pyplot as plt
from sklearn import linear_model

def read_data():
    f = open('age_gender_2022.csv')
    data = csv.reader(f)
    for row in data:
        if name in row[0]:
            for i in row[3:104]:
                male.append(-int(i.replace(',',''))) #남성은 인구 수 -로
            for i in row[106:]:
                female.append(int(i.replace(',','')))
            break

             
            

if __name__ == '__main__':
    
      with open('WGS84.json', 'rt', encoding='UTF-8') as f:
         f = f.read()
      state_geo = f
      state_unemployment = 'age.csv'
      state_data = pd.read_csv(state_unemployment, encoding = 'euc-kr')
      state_data.columns = ['Code', 'Population']
      state_data['Code'] = state_data.Code.map(lambda x : str(x).zfill(5))
      state_data.head(1)
      
      
      
      
      m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
      
      
      m.choropleth(
          geo_data=state_geo,
          name='choropleth',
          data=state_data,
          columns=['Code', 'Population'],
          key_on='feature.properties.SIG_CD',
          fill_color='YlGn',
          fill_opacity=0.7,
          line_opacity=0.5,
          legend_name='Population Rate (%)'
          )
      
      folium.LayerControl().add_to(m)
      
     
      m.save('folium_kr.html')
      webbrowser.open_new("folium_kr.html")
    
    
    
    
    
      male = []
      female = []
      age_tmp=[]
      gap=[]
      name=input('인구 피라미드를 구하고 싶은 지역의 이름(ex.서울특별시)을 입력하세요 : ')#전국/서울특별시/제주특별자치도/전국팔도/광역시
      read_data()
      plt.rcParams['font.family'] ='Malgun Gothic' #한글깨짐 방지 한글폰트로 설정
      plt.rcParams['axes.unicode_minus']=False #마이너스 부호 깨짐 방지
      plt.style.use('ggplot') #격자그래프
      plt.figure(figsize=(8,15), dpi=150) #그림사이즈 8,15 /해상도 150
      plt.title('{}의 인구 피라미드'.format(name))
      plt.xlabel('인구 수')
      plt.ylabel('연령')
      plt.yticks(range(101))
      plt.barh(range(101),male,label='남성')
      plt.barh(range(101),female,label='여성')
      plt.legend()
      plt.show()
      
      
      for i in range(101):
          age_tmp.append(i)
          male[i]=-male[i]
          
      y_range=max(max(male),max(female))+10000
      plt.title('{}의 인구 산점도'.format(name))    
      plt.scatter(age_tmp,male,color='red',s=10,label='남성')
      plt.scatter(age_tmp,female,color='blue',marker='+',label='여성')
      plt.legend()
      plt.grid()
      plt.xlim([0,101])
      plt.ylim([0,y_range])
      plt.xlabel('나이')
      plt.ylabel('인구 수')
      plt.show()
      
      
      for i in range(101):
          gap.append(male[i]-female[i])
      
      arr=np.stack((age_tmp,gap),axis=1)
      x=[arr[i][0] for i in range(len(arr))]
      y=[arr[i][1] for i in range(len(arr))]
      
        
      y_range2=max(max(gap),-min(gap))+100
      
      x6=[[x[k]**n for n in range(1,5)] for k in range(len(arr))]
      reg6 = linear_model.LinearRegression()
      reg6.fit(x6,y)
      
      xp6 = [0.1*k for k in range(3000)]
      Xp6 = [[xp6[k]**n for n in range(1,5)] for k in range(3000)]
      yp6 = reg6.predict(Xp6)
      
      plt.title('{}의 남녀 인구 수 차이 추세선'.format(name))    
      plt.legend()
      plt.grid()
      plt.xlim([0,105])
      plt.ylim([-y_range2,y_range2])
      plt.xlabel('나이')
      plt.ylabel('남자 인구 수 - 여자 인구 수')
      plt.scatter(x,y,color='red',s=10,label='남녀 인구 수 차이')
      plt.plot(xp6, yp6)
      plt.show()
      
      
      
      
      
     
        

      
     
   
    