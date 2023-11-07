import os
import logging
import argparse

from converter import convert

logging.basicConfig(
    format="%(asctime)s - %(levelname)s : %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)
CACHE_DIR="cache"
OUT_DIR="pdf"

def main():
    argparser = argparse.ArgumentParser(description="anotate music sheet")
    argparser.add_argument("-i", "--infile", default=None, type=str,
                         help="input filename")
    argparser.add_argument("-d", "--indir", default=None, type=str,
                         help="input filename")
    argparser.add_argument("-o", "--outdir", default=None, type=str,
                         help="output filename")
    args = argparser.parse_args()

    if args.indir:
        files = os.listdir(args.indir)
    elif args.infile:
        files = [args.infile]
    else:
        logging.error("no input file")
        return False

    for file in files:
        file_name = file.split("/")[-1].split(".")[0]
        ext = file.split(".")[-1]
        if ext not in ["mid", "mscx", "musicxml", "mxl"]:
            logging.error(f"{file_name} : extension .{ext} not supprted")
            continue
        convert(old=file, new=f"{CACHE_DIR}/{file_name}.mscx", logger=logging)
        convert(old=f"{CACHE_DIR}/{file_name}.mscx", new=f"{args.outdir or OUT_DIR}/{file_name}.pdf", logger=logging)
        os.remove(f"{CACHE_DIR}/{file_name}.mscx")


if __name__ == "__main__":
    main()