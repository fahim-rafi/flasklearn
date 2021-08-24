import os
from PIL import Image
from flask import url_for, current_app


def add_profile_picture(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split(".")
