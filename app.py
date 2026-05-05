import streamlit as st
import pandas as pd

st.set_page_config(page_title="Generator Boarding Pass Ferizy", layout="centered")

def render_boarding_pass(data):
    html_template = f"""
<div id="ticket" style="width:280px;padding:12px;margin:auto;
font-family:monospace;background:#fff;color:#000;
font-size:12px;line-height:1.2;letter-spacing:0.3px;">

<div style="display:flex;justify-content:space-between;align-items:center;">
<div style="font-weight:bold;font-size:16px;">ferizy</div>
<div style="text-align:center;font-size:10px;">
<b>BOARDING PASS</b><br>Untuk Pengguna Jasa
</div>
<div style="font-size:18px;font-weight:bold;">B</div>
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="display:flex;justify-content:space-between;">
<div>ASAL<br><b>{data['Asal']}</b></div>
<div>→</div>
<div style="text-align:right;">TUJUAN<br><b>{data['Tujuan']}</b></div>
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<table style="width:100%;text-align:center;font-size:11px;">
<tr>
<td>Kelas<br><b>{data['Kelas Layanan']}</b></td>
<td>Gol<br><b>{data['Golongan']}</b></td>
<td>PNP<br><b>{data['Total PNP']}</b></td>
<td>Derm<br><b>{data['Dermaga']}</b></td>
</tr>
</table>

<div style="font-size:9px;text-align:center;margin:4px 0;">
Cek info dermaga di pelabuhan
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<table style="width:100%;font-size:11px;">
<tr><td>Check-in</td><td>: {data['Waktu Check-In']}</td></tr>
<tr><td>No Tiket</td><td>: {data['No Tiket']}</td></tr>
<tr><td>Nama</td><td>: {data['Nama']}</td></tr>
<tr><td>Nopol</td><td>: {data['No Polisi']}</td></tr>
<tr><td>Berat</td><td>: {data['Berat']} KG</td></tr>
<tr><td>Tarif</td><td>: {data['Tarif']}</td></tr>
</table>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="font-size:9px;">
- Tunjukkan saat naik kapal<br>
- Tutup 15 menit sebelum berangkat<br>
- Termasuk asuransi<br>
- Tidak bisa dibatalkan
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="text-align:center;font-size:9px;">
Call Center: (021) 191<br>
www.ferizy.com
</div>

</div>

<br>

<button onclick="downloadImage()" style="padding:6px 10px;font-size:12px;">
📥 Download PNG
</button>

<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>

<script>
function downloadImage() {{
    const ticket = document.getElementById("ticket");
    html2canvas(ticket).then(canvas => {{
        const link = document.createElement('a');
        link.download = 'boarding_pass.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    }});
}}
</script>
"""
    st.components.v1.html(html_template, height=520)
    
st.title("⛴️ Generator Boarding Pass Ferizy")

tab1, tab2 = st.tabs(["✍️ Input Manual", "📁 Upload Excel"])

# --- TAB 1: INPUT MANUAL ---
with tab1:
    st.subheader("Isi Data Boarding Pass")
    
    with st.form("manual_form"):
        col1, col2 = st.columns(2)
        with col1:
            asal = st.text_input("Asal", value="MERAK")
            kelas = st.text_input("Kelas Layanan", value="REGULER")
            pnp = st.number_input("Total PNP", min_value=1, value=1)
            waktu = st.text_input("Waktu Check-In", value="03-05-2026 22:14:54")
            nama = st.text_input("Nama", value="WARSITO")
            berat = st.number_input("Berat (KG)", min_value=0, value=348)
        
        with col2:
            tujuan = st.text_input("Tujuan", value="BAKAUHENI")
            golongan = st.text_input("Golongan", value="VIB")
            dermaga = st.text_input("Dermaga", value="II")
            no_tiket = st.text_input("No Tiket", value="03A00TLSGT01")
            nopol = st.text_input("No Polisi", value="BE8598AMN")
            tarif = st.text_input("Tarif", value="Rp1.285.200")
            
        submit = st.form_submit_button("Generate Boarding Pass")
        
    if submit:
        data = {
            "Asal": asal.upper(), "Tujuan": tujuan.upper(), "Kelas Layanan": kelas.upper(),
            "Golongan": golongan.upper(), "Total PNP": pnp, "Dermaga": dermaga.upper(),
            "Waktu Check-In": waktu, "No Tiket": no_tiket.upper(), "Nama": nama.upper(),
            "No Polisi": nopol.upper(), "Berat": berat, "Tarif": tarif
        }
        st.success("Boarding Pass Berhasil Dibuat!")
        render_boarding_pass(data)

# --- TAB 2: UPLOAD EXCEL ---
with tab2:
    st.subheader("Generate Massal via Excel")
    st.info("Upload file Excel dengan format kolom yang sesuai dengan template.")
    
    uploaded_file = st.file_uploader("Upload file Excel (.xlsx)", type=["xlsx"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success(f"Berhasil membaca {len(df)} data!")
            
            # Button untuk merender semua tiket di dalam excel
            if st.button("Tampilkan Semua Boarding Pass"):
                for index, row in df.iterrows():
                    # Mengamankan data dari null value
                    data = {
                        "Asal": str(row.get("Asal", "MERAK")).upper(),
                        "Tujuan": str(row.get("Tujuan", "BAKAUHENI")).upper(),
                        "Kelas Layanan": str(row.get("Kelas Layanan", "REGULER")).upper(),
                        "Golongan": str(row.get("Golongan", "VIB")).upper(),
                        "Total PNP": row.get("Total PNP", 1),
                        "Dermaga": str(row.get("Dermaga", "II")).upper(),
                        "Waktu Check-In": str(row.get("Waktu Check-In", "03-05-2026 22:14:54")),
                        "No Tiket": str(row.get("No Tiket", "-")).upper(),
                        "Nama": str(row.get("Nama", "-")).upper(),
                        "No Polisi": str(row.get("No Polisi", "-")).upper(),
                        "Berat": row.get("Berat", 0),
                        "Tarif": str(row.get("Tarif", "Rp0"))
                    }
                    render_boarding_pass(data)
                    st.markdown("---") # Pemisah antar struk
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
