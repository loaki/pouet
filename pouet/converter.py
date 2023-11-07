import subprocess


def convert(
    old,
    new,
    MS="mscore",
    logger=None,
):
    """Calls "MS -fo new old", which converts old to new with the given MuseScore executable."""
    process = [
        MS,
        "-fo",
        new,
        old,
    ]  # [MS, '--appimage-extract-and-run', "-fo", new, old] if MS.endswith('.AppImage') else [MS,
    # "-fo", new, old]
    if subprocess.run(process, capture_output=True, text=True):
        logger.info(f"Converted {old} to {new}")
    else:
        logger.warning("Error while converting " + old)
