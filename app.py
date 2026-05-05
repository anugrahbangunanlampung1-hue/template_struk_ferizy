def get_html_template(data):
    """Fungsi untuk menghasilkan string HTML (Rata Kiri untuk mencegah bug Streamlit)"""
    return f"""
<div style="width: 320px; padding: 15px; margin: 0 auto; font-family: monospace; background-color: #ffffff; color: #000;">
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <div style="font-weight: 900; font-size: 26px; font-family: sans-serif; font-style: italic;">ferizy</div>
        <div style="text-align: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">BOARDING PASS<br>Untuk Pengguna Jasa</div>
        <div style="font-size: 30px; font-weight: bold; font-family: sans-serif;">B</div>
    </div>
    
    <hr style="border: none; border-top: 1px dashed #333; margin: 10px 0;">
    
    <div style="display: flex; justify-content: space-between; font-size: 12px; text-align: center;">
        <div style="width: 40%; text-align: left;">
            <span style="font-size: 10px;">ASAL</span><br>
            <b style="font-size: 16px; font-family: sans-serif;">{data['Asal']}</b>
        </div>
        <div style="width: 20%; font-size: 16px; line-height: 2;">&#10142;</div>
        <div style="width: 40%; text-align: right;">
            <span style="font-size: 10px;">TUJUAN</span><br>
            <b style="font-size: 16px; font-family: sans-serif;">{data['Tujuan']}</b>
        </div>
    </div>
    
    <hr style="border: none; border-top: 1px dashed #333; margin: 10px 0;">
    
    <table style="width: 100%; font-size: 10px; text-align: center; border-collapse: collapse; font-family: sans-serif;">
        <tr>
            <td style="padding: 2px;">Kelas Layanan<br><b style="font-size: 13px;">{data['Kelas Layanan']}</b></td>
            <td style="padding: 2px;">Golongan<br><b style="font-size: 13px;">{data['Golongan']}</b></td>
            <td style="padding: 2px;">Total PNP<br><b style="font-size: 13px;">{data['Total PNP']}</b></td>
            <td style="padding: 2px;">Dermaga<br><b style="font-size: 13px;">{data['Dermaga']}</b></td>
        </tr>
    </table>
    
    <div style="font-size: 10px; text-align: center; margin-top: 10px; font-style: italic; color: #444;">
        Silakan cek informasi dermaga di pelabuhan dan ikuti arahan petugas untuk menuju ke arah dermaga
    </div>
    
    <br>
    
    <div style="position: relative; padding: 5px 0;">
        <div style="position: absolute; top: 30%; left: 0; right: 0; text-align: center; font-size: 50px; font-weight: bold; color: rgba(200, 200, 200, 0.2); z-index: 0; font-family: sans-serif; letter-spacing: 2px; overflow: hidden; white-space: nowrap;">
            {data['Kelas Layanan']}
        </div>
        <table style="width: 100%; font-size: 12px; text-align: left; line-height: 1.8; position: relative; z-index: 1; font-family: monospace;">
            <tr><td style="width: 40%; white-space: nowrap;">WAKTU CHECK-IN</td><td style="width: 5%;">:</td><td>{data['Waktu Check-In']}</td></tr>
            <tr><td style="white-space: nowrap;">NO. TIKET</td><td>:</td><td>{data['No Tiket']}</td></tr>
            <tr><td style="white-space: nowrap;">NAMA</td><td>:</td><td>{data['Nama']}</td></tr>
            <tr><td style="white-space: nowrap;">NO. POLISI</td><td>:</td><td>{data['No Polisi']}</td></tr>
            <tr><td style="white-space: nowrap;">BERAT</td><td>:</td><td>{data['Berat']} KG</td></tr>
            <tr><td style="white-space: nowrap;">TARIF</td><td>:</td><td>{data['Tarif']}</td></tr>
        </table>
    </div>
    
    <br>
    
    <div style="font-size: 10px; line-height: 1.4; font-family: sans-serif;">
        <b>Keterangan :</b><br>
        - Tunjukkan boarding pass saat naik kapal,<br>
        - Waktu yang tertera adalah waktu pelabuhan setempat<br>
        - Pintu rampdoor kapal akan ditutup 15 menit sebelum<br>
        &nbsp;&nbsp;keberangkatan<br>
        - Harga tiket sudah termasuk asuransi;<br>
        - Tiket tidak dapat dibatalkan;
    </div>
    
    <hr style="border: none; border-top: 1px dashed #333; margin: 10px 0;">
    
    <div style="text-align: center; font-size: 10px; line-height: 1.5; font-family: sans-serif;">
        Butuh Informasi Lebih Lanjut? Hubungi Call Center ASDP Di :<br>
        (021) - 191 &nbsp;&nbsp;|&nbsp;&nbsp; 0811 1021 191 &nbsp;&nbsp;|&nbsp;&nbsp; cs@asdp.id<br>
        <b style="font-size: 12px;">www.ferizy.com</b>
    </div>
    
    <hr style="border: none; border-top: 1px dashed #333; margin: 10px 0;">
    
    <div style="text-align: center; font-size: 9px; line-height: 1.3; color: #333; font-family: sans-serif;">
        <b>PT ASDP Indonesia Ferry (Persero)</b><br>
        Jl. Jend. Ahmad Yani Kav 52 A, Cempaka Putih Timur<br>
        Kota Jakarta Pusat, 10510<br>
        NPWP: 01.061.041.8-093.000<br>
        <br>
        reg2-2 - (02001077) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; expired : 04-05-2026 22:14:54
    </div>
</div>
"""
