import streamlit as st
import pandas as pd
import os

st.set_page_config(
  page_title="Hệ thống dự đoán biến động giá các cổ phiếu nhóm ngành Ngân hàng trong thị trường chứng khoán Việt Nam",
  page_icon="📈",
  layout="wide",
  initial_sidebar_state="expanded"
)
st.title("Hệ thống dự đoán biến động giá các cổ phiếu nhóm ngành Ngân hàng trong thị trường chứng khoán Việt Nam")

# Dark mode
dark_mode_css = """
  <style>
    body {
      background-color: #121212;
      color: white;
    }
    .stApp {
      background-color: #121212;
      color: white;
    }
    .stButton>button {
      background-color: #1DB954;
      color: white;
    }
    .stDataFrame, .stTable {
      background-color: #181818;
      color: white;
    }
  </style>
"""

light_mode_css = """
  <style>
    body {
      background-color: white;
      color: black;
    }
    .stApp {
      background-color: white;
      color: black;
    }
    .stButton>button {
      background-color: black;
      color: white;
    }
    .stDataFrame, .stTable {
      background-color: #f2f2f2;
      color: black
    }
  </style>
"""

dark_mode = st.toggle("🌙 Dark Mode", value=False)

# Apply CSS based on mode
st.markdown(dark_mode_css if dark_mode else light_mode_css, unsafe_allow_html=True)


def in_detail_BID():
    st.header("Giới thiệu")
    st.write("BIDV là một trong những ngân hàng thương mại lớn nhất Việt Nam, với lịch sử phát triển hơn 60 năm.")

    st.header("Lịch sử hình thành")
    history = {
        "1957": "Thành lập với tên gọi Ngân hàng Kiến thiết Việt Nam.",
        "1981": "Đổi tên thành Ngân hàng Đầu tư và Xây dựng Việt Nam.",
        "1990": "Đổi tên thành Ngân hàng Đầu tư và Phát triển Việt Nam.",
        "1995": "Chuyển sang hoạt động như một Ngân hàng thương mại.",
        "2001": "Ngân hàng đầu tiên tại Việt Nam nhận chứng chỉ ISO 9001:2000.",
        "2012": "Thực hiện cổ phần hóa, trở thành Ngân hàng TMCP Đầu tư và Phát triển Việt Nam.",
        "2014": "Niêm yết cổ phiếu trên Sở giao dịch chứng khoán TP.HCM.",
        "2015": "Sáp nhập Ngân hàng Phát triển Nhà Đồng bằng Sông Cửu Long (MHB)."
    }
    for year, event in history.items():
        st.write(f"**{year}**: {event}")

    st.header("Ngành nghề kinh doanh")
    industries = [
        "Cấp tín dụng (cho vay, chiết khấu, bảo lãnh, phát hành thẻ tín dụng…)",
        "Dịch vụ huy động vốn (tiền gửi tiết kiệm, trái phiếu, kỳ phiếu)",
        "Dịch vụ tài trợ thương mại",
        "Dịch vụ thanh toán (trong nước, quốc tế)",
        "Dịch vụ tài khoản",
        "Dịch vụ thẻ ngân hàng",
        "Các dịch vụ khác theo giấy chứng nhận đăng ký kinh doanh"
    ]
    for industry in industries:
        st.write(f"- {industry}")

    st.header("Địa bàn kinh doanh")
    st.write(
        "BIDV có mạng lưới rộng khắp với 182 chi nhánh, 799 phòng giao dịch, 06 văn phòng đại diện ở nước ngoài, và nhiều công ty con."
    )

    st.header("Thông tin liên hệ")
    st.write("**Địa chỉ:** Tháp BIDV, 194 Trần Quang Khải, Hoàn Kiếm, Hà Nội, Việt Nam")
    st.write("**Điện thoại:** +84-(04)-2220 5544")
    st.write("**Fax:** +84-(04)-2220 0399")
    st.write("**Email:** hadautu@bidv.com.vn")
    st.write("**Website:** [BIDV](http://www.bidv.com.vn)")

def in_detail_CTG():
    st.title("Giới thiệu")

    st.header("Lịch sử hình thành")
    st.write("""
    Ngân hàng Thương mại Cổ phần Công thương Việt Nam (VietinBank), tiền thân là Ngân hàng Công thương Việt Nam,
    được thành lập theo Nghị định số 53/NĐ-HĐBT ngày 26/03/1988 của Hội đồng Bộ trưởng.
    """)

    st.header("Ngành nghề kinh doanh")
    st.write("""
    - Cung cấp các dịch vụ ngân hàng bán buôn và bán lẻ trong và ngoài nước.
    - Cho vay và đầu tư, tài trợ thương mại, bảo lãnh và tái bảo lãnh.
    - Kinh doanh ngoại hối, tiền gửi, thanh toán, chuyển tiền, phát hành và thanh toán thẻ tín dụng.
    - Kinh doanh chứng khoán, bảo hiểm và cho thuê tài chính.
    - Cung cấp các dịch vụ tài chính - ngân hàng khác.
    """)

    st.header("Địa bàn kinh doanh")
    st.write("""
    VietinBank có trụ sở chính tại số 108 Trần Hưng Đạo, Quận Hoàn Kiếm, Hà Nội.
    Với 151 chi nhánh trong nước, 2 chi nhánh ở nước ngoài, 3 văn phòng đại diện, gần 1.000 phòng giao dịch.
    """)

    st.header("Thị phần của doanh nghiệp (tính đến 30/9/2015)")
    st.write("""
    - Cho vay: 12,6%
    - Huy động vốn: 9,7%
    - Chuyển tiền: 15%
    - Thanh toán quốc tế: 12,9%
    - Dịch vụ thanh toán thẻ: 21%
    """)

    st.header("Sản phẩm chủ chốt")
    st.write("""
    - Bảo hiểm nhân thọ và phi nhân thọ
    - Tư vấn đầu tư và tài chính
    - Cho thuê tài chính
    - Môi giới chứng khoán, tự doanh, bảo lãnh, phát hành chứng khoán
    - Quản lý tài sản xiết nợ
    """)

    st.header("Vị thế của doanh nghiệp")
    st.write("""
    VietinBank là một trong những ngân hàng chủ lực của hệ thống ngân hàng Việt Nam.
    Định hướng phát triển thành ngân hàng số 1 tại Việt Nam và vươn tầm khu vực Đông Nam Á.
    """)

    st.header("Chiến lược phát triển trong tương lai")
    st.write("""
    VietinBank đặt mục tiêu trở thành ngân hàng hiện đại, đa năng, có tầm cỡ khu vực Đông Nam Á.
    Tập trung vào nâng cao năng lực tài chính, công nghệ, quản trị rủi ro, và đổi mới sáng tạo.
    """)

    st.header("Thông tin liên hệ")
    st.write("""
    - **Địa chỉ:** Số 108 Trần Hưng Đạo, Quận Hoàn Kiếm, Hà Nội
    - **Điện thoại:** (84-24) 3942 1030
    - **Fax:** (84-24) 3942 1032
    - **Email:** investor@vietinbank.vn
    - **Website:** [www.vietinbank.vn](http://www.vietinbank.vn)
    """)

def in_detail_STB():
  st.title("Giới thiệu")

  # Lịch sử hình thành
  st.header("Lịch sử hình thành")
  st.write(
      "Ngân hàng thương mại cổ phần Sài Gòn Thương Tín thành lập năm 1991. Vốn điều lệ ban đầu 3 tỷ đồng. "
      "Vốn điều lệ hiện nay 5.115,6 tỷ đồng.")

  st.write(
      "Ngân hàng có 04 công ty con: "
      "- Công ty Quản lý nợ và khai thác tài sản Sacombank AMC.\n"
      "- Công ty Kiều hối Sacombank SacomRex.\n"
      "- Công ty cho thuê tài chính Sacombank Leasing.\n"
      "- Công ty chứng khoán Sacombank Securities.")

  st.write(
      "Ngân hàng liên doanh và liên kết với Dragon Capital thành lập Công ty liên doanh quản lý Quỹ đầu tư chứng khoán Việt Nam (VietFund Management). "
      "Ngoài ra, ngân hàng có 03 đối tác chiến lược nước ngoài: "
      "- International Financial Company (IFC) thuộc World Bank (7,66% vốn cổ phần).\n"
      "- Dragon Financial Holdings Capital thuộc Anh Quốc (8,77% vốn cổ phần).\n"
      "- Tập đoàn Ngân hàng Australia và New Zealand (ANZ) (9,87% vốn cổ phần).")

  st.write("Tổng số lao động năm 2007: 4.500 người.")
  st.write("Ngân hàng có 190 điểm giao dịch tại 40 tỉnh thành và 9600 đại lý thuộc 240 ngân hàng tại 90 quốc gia.")

  # Ngành nghề kinh doanh
  st.header("Ngành nghề kinh doanh")
  st.write("- Huy động vốn ngắn hạn, trung và dài hạn dưới hình thức tiền gửi có kỳ hạn, không kỳ hạn, chứng chỉ tiền gửi.")
  st.write("- Tiếp nhận vốn đầu tư và phát triển của các tổ chức trong nước, vay vốn của các tổ chức tín dụng khác.")
  st.write("- Cho vay ngắn hạn, trung và dài hạn.")
  st.write("- Chiết khấu thương phiếu, trái phiếu và giấy tờ có giá.")
  st.write("- Hùn vốn và liên doanh theo pháp luật.")
  st.write("- Làm dịch vụ thanh toán giữa các khách hàng.")
  st.write("- Kinh doanh ngoại tệ, vàng bạc, thanh toán quốc tế.")
  st.write("- Hoạt động thanh toán và huy động vốn từ nước ngoài.")

  # Thông tin liên hệ
  st.header("Thông tin liên hệ")
  st.write("**Địa chỉ:** 266-268 Nam Kỳ Khởi Nghĩa, Phường 8, Quận 3, TP. HCM")
  st.write("**Điện thoại:** 84-(8) 3932 04 20")
  st.write("**Fax:** 84-(8) 3932 04 24")
  st.write("**Người công bố thông tin:** Ông Hà Văn Trung")
  st.write("**Email:** info@sacombank.com")
  st.write("**Website:** [Sacombank](http://www.sacombank.com.vn)")

def in_detail_TCB():
  st.title("Giới thiệu")

  # Nội dung Lịch sử hình thành
  st.subheader('Lịch sử hình thành:')
  st.markdown("""
      Được thành lập ngày 27/09/1993 với số vốn ban đầu là 20 tỷ đồng, trải qua 18 năm hoạt động, đến nay Techcombank đã trở thành một trong những ngân hàng thương mại cổ phần hàng đầu Việt Nam với tổng tài sản đạt trên 180.874 tỷ đồng (tính đến hết năm 2011).
      Techcombank có cổ đông chiến lược là ngân hàng HSBC với 20% cổ phần. Với mạng lưới hơn 300 chi nhánh, phòng giao dịch trên 44 tỉnh và thành phố trong cả nước, dự kiến đến cuối năm 2012, Techcombank sẽ tiếp tục mở rộng, nâng tổng số Chi nhánh và Phòng giao dịch lên trên 360 điểm trên toàn quốc. Techcombank còn là ngân hàng đầu tiên và duy nhất được Financial Insights tặng danh hiệu Ngân hàng dẫn đầu về giải pháp và ứng dụng công nghệ. Hiện tại, với đội ngũ nhân viên lên tới trên 7.800 người, Techcombank luôn sẵn sàng đáp ứng mọi yêu cầu về dịch vụ dành cho khách hàng. Techcombank hiện phục vụ trên 2,3 triệu khách hàng cá nhân, trên 66.000 khách hàng doanh nghiệp.
  """)

  # Các cột mốc lịch sử
  st.subheader('Các cột mốc lịch sử:')
  st.markdown("""
      - **1994-1995:** Tăng vốn điều lệ lên 51,495 tỷ đồng. Thành lập Chi nhánh Techcombank Hồ Chí Minh.
      - **1996:** Thành lập Chi nhánh Techcombank Thăng Long tại Hà Nội.
      - **1998:** Trụ sở chính được chuyển sang Toà nhà Techcombank tại Hà Nội.
      - **1999:** Tăng vốn điều lệ lên 80,020 tỷ đồng. Khai trương Phòng giao dịch số 3 tại phố Khâm Thiên, Hà Nội.
      - **2000:** Thành lập Phòng Giao dịch Thái Hà tại Hà Nội.
      - **2001:** Ký kết hợp đồng với Temenos Holding NV để triển khai hệ thống phần mềm ngân hàng GLOBUS.
      - **2002:** Thành lập Chi nhánh Hải Phòng và Thanh Khê tại Đà Nẵng.
      - **2003:** Chính thức phát hành thẻ thanh toán F@stAccess-Connect 24.
      - **2004:** Tăng vốn điều lệ lên 234 tỉ đồng.
      - **2005:** Thành lập các chi nhánh cấp 1 tại các tỉnh. Khai trương phần mềm chuyển mạch và quản lý thẻ của hãng Compass Plus.
      - **2006:** Nhận giải thưởng về thanh toán quốc tế từ Bank of NewYorks, Citibank.
      - **2007:** Tổng tài sản đạt gần 2,5 tỷ USD.
      - **2008:** Ra mắt thẻ tín dụng Techcombank Visa Credit.
      - **2009:** Tăng vốn điều lệ lên 5.400 tỷ đồng và ký kết hợp đồng tài trợ vốn vay.
      - **2010:** Triển khai chương trình chuyển đổi chiến lược tổng thể và tái cấu trúc mô hình kinh doanh.
      - **2011:** Nhận giải thưởng “Ngân hàng tốt nhất Việt Nam 2011” do các tổ chức quốc tế trao tặng.
  """)

  # Các giải thưởng
  st.subheader('Các giải thưởng nổi bật:')
  st.markdown("""
      - **2011:**
          - “Ngân hàng tốt nhất Việt Nam” do Finance Asia trao tặng.
          - “Ngân hàng thanh toán quốc tế xuất sắc năm 2009” do Citi Bank trao tặng.
          - “Ngân hàng quản lý tiền tệ tốt nhất Việt Nam” do Alpha South East Asia trao tặng.
          - “Ngân hàng cung cấp ngoại hối tốt nhất Việt Nam” do Asia Money trao tặng.
      - **2010:**
          - Giải thưởng “Ngôi sao quốc tế dẫn đầu về quản lý chất lượng” do BID trao tặng.
          - Giải thưởng “Thương hiệu quốc gia 2010”.
  """)

  # Thông tin về các dịch vụ và sản phẩm
  st.subheader('Dịch vụ và sản phẩm nổi bật:')
  st.markdown("""
      - **Sản phẩm dịch vụ ngân hàng:** Techcombank cung cấp đa dạng các dịch vụ tài chính cá nhân và doanh nghiệp, bao gồm các sản phẩm vay tiêu dùng, thẻ tín dụng, dịch vụ chuyển tiền quốc tế, thanh toán hóa đơn, và các sản phẩm tiết kiệm.
      - **Ứng dụng công nghệ:** Techcombank luôn tiên phong trong việc ứng dụng công nghệ mới nhất, bao gồm F@st i-Bank, các giải pháp thanh toán điện tử F@stVietPay, và hệ thống ATM hiện đại.
  """)

  # Thông tin liên hệ
  st.subheader('Thông tin liên hệ:')
  st.markdown("""
      - **Địa chỉ:** 191 Bà Triệu, Phường Lê Đại Hành, Quận Hai Bà Trưng, Hà Nội
      - **Điện thoại:** +84-(04)-3944 6368
      - **Fax:** +84-(04)-3944 63695
      - **Email:** ho@techcombank.com.vn
      - **Website:** [Techcombank](http://www.techcombank.com.vn)
  """)


def in_detail_VCB():
    st.title("Giới thiệu")

    st.header("Lịch sử hình thành")
    st.write("""
    Ngân hàng TMCP Ngoại Thương Việt Nam (Vietcombank) được thành lập ngày 30 tháng 10 năm 1962
    theo Quyết định số 115/CP do Hội đồng Chính phủ ban hành trên cơ sở tách ra từ Cục quản lý Ngoại hối trực thuộc Ngân hàng Trung ương.
    - Ngày 01 tháng 04 năm 1963, chính thức khai trương hoạt động NHNT như một ngân hàng đối ngoại độc quyền.
    - Ngày 14 tháng 11 năm 1990, NHNT chuyển từ ngân hàng chuyên doanh sang NHTM Nhà nước đa năng.
    - Ngày 21 tháng 09 năm 1996, NHNT được thành lập lại theo mô hình Tổng công ty 90, 91 và mang tên Vietcombank.
    - Tính đến cuối năm 2006, Vietcombank đã phát triển thành một ngân hàng đa năng với 58 chi nhánh, 87 phòng giao dịch và các công ty con trong và ngoài nước.
    - Năm 2008, Vietcombank chuyển sang mô hình ngân hàng thương mại cổ phần với vốn điều lệ 12.100 tỷ đồng.
    """)

    st.header("Ngành nghề kinh doanh")
    st.write("""
    - **Huy động vốn**: Nhận tiền gửi, phát hành giấy tờ có giá, vay vốn từ các tổ chức tín dụng trong và ngoài nước, vay tái cấp vốn từ Ngân hàng Nhà nước.
    - **Hoạt động tín dụng**: Cho vay, chiết khấu thương phiếu, bảo lãnh, cấp tín dụng dưới các hình thức khác.
    - **Dịch vụ thanh toán và ngân quỹ**: Mở tài khoản tiền gửi, cung ứng phương tiện thanh toán, thực hiện các dịch vụ thanh toán trong nước và quốc tế.
    - **Kinh doanh ngoại hối và vàng**: Thực hiện kinh doanh ngoại hối và vàng trên thị trường quốc tế và trong nước.
    - **Các hoạt động khác**: Góp vốn, mua cổ phần, tham gia thị trường tiền tệ, ủy thác, dịch vụ bảo hiểm, tư vấn tài chính, cho thuê tủ két.
    """)

    st.header("Địa bàn kinh doanh")
    st.write("""
    Vietcombank có **96 chi nhánh** và **368 phòng giao dịch** tại **50/63 tỉnh thành** trong cả nước.
    Mạng lưới hoạt động được phân bố rộng khắp:
    - **Bắc Trung Bộ**: 8,3%
    - **Đông Bắc Bộ**: 7,3%
    - **Đồng bằng Sông Hồng**: 10,4%
    - **Hà Nội**: 15,6%
    - **Đồng bằng Sông Cửu Long**: 14,6%
    - **Đông Nam Bộ**: 11,5%
    - **Hồ Chí Minh**: 17,7%
    - **Nam Trung Bộ**: 10,4%
    - **Tây Nguyên**: 4,2%
    - Ngoài ra, Vietcombank còn có **1856 ngân hàng đại lý** tại **176 quốc gia** và **vùng lãnh thổ** trên toàn thế giới.
    """)

    st.header("Thông tin liên hệ")
    st.write("""
    - **Địa chỉ**: Tầng 15 - Tòa nhà Vietcombank Tower, 198 Trần Quang Khải, Q. Hoàn Kiếm, Hà Nội
    - **Điện thoại**: +84-(04) 3934 3137
    - **Fax**: +84-(04) 3824 1395
    - **Email**: [ir@vietcombank.com.vn](mailto:ir@vietcombank.com.vn)
    - **Website**: [www.vietcombank.com.vn](http://www.vietcombank.com.vn)
    """)

def in_detail_VPB():
  # Introduction
  st.header("Giới thiệu")
  st.markdown(
      """
      Là một trong những ngân hàng thương mại cổ phần được thành lập sớm nhất tại Việt Nam, VPBank đã có lịch sử phát triển bền vững trong 30 năm. Hiện nay, VPBank là một trong những ngân hàng thương mại hàng đầu tại Việt Nam về hiệu quả và lợi nhuận kinh doanh. Ngân hàng hoạt động mạnh mẽ trong các phân khúc bán lẻ và SME, đồng thời tiên phong trong chuyển đổi số để mang lại sản phẩm, dịch vụ tài chính tốt nhất và nhanh nhất.

      - **Tổng tài sản (31/12/2022):** xấp xỉ 27 tỷ USD
      - **Chi nhánh trên toàn quốc:** 251
      - **Hệ số CAR:** xấp xỉ 15%
      """
  )

  # History
  st.header("Lịch sử hình thành")
  st.markdown(
      """
      - **12/08/1993:** Thành lập theo Giấy phép số 0042/NH-GP.
      - **27/07/2010:** Đổi tên thành Ngân hàng TMCP Việt Nam Thịnh Vượng.
      - **20/08/2013:** Nhận bằng khen của Thống đốc NHNN Việt Nam.
      - **17/08/2017:** 1,33 tỷ cổ phiếu VPBank (mã VPB) chính thức giao dịch trên HOSE.
      - **21/10/2018:** Đồng tổ chức giải chạy Hanoi International Heritage Marathon.
      - **01/02/2019:** VPBank lọt Top 500 Thương hiệu Ngân hàng giá trị nhất toàn cầu.
      - **04/2019:** Áp dụng tiêu chuẩn Basel II.
      - **04/2021:** Bán 49% vốn điều lệ tại FE Credit cho Tập đoàn SMBC Nhật Bản.
      - **27/03/2023:** Bán 15% vốn điều lệ cho Ngân hàng SMBC Nhật Bản.
      """
  )

  # Network
  st.header("Mạng lưới hoạt động")
  st.markdown(
      """
      - **Tổng số chi nhánh & phòng giao dịch:** 260
      - **Tại Hà Nội:** 1 Trụ sở chính, 259 chi nhánh và phòng giao dịch.
      - **Miền Bắc:** 122 Chi nhánh & Phòng giao dịch (Bắc Ninh, Bắc Giang, Vĩnh Phúc,...).
      - **Miền Trung:** 49 Chi nhánh & Phòng giao dịch (Thanh Hóa, Nghệ An, Hà Tĩnh,...).
      - **Miền Nam:** 79 Chi nhánh & Phòng giao dịch (TP Hồ Chí Minh, Đồng Nai,...).
      """
  )

  # Services
  st.header("Sản phẩm, dịch vụ chính")
  st.markdown(
      """
      - Huy động vốn (nhận tiền gửi VNĐ, ngoại tệ, vàng).
      - Sử dụng vốn (cấp tín dụng, hùn vốn, liên doanh).
      - Dịch vụ trung gian (thanh toán, ngân quỹ, kiều hối).
      - Kinh doanh ngoại tệ.
      - Phát hành & thanh toán thẻ tín dụng, thẻ ghi nợ.
      """
  )

  # Contact Information
  st.header("Liên hệ")
  st.markdown("**Địa chỉ:** Số 89 Láng Hạ, phường Láng Hạ, quận Đống Đa, TP Hà Nội")
  st.markdown("**Điện thoại:** 84-(4) 3928 8869")
  st.markdown("**Fax:** 84-(4) 3928 8867")
  st.markdown("**Email:** customercare@vpb.com.vn")
  st.markdown("**Website:** [VPBank](https://www.vpbank.com.vn/)")


# Hàm hiển thị thông tin chi tiết về cổ phiếu
def show_stock_details(stock_code, bank_url):
  tab1, tab2, tab3, tab4 = st.tabs(["Thông tin doanh nghiệp", "Lịch sử giao dịch", "Dự đoán", "Tin tức tổng hợp"])
  info ={"BID":['Ngân hàng thương mại','68,975,274,390,000 đồng','6,897,515,268 cp','7,021,361,917 cp'],
         "CTG":['Ngân hàng thương mại','53,699,917,480,000 đồng','5,369,991,748 cp','5,369,991,748 cp'],
         "STB":['Ngân hàng thương mại','18,852,157,160,000 đồng','1,885,215,716 cp','1,885,215,716 cp'],
         "TCB":['Ngân hàng thương mại','70,450 tỷ đồng','7,094,851,739 cp','7,094,651,739 cp'],
         "VCB":['Ngân hàng thương mại','83,556,914,350,000 đồng','5,589,091,262 cp','8,355,675,094 cp'],
         "VPB":['Ngân hàng thương mại','79,339,236,010,000 đồng','7,933,923,601 cp','7,933,923,601 cp'],}
  with tab1:
    st.header(f"Thông tin về {stock_code}")

    # Tạo layout với hai cột
    col1, col2 = st.columns([1, 2])  # Chia tỷ lệ 1:2 giữa logo và thông tin

    with col1:
        def get_image_base64(image_path):
            import base64
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        # Hiển thị logo doanh nghiệp
        logo_path = f"LOGO_{stock_code}.jpg"
        logo_html = ""
      
        st.markdown(
            f"""
            <div style="border: 2px solid #000; padding: 5px; display: inline-block;">
                <img src="data:image/jpg;base64,{get_image_base64(logo_path)}" width="250">
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
      st.markdown(f"**Nhóm ngành:** {info[stock_code][0]}")
      st.markdown(f"**Vốn điều lệ:** {info[stock_code][1]}")
      st.markdown(f"**KL CP đang niêm yết:** {info[stock_code][2]}")
      st.markdown(f"**KL CP đang lưu hành:** {info[stock_code][3]}")

    # Hiển thị banner giá trị cốt lõi từ Google Drive
    banner_path = f"{stock_code}_GTCL.png"
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)

    if stock_code == "BID":
      in_detail_BID()
    elif stock_code == "CTG":
      in_detail_CTG()
    elif stock_code == "STB":
      in_detail_STB()
    elif stock_code == "TCB":
      in_detail_TCB()
    elif stock_code == "VCB":
      in_detail_VCB()
    elif stock_code == "VPB":
      in_detail_VPB()

  with tab2:
    # st.header(f"Lịch sử giao dịch {stock_code}")
    st.markdown(
      f"<h1 style='text-align: center;'>{f'Lịch sử giao dịch {stock_code}'}</h1>",
      unsafe_allow_html=True
    )
    start_date_tab2 = st.date_input("Chọn ngày bắt đầu", min_value=pd.to_datetime("2020-01-01"), key= "start_date_tab2")
    end_date_tab2 = st.date_input("Chọn ngày kết thúc", min_value=start_date_tab2, key= "end_date_tab2")

    @st.cache_data
    def load_data(file_path):
      try:
        return pd.read_csv(file_path, encoding='utf-8', sep=',', on_bad_lines='skip')
      except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='ISO-8859-1', sep=',', on_bad_lines='skip')
      except pd.errors.ParserError:
        return pd.read_csv(file_path, encoding='utf-8', sep=';', on_bad_lines='skip')

    def display_paginated_data(df, rows_per_page=10):
      total_rows = len(df)
      if total_rows == 0:
        st.warning("Không có dữ liệu trong khoảng thời gian này.")
        return

      total_pages = (total_rows + rows_per_page - 1) // rows_per_page
      page = st.number_input("Chọn trang:", min_value=1, max_value=total_pages, step=1)

      start_row = (page - 1) * rows_per_page
      end_row = min(start_row + rows_per_page, total_rows)

      st.write(df.iloc[start_row:end_row])

    file_path = f"Price_{stock_code}.csv"


    df = load_data(file_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    df_filtered = df[(df['Date'] >= pd.to_datetime(start_date_tab2)) & (df['Date'] <= pd.to_datetime(end_date_tab2))]
    display_paginated_data(df_filtered)



  with tab3:
    st.markdown(
      f"<h1 style='text-align: center;'>{f'Dự đoán giá {stock_code}'}</h1>",
      unsafe_allow_html=True
    )

    chart_files = [
      f"LSTM_{stock_code}_final.png",
      f"GRU_{stock_code}_final.png",
      f"CNN_GRU_{stock_code}_final.png",
    ]

    captions = {
      'LSTM': f"<h3 style='text-align: center; font-weight: bold; font-size: 25px;'>Hình 1: Biểu đồ so sánh giá Đóng cửa thực tế và dự đoán của {stock_code} dựa trên mô hình LSTM</h3>",
      'GRU': f"<h3 style='text-align: center; font-weight: bold; font-size: 25px;'>Hình 2: Biểu đồ so sánh giá Đóng cửa thực tế và dự đoán của {stock_code} dựa trên mô hình GRU</h3>",
      'CNNGRU': f"<h3 style='text-align: center; font-weight: bold; font-size: 25px;'>Hình 3: Biểu đồ so sánh giá Đóng cửa thực tế và dự đoán của {stock_code} dựa trên mô hình CNN-GRU</h3>",
    }

    found_chart = False
    for chart_file in chart_files:
        chart_path = chart_file
        model_type = chart_file.split('_')[0]

   
        st.markdown(
        """
        <style>
            .stImage img {
              display: block;
              margin-left: auto;
              margin-right: auto;
              width: 80%;  /* Điều chỉnh chiều rộng ảnh nhỏ lại */
              max-width: 800px;  /* Kích thước tối đa */
            }
        </style>
        """, unsafe_allow_html=True)
        st.image(chart_path)
        # st.markdown(captions.get(model_type, "Biểu đồ không xác định"), unsafe_allow_html=True)
        found_chart = True


  with tab4:
    st.header(f"Tin tức tổng hợp {stock_code}")
    # Hàm đọc dữ liệu từ file .xlsx
    @st.cache_data
    def load_data_from_excel(file_path_xlsx):
        return pd.read_excel(file_path_xlsx)

    # Hàm hiển thị card tin tức
    def display_news_cards(df):
      # Chuyển đổi giá trị cột Sentiment
      df['Sentiment'] = df['Sentiment'].replace({'Positive': 'Tích cực', 'Negative': 'Tiêu cực'})
      df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

      cols = st.columns(4)  # Chia layout thành 4 cột

      for i, row in df.iterrows():
        with cols[i % 4]:  # Xoay vòng qua các cột
          description = row['Description']
          # Kiểm tra xem 'Description' có phải là chuỗi không, nếu không thì gán là chuỗi rỗng
          if isinstance(description, str):
            description_preview = description[:100]
          else:
            description_preview = ""
          st.markdown(
            f"""
            <a href="{row['Link']}" target="_blank" style="text-decoration: none">
              <div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; margin-bottom: 16px; background-color: #f9f9f9;">
                <span style="font-size: 14px; font-weight: bold; color: {'green' if row['Sentiment'] == 'Tích cực' else 'red'}; " >
                  {row["Sentiment"]}
                </span>
                <h4 style="margin: 8px 0;" class="title">{row['Title']}</h4>
                <p style="font-size: 14px; color: #555;">{description_preview}...</p>
                <p style="font-size: 12px; color: #555; position: absolute; bottom: 10px, right: 15px">{row['Date']}</p>
              </div>
            </a>

            """, unsafe_allow_html=True
          )

    file_path_xlsx = f"sentiment_voting_{stock_code}.xlsx"
    start_date_tab4 = st.date_input("Chọn ngày bắt đầu", min_value=pd.to_datetime("2020-01-01"), key= "start_date_tab4")
    end_date_tab4 = st.date_input("Chọn ngày kết thúc", min_value=start_date_tab4, key= "end_date_tab4")
    
    df = load_data_from_excel(file_path_xlsx)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    df_filtered = df[(df['Date'] >= pd.to_datetime(start_date_tab4)) & (df['Date'] <= pd.to_datetime(end_date_tab4))]
    display_news_cards(df_filtered)

# Cập nhật mã cổ phiếu và URL tương ứng
def show_BID():
    show_stock_details("BID", "https://cafef.vn/du-lieu/hose/bid-ngan-hang-thuong-mai-co-phan-dau-tu-va-phat-trien-viet-nam.chn")

def show_CTG():
    show_stock_details("CTG", "https://cafef.vn/du-lieu/hose/ctg-ngan-hang-cong-thuong-viet-nam.chn")

def show_STB():
    show_stock_details("STB", "https://cafef.vn/du-lieu/hose/stb-ngan-hang-sacombank.chn")

def show_TCB():
    show_stock_details("TCB", "https://cafef.vn/du-lieu/hose/tcb-ngan-hang-techcombank.chn")

def show_VCB():
    show_stock_details("VCB", "https://cafef.vn/du-lieu/hose/vcb-ngan-hang-vietcombank.chn")

def show_VPB():
    show_stock_details("VPB", "https://cafef.vn/du-lieu/hose/vpb-ngan-hang-vpbank.chn")

# Các trang cho từng mã cổ phiếu
pages = {
    "BID": show_BID,
    "CTG": show_CTG,
    "STB": show_STB,
    "TCB": show_TCB,
    "VCB": show_VCB,
    "VPB": show_VPB,
}

option = st.selectbox(
    "Chọn 1 mã chứng khoán",
    list(pages.keys()),
)

if option:
    pages[option]()