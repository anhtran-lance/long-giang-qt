# -*- coding: utf-8 -*-
"""Nguồn dữ liệu chung cho bản HTML và Excel – Tập đoàn Long Giang."""

UNITS = {
    "LGG": "Tập đoàn Long Giang (khối hỗ trợ)",
    "LGL": "Long Giang Land – phát triển dự án",
    "LGEC": "Long Giang E&C – tổng thầu xây lắp",
    "RI": "Rivera Invest / Rivera Homes – khai thác & vận hành",
}

# (mã nhóm, tên lĩnh vực như file danh mục, đơn vị, [tên QT...])
CATALOG = [
    ("PTDA", "PTDA - LGL", "LGL", [
        "Quy trình Lập và Phê duyệt kế hoạch công tác Phát triển dự án",
        "Quy trình lập và phê duyệt văn bản gửi các Cơ quan QLNN về Pháp lý Dự án",
        "Quy trình đàm phán, soạn thảo và ký kết hợp đồng M&A",
        "Quy trình triển khai công tác giải phóng mặt bằng/nhận chuyển nhượng đất Dự án",
        "Quy trình lập và phê duyệt chủ trương điều chỉnh Dự án đầu tư"]),
    ("QLDA-LGL", "QLDA - LGL", "LGL", [
        "Quy trình phê duyệt hồ sơ thiết kế của Dự án",
        "Quy trình quản lý hợp đồng với Đơn vị tư vấn/NT/NCC",
        "Quy trình kiểm soát hồ sơ tài liệu của Dự án"]),
    ("QLDA-LGEC", "QLDA - LGEC", "LGEC", [
        "Quy trình quản lý tiến độ thi công Công trình",
        "Quy trình quản lý chất lượng: vật tư - thiết bị đầu vào, quy trình thi công, nghiệm thu",
        "Quy trình sửa lỗi chất lượng các hạng mục của Công trình",
        "Quy trình kiểm soát KH công tác AN-PCCN-ATLĐ-VSMT-NDTH các công trình",
        "Quy trình lập và nộp hồ sơ thanh toán với CĐT",
        "Quy trình thanh toán cho các đơn vị tư vấn/NT/NCC",
        "Quy trình lựa chọn Nhà thầu phụ/NCC"]),
    ("CUNGUNG", "Cung ứng VT-TB LGEC", "LGEC", [
        "Quy trình đặt hàng VT - TB",
        "Quy trình cấp Vật tư - Thiết bị",
        "Quy trình kiểm soát công tác bảo dưỡng, sửa chữa Thiết bị thi công"]),
    ("KD", "Kinh doanh - LGL", "LGL", [
        "Quy trình kiểm soát giá bán và chính sách bán hàng",
        "Quy trình lập và phê duyệt Phương án kinh doanh Dự án",
        "Quy trình kiểm soát công tác CSKH, khiếu nại và cam kết với Khách hàng",
        "Quy trình phê duyệt và đăng thông tin tiếp thị của dự án",
        "Quy trình ký HĐ/PLHĐ mua bán sản phẩm Bất động sản",
        "Quy trình phê duyệt các đề xuất của ĐV Tư vấn quản lý bán hàng/môi giới",
        "Quy trình tiếp nhận và xử lý thông tin khách hàng"]),
    ("QLVH", "QLVH – RI", "RI", [
        "Quy trình lập và phê duyệt dự toán chi phí vận hành của toà nhà",
        "Quy trình kiểm soát chất lượng dịch vụ tòa nhà",
        "Quy trình lập và phê duyệt dự toán chi phí bảo dưỡng/sửa chữa TSCĐ"]),
    ("QLTS", "QLTS - RI", "RI", [
        "Quy trình kiểm kê tài sản và hồ sơ tài liệu quan trọng",
        "Quy trình kiểm soát công tác vận hành HTKT",
        "Quy trình kiểm soát công tác bảo dưỡng sửa chữa HTKT"]),
    ("TT", "Truyền thông - LGG", "LGG", [
        "Quy trình soạn thảo và đăng tin bài Truyền thông đối ngoại và thương hiệu",
        "Quy trình xử lý khủng hoảng Truyền thông",
        "Quy trình kiểm soát rủi ro trong công tác Truyền thông"]),
    ("TCKT", "Tài chính - Kế toán - LGG", "LGG", [
        "Quy trình triển khai kế hoạch tài chính",
        "Quy trình thu hồi công nợ phải thu/công nợ cho vay",
        "Quy trình lập và phê duyệt báo cáo chi phí giá thành các Dự án",
        "Quy trình lập và phê duyệt báo cáo tài chính của Công ty",
        "Quy trình kiểm soát kế hoạch tài chính cho từng Dự án",
        "Quy trình kiểm soát kế hoạch quản lý doanh thu-chi phí-giá thành",
        "Quy trình quản lý cam kết với ngân hàng/đối tác",
        "Quy trình lập và phê duyệt Phương án huy động vốn vay",
        "Quy trình chi trả nợ gốc, lãi vay Ngân hàng/Tổ chức/Cá nhân và phí mượn tài sản",
        "Quy trình tạm ứng/thanh toán nội bộ"]),
    ("NS", "Nhân sự - LGG", "LGG", [
        "Quy trình đào tạo nhân sự nội bộ",
        "Quy trình đánh giá hiệu quả làm việc CBNV hàng tháng",
        "Quy trình kiểm soát công tác tuyển dụng Nhân sự",
        "Quy trình tuyển dụng nhân sự"]),
    ("VP", "Văn phòng - LGG", "LGG", [
        "Quy trình phê duyệt và ban hành văn bản",
        "Quy trình quản lý văn bản đi (Công văn)",
        "Quy trình quản lý văn bản đến",
        "Quy trình lập và phê duyệt phương án mua sắm, sửa chữa và bảo trì tài sản, trang thiết bị"]),
    ("KSNB", "KSNB – LGG", "LGG", [
        "Quy trình kiểm soát hồ sơ pháp lý công ty/dự án",
        "Quy trình giải quyết tranh chấp, khiếu nại và tố tụng"]),
]

# Cách viết bước:  id|chỉ số làn|loại|nội dung|bước kế tiếp|biểu mẫu/ghi chú
# loại: S bắt đầu, T công việc, D quyết định, E kết thúc.  Bước kế tiếp: "3" hoặc "5:Đạt,2:Chưa đạt"
FLOWS = [
 dict(
  group="PTDA", idx=5, wave="Đợt 3", app="Base BPM (luồng nhiều cấp) + E-Office (lưu quyết định)",
  goal="Bảo đảm mọi điều chỉnh quy mô, tiến độ, vốn của dự án đều được thẩm định đủ góc độ và có chủ trương hợp lệ trước khi trình cơ quan nhà nước.",
  inp="Đề xuất điều chỉnh từ ban dự án; hồ sơ pháp lý và tài chính hiện hành",
  out="Nghị quyết/quyết định chấp thuận điều chỉnh; hồ sơ pháp lý cập nhật",
  lanes=["Phòng PTDA (LGL)", "Pháp chế / KSNB", "Phòng TCKT", "Ban Tổng giám đốc", "HĐQT / ĐHĐCĐ", "Cơ quan QLNN"],
  steps="""
1|0|S|Phát sinh nhu cầu điều chỉnh dự án (quy hoạch, quy mô, tiến độ, vốn)|2|
2|0|T|Lập tờ trình và thuyết minh đề xuất điều chỉnh|3,4|Mẫu tờ trình điều chỉnh dự án
3|1|T|Rà soát cơ sở pháp lý, điều kiện điều chỉnh|5|
4|2|T|Đánh giá tác động tài chính, hiệu quả đầu tư sau điều chỉnh|5|Bảng phân tích hiệu quả đầu tư
5|3|D|Tổng giám đốc thẩm định có đạt không?|6:Đạt,2:Chưa đạt|
6|4|D|HĐQT/ĐHĐCĐ thông qua chủ trương?|7:Thông qua,2:Chưa thông qua|Nghị quyết/biên bản họp
7|0|T|Lập hồ sơ điều chỉnh chủ trương đầu tư gửi cơ quan QLNN|8|
8|5|D|Cơ quan QLNN chấp thuận hồ sơ?|9:Chấp thuận,7:Bổ sung|
9|0|T|Cập nhật quyết định vào hồ sơ dự án, thông báo các bên liên quan|10|
10|0|E|Lưu hồ sơ pháp lý, chuyển QLDA và Kinh doanh triển khai|
"""),
 dict(
  group="QLDA-LGL", idx=1, wave="Đợt 2", app="Base BPM (phê duyệt theo giai đoạn thiết kế) + Base Projects",
  goal="Mỗi bản vẽ phát hành đều qua thẩm tra kỹ thuật và góp ý công năng, thương mại, vận hành trước khi duyệt.",
  inp="Hồ sơ thiết kế do đơn vị tư vấn nộp theo từng giai đoạn",
  out="Hồ sơ thiết kế được phê duyệt, ban hành có kiểm soát phiên bản",
  lanes=["Đơn vị tư vấn thiết kế", "Ban QLDA (LGL)", "Phòng Kỹ thuật", "Kinh doanh / QLVH (góp ý)", "Ban Tổng giám đốc"],
  steps="""
1|1|S|Nhận nhiệm vụ thiết kế theo giai đoạn (cơ sở, kỹ thuật, thi công)|2|
2|0|T|Lập hồ sơ thiết kế, nộp Ban QLDA|3|Hồ sơ thiết kế + bản vẽ kèm số phiên bản
3|1|T|Kiểm tra sơ bộ tính đầy đủ của hồ sơ|4,5|
4|2|T|Thẩm tra chuyên môn: kết cấu, MEP, PCCC, quy chuẩn|6|Phiếu thẩm tra
5|3|T|Góp ý công năng, giá trị thương mại, khả năng vận hành|6|Phiếu góp ý
6|1|D|Tổng hợp ý kiến: có cần chỉnh sửa không?|2:Cần sửa,7:Không|
7|4|D|Tổng giám đốc có phê duyệt không?|8:Duyệt,2:Không duyệt|
8|1|T|Ban hành quyết định, phát hành bản vẽ được duyệt|9|
9|1|E|Lưu kiểm soát tài liệu, bàn giao LGEC thi công|
"""),
 dict(
  group="QLDA-LGEC", idx=7, wave="Đợt 2", app="Base BPM + Base Requests (hồ sơ nhà thầu), Base Dataset (danh sách NTP/NCC)",
  goal="Chọn nhà thầu phụ/nhà cung cấp minh bạch, có so sánh giá và có phê duyệt rõ ràng trước khi ký hợp đồng.",
  inp="Nhu cầu thuê NTP/NCC kèm khối lượng, tiến độ từ công trình",
  out="Hợp đồng đã ký; danh sách NTP/NCC được duyệt",
  lanes=["Ban chỉ huy công trình", "Phòng Cung ứng / Đấu thầu", "Hội đồng đánh giá", "Phòng TCKT", "Lãnh đạo LGEC"],
  steps="""
1|0|S|Đề xuất nhu cầu thuê NTP/NCC (khối lượng, tiến độ, yêu cầu kỹ thuật)|2|
2|1|T|Lập danh sách NTP/NCC tiềm năng, kiểm tra hồ sơ năng lực|3|Dataset NTP/NCC
3|1|T|Phát hành hồ sơ mời, thu báo giá|4|
4|2|T|Mở thầu, đánh giá kỹ thuật và thương mại|5|Bảng chấm điểm
5|3|T|Thẩm định giá, điều kiện thanh toán, năng lực tài chính|6|
6|4|D|Lãnh đạo có phê duyệt kết quả lựa chọn không?|7:Duyệt,3:Mời lại|
7|1|T|Thương thảo và soạn thảo hợp đồng|8|Hợp đồng mẫu LGEC
8|4|T|Ký hợp đồng|9|
9|0|E|Cập nhật danh sách NTP/NCC được duyệt, triển khai thi công|
"""),
 dict(
  group="QLDA-LGEC", idx=5, wave="Đợt 3", app="Base BPM + Base Requests; liên thông Base Finance nếu có",
  goal="Hồ sơ thanh toán gửi chủ đầu tư luôn đủ, đúng khối lượng nghiệm thu, giảm số lần bị trả về và rút ngắn thời gian thu tiền.",
  inp="Biên bản nghiệm thu khối lượng giai đoạn; hợp đồng với CĐT",
  out="Hồ sơ thanh toán được CĐT xác nhận; hóa đơn; ghi nhận công nợ phải thu",
  lanes=["Ban chỉ huy công trình", "Phòng QLDA / Kỹ thuật LGEC", "Phòng TCKT LGEC", "Lãnh đạo LGEC", "Chủ đầu tư (LGL)"],
  steps="""
1|0|S|Hoàn thành khối lượng giai đoạn, lập biên bản nghiệm thu khối lượng|2|
2|1|T|Lập hồ sơ thanh toán (bảng khối lượng, nghiệm thu, hóa đơn…)|3|Bộ hồ sơ thanh toán theo hợp đồng
3|2|T|Đối chiếu hợp đồng, giá trị lũy kế, tạm ứng cần thu hồi|4|
4|2|D|Hồ sơ đã đủ và đúng chưa?|5:Đạt,2:Chưa đạt|
5|3|T|Ký duyệt hồ sơ, trình chủ đầu tư|6|
6|4|T|Chủ đầu tư tiếp nhận, kiểm tra khối lượng|7|
7|4|D|Chủ đầu tư có chấp thuận không?|8:Chấp thuận,2:Điều chỉnh|
8|2|T|Xuất hóa đơn, theo dõi thanh toán|9|
9|2|E|Ghi nhận thanh toán, đối chiếu công nợ|
"""),
 dict(
  group="QLDA-LGEC", idx=2, wave="Đợt 2", app="Base Requests/BPM (phiếu yêu cầu nghiệm thu) + Base Projects/Cowork (tiến độ theo hạng mục) + Base Dataset (hồ sơ chất lượng)",
  goal="Mọi vật tư – thiết bị vào công trường và mọi hạng mục thi công đều được kiểm tra, nghiệm thu có biên bản trước khi sang bước sau hoặc mở thanh toán.",
  inp="Vật tư – thiết bị về công trường; hạng mục thi công theo biện pháp được duyệt",
  out="Biên bản nghiệm thu; hồ sơ chất lượng và hoàn công; điều kiện mở thanh toán đợt",
  lanes=["Tổ đội / Nhà thầu phụ", "Ban chỉ huy công trình", "Phòng QA/QC LGEC", "Tư vấn giám sát / CĐT"],
  steps="""
1|0|S|Vật tư – thiết bị về công trường|2|
2|1|T|Kiểm tra chứng chỉ xuất xưởng, CO/CQ, lấy mẫu thí nghiệm|3|Phiếu kiểm tra vật tư đầu vào
3|2|D|Vật tư – thiết bị có đạt yêu cầu không?|4:Đạt,1:Không đạt, trả NCC|
4|0|T|Thi công hạng mục theo biện pháp được duyệt|5|Biện pháp thi công
5|1|T|Tự kiểm tra, lập phiếu yêu cầu nghiệm thu|6|Phiếu yêu cầu nghiệm thu
6|2|D|Kiểm tra nội bộ có đạt không?|7:Đạt,4:Cần sửa|
7|3|T|Nghiệm thu hạng mục tại hiện trường, ký biên bản|8|Biên bản nghiệm thu
8|3|D|TVGS/CĐT có chấp thuận không?|9:Chấp thuận,4:Yêu cầu sửa|Chuyển QT Sửa lỗi chất lượng nếu có lỗi
9|1|T|Lập hồ sơ nghiệm thu, hoàn công|10|
10|2|E|Lưu hồ sơ chất lượng, cập nhật nhật ký công trình, mở điều kiện thanh toán đợt|
"""),
 dict(
  group="CUNGUNG", idx=1, wave="Đợt 2", app="Base Requests/BPM (đề nghị – PO) + Base Inventories (nhập kho)",
  goal="Đặt vật tư – thiết bị đúng nhu cầu, đúng tiến độ, có so sánh giá và đối chiếu được PO – phiếu nhập – hóa đơn.",
  inp="Đề nghị vật tư của công trình theo kế hoạch tiến độ",
  out="PO được duyệt; vật tư nhập kho; công nợ NCC được ghi nhận",
  lanes=["Ban chỉ huy công trình", "Phòng Cung ứng", "Lãnh đạo LGEC", "Nhà cung cấp", "Kho công trình", "Phòng TCKT"],
  steps="""
1|0|S|Lập đề nghị vật tư theo kế hoạch tiến độ|2|
2|1|T|Kiểm tra định mức, đối chiếu dự toán và tồn kho|3|
3|1|D|Còn tồn kho hoặc điều chuyển được không?|4:Có,5:Không|
4|1|E|Chuyển sang quy trình Cấp vật tư – thiết bị|
5|1|T|Hỏi giá, so sánh tối thiểu 3 NCC, lập đề xuất PO|6|Bảng so sánh giá
6|2|D|Lãnh đạo có phê duyệt theo hạn mức không?|7:Duyệt,5:Điều chỉnh|
7|1|T|Phát hành PO/hợp đồng nguyên tắc cho NCC|8|
8|3|T|NCC xác nhận và giao hàng|9|
9|4|T|Kiểm tra, nhập kho, lập biên bản|10|
10|5|E|Đối chiếu PO – phiếu nhập – hóa đơn, ghi nhận công nợ|
"""),
 dict(
  group="KD", idx=2, wave="Đợt 2", app="Base BPM + Base Commerce (bảng giá, chính sách) + Base Lead/CRM",
  goal="Phương án kinh doanh được xây trên số liệu thị trường, dòng tiền và pháp lý trước khi mở bán.",
  inp="Dự án đủ điều kiện chuẩn bị mở bán; số liệu thị trường",
  out="Phương án kinh doanh được HĐQT phê duyệt; kế hoạch bán hàng",
  lanes=["Phòng Kinh doanh", "ĐV tư vấn / môi giới", "Phòng TCKT", "Pháp chế", "Ban Tổng giám đốc", "HĐQT"],
  steps="""
1|0|S|Dự án đủ điều kiện, bắt đầu chuẩn bị mở bán|2|
2|0|T|Nghiên cứu thị trường, đề xuất sản phẩm, giá, tiến độ và chính sách bán|3,4,5|Mẫu phương án kinh doanh
3|1|T|Đơn vị tư vấn bán hàng góp ý, đề xuất|6|
4|2|T|Cân đối dòng tiền, doanh thu – chi phí, hiệu quả|6|
5|3|T|Rà soát điều kiện pháp lý mở bán, hợp đồng mẫu|6|
6|4|D|Tổng giám đốc thẩm định có đạt không?|7:Đạt,2:Chưa đạt|
7|5|D|HĐQT có phê duyệt không?|8:Duyệt,2:Không duyệt|
8|0|T|Ban hành phương án, phổ biến cho các bên|9|
9|0|E|Triển khai bán hàng, theo dõi thực hiện theo kỳ|
"""),
 dict(
  group="KD", idx=5, wave="Đợt 2", app="Base BPM + eSign (ký số) + Base Commerce/CRM (trạng thái căn)",
  goal="Hợp đồng mua bán soạn đúng mẫu, đúng giá, đúng tiến độ thu tiền; điều khoản ngoài mẫu phải qua pháp chế.",
  inp="Thông tin khách hàng, căn/sản phẩm, giá, phương thức thanh toán",
  out="Hợp đồng/PLHĐ đã ký, lưu sổ; trạng thái căn được cập nhật",
  lanes=["Sales / Môi giới", "Kinh doanh – Admin", "Pháp chế", "Phòng TCKT", "Lãnh đạo ký", "Khách hàng"],
  steps="""
1|0|S|Khách hàng đặt cọc/xác nhận mua|2|
2|1|T|Lập đề nghị soạn hợp đồng (khách, căn, giá, lịch thanh toán)|3|Phiếu đề nghị soạn HĐ
3|2|D|Hợp đồng có theo mẫu chuẩn không?|5:Đúng mẫu,4:Ngoài mẫu|
4|2|T|Soát xét điều khoản đặc biệt, trình lãnh đạo chấp thuận|5|
5|3|T|Kiểm tra tiền đã thu và lịch thanh toán|6|
6|5|T|Khách hàng xem và ký hợp đồng|7|
7|4|T|Lãnh đạo ký, đóng dấu|8|
8|1|T|Bàn giao bản cho khách, lưu hồ sơ, cập nhật sổ HĐ và trạng thái căn|9|
9|3|E|Theo dõi tiến độ thanh toán, nhắc hạn|
"""),
 dict(
  group="QLVH", idx=1, wave="Đợt 2", app="Base Requests/BPM + Base Dataset (định mức, đơn giá)",
  goal="Dự toán chi phí vận hành từng tòa nhà được lập theo định mức, được duyệt trước kỳ và đối chiếu thực tế hằng tháng.",
  inp="Hợp đồng dịch vụ, định mức, phí dịch vụ thu được",
  out="Dự toán được duyệt; báo cáo chênh lệch thực tế so với dự toán",
  lanes=["Ban quản lý tòa nhà", "Phòng QLVH (Rivera Homes)", "Phòng TCKT", "Lãnh đạo Rivera"],
  steps="""
1|0|S|Đến kỳ lập dự toán chi phí vận hành năm|2|
2|0|T|Tổng hợp hạng mục: nhân sự, an ninh, vệ sinh, điện nước, bảo trì|3|Mẫu dự toán theo tòa nhà
3|1|T|Rà soát định mức, đơn giá, hợp đồng dịch vụ|4|
4|2|T|Đối chiếu ngân sách và nguồn phí dịch vụ thu|5|
5|3|D|Lãnh đạo có phê duyệt không?|6:Duyệt,2:Điều chỉnh|
6|1|T|Công bố dự toán, giao Ban quản lý thực hiện|7|
7|0|T|Thực hiện, báo cáo chi phí thực tế hằng tháng|8|
8|2|E|Đối chiếu thực tế – dự toán, báo cáo chênh lệch|
"""),
 dict(
  group="QLTS", idx=3, wave="Đợt 2", app="Base Requests/BPM + Base Dataset (hồ sơ thiết bị) + Base Tasks (lịch bảo trì)",
  goal="Mọi công việc bảo dưỡng định kỳ và sửa chữa sự cố hệ thống kỹ thuật được ghi nhận, nghiệm thu và lưu lý lịch thiết bị.",
  inp="Kế hoạch bảo dưỡng năm hoặc sự cố phát sinh",
  out="Thiết bị được nghiệm thu; lý lịch/nhật ký cập nhật; chi phí được thanh toán",
  lanes=["Kỹ thuật tòa nhà", "Trưởng Ban quản lý", "Phòng QLTS / QLVH", "Nhà thầu bảo trì"],
  steps="""
1|0|S|Đến lịch bảo dưỡng định kỳ hoặc phát sinh sự cố|2|
2|0|D|Loại công việc là gì?|3:Định kỳ,4:Sự cố/sửa chữa|
3|0|T|Lập lệnh bảo dưỡng theo kế hoạch năm|5|Lệnh bảo dưỡng
4|0|T|Lập phiếu đề nghị sửa chữa, đánh giá mức độ khẩn|5|Phiếu đề nghị sửa chữa
5|1|D|Vượt hạn mức hoặc ngoài khả năng tự làm?|6:Không,7:Có|
6|0|T|Kỹ thuật tự thực hiện bảo dưỡng/sửa chữa|9|
7|2|T|Lập dự toán, duyệt và chọn nhà thầu|8|
8|3|T|Nhà thầu thực hiện và bàn giao|9|
9|1|T|Nghiệm thu kết quả|10|Biên bản nghiệm thu
10|2|E|Cập nhật lý lịch thiết bị, nhật ký HTKT; chuyển TCKT thanh toán|
"""),
 dict(
  group="TCKT", idx=8, wave="Đợt 3", app="Base BPM + eSign; đính kèm hồ sơ vay trong Base Dataset",
  goal="Mỗi khoản vay mới đều có phân tích dòng tiền, so sánh nhiều nguồn vốn, rà soát pháp lý và được cấp thẩm quyền duyệt.",
  inp="Nhu cầu vốn của dự án/đơn vị (mục đích, số tiền, thời hạn)",
  out="Hợp đồng tín dụng; lịch giải ngân và trả nợ chuyển sang theo dõi cam kết",
  lanes=["Đơn vị đề xuất", "Phòng TCKT", "Pháp chế", "Ban Tổng giám đốc", "HĐQT", "Ngân hàng / tổ chức tín dụng"],
  steps="""
1|0|S|Đề xuất nhu cầu vốn (mục đích, số tiền, thời hạn)|2|
2|1|T|Phân tích dòng tiền, cơ cấu vốn, ước tính chi phí vay|3|
3|1|T|Làm việc sơ bộ với tối thiểu 2 ngân hàng/tổ chức, so sánh điều kiện|4|Bảng so sánh điều kiện vay
4|2|T|Rà soát điều kiện tín dụng và tài sản bảo đảm|5|
5|3|D|Tổng giám đốc có trình HĐQT không?|6:Đạt,2:Chưa đạt|
6|4|D|HĐQT có phê duyệt phương án không?|7:Duyệt,2:Không duyệt|
7|1|T|Hoàn thiện hồ sơ vay, nộp ngân hàng|8|
8|5|T|Ngân hàng thẩm định, phê duyệt hạn mức, ký hợp đồng tín dụng|9|
9|1|E|Giải ngân, đưa vào theo dõi cam kết và lịch trả nợ|
"""),
 dict(
  group="TCKT", idx=10, wave="Đợt 1", app="Base Requests (đề nghị tạm ứng/thanh toán) + Base Finance nếu có",
  goal="Một cửa đề nghị chi tiền: đúng hạn mức, đủ chứng từ, theo dõi được hoàn ứng.",
  inp="Đề nghị tạm ứng hoặc thanh toán kèm chứng từ",
  out="Khoản chi được thực hiện và hạch toán; hoàn ứng được theo dõi",
  lanes=["Người đề nghị", "Trưởng đơn vị", "Kế toán", "Kế toán trưởng", "Lãnh đạo", "Thủ quỹ"],
  steps="""
1|0|S|Lập đề nghị tạm ứng/thanh toán kèm chứng từ|2|Giấy đề nghị tạm ứng/thanh toán
2|1|D|Trưởng đơn vị có duyệt nhu cầu không?|3:Duyệt,1:Trả lại|
3|2|T|Kiểm tra chứng từ, ngân sách, dư tạm ứng|4|
4|3|D|Chứng từ đã hợp lệ chưa?|5:Hợp lệ,1:Bổ sung|
5|3|D|Giá trị có vượt hạn mức không?|6:Vượt,7:Không|
6|4|T|Lãnh đạo phê duyệt|7|
7|5|T|Chi tiền hoặc chuyển khoản|8|
8|2|E|Hạch toán, theo dõi hoàn ứng và quyết toán|
"""),
 dict(
  group="NS", idx=4, wave="Đợt 1", app="Base Careers/HRM (tuyển dụng, thử việc, onboarding) + Base Requests/BPM (phê duyệt) + eSign",
  goal="Tuyển dụng theo định biên và kế hoạch được Chủ tịch Hội đồng tuyển dụng phê duyệt ở từng điểm kiểm soát; tổng thời gian chuẩn khoảng 180 ngày từ nhu cầu đến đánh giá sau 3 tháng làm việc chính thức. Theo QT.NS 01 của Long Giang.",
  inp="Phiếu yêu cầu tuyển dụng nhân sự của đơn vị có nhu cầu (BM.NS.TD.01.01)",
  out="Nhân sự ký HĐLĐ chính thức và được đánh giá sau 3 tháng (BM.NS.TD.01.26)",
  lanes=["Đơn vị có nhu cầu tuyển dụng", "Chủ tịch Hội đồng tuyển dụng", "Phòng Hành chính – Nhân sự", "Giám đốc điều hành Công ty"],
  steps="""
1|0|S|Lập nhu cầu tuyển dụng|2|BM.NS.TD.01.01|1 ngày
2|1|D|Phê duyệt nhu cầu tuyển dụng (HCNS thẩm định theo định biên, chủ trương)|3:Phê duyệt,1:Hiệu chỉnh|Phòng HCNS thẩm định trước khi trình|1 ngày
3|2|T|Lập kế hoạch tuyển dụng|4|BM.NS.TD.01.02|1 ngày
4|1|D|Phê duyệt kế hoạch tuyển dụng|5:Phê duyệt,3:Hiệu chỉnh|HCNS hiệu chỉnh theo ý kiến CT HĐTD|1 ngày
5|2|T|Đăng tuyển và tìm kiếm ứng viên|6|BM.NS.TD.01.03, 01.04, 01.05|14 ngày
6|2|T|Sàng lọc hồ sơ ứng viên (HCNS theo tiêu chuẩn chung, đơn vị theo tiêu chuẩn chuyên môn)|7||1 ngày
7|2|T|Phỏng vấn và đánh giá ứng viên (Hội đồng phỏng vấn)|8|BM.NS.TD.01.06, 01.07, 01.08, 01.09|5 ngày
8|1|T|Phê duyệt kết quả lựa chọn ứng viên|9|BM.NS.TD.01.10, 01.11|1 ngày
9|2|T|Đàm phán nội dung chính của hợp đồng|10|BM.NS.TD.01.12, 01.13|1 ngày
10|1|T|Phê duyệt đề xuất tiếp nhận nhân sự|11|BM.NS.TD.01.14, 01.15, 01.16|1 ngày
11|2|T|Tiếp nhận, thử việc và đánh giá sau tuyển dụng|12|BM.NS.TD.01.17, 01.18, 01.22, 01.23|60 ngày
12|1|T|Phê duyệt: ký HĐLĐ chính thức, chấm dứt thử việc hoặc khác|13|BM.NS.TD.01.24|1 ngày
13|3|T|Ký hợp đồng lao động chính thức|14|BM.NS.TD.01.25|1 ngày
14|0|T|Lập báo cáo, đánh giá nhân sự sau 3 tháng làm việc chính thức|15|BM.NS.TD.01.26|90 ngày
15|1|E|Phê duyệt báo cáo đánh giá nhân sự sau 3 tháng||BM.NS.TD.01.26|1 ngày
"""),
 dict(
  group="VP", idx=1, wave="Đợt 1", app="Base E-Office (trình ký, cấp số) + eSign",
  goal="Mọi văn bản nội bộ đều qua rà soát thể thức, pháp lý, được ký đúng thẩm quyền, cấp số và phát hành có kiểm soát.",
  inp="Dự thảo văn bản (quy chế, quyết định, thông báo)",
  out="Văn bản ban hành, có số, lưu bản gốc, đến đúng nơi nhận",
  lanes=["Đơn vị soạn thảo", "Phòng Pháp chế", "Văn phòng", "Lãnh đạo ký", "Văn thư"],
  steps="""
1|0|S|Soạn dự thảo văn bản|2|
2|0|T|Trưởng đơn vị kiểm tra, ký nháy|3|
3|1|T|Rà soát căn cứ pháp lý và nội dung|4|
4|2|T|Kiểm tra thể thức, trình bày|5|
5|3|D|Lãnh đạo có ký ban hành không?|6:Ký,1:Chỉnh sửa|
6|4|T|Đóng dấu, cấp số, ghi sổ văn bản|7|
7|2|T|Phát hành tới nơi nhận, lưu bản gốc|8|
8|0|E|Tiếp nhận, triển khai và theo dõi hiệu lực|
"""),
 dict(
  group="KSNB", idx=1, wave="Đợt 3", app="Base Dataset (sổ pháp lý, nhắc hạn) + E-Office (lưu trữ)",
  goal="Hồ sơ pháp lý công ty và dự án luôn đầy đủ, còn hiệu lực và có cảnh báo trước khi hết hạn.",
  inp="Hồ sơ pháp lý mới hoặc cập nhật (giấy phép, quyết định, ĐKKD…)",
  out="Sổ theo dõi pháp lý cập nhật; báo cáo tình trạng pháp lý định kỳ",
  lanes=["Đơn vị quản lý hồ sơ", "Bộ phận KSNB", "Văn phòng (lưu trữ)", "Ban Tổng giám đốc"],
  steps="""
1|0|S|Phát sinh hoặc cập nhật hồ sơ pháp lý|2|
2|0|T|Nộp bản scan và bản gốc kèm phiếu giao nộp|3|Phiếu giao nộp hồ sơ
3|1|T|Kiểm tra tính đầy đủ, hiệu lực, thời hạn|4|
4|1|D|Hồ sơ có đạt yêu cầu không?|5:Đạt,2:Thiếu/sai|
5|1|T|Cập nhật sổ theo dõi pháp lý, gắn mã hồ sơ, đặt cảnh báo hạn|6|
6|2|T|Lưu trữ bản gốc, phân quyền khai thác|7|
7|1|D|Có hồ sơ sắp hết hạn hoặc sai lệch không?|8:Có,9:Không|
8|3|T|Chỉ đạo xử lý: gia hạn, bổ sung|2|
9|1|E|Báo cáo định kỳ tình trạng pháp lý|
"""),
]


def build():
    """Trả về (catalog, flows) đã gắn mã QT."""
    catalog, code_of = [], {}
    stt = 0
    for gkey, field, unit, names in CATALOG:
        for i, name in enumerate(names, 1):
            stt += 1
            code = f"{gkey}-{i:02d}"
            code_of[(gkey, i)] = code
            catalog.append(dict(stt=stt, group=gkey, field=field, unit=unit, code=code, name=name))
    flows = []
    for f in FLOWS:
        code = code_of[(f["group"], f["idx"])]
        item = next(c for c in catalog if c["code"] == code)
        steps = []
        for line in f["steps"].strip().splitlines():
            parts = line.split("|"); parts += [""] * (7 - len(parts)); sid, lane, typ, text, nxt, note, sla = parts[:7]
            nx = []
            for part in [p for p in nxt.split(",") if p.strip()] if ":" not in nxt else _split_next(nxt):
                if ":" in part:
                    to, lab = part.split(":", 1)
                else:
                    to, lab = part, ""
                nx.append(dict(to=to.strip(), label=lab.strip()))
            steps.append(dict(id=sid, lane=int(lane), type=typ, text=text, next=nx, note=note, sla=sla))
        import lanes_map
        flows.append(dict(code=code, name=item["name"], field=item["field"], unit=item["unit"],
                          wave=f["wave"], app=f["app"], goal=f["goal"], inp=f["inp"], out=f["out"],
                          lanes=lanes_map.apply(code, f["lanes"]), steps=steps))
        item["flow"] = True
        item["wave"] = f["wave"]
        item["app"] = f["app"]
    return catalog, flows


def _split_next(s):
    # tách theo dấu phẩy nhưng chỉ khi sau dấu phẩy là "số:"  (nhãn có thể chứa dấu phẩy)
    import re
    parts, cur = [], ""
    for tok in re.split(r",(?=\s*\d+(?::|$|,))", s):
        parts.append(tok)
    return parts


if __name__ == "__main__":
    cat, fl = build()
    print(len(cat), "QT trong danh mục;", len(fl), "lưu đồ")
    for f in fl:
        ids = {s["id"] for s in f["steps"]}
        for s in f["steps"]:
            for n in s["next"]:
                assert n["to"] in ids, (f["code"], s["id"], n)
            assert 0 <= s["lane"] < len(f["lanes"]), (f["code"], s["id"])
        print(f["code"], len(f["steps"]), "bước", f["wave"])
