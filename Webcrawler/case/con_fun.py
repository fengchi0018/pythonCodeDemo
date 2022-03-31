''''
@File  : con_fun.py
@Author: Feng
@Date  : 2022/3/30
@Desc  : 
'''

"""
音频视频合并
import subprocess
cmd = f"ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4"
subprocess.run(cmd, shell=True)
"""

"""
鼠标下滑
def drop_down():
    for x in range(1, 8, 2):  # 1.3.5.7.9在不断下拉过程中，页面高度也会变
        time.sleep(1)
        j = x / 9  # 1/9  3/9 9/9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
"""

