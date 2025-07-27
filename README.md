<h1 align = 'center'>
    <img 
        src = '/assets/icon.png'
        height = '200' 
        width = '200' 
        alt = 'Icon' 
    />
    <br>
    TSFusion
    <br>
</h1>

<div align = 'center'>
    <a href = 'https://github.com/jedrzejme/TSFusion/'>
        <img src = 'https://img.shields.io/github/stars/jedrzejme/TSFusion?style=for-the-badge&color=%23cfb002'/>
    </a>
    <a href = 'https://github.com/jedrzejme/TSFusion/tags'>
        <img src = 'https://img.shields.io/github/v/tag/jedrzejme/TSFusion?style=for-the-badge&label=version'/>
    </a>
    <a href = 'https://github.com/jedrzejme/TSFusion/issues'>
        <img src = 'https://img.shields.io/github/issues/jedrzejme/TSFusion?style=for-the-badge&color=%23ff6f00'/>
    </a>
    <a href = 'https://github.com/jedrzejme/TSFusion/pulls'>
        <img src = 'https://img.shields.io/github/issues-pr/jedrzejme/TSFusion?style=for-the-badge'/>
    </a>
</div>

<br>

> [!IMPORTANT]
> Currently TSFusion works with URLs that have *seg-{number}* in them

**❓ What is this?** TSFusion is a lightweight and efficient tool designed to simplify the process of downloading and merging .ts (MPEG Transport Stream) video segments into a single .mp4 file. Whether you're working with HLS streams or segmented video sources, TSFusion automates the entire workflow — from fetching .ts files to generating a smooth, playable .mp4.

**❓ How to use it?**
* [**Using Python**](#using-python-to-run-tsfusion)
* [**Using .exe**](#using-exe-to-run-tsfusion)

**❓ What did I use?**
* [Python](https://www.python.org/)
* [Python libraries](/requirements.txt)
* [Coding](https://code.visualstudio.com/)
* [Git management](https://desktop.github.com/)

## 🐍 Using Python to run TSFusion
1) Install ffmpeg:
   - Windows: ```winget install --id=Gyan.FFmpeg  -e```
   - Linux: ```sudo apt install ffmpeg```
   - MacOS: ```brew install ffmpeg```
2) Install Python
3) Clone this repository and enter its directory:
```
git clone https://github.com/jedrzejme/TSFusion.git
```
4) Install requirements.txt:
```
python -m pip install -r requirements.txt
```
5) Run main.py:
```
python main.py
```
6) Paste your URL
7) Type in the name of directory
8) Press Enter
9) It works!

## 💾 Using .exe to run TSFusion
1) Go to [releases](https://github.com/jedrzejme/TSFusion/releases)
2) Download latest version
3) Install ffmpeg from cmd: ```winget install --id=Gyan.FFmpeg  -e```
4) Run TSFusion.exe
5) Paste your URL
6) Type in the name of directory
7) Press Enter
8) It works!

## 🚀 Features
* 📥 Download .ts video segments from a given playlist or URL
* 🔗 Automatically merge segments into a single .mp4 file
* ⚡ Fast, clean, and easy-to-use
* 💡 Ideal for video stream archiving or offline playback

## 💲 Support
<p><a href="https://support.jedrzej.me/" target="_blank"> <img align="left" src="https://raw.githubusercontent.com/jedrzejme/jedrzejme/main/assets/supportme.svg" height="50" width="210" alt="jedrzejme" /></a></p>