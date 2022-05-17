from moviepy.editor import AudioFileClip

def video2wav(file_path: str, fps=16000, *args, **kwargs):
    '''默认16bit编码 16000采样率'''
    output_path = file_path.rsplit('.', maxsplit=1)[0] + '.wav'
    AudioFileClip(file_path).write_audiofile(output_path, fps=fps)

def read_audio(file_path, *args, **kwargs):
    return AudioFileClip(file_path, *args, **kwargs)
