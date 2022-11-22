## 1117-0250: Front update했습니다.  

---

## 1118-1130: Back update & organize code
- 게시글 & 해시태그 모델링(정상 입력확인)  
- 게시글 조회 정상작동  
- 게시글 상세조회 및 삭제 정상작동(수정기능은 검토필요, 태그기능 때문에 간단하지않음)  
- 영화 목록 조회 정상작동
- 영화 정보 상세 조회 정상작동
- 영화 장르별 영화목록 조회기능 정상작동
- 회원가입 기능 정상작동
- 로그인 기능 정상작동
  
기능별 요청위치(axios url주소 입력시 참고)  
`http://127.0.0.1:8000/` - 기본주소  
- api/v1/ - SNS  
  - `community/` , GET - 커뮤니티 글 목록 조회  
  - `community/` , POST - 커뮤니티 글 게시 
  - `community/{pk}` , GET - 글 상세조회 (pk는 게시글 id값)
  - `community/{pk}` , DELETE - 커뮤니티 글 삭제 (pk는 게시글 id값)
- api/v2/ - movie
  - `movies/` , GET - 영화정보 목록 조회 
  - `movies/<int:movie_id>/` , GET - 영화정보 상세 조회 (영화 id값)
  - `genre/<int:genre_id>/` , GET - 해당 장르 영화목록 조회 (장르 id값)       
- account - account
  - `accounts/login/` , POST - 로그인
  - `accounts/signup/` , POST - 회원가입     
    
  
모델별 데이터값(데이터 요청 및 사용시 참고)  
\<community post,get\>  
title : 100자 제한(not null)  
content : 제한없음(not null)   
tags : #으로 구분됨(blank true)  
유저토큰헤더 =  
`headers: {Authorization: Token {usertoken}}` 
  
\<movie (한글 제공)\>  
title = 제목  
overview = 줄거리(빈값일수도있음)  
poster_path = 포스터 url. `https://image.tmdb.org/t/p/{w500 or original}/{poster_path}` 형태로 사용  
vote_average = 평점(소수점)  
release_data = 개봉일자  

---

## 1118-1820: Back update & Front(movie) update  
  
\<back\>  
- SNS POST data 수신 오류 해결  
  
\<front\>  
- movie 추천목록 axios get & 출력  
- movie 추천목록 슬라이드 템플릿 구성  
- 추천영화 클릭시 detail 페이지 이동  
- movie detail axios get & 출력  
- sns POST 메서드 수정  

---  
## 1119-1647: Front(account) update  
  
\<front\>  

- login, signup 페이지, router, store 함수 작성    
- account, article axios 에러 발생 중   (도와주세요.)   

---

## 1119-2147: Front update  
  - login, signup 완료  
  - logout 구현 완료  

---

## 1120-0055: Back & Front(movie) update

\<back\>

- SNS 태그 id -> 이름 데이터 전송
- 게시글 수정 / 삭제 기능 구현
- 태그 검색 기능 구현(postman에서 구현 성공)
- 영화 검색 기능 구현(front쪽에서도 확인)
- 영화 데이터 추가(기존 약 400개 -> 10000개)  
- flow 및 데이터 출력위치 조정  

\<front\>  

- 영화 검색 기능 구현(실사용 가능)  
- 영화 상세 정보 페이지 모델 수정(개봉일자 추가)  

---

## 1120-1712: Front update  
  - community User ID 출력 완료  
  - community 검색창 출력 완료  
  - ProfileView 작성 중  
    - UserProfile component 연결 완료  
    - UserArticle component 틀 작성, 연결 완료  

---

## 1120-2030: Back & Front(movie) update

\<back\>

- popular 영화 추천 변경
- 영화 데이터 모델링 변경으로 인해 데이터 재추출 및 가공
- 랜덤으로 3개 장르 추천하는 영화추천 구현 및 프론트 연동 완료
- 장르 추천시, 인기도/평점 기반으로 앞에서 20개 가량 추출
- 영화에서 장르 id가 아닌 영화장르 값을 사용할수있도록 전송 데이터 가공
- 프론트에서 요청시 유저 정보 & 유저 작성 sns글 볼 수 있도록 기능 구현

\<front\>

- 랜덤 장르 영화 3개 화면에 구성
- 영화 상세 정보에서 영화 장르를 한글명으로 출력
- 영화 추천 슬라이드 초안 제작
- 영화 검색시 출력 초안 제작

기능별 요청위치 추가(axios url주소 입력시 참고)    


`http://127.0.0.1:8000/` - 기본주소
- api/v1/ - SNS 
  - `community/<int:community_pk>/` , PUT - 글 수정 (pk는 게시글 id값/요청 형태는 GET과 유사)
  - `community/tag/<str:tag_str>/` , GET - 해당 태그 검색 결과 요청

- api/v3/ - profile  
  - `profile/<str:username>/` , GET - 유저 정보 요청
  - `community/post/<str:username>/` , GET - 유저가 작성한 sns 글 목록 요청

## 1122-1708: front update
  - 커뮤니티, 프로필 게시물 edit, detail 모달창 구현
  - 게시글 생성 모달창으로 구현 예정
  - 개인 프로필 컴포넌트 생성 예정
  - 태그 검색창 구현 예정