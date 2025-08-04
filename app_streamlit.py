import streamlit as st
from predict_utils import make_prediction, load_models

# Load all models
models = load_models()

def main():
    st.set_page_config(page_title="📊 Mortgage Default Prediction", layout="centered")
    st.title("🏡 Mortgage Default Prediction App")

    if not models:
        st.error("❌ No models loaded. Please check the models directory.")
        return


    # Model selection based on loaded models
    model_key = st.selectbox("Select a Model", list(models.keys()))

    # Input form
    with st.form("prediction_form"):
        CreditScore = st.text_input("Credit Score")
        OCLTV = st.text_input("OCLTV")
        DTI = st.text_input("DTI")
        OrigUPB = st.text_input("Original UPB")
        OrigInterestRate = st.text_input("Original Interest Rate")

        submit = st.form_submit_button("Predict")

    if submit:
        try:
            # Validate non-empty
            if "" in (CreditScore, OCLTV, DTI, OrigUPB, OrigInterestRate):
                st.warning("⚠️ Please fill in all fields before submitting.")
                return

            # Convert inputs to floats
            features = list(map(float, [CreditScore, OCLTV, DTI, OrigUPB, OrigInterestRate]))

            # Make prediction
            result = make_prediction(model_key, features)

            if "prediction" in result:
                st.success(f"🎯 Prediction from `{model_key}`: {result['prediction']}")
            else:
                st.error(f"❌ {result.get('error', 'Unknown error')}")

        except ValueError:
            st.error("❌ Please enter valid numeric values.")
        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
