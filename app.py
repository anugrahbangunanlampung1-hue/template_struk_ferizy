import streamlit as st
import pandas as pd
import base64
from datetime import datetime, timedelta

st.set_page_config(page_title="Generator Boarding Pass Ferizy", layout="centered")

def render_boarding_pass(data):
    with open("logo_ferizy.png", "rb") as img:
        logo_base64 = base64.b64encode(img.read()).decode()
        
    # Menambahkan 1 hari untuk waktu BERLAKU
    try:
        checkin_dt = datetime.strptime(data['Waktu Check-In'], "%d-%m-%Y %H:%M:%S")
        berlaku_dt = checkin_dt + timedelta(days=1)
        waktu_berlaku = berlaku_dt.strftime("%d-%m-%Y %H:%M:%S")
    except Exception:
        # Fallback jika format waktu tidak sesuai standar
        waktu_berlaku = data['Waktu Check-In']
        
    html_template = f"""
<div id="ticket" style="
width:370px;
padding:12px;
font-family:monospace;
background:#fff;
color:#000;
font-size:12px;
line-height:1.35;
">

<div style="font-size:10px;font-style: italic;">
Reg3.3 - (02002078)<br>
{data['Waktu Check-In']}
</div>

<div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px;">
<div>
<img src="data:image/png;base64,{logo_base64}" style="width:80px; filter: grayscale(100%); -webkit-filter: grayscale(100%); display:block;">
<div style="font-size:10px;">Naik Ferry, Easy!</div>
</div>

<div style="text-align:center; line-height:1;">
    <div style="font-weight:900; font-size:20px; letter-spacing:1px;">
        BOARDING PASS
    </div>
    <div style="font-weight:900; font-size:15px;">
        Untuk Kendaraan
    </div>
</div>

<div style="
font-weight:900;
font-size:36px;
line-height:1;
">
B
</div>
</div> <hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="margin-bottom: 12px;">
<div style="font-weight:bold;">Keberangkatan REG</div>
<div>{data['Asal']} - {data['Tujuan']}</div>
<div>Reguler {data['Waktu Check-In'].split(' ')[0]}</div>
</div>

<table style="width:100%;font-size:12px;border-collapse:collapse;">
<tr>
<td style="width:40%;">BERLAKU</td>
<td style="width:5%;text-align:center;">:</td>
<td>{waktu_berlaku}</td>
</tr>
<tr>
<td>KD. BOOKING</td>
<td style="text-align:center;">:</td>
<td>{data['No Tiket'][2:]}</td>
</tr>
<tr>
<td>NO. TIKET</td>
<td style="text-align:center;">:</td>
<td>{data['No Tiket']}</td>
</tr>
<tr>
<td>NAMA</td>
<td style="text-align:center;">:</td>
<td>{data['Nama']}</td>
</tr>
<tr>
<td>NO. POLISI</td>
<td style="text-align:center;">:</td>
<td>{data['No Polisi']}</td>
</tr>
<tr>
<td>GOLONGAN</td>
<td style="text-align:center;">:</td>
<td>GOLONGAN {data['Golongan']}</td>
</tr>
<tr>
<td>BERAT</td>
<td style="text-align:center;">:</td>
<td>{data['Berat']} KG</td>
</tr>
<tr>
<td>TARIF</td>
<td style="text-align:center;">:</td>
<td>{data['Tarif']}</td>
</tr>
</table>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="font-size:12px;">
<b>Keterangan :</b>
<table style="width:100%; font-size:11px; border-collapse:collapse; margin-top:2px;">
<tr><td style="vertical-align:top; width:10px;">-</td><td>Tunjukan boarding pass saat naik kapal</td></tr>
<tr><td style="vertical-align:top;">-</td><td>Waktu tertera adalah waktu pelabuhan setempat</td></tr>
<tr><td style="vertical-align:top;">-</td><td>Pintu kapal ditutup 30 menit sebelum keberangkatan</td></tr>
<tr><td style="vertical-align:top;">-</td><td>Harga tiket sudah termasuk asuransi</td></tr>
<tr><td style="vertical-align:top;">-</td><td>Tiket tidak dapat dibatalkan</td></tr>
</table>
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="font-size:11px;">
Butuh informasi lebih lanjut ? Hubungi Call Center ASDP Di
</div>

<div style="display:flex;justify-content:space-between;font-size:15px;margin-top:5px;">
<div>📞 (021)-191</div>
<div>📱 0811 1021 191</div>
<div>✉ cs@asdp.id</div>
</div>

<div style="text-align:center;margin-top:10px;font-weight:bold;">
www.ferizy.com
</div>

<hr style="border-top:1px dashed #000;margin:6px 0;">

<div style="text-align:center;font-size:9px;">
<b>PT. ASDP Indonesia Ferry (Persero)</b><br>
Jl. Jend. Ahmad Yani Kav 52 A, Cempaka Putih Timur<br>
Kota Jakarta Pusat, 10510<br>
NPWP : 01.061.041.8-093.000
</div>

</div>

<br>

<button onclick="downloadImage()">📥 Download PNG</button>

<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>

<script>
function downloadImage() {{
    const ticket = document.getElementById("ticket");
    html2canvas(ticket).then(canvas => {{
        const link = document.createElement('a');
        link.download = 'boarding_pass.png';
        link.href = canvas.toDataURL();
        link.click();
    }});
}}
</script>
"""
    st.components.v1.html(html_template, height=720)
    
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
            berat = st.number_input( "Berat (KG)",min_value=0.0, value=38.50,step=0.01, format="%.2f" )
        
        with col2:
            tujuan = st.text_input("Tujuan", value="BAKAUHENI")
            golongan = st.text_input("Golongan", value="VIB")
            dermaga = st.text_input("Dermaga", value="II")
            no_tiket = st.text_input("No Tiket", value="03A00TLSGT01")
            nopol = st.text_input("No Polisi", value="BE8598AMN")
            tarif = st.text_input("Tarif", value="Rp1.285.200")
            
        submit = st.form_submit_button("Generate Boarding Pass")
        
    if submit:
        # Pengecekan agar integer tidak pakai koma dua digit di belakang
        berat_str = f"{int(berat)}" if float(berat).is_integer() else f"{berat:.2f}"
        
        data = {
            "Asal": asal.upper(), "Tujuan": tujuan.upper(), "Kelas Layanan": kelas.upper(),
            "Golongan": golongan.upper(), "Total PNP": pnp, "Dermaga": dermaga.upper(),
            "Waktu Check-In": waktu, "No Tiket": no_tiket.upper(), "Nama": nama.upper(),
            "No Polisi": nopol.upper(), "Berat": berat_str, "Tarif": tarif
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
            
            # Button untuk merender semua tiket di dalam excel
            if st.button("Tampilkan Semua Boarding Pass"):
                for index, row in df.iterrows():
                    
                    # 1. Parsing & Standarisasi Waktu (Untuk hitung BERLAKU H+1)
                    raw_waktu = row.get("Waktu Check-In")
                    if pd.isna(raw_waktu):
                        waktu_str = "03-05-2026 22:14:54"
                    else:
                        try:
                            # Memaksa pandas baca dengan dayfirst karena format tanggal ID
                            parsed_dt = pd.to_datetime(raw_waktu, dayfirst=True)
                            waktu_str = parsed_dt.strftime("%d-%m-%Y %H:%M:%S")
                        except:
                            waktu_str = str(raw_waktu)
                            
                    # 2. Parsing & Standarisasi Berat (Agar 30.0 jadi 30)
                    raw_berat = row.get("Berat")
                    if pd.isna(raw_berat):
                        berat_str = "0"
                    else:
                        try:
                            num_berat = float(raw_berat)
                            berat_str = f"{int(num_berat)}" if num_berat.is_integer() else f"{num_berat:.3f}"
                        except:
                            berat_str = str(raw_berat)
                            
                    # 3. Parsing & Standarisasi Tarif (Format Ribuan Rp)
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
                    
                    # Mengamankan data ke dalam dictionary
                    data = {
                        "Asal": str(row.get("Asal", "MERAK")).upper(),
                        "Tujuan": str(row.get("Tujuan", "BAKAUHENI")).upper(),
                        "Kelas Layanan": str(row.get("Kelas Layanan", "REGULER")).upper(),
                        "Golongan": str(row.get("Golongan", "VIB")).upper(),
                        "Total PNP": row.get("Total PNP", 1),
                        "Dermaga": str(row.get("Dermaga", "II")).upper(),
                        "Waktu Check-In": waktu_str,
                        "No Tiket": str(row.get("No Tiket", "-")).upper(),
                        "Nama": str(row.get("Nama", "-")).upper(),
                        "No Polisi": str(row.get("No Polisi", "-")).upper(),
                        "Berat": berat_str,
                        "Tarif": tarif_str
                    }
                    render_boarding_pass(data)
                    st.markdown("---") # Pemisah antar struk
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
