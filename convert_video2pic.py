import os
# import cv2
# from PIL import Image

import argparse
import imageio
# import progress

from progress.bar import Bar

def extract_video(video_path, output_dir):
    if os.path.isfile(video_path) == False:
        print('Video {} not exists!'.format(video_path))

    videoReader = imageio.get_reader(video_path, 'ffmpeg')
    frameNum = videoReader.count_frames()

    print('Frame num = ', frameNum)

    bar = Bar('Processing', max=frameNum)

    if os.path.isdir(output_dir) == False:
        os.makedirs(output_dir)

    for num, image in enumerate(videoReader):
        image = videoReader.get_data(num)

        img_path = '{}/frame_{}.jpg'.format(output_dir, num)

        imageio.imwrite(img_path, image)

        bar.next()

    bar.finish()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert video to frame images.')
    parser.add_argument('--video_path', default='default.mp4', help='Input video path')
    parser.add_argument('--output_dir', default='default_frame', help='Output dir for frame images')

    args = parser.parse_args()

    video_path = args.video_path
    output_dir = args.output_dir

    print('video_path = {}'.format(video_path))
    print('output_dir = {}'.format(output_dir))

    extract_video(video_path, output_dir)  # Video to frames