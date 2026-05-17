import winsound
import time

def play_audio(type):
    if type == "scan_main":
        winsound.Beep(800, 200) # Nada tinggi (Barang Utama)
    elif type == "scan_bonus":
        winsound.Beep(1200, 200) # Nada lebih tinggi (Barang Bonus)
    elif type == "valid":
        winsound.MessageBeep() # Suara Windows (Sukses)
    elif type == "error":
        winsound.Beep(200, 600) # Nada rendah (Error)

def pda_kasir_b1g1():
    print("="*55)
    print("      SISTEM VALIDATOR PROMO BUY 1 GET 1 (PDA)")
    print("="*55)
    print("Aturan: Setiap Barang 'A' harus punya pasangan Barang 'B'")
    print("Input: A (Main Item), B (Bonus Item), | (Checkout)")
    print("Contoh: A A B B |")
    print("="*55)

    while True:
        raw_input = input("\n[KASIR] Scan Barang: ").strip().upper()
        if raw_input == 'EXIT': break
        
        tokens = raw_input.split()
        stack = []
        is_error = False
        
        print("\n--- Log Transaksi ---")
        for item in tokens:
            if item == 'A':
                stack.append('X') # PUSH: Catat kewajiban bonus
                print(f"Scan A: Barang Utama masuk. (Hutang Bonus: {len(stack)})")
                play_audio("scan_main")
            
            elif item == 'B':
                if len(stack) > 0:
                    stack.pop() # POP: Lunasi kewajiban bonus
                    print(f"Scan B: Barang Bonus masuk. (Sisa Hutang: {len(stack)})")
                    play_audio("scan_bonus")
                else:
                    print("Error: Barang B (Bonus) tidak memiliki pasangan A!")
                    is_error = True
                    break
            
            elif item == '|':
                print("Proses: Menekan tombol Checkout...")
                break
            else:
                print(f"Error: Kode '{item}' tidak terdaftar!")
                is_error = True
                break

        # Evaluasi Akhir PDA
        if not is_error and len(stack) == 0 and '|' in tokens:
            print("\n>>> HASIL: TRANSAKSI VALID (Stok Sinkron) <<<")
            play_audio("valid")
        else:
            if '|' not in tokens:
                print("\n>>> HASIL: GAGAL (Transaksi belum di-Checkout '|') <<<")
            elif len(stack) > 0:
                print(f"\n>>> HASIL: GAGAL (Kurang {len(stack)} Barang Bonus!) <<<")
            else:
                print("\n>>> HASIL: TRANSAKSI DITOLAK (REJECTED) <<<")
            play_audio("error")
        
        print("-" * 55)

if __name__ == "__main__":
    pda_kasir_b1g1()