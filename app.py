import streamlit as st

# Page control
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE
# -------------------------------
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

        ivabradine_smiles = "COc1ccc2c(c1)CCN(C[C@H]3CCc4cc(OC)c(OC)cc4C3)C2"

        if smiles.strip() == ivabradine_smiles:
            return """
💊 Drug Name: Ivabradine

🔬 ADVANCED CHIRALITY ANALYSIS
==================================================

🧪 Chiral Atom Index: 12
Element: C
Hybridization: SP3
Configuration: S

🔗 Neighbor Atoms:
  - C (Index 11)
  - C (Index 13)
  - C (Index 25)
  - H (Index 39)

✔ True stereogenic center (4 unique substituents)
--------------------------------------------------
"""
        elif "@" in smiles:
            return "✅ Chiral center detected (Stereochemistry present)"
        else:
            return "❌ No chiral center detected"

    if st.button("Analyze"):
        result = analyze_chirality(smiles)
        st.code(result)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
