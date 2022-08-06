# HTML(Hyper Text Markup Language)

- 웹 페이지를 작성, 구조화하기 위한 언어
- 태그로 만든 구조로 문서를 만들어서 브라우저로 실행

## Hyper Text란?

- 팀 버너스리가 기획한 이론
- 이 문서에서 저 문서로 한 번에 접근할 수 있는 기능…

## Markup Language

- 태그를 이용하여 문서나 데이터의 구조를 명시하는 언어
- 대표적인 예 : HTML, Mardown
- `<head>` `</head>`
- 태그를 이용하여 내가 원하는 구조를 만들 수 있다

## HTML 스타일 가이드

- `2 space` (파이썬은 4 space)
- indent 없어도 문제를 없지만 해야 가독성이 좋음

## HTML 기본 구조

- `html` : 문서의 최상위(root)요소
    - `head`  문서 메타데이터 요소
        - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
        - 실제 데이터 내용(body)을 위한 메타데이터
        - 일반적으로 브라우저에 나타나지 않는 내용
        - 사진을 위한 메타데이터 : 찍은 곳, 시간, 해상도 등의 내용이 있는 곳
    - `body`
        - 실제 화면에 나타나는 문서

### head 예시

- `title` : 브라우저 상단 타이틀
- `meta` : 문서 레벨 메타데이터 요소
- `link` : 외부 리소스 연결
- `script` : 스크립트 요소(`Javascript`)
- `style` : CSS 직접 작성

```html
<head>
	<title></title>
</head>
```

- Open Graph Protocol (OG)
    - 링크의 썸네일을 결정하는 meta 태그
    - 메타 데이터를 표현하는 새로운 규약
    - 문서의 정보, 정보에 해당하는 제목, 설명 쓸 수 있도록 정의
    

## 요소 (element)

- 태그와 내용(contents)로 구성되어 있다
- `<h1>`(여는 태그) / `</h1>` (종료 태그)
- 태그들이 내용을 감싸는 것으로 그 정보의 성격과 의미 정의
- 내용이 없는 태그도 존재(닫는 태그가 없음) : `br` `hr` `img` `input` `link` `meta`
- 요소는 중첩될 수 있음
- 태그 쌍을 잘 확인해야 함, 오류를 반환하는 게 아니라 레이아웃이 깨진 상태로 출력

## 속성

- 태그의 디테일한 정보 전달
- <a `href(속성명)` = `"https://google.com"(속성값)`></a>
- 태그의 부가적 정보 설정
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 특정 태그에 따라 사용할 수 있는 속성이 다르지만
- 태그와 상관없이 사용 가능한 속성(HTML Grobal Attribute)도 존재

### HTML Global Attribute

- `id` : 문서 전체에서 유일한 고유 식별자 지정
- `class` : 여러 요소에 원하는 속성을 지정하고 싶을 때
- `data-*` : 데이터 주고받을 때, 좋아요 기능 만들때 사용
- `style` : 꾸미기
- `tabindex` : 웹 페이지에서 탭을 누를 때 각각 선택되는 순서를 결정하는 거

### HTML 코드 예시

```html
<!DOCTYPE html>
<html lang= "en">
<head>
	<meta charset="UTF-8">
	<title>Hello, HTML</title>

</head>
<body>
	<!--이것은 주석입니다.-->
	<h1>나의 첫번째 HTML</h1>
	<p>이것은 본문입니다.</p>
	<span>이것은 인라인요소</span>
	<a href="https://www.google.com">네이버로 이동!!</a>
</body>
</html>
```

## 시맨틱 태그

- 의미를 가치를 가지는 태그
- `h1` 태그는 이 페이지에서 최상위 제목인 텍스트를 감싸는 역할
- Non semantic 요소로는 div, span이 있음
- `<header>`, `<nav>`, `<section>`, `<footer>`, `<article>`

- 검색엔진에서 정보의 그룹을 태그로 표현
- 검색엔진 최적화를 위해서 메타태그, 시맨틱 태그를 통한 마크업을 효과적으로 활용 해야

## 렌더링

- 웹 사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

## DOM(Document Object Medel) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링하기 위한 구조
- HTML 문서에 대한 모델 구성
- HTML 문서를 각 요소 별로 잘라서 각각 접근한 뒤 화면에 그려내는 것


![1200px-DOM-model svg](https://user-images.githubusercontent.com/97926368/182071541-a3a8142c-aa70-44bd-8f50-57e19af577a4.png)


