# HTML 문서 구조화

## 인라인 / 블록 요소

- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용

## 텍스트 요소

- `<a></a>` : 하이퍼링크
- `<b><strong>` : 글씨 강조
- `<i></i>, <em></em>` : 이탤릭체
- `<br>` : 줄바꿈
- `<img>` : 이미지
- `<span></span>` : 의미 없는 인라인 컨테이너 *ex. 투명한 쇼핑백…*

## 그룹 컨텐츠

- `<p></p>` 하나의 문단
- `<hr>` 수평선
- `<ol></ol> <ul></ul>` : 순서 있는 리스트, 없는 리스트
- `<pre>` : HTML 작성 내용 그대로 표현
- `<blockquote>` : 텍스트가 긴 인용문
- `<div></div>` : 작업을 위한 의미 없는 블록 컨테이너

## form

- 사용자가 브라우저를 통해서 서버에 데이터를 전송하고 싶을 때 사용하는 태그
- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- *로그인 창의 ID와 PW / 게시판의 게시글 작성 버튼 누를 때 form 이용해서 서버에 전송*
    - `action` : 데이터를 보낼 곳(*naver or google)*
    - `method` : 데이터를 전송하기 위한 방식 (`GET` 방식 또는 `POST` 방식)
    - `enctype` : POST인 경우 데이터 유형 : 파일 전송시 따로 설정을 해주어야 한다는..
- form 을 통해서 구글에 데이터를 요청하고 어쩌구…

## input

- form은 데이터 보내는 종이, input은 직접적으로 데이터를 넣기 위한 태그
- `name` : 적용되는 이름
- `value` : 적용되는 값
- `required`, `readonly`, `autofocus, autocomplete, disabled...`

```html
<form action="/search">
	<input type="text" name="q">
</form>
```

## input 유형

### input - label

- input 태그에 대한 상세한 설명, 내용을 넣기 위해서 사용
- input 에 `id` 속성을, label에 `for` 속성을 활성화시켜 상호 연관

```html
<label for = "agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement"> 
```

## VSCODE 실습코드

### 일반

- `text` 텍스트 입력
- `password` : 입력시 값이 보이지 않고 특수기호(*)로 표현
- `email` : 이메일 형식 아닌 경우 form 제출 불가
- `number` : 숫자 범위 설정 가능
- `file`: `accept` 속성으로 파일 속성 지정 가능

### 항목 중 선택

- `checkbox` :다중 선택
- `radio` : 단일 선택

### 기타

- `color` : 색상 고르게하기
- `date` : 날짜 고르게 하기
- `hidden` : 사용자에게 보이지 않는 input 필요할 때

### 마크업 실습

- `img` `alt` : 이미지 깨졌을 때 설명해주는 글
- `<a>` 태그 안에는 글자 뿐 아니라 이미지도 들어갈 수 있음
- `<section>` : 본문
    - 제출이 목적이기 때문에 마지막에 제출 버튼을 만들고나서 내용 만들기
    - <input type = “submit” value = “제출”> ⇒ `제출`
    
    ```html
    <div>
    	<label for="name">이름을 기재해주세요.</label><br>
    	<input type="text" id="name">
    </div>
    
    <div>
    	<select name="region" id="region" required> <!--필수 요소-->
    </div>
    
    <div>
    	<input type ="radio" name="body-heat" id="normal" chcekced> <!--기본 선택-->
    </div>
    ```
    
- `<footer>` : 마지막 부분이라는 의미