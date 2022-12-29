import xlwt
def export_excel(currency, items):
    workbook = xlwt.Workbook(encoding="utf-8")

    sheet1 = workbook.add_sheet(currency)

    sheet1.write(0, 0, "币种")
    sheet1.write(0, 1, "链")
    sheet1.write(0, 2, "hash")
    sheet1.write(0, 3, "块高")
    sheet1.write(0, 4, "交易前余额")
    sheet1.write(0, 5, "交易后余额")
    row = 1
    # items = claimed_reward("ksm",last_block, address)

    for item in items:
        sheet1.write(row, 0, item["currency"])
        sheet1.write(row, 1, item["address"])
        sheet1.write(row, 2, item["amount"])
        sheet1.write(row, 3, item["hash"])
        sheet1.write(row, 4, item["block"])
        sheet1.write(row, 5, item["block_time"])
        row += 1

    workbook.save("staking-profit-%s.xls" % currency)

