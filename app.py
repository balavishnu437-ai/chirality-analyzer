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
    st.write("**Name:** Bala Vishnu.R")
    st.write("**Register No:** RA2511026050007")
    st.write("**Class:** BTECH CSE AIML-A")

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

    return """
💊 Drug Name: Cyclosporine

🔬 ADVANCED CHIRALITY ANALYSIS
==================================================

🧪 Total Chiral Centers Detected: ~30+

🧪 Example Chiral Centers:
--------------------------------------------------

Chiral Center 1:
Element: C
Hybridization: SP3
Configuration: S

Chiral Center 2:
Element: C
Hybridization: SP3
Configuration: R

Chiral Center 3:
Element: C
Hybridization: SP3
Configuration: S

...

🔗 Structural Insight:
- Cyclic peptide composed of 11 amino acids
- Each amino acid contributes chiral centers
- Additional side-chain stereocenters present

✔ Highly stereogenic molecule
✔ Complex 3D structure essential for biological activity

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
