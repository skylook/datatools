import os
# import cv2
# from PIL import Image

import argparse
import imageio
# import progress

from progress.bar import Bar

def unlock_movie(movie_path, output_dir):
    if os.path.isfile(movie_path) == False:
        print('Movie {} not exists!'.format(movie_path))

    videoReader = imageio.get_reader(movie_path, 'ffmpeg')
    frameNum = videoReader.get_length()

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

    # while suc:
    #     frame_count += 1
    #     suc, frame = cap.read()
    #
    #     if suc == False:
    #         continue
    #
    #     params = []
    #     params.append(2)  # params.append(1)
    #
    #     img_path = '{}/frame_{}.jpg'.format(output_dir, frame_count)
    #
    #     cv2.imwrite(img_path, frame, params)
    #
    #     print('img_path = %s' % img_path)
    #
    # cap.release()
    # print('unlock movie: ', frame_count)


# def jpg_to_video(path, fps):
#     """ 将图片合成视频. path: 视频路径，fps: 帧率 """
#     fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#     images = os.listdir('frames')#os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
#     image = Image.open('frames/' + images[0])
#     vw = cv2.VideoWriter(path, fourcc, fps, image.size)
#
#     os.chdir('frames')
#     for i in range(len(images)):
#         # Image.open(str(image)+'.jpg').convert("RGB").save(str(image)+'.jpg')
#         jpgfile = str(i + 1) + '.jpg'
#     try:
#         new_frame = cv2.imread(jpgfile)
#         vw.write(new_frame)
#     except Exception as exc:
#         print(jpgfile, exc)
#     vw.release()
#     print(path, 'Synthetic success!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert movie to frame images.')
    parser.add_argument('--movie_path', default='default.mp4', help='Input movie path')
    parser.add_argument('--output_dir', default='default_frame', help='Output dir for frame images')

    args = parser.parse_args()

    movie_path = args.movie_path
    output_dir = args.output_dir

    print('movie_path = {}'.format(movie_path))
    print('output_dir = {}'.format(output_dir))

    # PATH_TO_MOVIES = os.path.join(movie_path)
    # PATH_TO_OUTCOME = os.path.join('detection_movies', 'beautiful_mind2_detection_1.avi')
    unlock_movie(movie_path, output_dir)  # 视频转图片
    # jpg_to_video(PATH_TO_OUTCOME, 24)  # 图片转视频