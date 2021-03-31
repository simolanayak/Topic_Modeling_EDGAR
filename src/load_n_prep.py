from sec_edgar_downloader import Downloader
import textwrap
import html2text
import os

PATH = "./filings"
dl = Downloader(PATH)

ARGS = {"Report Type" : "10-K"}