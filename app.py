import streamlit as st
import math
from supabase import create_client

url = "https://rpuziygolczsdejpmrbj.supabase.co"
key = "sb_publishable_C-jZMxGoUZNih_twrG0AMw_hbCVZ_kq"

supabase = create_client(url, key)

PREIS = 3.90
ZIEL = 99

def get_count():
    res = supabase.table("counter").select("count").eq("id", 1).execute()
    return res.data[0]["count"]

def update_count(new_count):
    supabase.table("counter").update({"count": new_count}).eq("id", 1).execute()

st.title("Boulder Counter 🧗")

count = get_count()

if st.button("+1 Bouldern"):
    count += 1
    update_count(count)
    st.rerun()  # wichtig!

summe = count * PREIS
rest = ZIEL - summe
noch = math.ceil(rest / PREIS) if rest > 0 else 0

st.write(f"**Besuche:** {count}")
st.write(f"**Gesamt:** {summe:.2f} €")
st.write(f"**Noch bis Schuh:** {max(rest,0):.2f} €")
st.write(f"**Noch nötig:** {noch}x")

if rest <= 0:
    st.success("🎉 Ziel erreicht!")

# optional
if st.button("Reset"):
    update_count(0)
    st.rerun()