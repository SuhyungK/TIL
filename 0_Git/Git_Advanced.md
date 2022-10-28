## Git undoing(깃 작업 되돌리기)
### `Working Directory` 작업 단계
- 수정한 파일 내용을 이전 커밋 상태로 되돌리기
- `git restore`

### git restore
- `Working Directory`에서 수정한 파일 수정 전(직전 커밋)으로 되돌리기
- 커밋한 다음에 수정했을 때 수정 전 상태로 되돌리는 것 
- 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
- 수정했던 파일 자체를 없애버리는 것(해당 내용 복원 불가)
- `git restore {파일 이름}`

- `git add.`
- `git commit -m '메세지'`
- `vi {파일명}` : 수정 상태로 진입
- `[ESC]` -> `:wq` : INSERT 상태 종료
- `git log --oneline` : log 출력
- `git restore {파일명}` : 수정된 거 삭제


### Staging Area 작업 단계 되돌리기
- root-commit 이 없는 경우 : `git rm --cached`
- root-commit 이 ?
  - `git restore --staged a.txt`
  

### Repository 작업 단계 되돌리기~
- `git commit -amend`
  - 커밋 완료한 파일 `Staging Area`로 되돌리기
  - `Staging Area`에 아무것도 없다면 그냥 `git commit --amend`
  - `Staging Area`에 뭐가 있다면
  
## git reset
- `--soft`
  - 해당 커밋으로 되돌아각
  - 되돌아간 커밋 이후의 파일들은 Staging Area

## Git Branch
1. 브랜치는 독립공간을 형성하기 때문에 원본에 대해 안전
2. 하나의 작업은 하나의 브랜치로 나누어 관리 -> 체계적 개발 가능
3. Git은 브랜치 만드는 속도가 굉장히 빠르고, 적은 용량 소모

### git branch
- 조회
  - `git branch` : 로컬 저장소 브랜치 목록 확인
  - `git branch -r` : 원격 저장소 브랜치 목록 확인
- 생성
  - `git branch {브랜치 이름}` : 새로운 브랜치 생성
  - `git branch {브랜치 이름} {커밋 iD}` : 커밋 기준으로 브랜치 생성

### git switch
- 현재 브랜치에서 다른 브랜치로 이동
  - `git switch - c 브랜치 이름` : 브랜치 새로 생성 및 이동
  - `git switch - c 브랜치 이름 커밋 ID` : 특정 커밋 기준