import os
import shutil


def get_root_path() -> str:
    # current_file_path/../../
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def remove_folder(folder_path: str) -> None:
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)


def create_folder_if_not_exists(folder_path: str) -> None:
    if not os.path.isdir(folder_path):
        # create the folder recursively
        os.makedirs(folder_path)


def is_dir(path: str) -> bool:
    return os.path.isdir(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def copy_file(src: str, dest: str) -> None:
    ensure_is_file(src)
    shutil.copy(src, dest)


def copy_folder(src: str, dest: str) -> None:
    ensure_is_dir(src)
    shutil.copytree(src, dest)


def ensure_is_dir(path: str) -> None:
    if not is_dir(path):
        raise FileNotFoundError(f"路径 '{path}' 不是文件夹")


def ensure_is_file(path: str) -> None:
    if not is_file(path):
        raise FileNotFoundError(f"路径 '{path}' 不是文件")


def ensure_path_exists(path: str) -> None:
    if not is_dir(path) and not is_file(path):
        raise FileNotFoundError(f"路径 '{path}' 不存在")


def file_in_text_mode(file_path):
    ensure_path_exists(file_path)
    try:
        with open(file_path, 'r') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 '{file_path}' 不存在")
    except Exception as e:
        raise e
