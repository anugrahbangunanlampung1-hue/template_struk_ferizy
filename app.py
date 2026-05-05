import streamlit as st
import pandas as pd
from weasyprint import HTML, CSS

st.set_page_config(page_title="Generator Boarding Pass Ferizy", layout="centered")

def get_html_template(data):
    """Fungsi untuk menghasilkan string HTML (Rata Kiri untuk mencegah bug Streamlit)"""
    return f"""
<div style="width: 350px; padding: 15px; margin: 0 auto; border: 1px solid #ccc; font-family: monospace; background-color: #fcfcfc; color: #000; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="font-weight: 900; font-size: 24px; font-family: sans-serif; font-style: italic;">ferizy</div>
<div style="text-align: center; font-size: 13px; font-weight: bold; font-family: sans-serif;">BOARDING PASS<br>Untuk Pengguna Jasa</div>
<div style="font-size: 32px; font-weight: bold; font-family: sans-serif;">B</div>
</div>

<hr style="border: none; border-top: 1px dashed #333; margin: 15px 0;">

<div style="display: flex; justify-content: space-between; font-size: 14px; text-align: center;">
<div style="width: 40%; text-align: left;">ASAL<br><b style="font-size: 16px; font-family: sans-serif;">{data['Asal']}</b></div>
<div style="width: 20%; font-size: 20px; line-height: 2;">&#10142;</div>
<div style="width: 40%; text-align: right;">TUJUAN<br><b style="font-size: 16px; font-family: sans-serif;">{data['Tujuan']}</b></div>
</div>

<hr style="border: none; border-top: 1px dashed #333; margin: 15px 0;">

<table style="width: 100%; font-size: 12px; text-align: center; border-collapse: collapse; font-family: sans-serif;">
<tr>
<td>Kelas Layanan<br><b style="font-size: 14px;">{data['Kelas Layanan']}</b></td>
<td>Golongan<br><b style="font-size: 14px;">{data['Golongan']}</b></td>
<td>Total PNP<br><b style="font-size: 14px;">{data['Total PNP']}</b></td>
<td>Dermaga<br><b style="font-size: 14px;">{data['Dermaga']}</b></td>
</tr>
</table>

<div style="font-size: 11px; text-align: center; margin-top: 12px; font-style: italic; color: #444;">
Silakan cek informasi dermaga di pelabuhan dan ikuti arahan petugas untuk menuju ke arah dermaga
</div>

<br>

<div style="position: relative;">
<div style="position: absolute; top: 15%; left: 10%; font-size: 60px; font-weight: bold; color: rgba(200, 200, 200, 0.2); z-index: 0; font-family: sans-serif; letter-spacing: 5px;">
{data['Kelas Layanan']}
</div>
<table style="width: 100%; font-size: 14px; text-align: left; line-height: 1.6; position: relative; z-index: 1;">
<tr><td style="width: 45%;">WAKTU CHECK-IN</td><td>: {data['Waktu Check-In']}</td></tr>
<tr><td>NO. TIKET</td><td>: {data['No Tiket']}</td></tr>
<tr><td>NAMA</td><td>: {data['Nama']}</td></tr>
<tr><td>NO. POLISI</td><td>: {data['No Polisi']}</td></tr>
<tr><td>BERAT</td><td>: {data['Berat']} KG</td></tr>
<tr><td>TARIF</td><td>: {data['Tarif']}</td></tr>
</table>
</div>

<br>

<div style="font-size: 11px; line-height: 1.4;">
<b>Keterangan :</b><br>
- Tunjukkan boarding pass saat naik kapal,<br>
- Waktu yang tertera adalah waktu pelabuhan setempat<br>
- Pintu rampdoor kapal akan ditutup 15 menit sebelum keberangkatan<br>
- Harga tiket sudah termasuk asuransi;<br>
- Tiket tidak dapat dibatalkan;
</div>

<hr style="border: none; border-top: 1px dashed #333; margin: 15px 0;">

<div style="text-align: center; font-size: 11px; line-height: 1.5; font-family: sans-serif;">
Butuh Informasi Lebih Lanjut? Hubungi Call Center ASDP Di :<br>
&#128222; (021) - 191 &nbsp;&nbsp; &#128241; 0811 1021 191 &nbsp;&nbsp; &#9993; cs@asdp.id<br>
<b style="font-size: 13px;">www.ferizy.com</b>
</div>

<hr style="border: none; border-top: 1px dashed #333; margin: 15px 0;">

<div style="text-align: center; font-size: 9px; line-height: 1.3; color: #555;">
<b>PT ASDP Indonesia Ferry (Persero)</b><br>
Jl. Jend. Ahmad Yani Kav 52 A, Cempaka Putih Timur<br>
Kota Jakarta Pusat, 10510<br>
NPWP: 01.061.041.8-093.000<br>
<br>
reg2-2 - (02001077) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; expired : 04-05-2026 22:14:54
</div>
</div>
"""

def generate_pdf_bytes(html_content):
    """Fungsi mengonversi HTML ke PDF ukuran A6 menggunakan WeasyPrint"""
    try:
        # Menambahkan aturan CSS khusus untuk ukuran kertas A6
        page_css = CSS(string='@page { size: A6; margin: 5mm; }')
        pdf_bytes = HTML(string=html_content).write_pdf(stylesheets=[page_css])
        return pdf_bytes
    except Exception as e:
        st.error(f"Error saat membuat PDF: {e}")
        return None

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
        
        html_str = get_html_template(data)
        st.success("Boarding Pass Berhasil Dibuat!")
        st.markdown(html_str, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        pdf_bytes = generate_pdf_bytes(html_str)
        if pdf_bytes:
            st.download_button(
                label="📥 Download PDF (A6)",
                data=pdf_bytes,
                file_name=f"Boarding_Pass_{data['Nama']}_{data['No Polisi']}.pdf",
                mime="application/pdf"
            )

# --- TAB 2: UPLOAD EXCEL ---
with tab2:
    st.subheader("Generate Massal via Excel")
    st.info("Upload file Excel dengan format kolom yang sesuai dengan template.")
    
    uploaded_file = st.file_uploader("Upload file Excel (.xlsx)", type=["xlsx"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success(f"Berhasil membaca {len(df)} data!")
            
            if st.button("Tampilkan Semua Boarding Pass"):
                for index, row in df.iterrows():
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
                    
                    html_str = get_html_template(data)
                    col_preview, col_btn = st.columns([3, 1])
                    
                    with col_preview:
                        st.markdown(html_str, unsafe_allow_html=True)
                        
                    with col_btn:
                        st.write(f"**Data Baris ke-{index+1}**")
                        pdf_bytes = generate_pdf_bytes(html_str)
                        if pdf_bytes:
                            st.download_button(
                                label="📥 Download PDF",
                                data=pdf_bytes,
                                file_name=f"Boarding_Pass_{data['Nama']}_{data['No Polisi']}.pdf",
                                mime="application/pdf",
                                key=f"download_btn_{index}"
                            )
                            
                    st.markdown("---")
                    
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")
