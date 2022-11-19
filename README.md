1117-0250: Front update했습니다.  

<hr>

1118-1130: Back update & organize code
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
<community post,get>  
title : 100자 제한(not null)  
content : 제한없음(not null)   
tags : #으로 구분됨(blank true)  
유저토큰헤더 =  
`headers: {Authorization: Token {usertoken}}` 
  
<movie (한글 제공)>  
title = 제목  
overview = 줄거리(빈값일수도있음)  
poster_path = 포스터 url. `https://image.tmdb.org/t/p/{w500 or original}/{poster_path}` 형태로 사용  
vote_average = 평점(소수점)  
release_data = 개봉일자  


<hr>

1118-1820: Back update & Front(movie) update

<back>
- SNS POST data 수신 오류 해결

<front>
- movie 추천목록 axios get & 출력
- movie 추천목록 슬라이드 템플릿 구성
- 추천영화 클릭시 detail 페이지 이동
- movie detail axios get & 출력
- sns POST 메서드 수정

1119-1647: Front(account) update

<front>
- login, signup 페이지, router, store 함수 작성
- account, article axios 에러 발생 중 (도와주세요.)