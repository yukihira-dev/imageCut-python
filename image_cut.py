import glob
from args import args
from PIL import Image as I


input_image_path = './input/'
output_image_path = './output/'


def error_check(images_name_list):
    if len(images_name_list) == 0:
        raise print('Image is not found')

    if args.right_lower_x < args.left_top_x or args.right_lower_y < args.left_top_y:
        raise print('Coordinate setting is incorrect')

    test_image = I.open(images_name_list[0])
    width = test_image.width
    height = test_image.height
    if width < args.right_lower_x or height < args.right_lower_y:
        print("Image's width is " + str(width))
        print("Image's height is " + str(height))
        raise print('Coordinate setting is larger than input image')

    if args.right_lower_x == 0 or args.right_lower_y == 0:
        raise print('Please set the coordinates')


def image_name_list_make():
    images_name_list = sorted(glob.glob(input_image_path + '*'))
    return images_name_list


def cut_image(images_name_list):
    if args.test:
        image = I.open(images_name_list[0])
        image = image.crop((args.left_top_x, args.left_top_y, args.right_lower_x, args.right_lower_y))
        image.save(output_image_path + 'test' + '.png', quality=95)
    else:
        for index, image_name in enumerate(images_name_list):
            image = I.open(image_name)
            image = image.crop((args.left_top_x, args.left_top_y, args.right_lower_x, args.right_lower_y))
            image.save(output_image_path + str(index) + '.png', quality=95)


if __name__ == '__main__':
    images_name_list = image_name_list_make()
    error_check(images_name_list)
    cut_image(images_name_list)
    print('finish');
