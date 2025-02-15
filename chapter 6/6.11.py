# программа для чтения длительностей видео

def main():
    video = r'files/videos.txt'
    video_file = open(video, 'r')

    total = 0
    count = 0

    for line in video_file:
        run_time = float(line)
        count += 1
        print(f"video {count}: {run_time} seconds")
        total += run_time

    video_file.close()
    print(f"total video {total} seconds")

if __name__ == '__main__':
    main()
