import qrcode

# Data identitas dengan pemisahan baris dan tanda tangan
data = """Nama: HILMAN IHZA AMRULLAH
NIM: 312210310
Kelas: TI.22.A.3
Matakuliah: KRIPTOGRAFI
Tanggal Lahir: 08 APRIL 2005
Tanda Tangan: https://drive.google.com/file/d/1nIqGuZF6W0CDBJIbUmKI2Sxos2TIaEEe/view?usp=sharing
"""

# Membuat QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Membuat gambar QR Code
qr_img = qr.make_image(fill='black', back_color='white')

# Simpan gambar QR Code
qr_img.save("qr_with_signature_text.png")

# Menampilkan hasil
qr_img.show()