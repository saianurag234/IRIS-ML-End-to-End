import streamlit as st
import os
from PIL import Image

os.chdir("C:\\Users\\hp\\Downloads\\archive (1)")

from tensorflow.keras.models import load_model
new_model = load_model('my_model.h5')

def IRIS_prediction(input_data):
    prediction1 = new_model.predict([input_data])
    
    prediction = []
    
    for i in range(0,3):
        prediction.append(prediction1[0][i])
    
    max_value = max(prediction)
    index = prediction.index(max_value)
    
    if(index == 0):
        return "Iris-Setosa"
    elif(index == 1):
        return "Iris-versicolor"
    elif(index == 2):
        return "Iris-virginica"
    else:
        return 0
    
def main():
    
    
    # giving a title
    st.title('IRIS Calssification Web App')
    
    
    # getting the input data from the user
    
    
    sepal_length = float(st.number_input('Sepal Length'))
    sepal_width = float(st.number_input('Sepal Width'))
    petal_length = float(st.number_input('Petal Length'))
    petal_width = float(st.number_input('Petal Width'))
   

    # creating a button for Prediction
    
    b = st.button('Predict')
    a = ''
    
    if b:
        model_prediction = IRIS_prediction([sepal_length, sepal_width , petal_length, petal_width])
        a = model_prediction
        print(a)
        
        st.subheader(a)
        
    if(a == "Iris-Setosa"):
        image = Image.open('C:/Users/hp/Downloads/iris-setosa.png')
        st.image(image)
    if(a == "Iris-versicolor"):
        image = Image.open('C:/Users/hp/Downloads/iris-versicolor.png')
        st.image(image)
    if(a == "Iris-virginica"):
        image = Image.open('C:/Users/hp/Downloads/iris_virginica.png')
        st.image(image)
    
      
    
if __name__ == '__main__':
    main()
