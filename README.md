# MiniProject_web
장고를 이용한 웹사이트 생성 미니프로젝트

## 목적 :
해수욕장에서 이안류로 인한 인명사고 발생 빈도가 높아짐에 따라 해수욕장 방문 전 각 해수욕장의 이안류 지수를 사용자가 파악할 수 있도록 정보를 제공

## 사용데이터
해양수산부에서 제공하는 이안류 정보를 사용하기 위하여 바다누리 해양정보 서비스에 가입해 OPEN API를 발급받고, 이안류 정보를 JSON형태로 제공받음.

## 데이터수집방법
이안류 관측소가 있는 해수욕장은 전국에 각 10개로 (경포,고래불,낙산,대천,망상,속초,송정,임랑,중문,해운대)
파이썬을 이용해 크롤링
 - 관측은 5분에 한번씩 하지만 가장 최근 데이터가 중요했으므로 30분에 한번씩 자동으로 크롤링하게 설정
  - 윈도우에 탑재된 작업스케줄러를 이용하여 자동크롤링

## 데이터저장
크롤링하면서 동시에 DB에 저장하도록 설정

## 웹페이지
  - free templates 사용
   -(https://templatemo.com/tm-554-ocean-vibes)
  - home버튼은 Bootstrap에서 사용
   -(https://www.w3schools.com/bootstrap5/bootstrap_buttons.php)
 
## Preview
![image](https://user-images.githubusercontent.com/108312161/197706444-7c07b0e1-e97b-45f2-86f3-16349f148685.png)
![image](https://user-images.githubusercontent.com/108312161/197706513-0c53df1f-027d-4a14-a7e9-80a4b628d68c.png)
![image](https://user-images.githubusercontent.com/108312161/197706594-b4a550d2-c12f-4ada-9e03-fc11cb7fcc53.png)

 
### Stacks
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

   
### Tools
![Git](https://img.shields.io/badge/Git-F05032.svg?&style=for-the-badge&logo=Git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?&style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
 

