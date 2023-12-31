# YouTube 썸네일 다운로더 🎬

## 설명
YouTube 채널의 모든 비디오 썸네일을 자동으로 다운로드해 주는 스크립트입니다.

## 시작하기 전에 🛠
1. Python 설치해 주시고 터미널에서 바로 사용할 수 있도록 환경변수 설정해주세요!
2. YouTube API 키가 필요합니다. [여기](https://cloud.google.com/apis?hl=ko)에서 API 키를 발급받을 수 있습니다.

## 설치 방법 📥
1. 이 레포지토리를 [ZIP 파일로 다운로드](https://github.com/verIdyia/thumbnail-downloader/archive/refs/heads/main.zip)합니다.
    - 또는 `git clone`을 사용하여 클론할 수 있습니다.
    ```
    git clone https://github.com/verIdyia/thumbnail-downloader.git
    ```
2. 다운로드한 폴더 안에서 터미널을 열고 가상환경을 설정합니다.
    ```
    python -m venv venv
    ```
3. 가상환경을 활성화합니다.
    - 윈도우
      ```
      venv\Scripts\activate
      ```
    - 맥과 리눅스
      ```
      source venv/bin/activate
      ```
4. 필요한 패키지를 설치합니다.
    ```
    pip install -r requirements.txt
    ```
5. 프로그램을 실행합니다.
    ```
    python index.py
    ```

## 사용 방법 🎮
1. 실행하면 창이 나타납니다.
2. YouTube 채널ID와 YouTube API 키를 입력합니다. 채널ID는 기본적으로 [헤징 유튜브 채널](https://www.youtube.com/@hejin0_0)으로 설정되어 있습니다.
3. "Download Thumbnails" 버튼을 클릭하여 썸네일 다운로드를 시작합니다.

## 주의 사항 ⚠️
- YouTube API 키를 잘못 입력하면 프로그램이 작동하지 않을 수 있습니다.
- 대량의 썸네일을 다운로드할 경우, YouTube의 제한에 걸릴 수 있으니 주의하세요. (하루 한도가 10000개 정도 되는 거 같아요.)

## 라이선스 📝
이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 `LICENSE` 파일을 참조해 주세요.
