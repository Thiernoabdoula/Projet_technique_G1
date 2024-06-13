import pickle
import streamlit as st
import pandas as pd
import numpy as np


# Sauvegarder le modèle dans un fichier pickle
#with open('amazon_model.pkl', 'wb') as model_file:
 #   pickle.dump(model, model_file)

# Charger le modèle
with open('amazon_model.pkl', 'rb') as model_import:
    model = pickle.load(model_import)


@st.cache()
def prediction( main_category, sub_category, ratings, no_of_ratings, actual_price):
    # Créer un DataFrame avec les valeurs d'entrée
    input_data = pd.DataFrame({
        'main_category': [main_category],
        'sub_category': [sub_category],
        'ratings': [ratings],
        'no_of_ratings': [no_of_ratings],
        'actual_price': [actual_price]
    })

    # Prédiction
    return model.predict(input_data)


def main():
    html_temp = """
    <div style="background-color:orange;padding:13px">
    <h1 style="color:black;text-align:center;"> Prédiction du prix des articles AMAZON</h1>
    </div>
    <hr>
    """
    result = ""
    st.markdown(html_temp, unsafe_allow_html=True)

    main_category = st.selectbox('Main category', list(range(20)))
    sub_category = st.selectbox('Sub category', list(range(112)))
    #ratings = st.selectbox('Ratings', np.arange(1.0, 5.1, 0.1))
    #no_of_ratings = st.number_input('No of ratings')
    ratings = st.slider('Rating', min_value=1.0, max_value=5.0, step=0.1)

    # Number input for the number of ratings
    no_of_ratings = st.number_input('No of ratings', min_value=0, step=1)
    actual_price = st.number_input('Actual price')

    if st.button("Predict"):

        print(f"Params: {[main_category, sub_category, ratings, no_of_ratings, actual_price]}")
        result = prediction(main_category, sub_category, ratings, no_of_ratings, actual_price)
        rounded_result = round(result[0], 2)
        st.success(f"Le prix discount prédit est: {rounded_result}")
        

        #st.success(f"Le prix discount prédit est: {result}")
        print(f"Le prix discount prédit est: {rounded_result}")




if __name__ == "__main__":
    main()
