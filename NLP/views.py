
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.externals import joblib
import pandas as pd
pipeline_from_joblib=joblib.load('./models/review.pkl')
# Create your views here.
def index(request):
    context={'a':'Your Review'}
    if request.method=='POST':
        temp={}
        temp['X']=request.POST.get('Review')
        print(temp)
        df=pd.DataFrame(data=temp,index=[0])
        df.head()
        check2=df['X']
        testdata=pipeline_from_joblib.predict(check2)[0]
        print(testdata)
        context={'a':'Good Or Bad Emoji','b':testdata }

    
    return render(request,'index.html',context)
# def predict(request):


    
#     if request.method=='POST':

#         temp={}
#         temp['X']=request.POST.get('Review')
#         print(temp)
#         df=pd.DataFrame(data=temp,index=[0])
#         df.head()
#         check2=df['X']
#         testdata=pipeline_from_joblib.predict(check2)[0]


#     context={'a':'Good Or Bad Emoji','b':testdata }
#     print(testdata)
#     return render(request,'index.html',context)