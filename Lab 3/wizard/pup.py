from PIL import Image, ImageDraw

SPRITES = Image.open('imgs/dog.png').convert('RGB')
SPRITE_HEIGHT = 96
SPRITE_WIDTH = 96

def get_sprite(row,col):
    # col in [0,3], row in [0,8]
    return SPRITES.crop((col*96, row*96, (col+1)*96, (row+1)*96))

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

def gen_gifs():
    '''
    Generates gif for each action
    :return:
    '''
    for action in CROPS:
        print(action)
        frames = CROPS[action]
        # snippet from https://blog.zhaytam.com/2018/08/21/creating-gifs-using-python-pillow/
        frames[0].save('imgs/doggy_%s.gif'%(action),
                       format='GIF', append_images=frames[1:], save_all=True,
                       duration=100,
                       loop=0,
                       transparency=255,
                       disposal=2)
