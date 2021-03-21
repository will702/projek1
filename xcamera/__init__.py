import os

project_dir = os.path.abspath(
    os.path.join(__file__, os.pardir, os.pardir, os.pardir, os.pardir))
using_pip = os.path.basename(project_dir).startswith('pip-')
# only exposes `XCamera` if not within `pip` ongoing install
if not using_pip:
    from .xcamera import XCamera  # noqa
