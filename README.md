# 구글독스 댓글 파서

## 사용법

1. 리포지토리를 다운받거나 `clone`한다.
2. 리포지토리 폴더 바로 아래에 작성자 이름으로 폴더를 만든다. e.g. `./철수`, `./영희`
3. 각 폴더 안에 각 작성자가 작성한 구글독스를 `.txt` 형식으로 export한 파일을 넣는다. 단, 파일 이름에는 참가자 넘버가 `P[0-9]+`형식으로 포함되어있어야만 한다. e.g.`P10의 응답.txt`
4. 파이썬 스크립트 실행(`python google-docs-csv-parser.py`)
5. `작성자 이름.csv`로 파싱된 파일이 생성된다.

