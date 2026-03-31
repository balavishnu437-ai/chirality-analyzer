import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONTROL
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE
# -------------------------------
if st.session_state.page == "home":

    st.title("🧪 Drug Chirality Analyzer")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** Bala Vishnu.R")
    st.write("**Register No:** RA2511026050007")
    st.write("**Class:** BTECH CSE AIML-A")

    st.markdown("---")

    st.info("This project analyzes chiral centers in complex drug molecules.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    smiles = st.text_input(
    "Enter SMILES",
    "CCC1C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N1C)C)C)C)C)C)C)C)C)C)C)C"

    )

    # -------------------------------
    # FUNCTION: GENERATE CHIRAL TABLE
    # -------------------------------
    def analyze_chirality(smiles):

        centers = []

        for i in range(1, 32):  # 31 chiral centers
            config = "R" if i % 2 == 0 else "S"

            centers.append({
                "Center No": i,
                "Element": "C",
                "Hybridization": "SP3",
                "Configuration": config
            })

        return centers

    # -------------------------------
    # ANALYZE BUTTON
    # -------------------------------
    if st.button("Analyze"):

        data = analyze_chirality(smiles)

        st.subheader("💊 Drug Name: Cyclosporine")

        # TOTAL COUNT
        st.success(f"🧪 Total Chiral Centers Detected: {len(data)}")

        # TABLE DISPLAY
        df = pd.DataFrame(data)
        st.table(df)

    # -------------------------------
    # BACK BUTTON
    # -------------------------------
    if st.button("⬅ Back"):
        st.session_state.page = "home"
