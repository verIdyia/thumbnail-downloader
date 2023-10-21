# 유튜브 썸네일 다운로더

## 설명

이 파이썬 스크립트는 지정된 유튜브 채널의 모든 비디오 썸네일을 유튜브 API를 사용하여 가장 높은 해상도로 다운로드합니다. 

기본 세팅이 [헤징](https://www.youtube.com/@hejin0_0) 유튜브 채널로 되어 있습니다.

## 기능

- 유튜브 채널의 모든 비디오 썸네일 다운로드
- 비디오 제목을 적절한 파일 이름으로 변환
- 가장 높은 사용 가능한 해상도 다운로드

## 설치 방법

### 의존성
- `google-api-python-client`
- `requests`

이 패키지들은 pip를 사용하여 설치할 수 있습니다:
```bash
pip install -r requirements.txt
```

### API 키
이 스크립트를 사용하려면 유튜브 데이터 API v3 키가 필요합니다. [여기서](https://cloud.google.com/apis) 생성할 수 있습니다.

## 사용 방법

1. 이 저장소를 클론합니다. zip으로 다운로드 하고 압축 해체 하셔도 됩니다.
```bash
git clone https://github.com/verIdyia/thumbnail-downloader.git
```
2. `api_key` 변수에 API 키를 입력합니다.
3. `channel_id` 변수에 썸네일을 다운로드하려는 채널 ID를 입력합니다. 채널 정보 페이지에서 공유 버튼을 클릭하면 확인하실 수 있어요.
4. 스크립트를 실행합니다.
```bash
python index.py
```
5. 화면에 표시되는 지시사항을 따라 썸네일을 다운로드합니다.

## 기여

수정하거나 개선할 부분이 있다면 프로젝트를 포크하고 변경 사항을 풀 리퀘스트로 제출하실 수 있습니다!
