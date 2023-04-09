from pytube import YouTube


def on_progress(stream, total_size, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')


url = input('Past your Youtube Video Link :')
yt = YouTube(url)
# print(yt.streams)
print('The video name and size : ', yt.title, yt.streams.get_highest_resolution().filesize_mb, 'Mb')
yt = YouTube(url, on_progress_callback=on_progress)

out = yt.streams.get_highest_resolution().download()

print(" Download complete")
