import streamlit as st

def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    Ish = V / Rsh
    Ia =( K * IL) - Ish
    CUL = (Ish ** 2) * Rsh + (Ia ** 2) * Ra
    Eff=(K*V*IL)*100/(K*V*IL+CL+CUL)
    return Eff, CUL

st.title("2205A21009-PS9")

st.write("calculate the efficiency of DC shunt generator at various loads")
col1,col2=st.columns(2)
with col1:
    with st.container(border=True):
        V = st.number_input("Vin(V) volts:",value=1)
        IL = st.number_input("IL in amps:",value=1)
        Rsh = st.number_input("Rsh in ohms:",value=1)
        Ra = st.number_input("Ra in ohms:",value=1)
        CL = st.number_input("CL in watts:",value=1)
        K = st.number_input("Loading on Generator (K):",value=1)
    
with col2:
    Eff, CUL=Gen_Eff(V, CL, IL, K, Rsh, Ra)
    st.write(f"Efficiency (Eff): {Eff:.2f}%")
    st.write(f"Copper Losses (CUL): {CUL:.2f} W")
       