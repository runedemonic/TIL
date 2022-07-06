# Git

## 동작흐름

Git은 파일을 modified, staged, committed로 관리 



- modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
- staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소) 
- committed : 커밋이 된 상태

![설명](https://git-scm.com/book/en/v2/images/areas.png)

## 기본 명령어

### $ git log

+ 현재 저장소에 기록된 커밋을 조회 
+  다양한 옵션을 통해 로그를 조회할 수 있음
+ $ git log -1 
+ $ git log --oneline 
+ $ git log -2 --oneline



### $ git status

+ Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

+ 파일의 상태를 알 수 있음

  + Untracked files 
    + Git이 관리하지 않는 상태

  + Changes not staged for commit 
    + 수정된 파일이 Staged상태가 아니라 commit 할 수 없음 
    + $git add로 Staged 상태로 만들면 해결
  + Changes to be committed
    + 수정된 파일이 commit 되어 히스토리에 남음

  

### $ git add

+ 특정 파일/폴더의 변경사항 추가
+ 파일을 staged 상태로 만듬



## 원격 저장소

1. GitHub에 Repository를 생성 후 
2. Repository .git주소 확인
3. $ git remote add origin <.git주소>로 정보를 로컬 저장소에 추가





### $ git remote -v

+ 원격 저장소의 정보를 확인함



### $ git push

+ $ git push <원격저장소이름> <브랜치이름>
+ 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
+ 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감



### $ git pull

+ $ git pull <원격저장소이름> <브랜치이름>
+ 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함



### $ git clone

+ $ git clone <원격저장소주소>
+ 원격 저장소를 복제하여 모든 버전을 가져옴
+ 원격 저장소 이름의 폴더로 이동해서 활용함



|             명령어             |                   내용                    |
| :----------------------------: | :---------------------------------------: |
|           git clone            |             원격 저장소 복제              |
|         git remote –v          |           원격저장소 정보 확인            |
|  git remote add <원격저장소>   | 원격저장소 추가 <br />(일반적으로 origin) |
|   git remote rm <원격저장소>   |              원격저장소 삭제              |
| git push <원격저장소> <브랜치> |             원격저장소에 push             |
| git pull <원격저장소> <브랜치> |           원격저장소로부터 pull           |







## .gitigonore

+ 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생한다.

+ Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.

+ 작성 예시

  + 특정 파일 : a.txt (모든 a.txt), test/a.txt (테스트 폴더의 a.txt)

  + 특정 디렉토리 : /my_secret

  + 특정 확장자 : *.exe

  + 예외 처리 : !b.exe

    

  #### 주의! 이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용됩니다.

## 참조

+ [Git - Reference (git-scm.com)](https://git-scm.com/docs)

+ [Git - 수정하고 저장소에 저장하기 (git-scm.com)](https://git-scm.com/book/ko/v2/Git의-기초-수정하고-저장소에-저장하기)

