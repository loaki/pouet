import subprocess


def convert(
    old,
    new,
    MS="mscore",
    ms_img=None,
    logger=None,
):
    """Calls "MS -fo new old", which converts old to new with the given MuseScore executable."""
    process = [
        MS,
        "-fo",
        new,
        old,
    ]
    process_img = [
        ms_img,
        "--appimage-extract-and-run",
        "-fo",
        new,
        old,
    ]  # [MS, '--appimage-extract-and-run', "-fo", new, old] if MS.endswith('.AppImage') else [MS,
    # "-fo", new, old]
    if ms_img and subprocess.run(process_img, capture_output=True, text=True):
        logger.info(f"Converted {old} to {new}")
    elif subprocess.run(process, capture_output=True, text=True):
        logger.info(f"Converted {old} to {new}")
    else:
        logger.warning("Error while converting " + old)
        return False
    return True
