import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

# =========================
# NHẬP THÔNG TIN
# =========================

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Đổi lãi suất % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Tiền lãi toàn bộ kỳ hạn
    tong_tien_lai = so_tien_gui * lai_suat_nam * ky_han / 12

    # Tính lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
        so_ky = 1
        don_vi = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = tong_tien_lai / ky_han
        so_ky = ky_han
        don_vi = "tháng"

    else:  # Hàng quý
        so_quy = ky_han / 3
        tien_lai_dinh_ky = tong_tien_lai / so_quy
        so_ky = so_quy
        don_vi = "quý"

    # Tổng gốc + lãi
    tong_tien_nhan = so_tien_gui + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ TÍNH TOÁN THÀNH CÔNG")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.metric(
        "💰 Tổng tiền gốc + lãi",
        f"{tong_tien_nhan:,.0f} VNĐ"
    )

    # Thông tin chi tiết
    st.divider()

    st.write("### 📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc == "Cuối kỳ":
        st.info(
            f"Bạn nhận toàn bộ tiền lãi vào cuối kỳ: "
            f"**{tong_tien_lai:,.0f} VNĐ**."
        )

    elif hinh_thuc == "Hàng tháng":
        st.info(
            f"Mỗi tháng bạn nhận khoảng: "
            f"**{tien_lai_dinh_ky:,.0f} VNĐ**."
        )

    else:
        st.info(
            f"Mỗi quý bạn nhận khoảng: "
            f"**{tien_lai_dinh_ky:,.0f} VNĐ**."
)
