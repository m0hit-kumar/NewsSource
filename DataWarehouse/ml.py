import pandas as pd
import string
import re
# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorization=TfidfVectorizer()
import pickle



def load_model(path):
    with open(path , 'rb') as f:
        model = pickle.load(f)

    return model


model1=load_model("models/DecisionTreeClassifier()_model")
model2=load_model("models/GradientBoostingClassifier(random_state=0)_model")
model3=load_model("models/LogisticRegression()_model")
# vectorization=load_model("models/vectorizer")
loaded_vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))




def clean(text):
  text =text.lower()
  text =re.sub('\[.*?\]','',text)
  text= re.sub("\\W",' ',text)
  # text= re.sub('https?://\S+[www\.\S+','',text)
  text=re.sub(r'^https?:\/\/.*[\r\n]*', '', text)
  text= re.sub ('<.*?>+','',text)
  text= re.sub('[%s]' % re.escape(string.punctuation),'', text)
  text= re.sub ('\n', '', text)
  text = re.sub('\w*\d\w*', '', text)
  return text


def percentage_cal(model1, model2):
    sum=model1+model2
    if(sum==0):
        return 0
    if(sum==1):
        return 30
    if(sum==2):
        return 75






def process_news(news):
    testing_news ={"text":[news]}
    new_def_test=pd.DataFrame(testing_news)
    new_def_test["text"]=new_def_test["text"].apply(clean)
    new_x_test=new_def_test["text"]
    new_xv_test=loaded_vectorizer.transform(new_x_test)
    model1_output=model1.predict(new_xv_test)
    # model2_output=model2.predict(new_xv_test)
    model3_output=model3.predict(new_xv_test)
    print(model3_output)
    print(model1_output)
    
    return percentage_cal(model1_output,model3_output)



# print(process_news("Almost every social media site is known for the topic it represents in the form of hashtags. Particularly for our case, Hashtags played an important part since we were interested in #Covid19 ,#Coronavirus, #StayHome, #InThisTogether, etc. Hence, the first step was forming a separate feature b"))    



