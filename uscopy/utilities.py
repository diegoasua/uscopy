import numpy as np
from pathlib import Path
import os
import re
import shutil
from tifffile import imread, imsave
from warnings import warn
import tqdm


def stack_single_tiffs(base_dir: str, remove_old=True, verbose=True) -> None:
    """stacks individual tiffs in a number of folders. Structure should be:
    /base_dir
    ├── datafolder1
    |   ├── tiff1
    |   ├── tiff2
    │   └── ...
    ├── datafolder2
    |   ├── tiff1
    |   ├── tiff2
    │   └── ...
    └── ...

    Args:
        base_dir (str): Base directory.
        remove_old (bool, optional): Whether to keep original folder. Defaults to True.
        verbose (bool, optional): Print logs. Defaults to True.
    """
    base_directory = Path(base_dir)
    logger = []
    datafolders = [
        name
        for name in os.listdir(base_directory)
        if os.path.isdir(os.path.join(base_directory, name))
    ]  # clean anything which is not a folder
    for datafolder in tqdm.tqdm(datafolders):
        path_to_data = base_directory / datafolder
        dataset = []
        files = sorted(
            os.listdir(path_to_data)
        )  # important: sort, otherwise os.listdir() returns a random order
        r = re.compile(".*tif")
        files = list(filter(r.match, files))  # clean list of anything which is not .tif
        for n_file_name, file_name in enumerate(files):
            this_file = imread(str(path_to_data / file_name))
            if this_file.ndim > 2:
                for piece in this_file:
                    dataset.append(
                        piece
                    )  # first file contains 10 frames (a mystery) so we just take only the last one.
            else:
                dataset.append(this_file)
        try:
            dataset = np.stack(dataset)
        except ValueError:
            print(
                f'\x1b[31m"Could not stack dataset: {datafolder}. Is the folder empty?"\x1b[0m'
            )
            continue

        name = path_to_data.name + ".tif"
        save_dir = path_to_data.resolve().parents[0]
        imsave(str(save_dir / name), dataset)
        if remove_old:
            shutil.rmtree(path_to_data)  # remove the directory, leave the tiff file
        logger.append(
            f"{datafolder}.tif \n\t data structure: {type(dataset)} \n\t shape: {dataset.shape} \n\t dtype: {dataset.dtype}\n"
        )

    # show logs
    if verbose:
        for entry in logger:
            print(entry)

    # save logs to a file
    with open(save_dir / "merge_logs.txt", "w") as text_file:
        for log in logger:
            text_file.write(log)
