import pickle
from kafka import KafkaProducer
import json
import datetime
import pandas as pd
from time import sleep



def data_to_kafka(nb_patient=10,n=2): 
                                                       

        #create kafka producer
    producer = KafkaProducer(bootstrap_servers= 'localhost:9092',
                       value_serializer=lambda v: json.dumps(v).encode('utf-8'))
  
   
    data= pd.read_csv('../Data/heart_failure_clinical_records_dataset.csv').iloc[:nb_patient,:]
    MODEL_PATH='../Data/model.pkl'
    model=pickle.load(open(MODEL_PATH,'rb'))
        
    for  i in data.index :
        X= data.iloc[[i],:12]
        print(X)
        classification=model.predict(X)
        
        # if 'target' in X.columns:              
        #     type_record= X.loc[i,'target']
        #     X= X.drop('target',axis=1)
                                ## type_record is a variable that identify the label of each record read.
        
        
        if  classification==1:
            
                topic_name = "urgent_data"  
                topic_info="personal_info"
        else:                              ## The kafka Topic is specified based on the type_record value(1 or 0)

                topic_name= "normal_data"
            
        medicalInfo=X.drop(['age','sex','smoking','time','diabetes'],axis=1).to_dict('records')[0]
        personalInfo= X.drop(['anaemia','creatinine_phosphokinase','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium'],axis=1).to_dict('records')[0]
        #doc['date']=str(datetime.datetime.now().date())
        #doc['time']=str(datetime.datetime.now().time())[:5]
        producer.send(topic_name,medicalInfo)
        producer.send(topic_info,personalInfo)
        
        print("this data is urgent !!!" if classification==1 else "this data is normal")
        sleep(n)
    producer.flush()

data_to_kafka(nb_patient=4) 




