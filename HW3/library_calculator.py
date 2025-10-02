# file: library_calculator.py

def calculate_discount(so_sach_muon_trung_binh: int, thoi_gian_gia_han: int) -> str:
    """
    Tính toán mức chiết khấu phí gia hạn thẻ thư viện dựa trên các quy tắc.

    Args:
        so_sach_muon_trung_binh: Số sách mượn trung bình mỗi tháng (nguyên).
        thoi_gian_gia_han: Số tháng gia hạn (nguyên).

    Returns:
        Một chuỗi chứa mức chiết khấu hoặc "Invalid".
    """
    if not (0 <= so_sach_muon_trung_binh <= 20 and 1 <= thoi_gian_gia_han <= 12):
        return "Invalid"
    if thoi_gian_gia_han < 6:
        if so_sach_muon_trung_binh < 5:
            return "0% discount" 
        elif 5 <= so_sach_muon_trung_binh <= 10:
            return "10% discount"
        else:  # so_sach_muon_trung_binh > 10
            return "20% discount" 
    else:  # thoi_gian_gia_han >= 6
        if so_sach_muon_trung_binh < 5:
            return "5% discount"  # [cite: 19]
        elif 5 <= so_sach_muon_trung_binh <= 10:
            return "15% discount" # [cite: 20]
        else:  # so_sach_muon_trung_binh > 10
            return "25% discount" 