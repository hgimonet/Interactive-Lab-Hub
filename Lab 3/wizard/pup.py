from PIL import Image, ImageDraw

SPRITES = Image.open('imgs/dog.png')
alpha = SPRITES.split()[-1]
SPRITES.putalpha(alpha)
SPRITE_HEIGHT = 96
SPRITE_WIDTH = 96

def get_sprite(row,col):
    # col in [0,3], row in [0,8]
    return SPRITES.crop((col*96, row*96, (col+1)*96, (row+1)*96))


def gen_gif(action):
    '''
    Generates gif for each action
    :return:
    '''
    print(action)
    frames = FRAMES[action]
    # snippet from https://blog.zhaytam.com/2018/08/21/creating-gifs-using-python-pillow/
    frames[0].save('imgs/doggy_%s.gif'%(action),
                   format='GIF', append_images=frames[1:], save_all=True,
                   duration=100,
                   loop=0,
                   transparency=255,
                   disposal=2)


def gen_frames(imgs, bg_w=240, bg_h=135, img_w=96, img_h=96, bg_col='white', love=False):
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    if love:
        hearts = Image.open('imgs/hearts.png')
        heart_offset = [(bg_w - hearts.width) // 2, (bg_h - hearts.height) // 2]
        heart_mask = hearts.split()[-1]
        bg_col = 'pink'
    frames = []
    for img in imgs:
        background = Image.new('RGB', (bg_w, bg_h), bg_col)
        if love:
            background.paste(hearts, heart_offset, mask=heart_mask)
        background.paste(img, offset, mask=img.split()[-1])
        frames.append(background.rotate(90, expand=True))
    return frames

# find the correct images within the image
CROPS = {
    'walk_front': [get_sprite(0, col) for col in range(4)],
    'walk_right': [get_sprite(1, col) for col in range(4)],
    'walk_back': [get_sprite(2, col) for col in range(4)],
    'walk_left': [get_sprite(3, col) for col in range(4)],
    'sit_front': [get_sprite(4, col) for col in range(4)],
    'sit_side': [get_sprite(5, col) for col in range(4)]+[get_sprite(6, col) for col in range(3)],
    'sitting_side': [get_sprite(5, 3), get_sprite(7,3)],
    'down_side': [get_sprite(7, col) for col in range(2)],
    'run_side': [get_sprite(8, col) for col in range(3)],
}

FRAMES = {}
for crop in CROPS:
    FRAMES[crop] = gen_frames(CROPS[crop])
    # gen_gif(crop)

FRAMES['love'] = gen_frames(CROPS['sitting_side'], love=True)*3
# gen_gif('love')

# for action in CROPS:
#     gen_gif(action)

# CROPS['sitting_side'][0].show()
# img = gen_frames(CROPS['sitting_side'][0], bg_col='cyan').show()



