import os

from PIL import Image, ImageDraw, ImageFont


def draw_signature(folder_name):
    dir_path = os.path.join(os.getcwd(), 'source-images')
    if not output_folder_name:
        output_images_dir = os.path.join(os.getcwd(), 'output-images')
    else:
        output_images_dir = os.path.join(os.getcwd(), folder_name)

    os.makedirs(output_images_dir, exist_ok=True)

    for filename in os.listdir(dir_path):
        if filename.endswith('.jpg'):
            message = filename.split('.')[0].replace('-', ' ')
            message = f'@{message}'
            color = 'rgb(255, 255, 255)'
            font = ImageFont.truetype('Roboto-Bold.ttf', size=22)

            image = Image.open(os.path.join(dir_path, filename))
            image_w, image_h = image.size

            draw = ImageDraw.Draw(image)
            w, h = draw.textsize(message, font=font)

            draw.text(
                (image_w - w - 10, image_h - h - 10),
                message,
                fill=color,
                font=font
            )

            image.save(
                os.path.join(output_images_dir, filename),
                'JPEG'
            )


if __name__ == '__main__':
    output_folder_name = input()
    draw_signature(output_folder_name)
