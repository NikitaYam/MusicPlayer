from pydub.utils import mediainfo
import os
import ffmpeg

info = mediainfo('1.mp3')


print('Filename:', info['filename'])
print('Format:', info['format_name'])
print('Sample Rate:', info['sample_rate'])
print('File Size:', int(info['size']), "bytes")