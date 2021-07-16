import matplotlib.pyplot as mp 
marks=[64,56,55,58,60,69,72]
bins=['label1','label2','label3','label4','label5','label6','label7',]
color=['green','white','cyan','yellow','black','blue','pink']
mp.pie(marks,labels=bins,colors=color,startangle=90,shadow='true',explode=(0.2,0,0,0.1,0,0.1,0),autopct='%1.2f%%',rotatelabels=True,counterclock=True)
mp.legend()
mp.show()