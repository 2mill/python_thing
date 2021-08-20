import sys, argparse, csv
import csv_processor

parser = argparse.ArgumentParser(prog="patchmap",
									description="Make port mapping easier with this tool",
									usage="unspecified",
									)
parser.add_argument('--csv', type=str, required=True, help='specify the CSV file to be used')
parser.add_argument('-o', '--output', type=str, help='Specify output format. Currently only supports plain unformatted text')
parser.add_argument('-c', '--config', type=str, help='Define a seperate header construction, more to be deinfed in README later')
args = parser.parse_args()
# temp_list = processor.create_list(args.csv)
# processor.generate_parent_room_list(temp_list)

def create_list(filename:str) -> list:
	# REQ utf-8-sig
	with open(f"./{filename}", encoding="utf-8-sig") as f:
		reader: list = csv.reader(f)
		csv_processor.process(reader)
