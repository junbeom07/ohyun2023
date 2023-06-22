# Ohyun2023
# 백엔드
## 1차시
https://dirt-record-7f9.notion.site/1-6-8-769827e2aa07401baa9f2db25efe096c?pvs=4

## 2차시
https://dirt-record-7f9.notion.site/2-6-13-f4dcbac7bfb146e39de5459ced310760?pvs=4

## 3차시
https://dirt-record-7f9.notion.site/3-6-15-858f775466e1435d82fee2251e4de16f?pvs=4

## 4차시
https://dirt-record-7f9.notion.site/4-6-20-6d12030474f2419e85e1d6cb3f223234?pvs=4

## 5차시
https://dirt-record-7f9.notion.site/5-6-22-d631e9d5a5d044b58245dcfd78fe94e8?pvs=4


## 기본 실행 방법

1. 가상환경 설치하고 들어가기
    - git을 clone하게 되면 env 파일이 없습니다. 설치해주세요
      ```bash
      python3 -m venv env
      ```
    - 가상환경 들어가기
      ```bash
      source env/bin/activate
      ```
2. django 설치하기
    - django 설치하기
      ```bash
      pip install django==3.2.14
      ```
3. 서버 실행하기
    - ls를 이용해서 현재 폴더 내에 `manage.py` 가 있는지 확인해주세요.
    - 터미널 맨 앞에 `(env)`가 있어야 실행이 가능합니다.
    - 데이터베이스 migrate해주기
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
    - admin 계정 만들기
      ```bash
      python manage.py createsuperuser

      사용자 이름(leave blank to use 'codespace') : admin
      이메일 주소 : admin@gmail.com
      Password : 
      Password (again) :
      ```

      - 비밀번호는 입력해도 아무런 값이 보이지 않습니다. 틀리지 않게 주의깊게 입력해주세요
      - 비밀번호 : abc123
      - 비밀번호를 입력하면 아래와 같은 경고가 뜹니다.
    
      ```bash
      비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
      비밀번호가 너무 일상적인 단어입니다.
      
      Bypass password validation and create user anyway? [y/N]:
      ```
    
      -  `y`를 누르고 엔터를 쳐서 승인을 해주세요
    

      `Superuser created successfully.` 가 떴으면 슈퍼유저가 제대로 생성된 것 입니다.

    - django 실행하기

      ```shell
      python manage.py runserver
      ```
    


----

# 프론트
## CSS

### 1. flex

<p align="center">
  <img src="https://github.com/min-bok/Ohyun2023/assets/81654172/686b16fd-845f-4a7b-bc6e-48ae13256515">
</p>

## JavaScript

- DOM 요소 조작하기