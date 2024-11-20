# etc
필요해서 만들다 나중에 또 쓸지도모르겠는것을 올려둡니다
### 배포하지마세요
#### 목록
1. success_mp4ToJpg.py
```
동영상의 첫프레임을 사진으로 저장하는 코드입니다
최상위 폴더를 경로로 적어놓으면 하위폴더에 있는동영상들을 싹 찾아서 저장합니다
mp4, avi, mkv, mov만 저장하도록하였습니다
ffmpeg가 설치되어있지않으면 정상작동 되지 않을 수 있습니다
```
https://ffmpeg.org/download.html 
```
에서 ffmpeg를 받으실수 있습니다
cmd 에서 ffmpeg -version 을 쳐보시면 설치되었나 확인가능하고
python OpenCV에서 활성화 되었는지 확인하려면
import cv2
print(cv2.getBuildInformation())

~~~~~~~~~~~~~
콘솔에 출력 내용 중 Video I/O 쪽에 FFMPEG : YES로 표기되어야 합니다
```

```
오류수정 1.
기존 cv2로 하던것이 정상작동하지 않기에
동영상을 보니 한글이름으로 작성된것들에서 제대로 되지않는것을 발견하였습니다
Pillow라이브러리를 사용하여 저장하도록 하여 한글도 정상적으로 저장됩니다

또 뭐 추가했던거같은데...뭐드라...
```

