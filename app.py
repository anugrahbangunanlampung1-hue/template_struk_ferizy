import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Generator Boarding Pass Ferizy", layout="centered")

def render_boarding_pass(data):
    try:
        with open("logo_ferizy.png", "rb") as img:
            logo_base64 = base64.b64encode(img.read()).decode()
    except:
        logo_base64 = "" # Fallback jika file tidak ditemukan

    html_template = f"""
<div id="ticket" style="
    width: 380px;
    padding: 20px;
    font-family: 'Courier New', Courier, monospace;
    background: #ffffff;
    color: #000;
    border: 1px solid #ddd;
    margin: auto;
">
    <!-- Header -->
    <div style="font-size: 11px; margin-bottom: 10px;">
        Reg3.3 - (02002078)<br>
        {data['Waktu Check-In']}
    </div>

    <!-- Logo & Title Section -->
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="width: 30%; vertical-align: top;">
                <img src="data:image/png;base64,{logo_base64}" style="width: 80px; filter: grayscale(100%);">
                <div style="font-size: 9px; margin-top: 5px;">Naik Ferry, Easy!</div>
            </td>
            <td style="text-align: center; vertical-align: middle;">
                <div style="font-weight: 900; font-size: 18px; line-height: 1.1;">BOARDING PASS</div>
                <div style="font-weight: bold; font-size: 13px;">Untuk Kendaraan</div>
            </td>
            <td style="width: 20%; text-align: right; font-weight: 900; font-size: 45px; vertical-align: middle;">
                B
            </td>
        </tr>
    </table>

    <hr style="border: none; border-top: 1px dashed #000; margin: 10px 0;">

    <!-- Route Info -->
    <div style="font-size: 13px;">
        <div style="font-weight: bold;">KEBERANGKATAN REG</div>
        <div style="font-size: 15px; font-weight: bold;">{data['Asal']} - {data['Tujuan']}</div>
        <div>Reguler {data['Waktu Check-In'][:10]}</div>
    </div>

    <hr style="border: none; border-top: 1px dashed #000; margin: 10px 0;">

    <!-- Details Table -->
    <table style="width: 100%; font-size: 12px; border-collapse: collapse; line-height: 1.5;">
        <tr><td style="width: 35%;">BERLAKU</td><td style="width: 5%;">:</td><td style="font-weight: bold;">{data['Waktu Check-In']}</td></tr>
        <tr><td>KD. BOOKING</td><td>:</td><td style="font-weight: bold;">{data['No Tiket'][:8]}</td></tr>
        <tr><td>NO. TIKET</td><td>:</td><td style="font-weight: bold;">{data['No Tiket']}</td></tr>
        <tr><td>NAMA</td><td>:</td><td>{data['Nama']}</td></tr>
        <tr><td>NO. POLISI</td><td>:</td><td style="font-weight: bold;">{data['No Polisi']}</td></tr>
        <tr><td>GOLONGAN</td><td>:</td><td>{data['Golongan']}</td></tr>
        <tr><td>BERAT</td><td>:</td><td>{data['Berat']} KG</td></tr>
        <tr><td>TARIF</td><td>:</td><td>{data['Tarif']}</td></tr>
    </table>

    <hr style="border: none; border-top: 1px dashed #000; margin: 10px 0;">

    <!-- Footer Notes -->
    <div style="font-size: 10px; line-height: 1.2;">
        <b>Keterangan :</b><br>
        • Tunjukan boarding pass saat naik kapal<br>
        • Waktu tertera adalah waktu pelabuhan setempat<br>
        • Pintu kapal ditutup 30 menit sebelum keberangkatan<br>
        • Harga tiket sudah termasuk asuransi<br>
        • Tiket tidak dapat dibatalkan
    </div>

    <hr style="border: none; border-top: 1px dashed #000; margin: 10px 0;">

    <div style="font-size: 10px; text-align: center;">
        Butuh informasi lebih lanjut? Hubungi Call Center ASDP:<br>
        <b>📞 191 | 📱 0811 1021 191 | ✉ cs@asdp.id</b><br>
        <div style="margin-top: 5px; font-size: 12px; font-weight: bold;">www.ferizy.com</div>
    </div>
</div>

<div style="text-align: center; margin-top: 20px;">
    <button onclick="downloadImage()" style="padding: 10px 20px; cursor: pointer;">📥 Download Boarding Pass (PNG)</button>
</div>

<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
<script>
function downloadImage() {{
    const ticket = document.getElementById("ticket");
    html2canvas(ticket, {{ scale: 2 }}).then(canvas => {{
        const link = document.createElement('a');
        link.download = 'boarding_pass_{data['No Polisi']}.png';
        link.href = canvas.toDataURL("image/png");
        link.click();
    }});
}}
</script>
"""
    st.components.v1.html(html_template, height=800, scrolling=True)
    
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
