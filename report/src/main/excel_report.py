from report.src.operators.xlsx_report_plugin import ExcelReportPlugin
from report.src.utils.discord.discord_webhook import send_to_discord
import os
import json

#Daily Gross Revenue per tanggal 25 Februari 2019
base_path = os.sep.join(os.getcwd().split(os.sep)[:-3])
print(f'base path: {base_path}')

input_file = base_path + '/input_data/supermarket_sales.xlsx'
output_file = base_path + '/output_data/report_penjualan_2019.xlsx'

# Opening JSON file
configs = open(base_path + '/configs/webhook.json')
webhook_url = json.load(configs)['webhook_url']

automate = ExcelReportPlugin(
    input_file=input_file,
    output_file=output_file
)
automate.main()
send_to_discord(webhook_url, output_file)