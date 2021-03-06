import os
import subprocess


LEVEL_DEV = 5
LEVEL_OWNER = 4
LEVEL_ADMIN = 3
LEVEL_MOD = 2
LEVEL_USER = 1
LEVEL_EVERYONE = 0

COLOR_YOUTUBE_RED = 0xcd201f
COLOR_WARCRAFTLOGS_GREY = 0x555555
ICON_YOUTUBE = "https://www.youtube.com/yts/img/favicon_144-vflWmzoXw.png"
ICON_WARCRAFTLOGS = "https://www.warcraftlogs.com/img/common/warcraft-logo.png"

DOWNLOAD_DIR = "/tmp/arwicbot/"
if not os.path.isdir(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

DATA_DIR = "data/"
DATA_EXT = ".db"
if not os.path.isdir(DATA_DIR):
    os.makedirs(DATA_DIR)

LOG_DIR = "logs/"
LOG_EXT = ".log"
if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

# get current git commit
CURRENT_COMMIT = subprocess.Popen('git log -n 1 --pretty=format:"%H"',
                                  shell=True,
                                  stdout=subprocess.PIPE).stdout.read()[:7].decode()
