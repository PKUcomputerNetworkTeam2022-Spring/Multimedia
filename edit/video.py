from moviepy.editor import *

def _example():
    # 导入视频
    origin = VideoFileClip("test.mp4")
    # 操作视频
    new_clip = (
        origin
        # .speedx(2)#倍速
        .subclip(0, 50)# 截取前50秒视频
        # 1.1.0 将源视频中指定范围子窗口内容输出到保存的视频文件。
        # .crop(0, 278, 540, 580)
    )
    # 保存
    new_clip.write_videofile("output.mp4")

    # 提取音频
    audio = origin.audio  # 单独提取音频
    origin_audio_clip = audio.volumex(0.8) # 提取视频音频，并调小音量
    # 背景音乐
    bgm_clip = AudioFileClip('bgm.wav')
    bgm_clip = afx.audio_loop(bgm_clip, duration=origin.duration).volumex(0.5)
    # 设背景音乐循环，时间与视频1时间一致
    # 视频声音和背景音乐，音频叠加
    audio_clip_add = CompositeAudioClip([origin_audio_clip, bgm_clip])

    # 读取视频、合并视频
    videoclip_2 = VideoFileClip("two.mp4") # 读取视频
    final_video = videoclip_2.set_audio(audio_clip_add)  # 音频+视频2合并
    final_video.write_videofile("video_result.mp4")  # 输出新视频
    concat_clip = concatenate_videoclips([final_video, new_clip])  # 合并视频
