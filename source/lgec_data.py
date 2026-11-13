# -*- coding: utf-8 -*-
"""Bộ quy trình tuần tự mảng Thi công xây lắp – Long Giang E&C (LGEC)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lg_data

UNITS = {"LGEC": "Long Giang E&C – tổng thầu thiết kế và thi công (D&B)"}

IN_DM = "Có trong danh mục"
ADD = "Đề xuất bổ sung"

PHASES = [
    ("P1", "1. Khởi động & nhận việc"),
    ("P2", "2. Chuẩn bị thi công"),
    ("P3", "3. Thi công & kiểm soát"),
    ("P4", "4. Thanh toán"),
    ("P5", "5. Hoàn thành & bảo hành"),
]

# thứ tự = trình tự áp dụng. src: mã trong danh mục Basework (nếu có)
SEQ = [
    # code, phase, name, source, catalog_code, from, to, prog(liên hệ tiến độ), wave
    ("LGEC-01", "P1", "Quy trình lập hồ sơ dự thầu / chào giá công trình (D&B)", ADD, "", [], ["LGEC-02"],
     "Chốt tiến độ sơ bộ và mốc cam kết ngay từ giá dự thầu.", "Đợt 3"),
    ("LGEC-02", "P1", "Quy trình ký hợp đồng thi công với CĐT và khởi động công trình", ADD, "", ["LGEC-01"], ["LGEC-03", "LGEC-04"],
     "Mốc tiến độ trong hợp đồng là đầu vào của tiến độ tổng thể.", "Đợt 3"),
    ("LGEC-03", "P2", "Quy trình lập tổ chức công trường và tổng mặt bằng thi công", ADD, "", ["LGEC-02"], ["LGEC-04", "LGEC-05"],
     "Mặt bằng và nguồn lực công trường quyết định tiến độ thực tế có đạt hay không.", "Đợt 2"),
    ("LGEC-04", "P2", "Quy trình lập và phê duyệt tiến độ thi công tổng thể, chi tiết", IN_DM, "QLDA-LGEC-01 (phần lập kế hoạch)", ["LGEC-02", "LGEC-03"], ["LGEC-05", "LGEC-06", "LGEC-09"],
     "Tạo baseline tiến độ: mọi quy trình sau đều đối chiếu với baseline này.", "Đợt 2"),
    ("LGEC-05", "P2", "Quy trình phê duyệt biện pháp thi công và bản vẽ thi công (shopdrawing)", ADD, "", ["LGEC-03", "LGEC-04"], ["LGEC-09", "LGEC-10"],
     "Chưa duyệt biện pháp thì hạng mục không được khởi công: là điều kiện ngoại vi của tiến độ.", "Đợt 2"),
    ("LGEC-06", "P2", "Quy trình lựa chọn Nhà thầu phụ/NCC", IN_DM, "QLDA-LGEC-07", ["LGEC-04"], ["LGEC-07", "LGEC-16"],
     "Thời gian chọn thầu phải nằm trong tiến độ; gói nào chọn muộn sẽ làm trễ mốc.", "Đợt 2"),
    ("LGEC-07", "P3", "Quy trình đặt hàng VT - TB", IN_DM, "CUNGUNG-01", ["LGEC-04", "LGEC-06"], ["LGEC-08"],
     "Ngày đặt hàng tính lùi từ ngày cần vật tư theo tiến độ, cộng thời gian giao hàng.", "Đợt 2"),
    ("LGEC-08", "P3", "Quy trình cấp Vật tư - Thiết bị cho thi công", IN_DM, "CUNGUNG-02", ["LGEC-07"], ["LGEC-09"],
     "Cấp vật tư kịp thời hoặc thiếu vật tư là nguyên nhân chậm tiến độ phổ biến.", "Đợt 2"),
    ("LGEC-09", "P3", "Quy trình quản lý tiến độ thi công (theo dõi tuần, báo cáo, bù tiến độ)", IN_DM, "QLDA-LGEC-01 (phần theo dõi)", ["LGEC-04", "LGEC-05", "LGEC-08", "LGEC-12", "LGEC-13"], ["LGEC-10", "LGEC-14", "LGEC-15"],
     "Trục chính của bộ quy trình: so sánh thực tế với baseline, bù tiến độ hoặc đề nghị điều chỉnh mốc.", "Đợt 1"),
    ("LGEC-10", "P3", "Quy trình quản lý chất lượng: vật tư - thiết bị đầu vào, thi công, nghiệm thu", IN_DM, "QLDA-LGEC-02", ["LGEC-05", "LGEC-09"], ["LGEC-11", "LGEC-15", "LGEC-17"],
     "Nghiệm thu hạng mục là mốc xác nhận hoàn thành tiến độ và điều kiện mở thanh toán.", "Đợt 2"),
    ("LGEC-11", "P3", "Quy trình sửa lỗi chất lượng các hạng mục của Công trình", IN_DM, "QLDA-LGEC-03", ["LGEC-10"], ["LGEC-10", "LGEC-09"],
     "Thời gian sửa lỗi phải đo được để biết lỗi chất lượng làm chậm bao nhiêu ngày.", "Đợt 2"),
    ("LGEC-12", "P3", "Quy trình kiểm soát KH công tác AN-PCCN-ATLĐ-VSMT-NDTH các công trình", IN_DM, "QLDA-LGEC-04", ["LGEC-03"], ["LGEC-09"],
     "Đình chỉ thi công vì mất an toàn sẽ được ghi nhận thành ngày chậm tiến độ.", "Đợt 2"),
    ("LGEC-13", "P3", "Quy trình kiểm soát công tác bảo dưỡng, sửa chữa Thiết bị thi công", IN_DM, "CUNGUNG-03", ["LGEC-03"], ["LGEC-09"],
     "Thiết bị hỏng giữa chừng là rủi ro chậm tiến độ; lịch bảo dưỡng bám theo lịch sử dụng.", "Đợt 3"),
    ("LGEC-14", "P3", "Quy trình xử lý thay đổi, phát sinh khối lượng", ADD, "", ["LGEC-09", "LGEC-10"], ["LGEC-04", "LGEC-15"],
     "Phát sinh được duyệt sẽ đổi baseline và có thể kéo dài tiến độ theo hợp đồng.", "Đợt 2"),
    ("LGEC-15", "P4", "Quy trình lập và nộp hồ sơ thanh toán với CĐT", IN_DM, "QLDA-LGEC-05", ["LGEC-10", "LGEC-14"], ["LGEC-17", "LGEC-18"],
     "Thanh toán theo khối lượng đã nghiệm thu, nên tiến độ thực tế quyết định dòng tiền thu về.", "Đợt 3"),
    ("LGEC-16", "P4", "Quy trình thanh toán cho các đơn vị tư vấn/NT/NCC", IN_DM, "QLDA-LGEC-06", ["LGEC-06", "LGEC-10"], ["LGEC-18"],
     "Thanh toán gắn với khối lượng và tiến độ NTP đã đạt, giữ lại theo hợp đồng.", "Đợt 3"),
    ("LGEC-17", "P5", "Quy trình nghiệm thu hoàn thành và bàn giao công trình", ADD, "", ["LGEC-10", "LGEC-15"], ["LGEC-18"],
     "Ngày nghiệm thu hoàn thành chốt tiến độ thực tế cuối cùng và bắt đầu thời hạn bảo hành.", "Đợt 3"),
    ("LGEC-18", "P5", "Quy trình quyết toán hợp đồng và bảo hành công trình", ADD, "", ["LGEC-15", "LGEC-16", "LGEC-17"], [],
     "Tổng kết tiến độ thực tế so với baseline làm dữ liệu cho dự thầu công trình sau.", "Đợt 3"),
]

# Cách viết bước giống lg_data
NEW = {
"LGEC-01": dict(
  goal="Quyết định tham gia dự thầu dựa trên quy mô, năng lực, rủi ro và biên lợi nhuận; giá dự thầu có giải pháp, tiến độ sơ bộ và dòng tiền đi kèm.",
  inp="Thư mời thầu hoặc yêu cầu chào giá của chủ đầu tư", out="Hồ sơ dự thầu được duyệt và nộp; kết quả trúng/trượt thầu",
  app="Base Requests/BPM (duyệt tham gia và giá dự thầu) + Base Dataset (hồ sơ năng lực, giá NTP/NCC)",
  lanes=["Ban Tổng giám đốc LGEC", "Phòng Đấu thầu / Dự toán", "Phòng Kỹ thuật / Thiết kế", "Phòng TCKT", "Chủ đầu tư"],
  steps="""
1|4|S|Nhận thư mời thầu hoặc yêu cầu chào giá|2|
2|1|T|Đánh giá cơ hội: quy mô, năng lực, rủi ro, biên lợi nhuận|3|Phiếu đánh giá cơ hội dự thầu
3|0|D|Ban Tổng giám đốc có quyết định tham gia không?|4:Tham gia,10:Không|
4|2|T|Lập giải pháp thiết kế, biện pháp thi công và tiến độ sơ bộ|5|
5|1|T|Bóc khối lượng, lập dự toán, hỏi giá NTP/NCC chủ chốt|6|Bảng dự toán dự thầu
6|3|T|Đánh giá dòng tiền, bảo lãnh, điều kiện thanh toán|7|
7|0|D|Ban Tổng giám đốc có duyệt giá dự thầu không?|8:Duyệt,5:Điều chỉnh|
8|1|T|Hoàn thiện và nộp hồ sơ dự thầu|9|
9|4|D|Chủ đầu tư có chọn LGEC không?|11:Trúng thầu,10:Không|
10|1|E|Dừng, lưu hồ sơ và rút kinh nghiệm|
11|1|E|Chuyển sang quy trình ký hợp đồng và khởi động|
"""),
"LGEC-02": dict(
  goal="Hợp đồng ký đúng điều khoản, bảo lãnh và thanh toán rõ ràng; công trình được khởi động với ban chỉ huy, ngân sách và mốc tiến độ thống nhất.",
  inp="Thông báo trúng thầu; hồ sơ dự thầu", out="Hợp đồng đã ký; ban chỉ huy công trình; mã công trình và ngân sách giá thành",
  app="Base BPM + eSign (ký hợp đồng) + Base Projects (mở dự án công trình)",
  lanes=["Chủ đầu tư (LGL)", "Phòng Pháp chế / Đấu thầu", "Phòng TCKT", "Ban Tổng giám đốc LGEC", "Chỉ huy trưởng công trình"],
  steps="""
1|1|S|Nhận thông báo trúng thầu|2|
2|1|T|Thương thảo điều khoản hợp đồng: giá, tiến độ, phạt, bảo hành|3|Hợp đồng mẫu LGEC
3|2|T|Rà soát bảo lãnh thực hiện, tạm ứng, điều kiện thanh toán|4|
4|3|D|Ban Tổng giám đốc có duyệt ký không?|5:Duyệt,2:Thương thảo lại|
5|0|T|Ký hợp đồng thi công|6|
6|3|T|Bổ nhiệm chỉ huy trưởng và ban chỉ huy công trình|7|
7|1|T|Họp bàn giao nội bộ: hợp đồng, rủi ro, mốc tiến độ, ngân sách|8|Biên bản bàn giao hợp đồng
8|2|T|Mở mã công trình, ngân sách giá thành, theo dõi chi phí|9|
9|4|E|Phát lệnh khởi công, chuyển sang tổ chức công trường|
"""),
"LGEC-03": dict(
  goal="Công trường sẵn sàng: tổ chức nhân sự, tổng mặt bằng, an toàn và huy động nguồn lực trước khi khởi công.",
  inp="Hợp đồng; mốc tiến độ; hồ sơ mặt bằng", out="Tổ chức công trường được duyệt; mặt bằng và lán trại sẵn sàng",
  app="Base Projects/Cowork (checklist khởi công) + Base Requests (đề nghị huy động nguồn lực)",
  lanes=["Chỉ huy trưởng", "Phòng Kỹ thuật", "Phòng Cung ứng", "Cán bộ ATLĐ", "Ban Tổng giám đốc LGEC"],
  steps="""
1|0|S|Nhận bàn giao hợp đồng và mốc tiến độ|2|
2|0|T|Lập sơ đồ tổ chức công trường, phân công chức danh|3,4|
3|1|T|Khảo sát mặt bằng, nhận bàn giao mốc, tim cốt|5|Biên bản bàn giao mặt bằng
4|3|T|Lập kế hoạch ATLĐ, PCCN, vệ sinh môi trường ban đầu|6|
5|1|T|Thiết kế tổng mặt bằng thi công: kho bãi, cẩu, đường, điện nước tạm|6|Bản vẽ tổng mặt bằng
6|2|T|Lập kế hoạch huy động nhân lực, máy móc, lán trại|7|
7|4|D|Ban Tổng giám đốc có duyệt tổ chức công trường không?|8:Duyệt,2:Điều chỉnh|
8|0|T|Xây dựng lán trại, hàng rào, điện nước tạm|9|
9|0|E|Báo cáo sẵn sàng khởi công, chuyển sang tiến độ và biện pháp thi công|
"""),
"LGEC-04": dict(
  goal="Có một tiến độ gốc (baseline) được duyệt: tổng thể, chi tiết theo tháng/tuần, kèm nhân lực, vật tư và dòng tiền, để mọi bộ phận cùng đối chiếu.",
  inp="Mốc tiến độ trong hợp đồng; điều kiện mặt bằng; cam kết của NTP và NCC", out="Tiến độ tổng thể và chi tiết được duyệt, phát hành cho các bên",
  app="Base Projects/Cowork (WBS, mốc, roadmap) + Base Dataset (biểu đồ nhân lực, vật tư)",
  lanes=["Ban chỉ huy công trình", "Phòng QLDA / Kế hoạch", "Phòng Cung ứng", "Nhà thầu phụ chủ chốt", "Ban Tổng giám đốc LGEC", "CĐT / Tư vấn giám sát"],
  steps="""
1|1|S|Nhận hợp đồng và mốc tiến độ cam kết với CĐT|2|
2|1|T|Lập tiến độ tổng thể: WBS, mốc chính, đường găng|3,4,5|Tiến độ tổng thể
3|2|T|Đối chiếu thời gian đặt hàng và giao hàng vật tư dài ngày|6|
4|3|T|Cam kết nhân lực, thiết bị và thời gian thi công từng gói|6|
5|0|T|Rà soát mặt bằng, điều kiện thi công, thời tiết|6|
6|1|T|Lập tiến độ chi tiết theo tháng/tuần, biểu đồ nhân lực, vật tư, dòng tiền|7|Tiến độ chi tiết
7|4|D|Ban Tổng giám đốc có duyệt nội bộ không?|8:Duyệt,2:Điều chỉnh|
8|5|D|CĐT/TVGS có chấp thuận tiến độ không?|9:Chấp thuận,6:Chỉnh sửa|
9|1|T|Chốt baseline tiến độ, phát hành cho các bên|10|
10|1|E|Cập nhật lên hệ thống, chuyển sang theo dõi tiến độ|
"""),
"LGEC-05": dict(
  goal="Mỗi hạng mục chỉ khởi công khi biện pháp thi công và bản vẽ thi công chi tiết đã được rà soát an toàn, chất lượng và được duyệt.",
  inp="Hạng mục sắp thi công theo tiến độ; hồ sơ thiết kế được duyệt", out="Biện pháp thi công và shopdrawing được duyệt, phát hành có kiểm soát phiên bản",
  app="Base BPM (trình duyệt nhiều bên) + E-Office (lưu hồ sơ kỹ thuật)",
  lanes=["Phòng Kỹ thuật / BCH", "Đơn vị tư vấn thiết kế", "Phòng QA/QC & ATLĐ", "Lãnh đạo LGEC", "TVGS / CĐT"],
  steps="""
1|0|S|Hạng mục đến kỳ chuẩn bị thi công theo tiến độ|2|
2|0|T|Lập biện pháp thi công và bản vẽ thi công chi tiết|3,4|Biện pháp thi công, shopdrawing
3|1|T|Xác nhận phù hợp thiết kế được duyệt|5|
4|2|T|Rà soát an toàn, chất lượng và phương án kiểm tra|5|
5|3|D|Lãnh đạo có duyệt nội bộ không?|6:Duyệt,2:Sửa|
6|4|D|TVGS/CĐT có chấp thuận không?|7:Chấp thuận,2:Yêu cầu sửa|
7|0|T|Phát hành bản vẽ và biện pháp được duyệt, kiểm soát phiên bản|8|
8|0|E|Phổ biến cho tổ đội, NTP và cho phép thi công hạng mục|
"""),
"LGEC-08": dict(
  goal="Xuất vật tư đúng định mức, đúng khối lượng thi công; vượt định mức phải giải trình; tồn kho thấp tự sinh nhu cầu đặt hàng.",
  inp="Phiếu đề nghị xuất vật tư theo khối lượng thi công trong tuần", out="Vật tư được cấp có ký nhận; sổ kho cập nhật; đề nghị đặt hàng bổ sung nếu cần",
  app="Base Inventories (xuất kho, tồn tối thiểu) + Base Requests (phiếu đề nghị)",
  lanes=["Tổ đội / Kỹ sư hiện trường", "Thủ kho", "Phòng Cung ứng", "Chỉ huy trưởng"],
  steps="""
1|0|S|Lập phiếu đề nghị xuất vật tư theo khối lượng thi công trong tuần|2|Phiếu đề nghị xuất vật tư
2|0|T|Kỹ sư xác nhận định mức và khối lượng cần dùng|3|
3|3|D|Số lượng có vượt định mức không?|5:Không,4:Có|
4|3|T|Xem xét giải trình, phê duyệt hoặc từ chối phần vượt|5|
5|1|T|Kiểm tồn, xuất kho, lập phiếu xuất|6|Phiếu xuất kho
6|0|T|Nhận vật tư, ký xác nhận|7|
7|1|T|Cập nhật sổ kho|8|
8|1|D|Tồn kho có thấp hơn mức tối thiểu không?|9:Có,10:Không|
9|2|E|Lập đề nghị đặt hàng bổ sung, chuyển sang quy trình đặt hàng|
10|1|E|Kết thúc, đối chiếu kho cuối kỳ|
"""),
"LGEC-09": dict(
  goal="Biết hằng tuần công trình đang nhanh hay chậm so với tiến độ gốc, vì sao chậm, bù thế nào, và khi nào phải xin CĐT điều chỉnh mốc.",
  inp="Khối lượng thực hiện hằng ngày/tuần; tiến độ gốc (baseline)", out="Báo cáo tiến độ tuần/tháng; phương án bù tiến độ; đề nghị điều chỉnh mốc (nếu cần)",
  app="Base Projects/Cowork (check-in tiến độ, roadmap, mốc) + Base Requests (đề nghị điều chỉnh tiến độ)",
  lanes=["Tổ đội / NTP", "Kỹ sư hiện trường", "Cán bộ kế hoạch (QLDA)", "Chỉ huy trưởng", "Lãnh đạo LGEC", "CĐT / TVGS"],
  steps="""
1|0|S|Cuối ngày/tuần báo cáo khối lượng đã thực hiện|2|
2|1|T|Xác nhận khối lượng thực tế tại hiện trường, ghi nhật ký thi công|3|Nhật ký thi công, biên bản khối lượng
3|2|T|Cập nhật tiến độ thực tế, so với baseline (phần trăm hoàn thành, đường găng)|4|
4|2|D|Có chậm tiến độ vượt ngưỡng cho phép không?|8:Không,5:Có|
5|2|T|Phân tích nguyên nhân: nhân lực, vật tư, thời tiết, mặt bằng, thiết kế|6|Phiếu phân tích nguyên nhân chậm
6|3|T|Lập phương án bù tiến độ: tăng ca, tăng tổ đội, đổi biện pháp|7|
7|4|D|Lãnh đạo xử lý thế nào?|8:Duyệt bù,9:Xin điều chỉnh mốc|
8|2|T|Tổng hợp báo cáo tiến độ tuần/tháng gửi chỉ huy trưởng, lãnh đạo, CĐT|10|Báo cáo tiến độ tuần/tháng
9|5|T|CĐT xem xét điều chỉnh mốc, gia hạn theo hợp đồng|8|
10|3|E|Họp giao ban tuần, chốt kế hoạch tuần tới|1:Chu kỳ tuần sau|
"""),
"LGEC-11": dict(
  goal="Lỗi chất lượng được ghi nhận, xác định trách nhiệm, sửa và nghiệm thu lại có biên bản; chi phí và số ngày chậm do sửa lỗi được ghi nhận.",
  inp="Lỗi phát hiện qua kiểm tra hoặc nghiệm thu không đạt", out="Biên bản đóng lỗi; chi phí sửa lỗi được quy trách nhiệm; hồ sơ chất lượng cập nhật",
  app="Base Requests/BPM (phiếu lỗi chất lượng) + Base Dataset (nhật ký lỗi)",
  lanes=["QA/QC / Kỹ sư hiện trường", "Chỉ huy trưởng", "Tổ đội / NTP", "TVGS / CĐT", "Phòng TCKT"],
  steps="""
1|0|S|Phát hiện lỗi chất lượng (kiểm tra hoặc nghiệm thu không đạt)|2|
2|0|T|Lập biên bản ghi nhận lỗi: vị trí, ảnh, mức độ|3|Biên bản lỗi chất lượng
3|1|T|Phân tích nguyên nhân, xác định bên chịu trách nhiệm|4|
4|1|T|Lập phương án khắc phục và thời hạn|5|
5|3|D|TVGS/CĐT có chấp thuận phương án không?|6:Chấp thuận,4:Chỉnh sửa|
6|2|T|Thực hiện sửa chữa theo phương án|7|
7|0|T|Kiểm tra lại, nghiệm thu sau sửa|8|
8|0|D|Kết quả sau sửa có đạt không?|9:Đạt,6:Chưa đạt|
9|4|T|Ghi nhận chi phí sửa lỗi, trừ hoặc truy thu bên chịu trách nhiệm|10|
10|0|E|Đóng biên bản, cập nhật tiến độ và hồ sơ chất lượng|
"""),
"LGEC-12": dict(
  goal="An toàn, PCCN và vệ sinh môi trường được lập kế hoạch, kiểm tra thường xuyên và xử lý vi phạm có hồ sơ.",
  inp="Biện pháp thi công; kế hoạch tiến độ", out="Báo cáo ATLĐ định kỳ; biên bản vi phạm và khắc phục",
  app="Base Requests/BPM (biên bản kiểm tra) + Base Dataset (sổ huấn luyện, thẻ ATLĐ)",
  lanes=["Cán bộ ATLĐ / PCCN", "Chỉ huy trưởng", "Tổ đội / NTP", "Lãnh đạo LGEC"],
  steps="""
1|0|S|Lập kế hoạch AT-PCCN-ATLĐ-VSMT theo từng giai đoạn thi công|2|Kế hoạch ATLĐ
2|1|D|Chỉ huy trưởng có duyệt kế hoạch không?|3:Duyệt,1:Chỉnh sửa|
3|0|T|Huấn luyện ATLĐ, cấp thẻ, kiểm tra trang bị bảo hộ|4|Sổ huấn luyện ATLĐ
4|2|T|Thi công theo biện pháp an toàn, ký cam kết|5|
5|0|T|Kiểm tra hiện trường hằng ngày/tuần, lập biên bản vi phạm|6|Biên bản kiểm tra ATLĐ
6|0|D|Có vi phạm hoặc nguy cơ mất an toàn không?|9:Không,7:Có|
7|1|T|Đình chỉ hạng mục có nguy cơ, yêu cầu khắc phục|8|
8|2|T|Khắc phục và báo cáo|5:Kiểm tra lại|
9|0|T|Tổng hợp báo cáo ATLĐ tuần/tháng|10|
10|3|E|Xem xét báo cáo, xử lý sự cố, rút bài học|
"""),
"LGEC-13": dict(
  goal="Thiết bị thi công được bảo dưỡng theo lịch, hỏng hóc xử lý nhanh và có lý lịch, tránh dừng máy làm chậm tiến độ.",
  inp="Lịch bảo dưỡng định kỳ hoặc thiết bị hỏng", out="Thiết bị vận hành lại; lý lịch và chi phí được cập nhật",
  app="Base Requests/BPM (phiếu sửa chữa) + Base Dataset (lý lịch thiết bị)",
  lanes=["Người vận hành", "Cán bộ thiết bị", "Chỉ huy trưởng", "Phòng Cung ứng / NCC dịch vụ", "Phòng TCKT"],
  steps="""
1|0|S|Phát hiện hỏng hóc hoặc đến chu kỳ bảo dưỡng|2|
2|1|T|Kiểm tra, ghi nhận tình trạng vào lý lịch thiết bị|3|Lý lịch thiết bị
3|1|D|Tự sửa được tại công trường không?|4:Được,5:Không|
4|1|T|Bảo dưỡng hoặc sửa chữa tại công trường|8|
5|3|T|Hỏi giá, chọn đơn vị sửa chữa hoặc thuê thiết bị thay thế|6|
6|2|D|Chỉ huy trưởng có duyệt chi phí không?|7:Duyệt,5:Điều chỉnh|
7|3|T|Sửa chữa hoặc thay thế, bố trí thiết bị dự phòng|8|
8|1|T|Nghiệm thu thiết bị sau sửa, cho vận hành lại|9|
9|4|E|Cập nhật lý lịch, ghi nhận chi phí, điều chỉnh lịch bảo dưỡng|
"""),
"LGEC-14": dict(
  goal="Mọi thay đổi và phát sinh có biên bản hiện trường, đề xuất khối lượng - đơn giá - tác động tiến độ, và được CĐT chấp thuận trước khi thanh toán.",
  inp="Yêu cầu của CĐT, sai khác thiết kế hoặc điều kiện hiện trường", out="Phụ lục/chấp thuận phát sinh; baseline tiến độ và khối lượng thanh toán được cập nhật",
  app="Base Requests/BPM (đề xuất phát sinh) + Base Projects (cập nhật tiến độ)",
  lanes=["Kỹ sư hiện trường", "Phòng QLDA / Dự toán", "Chỉ huy trưởng", "CĐT / TVGS", "Lãnh đạo LGEC"],
  steps="""
1|0|S|Phát sinh thay đổi (yêu cầu CĐT, sai khác thiết kế, điều kiện hiện trường)|2|
2|0|T|Lập biên bản hiện trường, ghi nhận khối lượng và ảnh|3|Biên bản phát sinh hiện trường
3|1|T|Lập đề xuất phát sinh: khối lượng, đơn giá, tác động tiến độ|4|Đề xuất phát sinh
4|2|D|Phát sinh có ảnh hưởng đáng kể tiến độ hoặc chi phí không?|6:Không,5:Có|
5|4|T|Quyết định hướng xử lý, đề xuất kéo dài tiến độ nếu cần|6|
6|3|T|CĐT xem xét, ra chỉ thị hoặc chấp thuận|7|
7|3|D|CĐT có chấp thuận phát sinh không?|8:Chấp thuận,9:Từ chối|
8|1|T|Lập phụ lục hợp đồng, cập nhật khối lượng thanh toán và baseline tiến độ|10|
9|2|T|Xử lý theo hợp đồng, lưu hồ sơ khiếu nại nếu cần|10|
10|1|E|Đồng bộ vào thanh toán và tiến độ|
"""),
"LGEC-16": dict(
  goal="Thanh toán cho NTP/NCC đúng khối lượng đã nghiệm thu, đủ hồ sơ, có giữ lại bảo hành theo hợp đồng.",
  inp="Đề nghị thanh toán của NTP/NCC; biên bản nghiệm thu khối lượng", out="Khoản chi được thực hiện; công nợ NTP/NCC được đối chiếu",
  app="Base Requests/BPM (đề nghị thanh toán) + eSign",
  lanes=["NTP / NCC", "Kỹ sư hiện trường / QLDA", "Phòng TCKT LGEC", "Chỉ huy trưởng", "Lãnh đạo LGEC"],
  steps="""
1|0|S|Hoàn thành khối lượng, gửi đề nghị thanh toán|2|Giấy đề nghị thanh toán
2|1|T|Xác nhận khối lượng đã nghiệm thu|3|
3|3|T|Xác nhận chất lượng và tiến độ, ký đề nghị|4|
4|2|T|Đối chiếu hợp đồng, hóa đơn, tạm ứng, giữ lại bảo hành|5|
5|2|D|Hồ sơ đã đủ chưa?|6:Đủ,1:Thiếu|
6|4|D|Lãnh đạo có duyệt chi không?|7:Duyệt,4:Chưa duyệt|
7|2|T|Thanh toán, hạch toán công nợ|8|
8|2|E|Đối chiếu công nợ NTP/NCC, cập nhật lũy kế|
"""),
"LGEC-17": dict(
  goal="Công trình hoàn thành được rà soát tồn đọng, nghiệm thu hoàn thành với CĐT và bàn giao đủ hồ sơ hoàn công.",
  inp="Hoàn thành thi công các hạng mục; hồ sơ chất lượng", out="Biên bản nghiệm thu hoàn thành; hồ sơ hoàn công bàn giao; bắt đầu thời hạn bảo hành",
  app="Base Projects/Cowork (danh mục tồn đọng) + Base Requests/BPM (biên bản) + eSign",
  lanes=["Ban chỉ huy công trình", "Phòng QA/QC LGEC", "Tư vấn giám sát", "Chủ đầu tư (LGL)", "Phòng QLDA LGEC"],
  steps="""
1|0|S|Hoàn thành thi công toàn bộ hạng mục|2|
2|1|T|Rà soát hồ sơ chất lượng, lập danh mục tồn đọng (punch list)|3|Danh mục tồn đọng
3|0|T|Khắc phục tồn đọng, hoàn thiện, vệ sinh công nghiệp|4|
4|4|T|Lập hồ sơ hoàn công và hồ sơ nghiệm thu|5|Hồ sơ hoàn công
5|2|T|Kiểm tra hồ sơ, đề nghị CĐT tổ chức nghiệm thu|6|
6|3|T|CĐT tổ chức nghiệm thu hoàn thành, kiểm tra hiện trường|7|
7|3|D|Nghiệm thu có đạt không?|8:Đạt,3:Còn tồn tại|
8|4|T|Ký biên bản nghiệm thu, bàn giao công trình và hồ sơ cho CĐT|9|Biên bản nghiệm thu hoàn thành
9|4|E|Chuyển sang quyết toán và bảo hành|
"""),
"LGEC-18": dict(
  goal="Quyết toán khớp khối lượng và thanh toán, theo dõi bảo hành đến khi CĐT xác nhận hoàn thành, và tổng kết công trình để rút kinh nghiệm.",
  inp="Biên bản nghiệm thu hoàn thành; hồ sơ thanh toán và phát sinh", out="Giá trị quyết toán được CĐT chấp thuận; tiền bảo hành được thu hồi; báo cáo tổng kết công trình",
  app="Base Requests/BPM + Base Dataset (sổ bảo hành, nhắc hạn)",
  lanes=["Phòng QLDA / Dự toán", "Phòng TCKT", "Chủ đầu tư (LGL)", "Kỹ thuật bảo hành", "Lãnh đạo LGEC"],
  steps="""
1|0|S|Công trình được bàn giao, bắt đầu quyết toán và tính thời hạn bảo hành|2|
2|0|T|Lập hồ sơ quyết toán khối lượng và phát sinh|3|Hồ sơ quyết toán
3|1|T|Đối chiếu giá trị quyết toán, đã thanh toán, tạm ứng|4|
4|2|D|CĐT có chấp thuận giá trị quyết toán không?|5:Chấp thuận,2:Điều chỉnh|
5|1|T|Xuất hóa đơn cuối, thu tiền, giữ lại tiền bảo hành theo hợp đồng|6|
6|3|T|Tiếp nhận yêu cầu bảo hành, kiểm tra và xử lý trong thời hạn|7|Phiếu yêu cầu bảo hành
7|3|D|Còn yêu cầu bảo hành hoặc còn trong thời hạn không?|6:Còn,8:Hết hạn|
8|2|T|CĐT xác nhận LGEC hoàn thành trách nhiệm bảo hành|9|
9|1|T|Thu hồi tiền bảo hành hoặc giải tỏa bảo lãnh|10|
10|4|E|Tổng kết công trình: lãi lỗ, tiến độ so với baseline, bài học; lưu hồ sơ|
"""),
}

# Quy trình lấy lại từ bộ 15 (nội dung giữ nguyên)
REUSE = {
    "LGEC-06": "QLDA-LGEC-07", "LGEC-07": "CUNGUNG-01", "LGEC-10": "QLDA-LGEC-02", "LGEC-15": "QLDA-LGEC-05",
}


def _parse(steps_text):
    import re
    out = []
    for line in steps_text.strip().splitlines():
        parts = line.split("|"); parts += [""] * (7 - len(parts))
        sid, lane, typ, text, nxt, note, sla = parts[:7]
        nx = []
        if nxt:
            toks = re.split(r",(?=\s*\d+(?::|$|,))", nxt) if ":" in nxt else [p for p in nxt.split(",") if p.strip()]
            for t in toks:
                to, lab = (t.split(":", 1) + [""])[:2] if ":" in t else (t, "")
                nx.append(dict(to=to.strip(), label=lab.strip()))
        out.append(dict(id=sid, lane=int(lane), type=typ, text=text, next=nx, note=note, sla=sla))
    return out


def build():
    _, old = lg_data.build()
    old_by = {f["code"]: f for f in old}
    phase_name = dict(PHASES)
    flows, catalog = [], []
    for i, (code, ph, name, src, dmcode, frm, to, prog, wave) in enumerate(SEQ, 1):
        if code in REUSE:
            o = old_by[REUSE[code]]
            f = dict(goal=o["goal"], inp=o["inp"], out=o["out"], app=o["app"], lanes=list(o["lanes"]),
                     steps=[dict(s, next=[dict(n) for n in s["next"]]) for s in o["steps"]])
        else:
            n = NEW[code]
            import lanes_map
            f = dict(goal=n["goal"], inp=n["inp"], out=n["out"], app=n["app"], lanes=lanes_map.apply(code, n["lanes"]), steps=_parse(n["steps"]))
        f.update(code=code, name=name, field=phase_name[ph], unit="LGEC", wave=src, prog=prog,
                 frm=frm, to=to, seq=i, dm=dmcode, priority=wave)
        flows.append(f)
        catalog.append(dict(stt=i, group=ph, field=phase_name[ph], unit="LGEC", code=code, name=name,
                            src=src, dm=dmcode, frm=frm, to=to, prog=prog, priority=wave, flow=True))
    return catalog, flows


if __name__ == "__main__":
    cat, fl = build()
    for f in fl:
        ids = {s["id"] for s in f["steps"]}
        for s in f["steps"]:
            for n in s["next"]:
                assert n["to"] in ids, (f["code"], s["id"], n)
            assert 0 <= s["lane"] < len(f["lanes"]), (f["code"], s["id"])
        print(f["code"], len(f["steps"]), "bước", f["wave"])
    codes = {f["code"] for f in fl}
    for f in fl:
        for c in f["frm"] + f["to"]:
            assert c in codes, (f["code"], c)
    print(len(fl), "QT OK")
