from tkinter import *
from tkinter import ttk
from kafka import KafkaConsumer
topic_name = 'urgent_data'
topic_info="personal_info"
consumer = KafkaConsumer(topic_name,group_id='new-consumer-group-topic1', auto_offset_reset= "earliest",bootstrap_servers= 'localhost:9092')
consumer1 = KafkaConsumer(topic_info, group_id='new-consumer-group-topic2', auto_offset_reset= "earliest",bootstrap_servers= 'localhost:9092')

# for msg in consumer:
# 	print("Nurse: urgent data")
# 	print(msg)

for msg , msg2 in zip(consumer,consumer1):
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Urgent Data").grid(column=0, row=0)
    ttk.Label(frm, text=str(msg.value)).grid(column=0, row=1)
    ttk.Label(frm, text="info data").grid(column=0, row=2)
    ttk.Label(frm, text=str(msg2.value)).grid(column=0, row=3)
    #ttk.Label(frm, text="Quit",command=root.destroy).grid(column=0, row=4)
    root.mainloop()  	
 
 
 
 





