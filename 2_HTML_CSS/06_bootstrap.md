# Bootstrap

> 반응형 웹 사이트를 부트스트랩과 함께 빠르게 만들 수 있게 해주는 것
> 

# 부트스트랩 기본 원리

## Spacing (Margin and Padding)

- `{property}{sides}-{size}`
- `property` : margin or padding
- `sides` : top, left, right, bottom
    - `s` : (start)maring-left, padding-left in LTR
    - `e` : (end)margin-right, padding-right
    - `x` : 좌우 / `y` : 상하
    - `blank` : 전 방향
- *mt-1 : 0.25rem = 4px (1rem = 16px)*
    - *m-2 : 0.5rem = 8px*
    - *m-3 : 1rem = 16px*
    - *m-4 : 1.5rem = 24px*
- *mx-0 : 좌우 margin 0*
- *mx-auto: 수평 중앙 정렬, 가로 가운데 정렬*
- *py-0 : 상하 padding 0*
- *ms-auto: 오른쪽 정렬*
- *me-auto : 왼쪽 정렬*

```html
<h2>Spacing</h2>
<div class="mt-3 ms-5 box"></div>
<div class="m-4 box">margin</div>
<div class="mx-auto box"></div>
<div class="me-auto box"></div>
```

## Colors

```html
<h2>Color</h2>
<div class="bg-primary">이건 파랑</div>
<div class="bg-secondary">이건 회색</div>
```

## Text

```html
<h2>Text</h2>
<p class="text-start">text-start</p>
<p class="text-center">text-center</p>
<p class="text-end">text-end</p>

<a href="#" class="text-decoration-none text-dark">Non-underline-Link</a>
<p class="fw-bold">Bold text</p>
<p class="fw-normal">Normal text</p>
<p class="fw-light">Light text</p>
```

- `a` : class 태그에 써야 함 / href 태그 X

## Position

```html
<div class="position-relative">
  <div class="position-absolute top-0 start-0"></div>
  <div class="position-absolute top-0 end-0"></div>
  <div class="position-absolute top-50 start-50"></div>
  <div class="position-absolute bottom-50 end-50"></div>
  <div class="position-absolute bottom-0 start-0"></div>
  <div class="position-absolute bottom-0 end-0"></div>
</div>
```

- `absolute` 쓰는 경우 부모가 `relative` 여야 함
- 아니면 윈도우 기준

```html
<h2>Position</h2>
  <div class="box fixed-top">fixed-top</div>
  <div class="box fixed-bottom">fixed-bottom</div>
```

```html
<div class="bigbox position-relative">
    <div class="box position-absolute top-0 start-0">top0/start0</div>
    <div class="box position-absolute top-0 end-0">top0/end0</div>
    <div class="box position-absolute bottom-0 start-0">bottom0/start0</div>
    <div class="box position-absolute bottom-0 end-0">bottom0/end0</div>
  </div>
```

- `.d-{breakpoint}-{value}` for `sm`, `md`, `lg`, `xl`, and `xxl`.

## Display

- `d-none` : display:none
- `d-inline`
- `d-block`
- `d-inline-block`

## Navbar

- 상단 혹은 사이드의 메뉴바

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

## Carousel

- 사진 순환을 위한 슬라이드쇼

## Modal

- 페이지를 이동하면 자동으로 사라짐
- 사용자와 상호작용 위해 긴급상황 알릴 때
- 시선 집중 시키고 다른 데 클릭하면 사라짐
- *넷플릭스에서 영화 눌렀을 때 가운데 뜨는 창*
- `button`의 `target`과 `id`가 연결됨
- 항상 body와 같은 top-level 포지션에 있어야 함

> *Modals use `position: fixed`, which can sometimes be a bit particular about its rendering. Whenever possible, place your modal HTML in a top-level position to avoid potential interference from other elements. You’ll likely run into issues when nesting a `.modal` within another fixed element.*
> 

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```

- `button` 의 `data-bs-target` = `modal` 의 `id`

## Card > Grid Card

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```

## Responsive Web

- 화면의 크기에 따라 사용자에게 보이는 페이지의 레이아웃이 달라지는 것
- 다양한 화면 크기를 가진 디바이스들에 맞춰서 나타남

# Bootstrap Grid System

## Grid System

- 요소들의 디자인과 배치에 도움 주는 시스템
    - `column` : 실제 컨텐츠 포함하는 부분
    - `gutter` : 칼럼과 칼럼 사이 공간
    - `container` : column 담고 있는 공간
- 12개의 column으로 이루어짐
- 6개의 grid breakpoints가 존재

## Breakpoints

- 화면의 크기에 따라 변경될 때 그 기준이 되는 각각의 분기점(point)
- 기본 : `.col` / `.col-{breakpoint}-`
- 구간마다 원하는 레이아웃 설정해서 변하게 할 수 있음

### Nesting

- Grid 시스템에서 컨텐츠끼리 중첩해서 배치, 정렬하는 것

![https://djangocms-cascade.readthedocs.io/en/latest/_images/nested-rows.png](https://djangocms-cascade.readthedocs.io/en/latest/_images/nested-rows.png)

```html
<div class="container text-center">
  <div class="row">
    <div class="col-sm-3">
      Level 1: .col-sm-3
    </div>
    <div class="col-sm-9">
      <div class="row">
        <div class="col-8 col-sm-6">
          Level 2: .col-8 .col-sm-6
        </div>
        <div class="col-4 col-sm-6">
          Level 2: .col-4 .col-sm-6
        </div>
      </div>
    </div>
  </div>
</div>h
```

### Offset

- 왼쪽에 여백 주기
- 여백을 주려는 컬럼에 offset 설정

![https://css3menu.com/web-design/data/upload/2017/04/offset-example.jpg](https://css3menu.com/web-design/data/upload/2017/04/offset-example.jpg)

```html
<div class="container text-center">
  <div class="row">
    <div class="col-md-4">.col-md-4</div>
    <div class="col-md-4 offset-md-4">.col-md-4 .offset-md-4</div>
  </div>
  <div class="row">
    <div class="col-md-3 offset-md-3">.col-md-3 .offset-md-3</div>
    <div class="col-md-3 offset-md-3">.col-md-3 .offset-md-3</div>
  </div>
  <div class="row">
    <div class="col-md-6 offset-md-3">.col-md-6 .offset-md-3</div>
  </div>
</div>
```