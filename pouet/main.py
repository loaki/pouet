import os
import logging
import argparse

from converter import convert

logging.basicConfig(
    format="%(asctime)s - %(levelname)s : %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)

def main():
    argparser = argparse.ArgumentParser(description="anotate music sheet")
    argparser.add_argument("-i", "--infile", default=None, type=str,
                         help="input filename")
    argparser.add_argument("-d", "--indir", default=None, type=str,
                         help="input filename")
    argparser.add_argument("-o", "--outdir", default=None, type=str,
                         help="output filename")
    argparser.add_argument("-ms", "--ms_img_path", default=None, type=str,
                         help="output filename")
    args = argparser.parse_args()

    if args.indir:
        files = os.listdir(args.indir)
    elif args.infile:
        files = [args.infile]
    else:
        logging.error("no input file")
        return False
    cache_dir = "cache"
    out_dir = args.outdir or "pdf"

    for file in files:
        file_name = file.split("/")[-1].split(".")[0]
        ext = file.split(".")[-1]
        if ext not in ["mid", "mscx", "musicxml", "mxl"]:
            logging.error(f"{file_name} : extension .{ext} not supprted")
            continue
        if convert(old=file, new=f"{cache_dir}/{file_name}.mscx", ms_img=args.ms_img_path, logger=logging):
            #parsing
            convert(old=f"{cache_dir}/{file_name}.mscx", new=f"{out_dir}/{file_name}.pdf", ms_img=args.ms_img_path, logger=logging)
            os.remove(f"{cache_dir}/{file_name}.mscx")


if __name__ == "__main__":
    main()