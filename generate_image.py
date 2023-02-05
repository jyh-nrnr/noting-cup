import textwrap
import time, os
from io import BytesIO
import cv2 
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random

def make_title_object(image, font_path, name_font_name, subtitle_font_name, name, taster, extraction, roasting):
    row, col, dim = image.shape
    subtitle = "TASTING@" + taster + "    |    " + "EXTRACTION@" + extraction + "    |    " + "ROASTING@" + roasting

    name_gap = int(col / 20)
    for name_fontsize in range(10, 500, 5):
        font = ImageFont.truetype(font_path+name_font_name, name_fontsize)
        width, _ = font.getsize(name)
        if width + name_gap + name_gap > col:
            break
    name_fontsize -= 5

    subtitle_gap = int(col / 20)
    for subtitle_fontsize in range(10, 500, 5):
        font = ImageFont.truetype(font_path+subtitle_font_name, subtitle_fontsize)
        width, _ = font.getsize(subtitle)
        if width + subtitle_gap + subtitle_gap > col :     
            break
    subtitle_fontsize -= 5

    return (name, subtitle, name_fontsize, subtitle_fontsize)

def add_upper_background(image, font_path, name_font_name, subtitle_font_name, upper_title):
    coffee_name, subtitle, name_fontsize, subtitle_fontsize = upper_title

    row, col, dim, = image.shape
    
    name_font = ImageFont.truetype(font_path+name_font_name, name_fontsize)
    _, name_height = name_font.getsize(coffee_name)

    subtitle_font = ImageFont.truetype(font_path+subtitle_font_name, name_fontsize)
    _, subtitle_height = subtitle_font.getsize(subtitle)

    upper_background_height = int(2.5*name_height) + subtitle_height

    upper_background = np.zeros((row + upper_background_height, col, dim)) + 255
    upper_background[upper_background_height:, :col, :] = image

    return upper_background

def add_title(image, font_path, name_font_name, subtitle_font_name, upper_title):
    name, subtitle, name_fontsize, subtitle_fontsize = upper_title
    row, col, dim, = image.shape

    name_font = ImageFont.truetype(font_path+name_font_name, name_fontsize)
    name_width, name_height = name_font.getsize(name)

    subtitle_font = ImageFont.truetype(font_path+subtitle_font_name, subtitle_fontsize)
    subtitle_width, subtitle_height = subtitle_font.getsize(subtitle)

    text_color = (0, 0, 0)

    position_y = name_height
    # ==========================
    image = Image.fromarray(image.astype('uint8'), 'RGB')
    draw = ImageDraw.Draw(image)

    name_position = ((col - name_width) / 2, position_y)
    draw.text(name_position, name, font=name_font, fill=text_color)

    position_y += name_height
    position_y += (name_height*0.5)

    subtitle_position = ((col - subtitle_width) / 2, position_y)
    draw.text(subtitle_position, subtitle, font=subtitle_font, fill=text_color)

    return np.array(image)

def find_width(text, font, col):
    thresh = int(col * 4 / 5)
    for i in range(10, 500, 5):
        lines = textwrap.wrap(text, width=i) 
        line_widths, line_heights = [], []
        for line in lines:
            line_width, line_height = font.getsize(line)
            line_widths.append(line_width)
        if max(line_widths) > thresh:
            break
    return i-5

def make_note_object(image, font_path, note_font_name, date_font_name, name_fontsize, note, now_date):
    row, col, dim = image.shape

    note_fontsize = int(name_fontsize * 2 / 3)
    note_font = ImageFont.truetype(font_path+note_font_name, note_fontsize)

    date_fontsize = int(name_fontsize * 2 / 5)

    text_color = (0,0,0)

    thresh = int(col * 4 / 5)
    for i in range(10, 500, 5):
        lines = textwrap.wrap(note, width=i) 
        line_widths, line_heights = [], []
        for line in lines:
            line_width, line_height = note_font.getsize(line)
            line_widths.append(line_width)
        if max(line_widths) > thresh:
            break
    note_width = i-5

    notes = textwrap.wrap(note, width=note_width) 

    return (notes, now_date, note_fontsize, date_fontsize)

def add_lower_background(image, font_path, note_font_name, date_font_name, lower_note):
    notes, now_date, note_fontsize, date_fontsize = lower_note

    row, col, dim, = image.shape

    note_font = ImageFont.truetype(font_path+note_font_name, note_fontsize)

    note_heights = 0
    for note in notes:
        _, note_height = note_font.getsize(note)
        note_heights += note_height

    date_font = ImageFont.truetype(font_path+date_font_name, date_fontsize)
    _, date_height = date_font.getsize(now_date)


    lower_background_height = int(2.5*note_heights) + date_height

    lower_background = np.zeros((row + lower_background_height, col, dim)) + 255
    lower_background[:row, :col, :] = image

    return lower_background

def add_note(image_add_lower, image_no_lower, font_path, note_font_name, date_font_name, lower_note):
    notes, now_date, note_fontsize, date_fontsize = lower_note

    row_l, col_l, dim_l, = image_add_lower.shape
    row, col, dim, = image_no_lower.shape

    note_font = ImageFont.truetype(font_path+note_font_name, note_fontsize)

    date_font = ImageFont.truetype(font_path+date_font_name, date_fontsize)

    image = Image.fromarray(image_add_lower.astype('uint8'), 'RGB')
    draw = ImageDraw.Draw(image)

    text_color = (0, 0, 0)

    _, note_height = note_font.getsize(notes[0])

    position_y = row + int(note_height/2)

    for note in notes:
        note_width, note_height = note_font.getsize(note)
        text_position = ((col - note_width) / 2, position_y)
        draw.text(text_position, note, font=note_font, fill=text_color)
        position_y = position_y + note_height + 10

    position_y += int(note_height/2)
    date_width, date_height = date_font.getsize(now_date)
    text_position = ((col - date_width) / 2, position_y)
    draw.text(text_position, now_date, font=date_font, fill=text_color)

    return np.array(image)