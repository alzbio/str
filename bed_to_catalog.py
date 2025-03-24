import csv
import json
from argparse import (ArgumentParser, FileType)

def parse_args():
	parser = ArgumentParser(description='Convert a BED format file to ExpansionHunter variant catalogue (JSON) file')
	parser.add_argument('--bed', type=str, required=True, help='Input BED file')
	parser.add_argument('--out', type=str, required=True, help='Output ExpansionHunter JSON file')
	
	return parser.parse_args() 

def main():
	args = parse_args()
	bedfile = args.bed
	jsonfile = args.out

	catalogue = []
	with open(bedfile, 'r') as bed:
		bedfile = csv.reader(bed, delimiter='\t')
		for row in bedfile:
			try:
				chrom = row[0]
				start = row[1]
				end = row[2]
				motif = row[3]
				catalogue.append({
					"LocusId": chrom + '-' + str(start) + '-' + str(end),
					"LocusStructure": '(' + motif + ')*',
					"ReferenceRegion": chrom + ':' + str(start) + '-' + str(end),
					"VariantType": "Repeat",
					})

			except IndexError:
				pass

	cat_json = json.dumps(catalogue, indent = 4)

	with open(jsonfile, "w") as outfile:
		outfile.write(cat_json)

if __name__ == '__main__':
	main()