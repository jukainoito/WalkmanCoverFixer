## 说明
该程序目前主要用于修复walkman中音频的封面无法正常显示

原理: 封面无法显示一般是的文件头不规范，可能walkman对文件头的容错很低。该程序将封面文件取出重新生成文件头后存入。

当前暂不支持多张封面图片，会删除第一张以外的图片，请注意

当前支持格式
* mp3
* flac


## 使用
```bash
python main.py files [files ...]
```
