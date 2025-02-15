# программа для сохранения длительностей видео

def main():
    num_videos = int(input("How many videos? "))
    videos = r'files/videos.txt'

    video_file = open(videos, 'w')

    print('Enter lenth of video:')
    for count in range(1, num_videos+1):
        run_time = float(input("Enter run time: "))
        video_file.write(str(run_time) + "\n")

    video_file.close()
    print('Video file saved successfully!')

if __name__ == '__main__':
    main()