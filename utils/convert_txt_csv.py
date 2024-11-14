import argparse
import csv
import os

def convert_txt_csv(fname: str) -> None:
    csv_fname = fname[:-3]
    with open(fname, 'r') as f:
        stripped = (line.strip() for line in f)
        lines = (line.split(",") for line in stripped if line)
        with open(f'{csv_fname}csv', 'w') as out_file:
            writer = csv.writer(out_file)
            #writer.writerow(('title', 'intro'))
            writer.writerows(lines)

    pass

def convert_dir_csv(dir_name: str) -> None:
    files = os.listdir(dir_name)
    for file in files:
        if file.split('.')[-1] == "txt":
            convert_txt_csv(os.path.join(dir_name, file))
    

def main(args):
    if args.fname:
        convert_txt_csv(args.fname)
    elif args.dir_name:
        convert_dir_csv(args.dir_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .txt files to .csv")

    parser.add_argument("-f", "--fname", type = str, help = "A single file ending in .txt")
    parser.add_argument("-dir", "--dir_name", type = str, help = "A single direcotry containing some .txt")

    args = parser.parse_args()

    main(args=args)