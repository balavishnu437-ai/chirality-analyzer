import streamlit as st

# -------------------------------
# HOME PAGE
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":

    st.title("🧪 Drug Chirality Analyzer")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** Vishnu")
    st.write("**Register No:** 123456")
    st.write("**Class:** B.Sc Chemistry")

    st.markdown("---")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    smiles = st.text_input(
        "Enter SMILES",
        "COc1ccc2c(c1)CCN(C[C@H]3CCc4cc(OC)c(OC)cc4C3)C2"
    )

    def analyze_chirality(smiles):
        if "@" in smiles:
            return "✅ Chiral center detected (Stereochemistry present)"
        else:
            return "❌ No chiral center detected"

    if st.button("Analyze"):
        result = analyze_chirality(smiles)
        st.success(result)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
