import streamlit as st
import pandas as pd
import base64
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="Generator Boarding Pass Ferizy", layout="centered")

def render_boarding_pass(data):
    # 1. Menyiapkan logo dan icon dalam format Base64
    logo_base64 = ""
    if os.path.exists("logo_ferizy.png"):
        with open("logo_ferizy.png", "rb") as img:
            logo_base64 = base64.b64encode(img.read()).decode()
            
    cruise_ship_base64 = ""
    if os.path.exists("cruise-ship.png"):
        with open("cruise-ship.png", "rb") as img:
            cruise_ship_base64 = base64.b64encode(img.read()).decode()
            
    ship_base64 = ""
    if os.path.exists("ship.png"):
        with open("ship.png", "rb") as img:
            ship_base64 = base64.b64encode(img.read()).decode()
            
    # Menambahkan 1 hari untuk waktu BERLAKU
    try:
        checkin_dt = datetime.strptime(data['Waktu Check-In'], "%d-%m-%Y %H:%M:%S")
        berlaku_dt = checkin_dt + timedelta(days=1)
        waktu_berlaku = berlaku_dt.strftime("%d-%m-%Y %H:%M:%S")
    except Exception:
        # Fallback jika format waktu tidak sesuai standar
        waktu_berlaku = data['Waktu Check-In']
        
    # Menyesuaikan penulisan untuk Watermark belakang
    watermark_text = str(data['Kelas Layanan']).capitalize()

    html_template = f"""
<div id="ticket" style="width:360px; padding:20px; font-family: Arial, Helvetica, sans-serif; background:#fff; color:#000; font-size:12px; line-height:1.4; position: relative; margin: 0 auto; box-shadow: 0 0 5px rgba(0,0,0,0.1);">

    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="width:80px; text-align:left;">
            {f'<img src="data:image/png;base64,{logo_base64}" style="width:100%; filter: grayscale(100%); -webkit-filter: grayscale(100%); display:block;">' if logo_base64 else '<b style="font-size:18px;">ferizy</b>'}
        </div>
        <div style="text-align:center; line-height:1.2; flex-grow: 1;">
            <b style="font-size:15px; letter-spacing: 0.5px;">BOARDING PASS</b><br>
            <span style="font-size:13px; color: #333;">Untuk Pengguna Jasa</span>
        </div>
        <div style="font-size:32px; font-weight:900; width: 40px; text-align: right;">B</div>
    </div>

    <hr style="border-top:1px dashed #000; margin:12px 0;">

    <div style="display:flex; justify-content:space-between; text-align:center;">
        <div style="width:40%; text-align:center;">
            <div style="font-size:11px; color: #444; margin-bottom: 2px;">ASAL</div>
            <b style="font-size:15px; letter-spacing: 0.5px;">{data['Asal']}</b>
        </div>
        <div style="width:20%; display:flex; align-items:center; justify-content:center;">
            {f'<img src="data:image/png;base64,{cruise_ship_base64}" style="width:26px; height:auto;">' if cruise_ship_base64 else '&#9973;'}
        </div>
        <div style="width:40%; text-align:center;">
            <div style="font-size:11px; color: #444; margin-bottom: 2px;">TUJUAN</div>
            <b style="font-size:15px; letter-spacing: 0.5px;">{data['Tujuan']}</b>
        </div>
    </div>

    <div style="border: 1px solid #000; border-radius: 12px; padding: 6px 12px; margin-top: 15px; display: flex; justify-content: space-between; text-align: center; align-items: center; position: relative;">
        <div style="position: absolute; left: -10px; top: 10px; background: #fff; padding: 2px 4px;">
            {f'<img src="data:image/png;base64,{ship_base64}" style="width:16px; height:auto;">' if ship_base64 else '&#9973;'}
        </div>
        <div style="position: absolute; right: -10px; top: 10px; background: #fff; font-size: 16px; padding: 2px;">&#9784;</div>
        
        <div style="flex:1;">
            <div style="font-size: 10px;">&#9432; Kelas Layanan</div>
            <b style="font-size: 13px;">{data['Kelas Layanan']}</b>
        </div>
        <div style="flex:1;">
            <div style="font-size: 10px;">Golongan</div>
            <b style="font-size: 13px;">{data['Golongan']}</b>
        </div>
        <div style="flex:1;">
            <div style="font-size: 10px;">Total PNP</div>
            <b style="font-size: 13px;">{data['Total PNP']}</b>
        </div>
        <div style="flex:1;">
            <div style="font-size: 10px;">Dermaga</div>
            <b style="font-size: 13px;">{data['Dermaga']}</b>
        </div>
    </div>

    <div style="text-align: center; font-size: 10px; font-style: italic; margin-top: 10px; color: #222; line-height: 1.3;">
        Silakan cek informasi dermaga di pelabuhan dan<br>ikuti arahan petugas untuk menuju ke arah dermaga
    </div>

    <br>

    <div style="position: relative; overflow: hidden; padding-bottom: 5px;">
        <div style="position: absolute; top: 40%; left: 0; right: 0; text-align: center; font-size: 55px; font-weight: bold; color: rgba(220, 220, 220, 0.4); z-index: 0; letter-spacing: 1px; transform: translateY(-50%) scaleY(1.1);">
            {watermark_text}
        </div>
        <table style="width: 100%; font-size: 13px; line-height: 1.6; position: relative; z-index: 1; border-collapse: collapse;">
            <tr><td style="width: 40%; padding: 0;">WAKTU CHECK-IN</td><td style="width: 5%; padding: 0;">:</td><td style="padding: 0;">{data['Waktu Check-In']}</td></tr>
            <tr><td style="padding: 0;">NO. TIKET</td><td style="padding: 0;">:</td><td style="padding: 0;">{data['No Tiket']}</td></tr>
            <tr><td style="padding: 0;">NAMA</td><td style="padding: 0;">:</td><td style="padding: 0;">{data['Nama']}</td></tr>
            <tr><td style="padding: 0;">NO. POLISI</td><td style="padding: 0;">:</td><td style="padding: 0;">{data['No Polisi']}</td></tr>
            <tr><td style="padding: 0;">BERAT</td><td style="padding: 0;">:</td><td style="padding: 0;">{data['Berat']} KG</td></tr>
            <tr><td style="padding: 0;">TARIF</td><td style="padding: 0;">:</td><td style="padding: 0;">{data['Tarif']}</td></tr>
        </table>
    </div>

    <hr style="border-top:1px dashed #000; margin:6px 0;">

    <div style="font-size: 10px; line-height: 1.2; color: #444;">
        <b style="color: #000;">Keterangan :</b><br>
        - Tunjukkan boarding pass saat naik kapal;<br>
        - Waktu yang tertera adalah waktu pelabuhan setempat<br>
        - Pintu rampdoor kapal akan ditutup 15 menit sebelum keberangkatan<br>
        - Harga tiket sudah termasuk asuransi;<br>
        - Tiket tidak dapat dibatalkan;
    </div>

    <hr style="border-top:1px dashed #000; margin:6px 0;">

    <div style="text-align: center; font-size: 11px;">
        Butuh Informasi Lebih Lanjut? Hubungi Call Center ASDP Di :<br>
        <div style="display: flex; justify-content: center; gap: 15px; margin-top: 8px; font-weight: bold; font-size: 12px; align-items: center;">
            <div style="display:flex; align-items:center;">&#128222; (021) - 191</div>
            <div style="display:flex; align-items:center;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="13" height="13" fill="#000" style="margin-right:5px;"> <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zM223.9 414.8c-32 0-63.3-8.6-90.8-24.9l-6.5-3.8-67.4 17.7 18-65.7-4.2-6.7c-17.8-28.5-27.2-61.5-27.2-95.3 0-103.8 84.5-188.3 188.4-188.3 50.3 0 97.6 19.6 133.2 55.2 35.6 35.6 55.2 82.9 55.2 133.2 0 103.8-84.5 188.3-188.4 188.3zm103.2-141.5c-5.7-2.8-33.6-16.6-38.8-18.5-5.2-1.9-9-2.8-12.8 2.8-3.8 5.7-14.7 18.5-18 22.3-3.3 3.8-6.6 4.3-12.3 1.4-5.7-2.8-24-8.8-45.7-28.1-16.9-15.1-28.3-33.8-31.1-39.5-2.8-5.7-.3-8.8 2.6-11.6 2.6-2.6 5.7-6.6 8.5-9.9 2.8-3.3 3.8-5.7 5.7-9.5 1.9-3.8.9-7.1-.5-9.9-1.4-2.8-12.8-30.8-17.5-42.2-4.6-11.1-9.3-9.6-12.8-9.8-3.3-.2-7.1-.2-10.9-.2-3.8 0-10 1.4-15.2 7.1-5.2 5.7-19.9 19.4-19.9 47.4 0 28 20.4 55 23.2 58.8 2.8 3.8 40.1 61.2 97.1 85.5 13.6 5.8 24.2 9.2 32.5 11.8 13.6 4.3 26 3.7 35.8 2.2 10.9-1.6 33.6-13.7 38.4-27 4.7-13.3 4.7-24.6 3.3-27-.8-2.6-4.6-4.5-10.3-7.4z"/> </svg>
                0811 1021 191
            </div>
            <div style="display:flex; align-items:center;">&#9993; cs@asdp.id</div>
        </div>
        <div style="margin-top: 4px; font-size: 15px; font-weight: 900; letter-spacing: 0.5px;">www.ferizy.com</div>
    </div>

    <hr style="border-top:1px dashed #000; margin:6px 0;">

    <div style="text-align: center; font-size: 9px; line-height: 1.2; color: #555;">
        <b style="color:#000;">PT ASDP Indonesia Ferry (Persero)</b><br>
        Jl. Jend. Ahmad Yani Kav 52 A, Cempaka Putih Timur<br>
        Kota Jakarta Pusat, 10510<br>
        NPWP: 01.061.041.8-093.000<br>
        <div style="display: flex; justify-content: space-between; margin-top: 10px; color: #888;">
            <span>REG2.2 - (02001072)</span>
            <span>expired : {waktu_berlaku}</span>
        </div>
    </div>
</div>

<br>

<button onclick="downloadImage()" style="margin: 0 auto; display: block; padding: 10px 20px; font-weight: bold; cursor: pointer; border-radius: 5px; border: 1px solid #ccc;">📥 Download PNG</button>

<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
<script>
function downloadImage() {{
    const ticket = document.getElementById("ticket");
    html2canvas(ticket, {{ scale: 3, backgroundColor: null, useCORS: true }}).then(canvas => {{
        const link = document.createElement('a');
        link.download = 'boarding_pass.png';
        link.href = canvas.toDataURL("image/png");
        link.click();
    }});
}}
</script>
"""
    st.components.v1.html(html_template, height=850)
    
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
            waktu = st.text_input("Waktu Check-In", value="03-07-2026 02:15:58")
            nama = st.text_input("Nama", value="RUDI")
            berat = st.text_input("Berat (KG)", value="29.980") 
        
        with col2:
            tujuan = st.text_input("Tujuan", value="BAKAUHENI")
            golongan = st.text_input("Golongan", value="VIB")
            dermaga = st.text_input("Dermaga", value="III")
            no_tiket = st.text_input("No Tiket", value="03A00LKMV801")
            nopol = st.text_input("No Polisi", value="B9022UZ")
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
    
    uploaded_file = st.file_uploader("Upload file Excel (.xlsx, .csv)", type=["xlsx", "csv"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"Berhasil membaca {len(df)} data!")
            
            if st.button("Tampilkan Semua Boarding Pass"):
                for index, row in df.iterrows():
                    
                    # 1. Parsing & Standarisasi Waktu
                    raw_waktu = row.get("Waktu Check-In")
                    if pd.isna(raw_waktu):
                        waktu_str = "03-07-2026 02:15:58"
                    else:
                        try:
                            parsed_dt = pd.to_datetime(raw_waktu, dayfirst=True)
                            waktu_str = parsed_dt.strftime("%d-%m-%Y %H:%M:%S")
                        except:
                            waktu_str = str(raw_waktu)
                            
                    # 2. Parsing Berat
                    raw_berat = row.get("Berat")
                    if pd.isna(raw_berat):
                        berat_str = "0"
                    else:
                        try:
                            if isinstance(raw_berat, float) or isinstance(raw_berat, int):
                                if raw_berat > 1000:
                                    berat_str = f"{int(raw_berat):,}".replace(",", ".")
                                else:
                                    berat_str = str(raw_berat)
                            else:
                                berat_str = str(raw_berat)
                        except:
                            berat_str = str(raw_berat)
                            
                    # 3. Parsing Tarif
                    raw_tarif = row.get("Tarif")
                    if pd.isna(raw_tarif):
                        tarif_str = "Rp0"
                    else:
                        try:
                            if isinstance(raw_tarif, str) and "Rp" in raw_tarif:
                                tarif_str = raw_tarif
                            else:
                                num_tarif = int(float(raw_tarif))
                                tarif_str = f"Rp{num_tarif:,}".replace(",", ".")
                        except:
                            tarif_str = str(raw_tarif)
                    
                    data = {
                        "Asal": str(row.get("Asal", "MERAK")).upper(),
                        "Tujuan": str(row.get("Tujuan", "BAKAUHENI")).upper(),
                        "Kelas Layanan": str(row.get("Kelas Layanan", "REGULER")).upper(),
                        "Golongan": str(row.get("Golongan", "VIB")).upper(),
                        "Total PNP": row.get("Total PNP", 1),
                        "Dermaga": str(row.get("Dermaga", "III")).upper(),
                        "Waktu Check-In": waktu_str,
                        "No Tiket": str(row.get("No Tiket", "-")).upper(),
                        "Nama": str(row.get("Nama", "-")).upper(),
                        "No Polisi": str(row.get("No Polisi", "-")).upper(),
                        "Berat": berat_str,
                        "Tarif": tarif_str
                    }
                    render_boarding_pass(data)
                    st.markdown("---") 
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
