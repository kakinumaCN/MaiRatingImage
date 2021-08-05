# -*- coding: utf-8 -*-

from PIL import Image,ImageFont,ImageDraw
import json


def drawRoundRec(drawObject, x, y, w, h, r, fill_color):
    '''Rounds'''
    drawObject.ellipse((x, y, x + r, y + r), fill=fill_color)
    drawObject.ellipse((x + w - r, y, x + w, y + r), fill=fill_color)
    drawObject.ellipse((x, y + h - r, x + r, y + h), fill=fill_color)
    drawObject.ellipse((x + w - r, y + h - r, x + w, y + h), fill=fill_color)

    '''rec.s'''
    drawObject.rectangle((x + r / 2, y, x + w - (r / 2), y + h), fill=fill_color)
    drawObject.rectangle((x, y + r / 2, x + w, y + h - (r / 2)), fill=fill_color)


def draw_plate_arc_style(img_, dic_):
    draw = ImageDraw.Draw(img_)

    # draw 1
    # draw cover
    gd_img = Image.open("./res/gd.png")
    gd_img = gd_img.resize((250, 250), Image.ANTIALIAS)
    img_.paste(gd_img,(25,25))

    # draw rating base
    # master 159 81 220
    draw.polygon((275, 25, 525, 25, 575, 75, 275, 75), diff_color[dic_["level_label"]])

    # write dx rating
    draw.text((275 + 20 , 25 + 8), " "+str(dic_["ra"])+" [" + str(dic_["ds"]) + "]", font=ImageFont.truetype('C:/windows/fonts/Dengb.ttf', 30), fill="#ffffff")

    # write b rank
    draw.text((800 , 25 + 8),  "#" + str(i+1), font=ImageFont.truetype('C:/windows/fonts/Dengb.ttf', 45), fill="#000000")
    print(str(i))

    # draw 2
    # write title
    draw.text((275 + 20, 25+50+25), dic_["title"], font=ImageFont.truetype('C:/windows/fonts/Deng.ttf', 44), fill="#000000")

    # draw 3
    # write score
    draw.text((275 + 20, 25 + 50 + 25 + 60), str(dic_["achievements"]) + "%", font=ImageFont.truetype('C:/windows/fonts/ALGER.TTF', 54),fill="#000000")

    # draw score rank "rate": "sssp"
    score_rank_img = Image.open("./res/" + dic_["rate"] + ".png")
    r, g, b, a = score_rank_img.split()
    img_.paste(score_rank_img,(625, 25 + 50 + 25 + 60 - 20),mask=a)


    #draw 4
    #draw type "type": "SD"
    music_type_img = Image.open("./res/" + dic_["type"] + ".png")
    r, g, b, a = music_type_img.split()
    img_.paste(music_type_img, (275 + 20, 25 + 50 + 25 + 60 + 90), mask=a)

    #draw fc "fc": "fcp"
    if len(dic_["fc"]) > 0:
        fc_img = Image.open("./res/" + dic_["fc"] + ".png")
    else:
        fc_img = Image.open("./res/" + "fc_dummy" + ".png")
    r, g, b, a = fc_img.split()
    img_.paste(fc_img, (275 + 20 + 150, 25 + 50 + 25 + 60 + 90 - 8), mask=a)

    # #draw fs "fs": ""
    if len(dic_["fs"]) > 0:
        fs_img = Image.open("./res/" + dic_["fs"] + ".png")
    else:
        fs_img = Image.open("./res/" + "fs_dummy" + ".png")
    r, g, b, a = fs_img.split()
    img_.paste(fs_img, (275 + 20 + 150 + 150 , 25 + 50 + 25 + 60 + 90 - 15), mask=a)


def draw_name_pad_mai_style(base_img_):
    # draw name pad
    # load res
    name_pad_img = Image.open("./res/name_pad.png")
    name_pad_img.convert('RGBA')
    name_pad_img = name_pad_img.resize((1800, 300), Image.ANTIALIAS)

    # draw ava
    ava_img = Image.open("./res/ava.png")
    ava_img = ava_img.resize((250, 260), Image.ANTIALIAS)
    r, g, b, a = ava_img.split()
    name_pad_img.paste(ava_img, (20, 20), mask=a)

    # draw rating base
    rating_base_img = Image.open("./res/rating_base_rainbow.png")
    rating_base_img = rating_base_img.resize((425, 85), Image.ANTIALIAS)
    # write rating
    draw = ImageDraw.Draw(rating_base_img)
    ra_sum = ra_sum_sd + ra_sum_dx21
    ra_sum_list = []
    ra_pos_list = [(364 + 6,20),(321+ 6,20),(275+ 6,20),(228+ 6,20),(188+ 6,20)] # max 99999

    while 1:
        r = ra_sum%10
        ra_sum_list.append(r)
        ra_sum = int(ra_sum/10)
        if 0 == ra_sum:
            break
    for i in range(len(ra_sum_list)):
        draw.text(ra_pos_list[i],  str(ra_sum_list[i]), font=ImageFont.truetype('C:/windows/fonts/Dengb.ttf', 40), fill="#ffff00")
    # paste rating base
    r, g, b, a = rating_base_img.split()
    name_pad_img.paste(rating_base_img, (20 + 250 + 10, 20), mask=a)

    # draw mai_logo
    maimai_img = Image.open("./res/logo.png")
    maimai_img = maimai_img.resize((int(110 * 16 / 9), 110), Image.ANTIALIAS)
    r, g, b, a = maimai_img.split()
    name_pad_img.paste(maimai_img, (20 + 250 + 10 + 425 + 10, 5), mask=a)

    # draw name base
    name_base_img = Image.new('RGBA', (900 - 225, 105), (255, 255, 255, 0))
    # write name
    draw = ImageDraw.Draw(name_base_img)
    drawRoundRec(draw,0,0,900 - 225, 105,25,"#666666")
    drawRoundRec(draw, 3, 3, 900 - 225-6, 105-6, 25, "#ffffff")
    draw.text((10 , 10),  "Kakinuma", font=ImageFont.truetype('C:/windows/fonts/ALGER.TTF', 72), fill="#000000")
    # paste name base
    r,g,b,a = name_base_img.split()
    name_pad_img.paste(name_base_img,(20 + 250 + 10, 20 + 85 + 5) ,mask=a)

    #draw trophy
    trophy_img = Image.open("./res/trophy.png")
    trophy_img = trophy_img.resize((900 - 225, 60), Image.ANTIALIAS)
    # write rating on trophy
    draw = ImageDraw.Draw(trophy_img)
    # draw.text((20, 7), "Standard:2222    DX2021:3333", font=ImageFont.truetype('C:/windows/fonts/Dengb.ttf', 40), fill="#333333")
    draw.text((20, 7), "Kakinuma/maimai_DX_rating_image", font=ImageFont.truetype('C:/windows/fonts/Dengb.ttf', 38), fill="#333333")
    # paste trophy
    r, g, b, a = trophy_img.split()
    name_pad_img.paste(trophy_img, (20 + 250 + 10, 20 + 85 + 5 + 105 +5), mask=a)

    base_img_.paste(name_pad_img,(plate_edge,plate_edge))


if __name__ == '__main__':
    # load json
    with open("./res/my.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    record_list = load_dict["records"]

    record_sd_list = []
    record_dx21_list = []
    for r in record_list:
        if r["is_new"]:
            record_dx21_list.append(r)
        else:
            record_sd_list.append(r)
    record_sd_list = sorted(record_sd_list, key=lambda e: e.__getitem__('ra'), reverse=True)
    record_dx21_list = sorted(record_dx21_list, key=lambda e: e.__getitem__('ra'), reverse=True)
    record_sd_num = len(record_sd_list)
    if record_sd_num > 25 :
        record_sd_num = 25
    record_dx21_num = len(record_dx21_list)
    if record_dx21_num > 15 :
        record_dx21_num = 15
    ra_sum_sd = 0
    ra_sum_dx21 = 0

    # define
    template_dic = {"title": "林檎華憐歌", "level": "11+", "level_index": 3, "level_label": "Master", "type": "SD", "dxScore": 1886, "achievements": 100.6206, "rate": "sssp", "fc": "fcp", "fs": "", "ra": 166, "ds": 11.8, "song_id": "322", "is_new": "false"}
    diff_color = {"Master":"#9f51dc","Expert":"#ff7b7b","Advanced":"#00ffff","Re:MASTER":"#c495ea"}
    plate_interval = 60
    plate_edge = 90
    plate_width = 900
    plate_height = 300

    # load base = 3*14 plate
    base_img = Image.new('RGBA', (plate_width*3+plate_interval*2+plate_edge*2, plate_height*14+plate_interval*13+plate_edge*2),(81,188,243,255))

    # merge sd plate to base
    plate_startX = plate_edge
    plate_startY = plate_edge + plate_height + plate_interval
    for i in range(record_sd_num):

        plate_img = Image.new('RGBA', (900, 300), (255, 255, 255, 255))
        plate_img.convert('RGBA')
        draw_plate_arc_style(plate_img, record_sd_list[i])
        ra_sum_sd += record_sd_list[i]["ra"]

        x = plate_startX + i%2 * (plate_width + plate_interval)
        y = plate_startY + int(i/2) * (plate_height + plate_interval)
        base_img.paste(plate_img, (x, y))
        print("SD",i,x,y)

    # merge dx plate to base
    plate_startX = plate_edge + plate_width + plate_interval + plate_width + plate_interval
    plate_startY = plate_edge
    for i in range(record_dx21_num):

        plate_img = Image.new('RGBA', (900, 300), (255, 255, 255, 255))
        plate_img.convert('RGBA')
        draw_plate_arc_style(plate_img, record_dx21_list[i])
        ra_sum_dx21 += record_dx21_list[i]["ra"]

        x = plate_startX
        y = plate_startY + i * (plate_height + plate_interval)
        if 14==i :
            # DX15 move to left*1 up*1 to align
            x -= (plate_width + plate_interval)
            y -= (plate_height + plate_interval)
        base_img.paste(plate_img, (x, y))
        print("DX",i,x, y)

    draw_name_pad_mai_style(base_img)
    base_img.save("./out.png")

    print(ra_sum_sd,ra_sum_dx21)
    
