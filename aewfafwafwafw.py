import subprocess

def convert_video(input_path, output_path):
    command = ['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-crf', '23', '-preset', 'medium', '-c:a', 'copy', output_path]
    subprocess.run(command)

# Specify the input video path
input_path = r'D:\_Lab Awards\_FINAL\Čapek_profipoint_2.mp4'

# Specify the output video path
output_path = r'D:\_Lab Awards\_FINAL\Čapek_profipoint_2_MAIN.mp4'

# Call the convert_video function with the input and output paths
convert_video(input_path, output_path)
