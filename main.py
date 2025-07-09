from clear_files import clear_all
from download_frames import download
from extract_tab_pics import extract_tab
from clean_tab import make_pdf
from main_directory import output_directory

main_directory = output_directory
clear_all(main_directory)
download(main_directory)
extract_tab(main_directory)
make_pdf(main_directory)
