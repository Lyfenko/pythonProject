from sys import argv
from pathlib import Path

def read_folder(path: Path) -> list[Path]:
    pass

def create_target_folders(path: Path) -> str:
    pass

def mormalize(name: str) -> str:
    return 'name'

def rename_file(name: str) -> str:
    pass

def archive(path: Path) -> str:
    pass

def delete_folders (path: Path) -> str:
    pass

def sort_files(path: Path) -> str:
    pass

def main() -> str:
    print(sort_files(Path(r'd:\testfolder')))

if __name__ == "main"
main()

# work_dir = Path(r'd:\testfolder')
#
# # print(len(list(work_dir.glob('**/*'))))
#
# for item in work_dir.glob('**/*'):
#     if irtem.is_file():
#         print(item.parent)
#
#
# CATEGORIES = {'music': ['.mp3', '.ogg'], 'documents': ['.docx', '.pdf']}
#
# for i in CATEGORIES:
#     if work_dir.joinpath(i).exist():
#         work_dir.joinpath(i).mkdir()
#
#
# def create_categories(path: str) -> dict:
#     with open(path) as f:
#         cats = f.readlines()
#         result = {}
#         for item in cats:
#             result[item.split(':')[0]] = item.split(':')[1]
#             return result
# CATEGORIES = create_categories('cat.txt')
#
# for k, v in CATEGORIES.items():
#     print(v)


#
# path = None
#
# print(sys.argv)
#
# try:
#     path = sys.argv[1]
# except IndexError:
#     print("No param")
#
# print(path)

def archive(path: Path) -> str:
    path.rmdir()
    pass
