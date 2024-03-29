# 최종 프로젝트

### 주제

  > Menu Driven으로 작동하는 연락처 관리 프로그램

---

### 목차

  1. [프로젝트 개요](https://github.com/firemancha/Subject-Homework/tree/python/%EA%B3%BC%ED%95%99%EA%B3%BC%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%A0%81%20%EC%82%AC%EA%B3%A0/%EC%B5%9C%EC%A2%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%9C%EC%9A%94)

  2. [파일 구성](https://github.com/firemancha/Subject-Homework/tree/python/%EA%B3%BC%ED%95%99%EA%B3%BC%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%A0%81%20%EC%82%AC%EA%B3%A0/%EC%B5%9C%EC%A2%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8#%ED%8C%8C%EC%9D%BC-%EA%B5%AC%EC%84%B1)

  3. [메인 메뉴 구성](https://github.com/firemancha/Subject-Homework/tree/python/%EA%B3%BC%ED%95%99%EA%B3%BC%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%A0%81%20%EC%82%AC%EA%B3%A0/%EC%B5%9C%EC%A2%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8#%EB%A9%94%EC%9D%B8-%EB%A9%94%EB%89%B4-%EA%B5%AC%EC%84%B1)

  4. [기능 설명](https://github.com/firemancha/Subject-Homework/tree/python/%EA%B3%BC%ED%95%99%EA%B3%BC%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%A0%81%20%EC%82%AC%EA%B3%A0/%EC%B5%9C%EC%A2%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8#%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)

  5. [클래스 구성](https://github.com/firemancha/Subject-Homework/tree/python/%EA%B3%BC%ED%95%99%EA%B3%BC%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%A0%81%20%EC%82%AC%EA%B3%A0/%EC%B5%9C%EC%A2%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8#%ED%81%B4%EB%9E%98%EC%8A%A4-%EA%B5%AC%EC%84%B1)

---

### 프로젝트 개요

  - Menu Driven으로 작동하는 연락처 관리 프로그램이다.

  - 프로그램에서 추가/수정/삭제한 데이터는 `info.json` 파일에 `JSON` 포맷으로 저장된다.(encoding: `UTF-8`)

  - 프로그램 첫 실행 시, `info.json`이 존재하지 않을 경우 `info.json`을 생성한다.

    - 이후 프로그램을 통해 추가/수정/삭제한 데이터가 `info.json`에 저장된다.
  
  - `File I/O` 관련 예외 및 사용자의 데이터 오입력으로 인한 예외를 처리한다.

  - 연락처에 정보를 추가할 시, `이름`과 `연락처`는 필수적으로 입력해야 한다.

  - 그 외의 정보들은 필수 사항이 아니며, 공백을 유지하기 위해선 어떠한 입력도 없이 `엔터`만 입력하면 된다.

  - 프로그램 실행 시 `info.json`의 데이터가 프로그램에 loading되며, 추가/수정/삭제 작업 종료 시 마다 프로그램에서 다루고 있는 데이터가 `info.json`에 덮어 씌워진다.

---

### 파일 구성

<div align=center>

  |     File     | Description                                                            |
  | :----------: | :--------------------------------------------------------------------- |
  |   Main.py    | 메인 프로그램 실행을 위한 파일이다.                                    |
  |  Friend.py   | `Friend` 클래스를 정의한 파일이다.                                     |
  |  Person.py   | `Person` 클래스를 정의한 파일이다.                                     |
  | Phonebook.py | `Phonebook` 클래스를 정의한 파일이다.                                  |
  |  Message.py  | 프로그램 내에서 사용되는 다양한 메세지를 정의한 파일이다.              |
  |  info.json   | 연락처 정보가 저장되어 프로그램 내에서 `File I/O`에 사용되는 파일이다. |

</div>

---

### 메인 메뉴 구성

<div align = center>

  |       Menu       | Description                                                    |
  | :--------------: | :------------------------------------------------------------- |
  |   연락처 추가    | 현재 연락처 정보에 새로운 사람의 연락처를 추가한다             |
  |   연락처 수정    | 연락처에 있는 특정 사람의 정보(주소, 나이, 학번 등)를 수정한다 |
  |   연락처 삭제    | 연락처에 있는 특정 사람의 정보를 삭제한다                      |
  |  연락처 초기화   | 연락처 프로그램에 등록된 모든 사람의 정보를 삭제한다           |
  |   연락처 조회    | 연락처에 있는 특정 사람의 정보를 검색하여 표기한다             |
  | 연락처 전체 조회 | 연락처 프로그램에 등록된 모든 사람의 정보를 표기한다           |
  |  프로그램 종료   | 프로그램을 종료한다                                            |

</div>

  - 각 메뉴에 해당하는 작업이 수행되면 갱신된 연락처 정보를 저장할 지 물어보고, 저장한다.

  - 프로그램 종료 시 프로그램을 정말 종료할 것인지 한번 물어본 후, 프로그램을 종료한다.

---

### 기능 설명

  1. 연락처 추가

       - 사용자로부터 `이름`, `나이`, `연락처`, `학번`, `동아리`, `대학교`, `전공`, `성별`, `주소`를 입력받는다.

       - 이 중 `이름`과 `연락처`는 필수 입력사항으로, 입력이 완료되지 않으면 사용자에게 지속적으로 재입력을 요구한다.

       - `나이`, `연락처`, `학번`의 경우 숫자로만 입력해야 하며, 문자가 포함되어 있을 시 사용자에게 지속적으로 재입력을 요구한다.

         - `연락처`의 경우 10 또는 11자리의 숫자를 입력받는 것으로 가정하며, 이 때 내부적으로 `XXX-XXX-XXXX` 또는 `XXX-XXXX-XXXX`의 포맷으로 변경한다.

       - `성별`의 경우 `남성`, `여성` 또는 `공백`의 값을 입력해야 하며, 그 외의 값이 입력될 경우 사용자에게 지속적으로 재입력을 요구한다.

       - 이 외의 데이터들에 대해서는 정해진 포맷이 없다

       - 입력이 완료되면 사용자에게 저장 여부를 물어본 후, 저장이 요구되면 해당 정보를 파일에 저장한다.
  
  2. 연락처 수정

       - 수정할 데이터를 찾기 위해 사용자로부터 `이름`과 상황에 따라 `연락처`를 입력받는다.

       - 사용자의 입력으로부터 데이터를 찾지 못한 경우, 수정 작업을 종료한다.

       - 데이터를 찾은 경우 메뉴를 표시하여 어떤 필드를 수정할 지 입력받는다.

       - 입력받은 필드에 따라 해당 필드의 값을 수정하며, 각 데이터의 포맷은 연락처 추가 기능에서 입력받는 데이터와 같다.

       - 수정 시 `이름`과 `연락처`를 제외한 데이터 필드는 `공백`값으로 수정 가능하다.

       - 수정이 완료되면 사용자에게 저장 여부를 물어본 후, 저장이 요구되면 해당 정보를 파일에 저장한다.

  3. 연락처 삭제

       - 삭제할 데이터를 찾기 위해 사용자로부터 `이름`과 상황에 따라 `연락처`를 입력받는다.

       - 사용자의 입력으로부터 데이터를 찾지 못한 경우, 삭제 작업을 종료한다.

       - 데이터를 찾은 경우 해당 데이터를 삭제할 것인지 물어본 후 삭제하고 파일에 저장한다.
  
  4. 연락처 초기화

       - 연락처의 모든 정보를 제거할 것인지 사용자로부터 `예` / `아니오` 의 값을 입력받는다.

       - `예`를 입력받으면 모든 정보를 제거한 후 파일에 저장한다.

  5. 연락처 조회

       - 조회 가능한 필드를 메뉴 형식으로 띄워준 후 어떤 필드로 조회할 것인지 입력받는다.

       - 필드에 따라 여러 개의 값이 노출될 수 있으므로, 연락처를 출력할 때 마다 엔터를 입력해 다음 목록을 확인한다.

  6. 연락처 전체 조회

      - 저장되어 있는 모든 연락처 정보를 조회하며, 한 개의 목록을 확인한 후 다음 목록을 확인하기 위해 엔터를 입력한다.

  7. 프로그램 종료

       - 프로그램을 종료할 것인지 사용자로부터 `예` / `아니오`의 값을 입력받는다.

       - `예`를 입력받으면 프로그램을 종료한다.

---

### 클래스 구성

<div align = center>

  |   Class   | Description                                                                                                                                                  |
  | :-------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |  Person   | `이름`과 `주소` 필드를 가지는 클래스로, `Friend`의 부모 클래스이다.                                                                                          |
  |  Friend   | `Person` 클래스를 상속받는 자식 클래스로,  `이름`, `주소` 필드 외에도 `나이`, `성별`, `학번`, `대학교`, `전공`, `동아리`, `연락처` 필드를 가지는 클래스이다. |
  | Phonebook | `Friend` 객체들이 나열되어 있는 리스트 `info`를 필드로 가지는 클래스로, 프로그램 대부분의 작업이 해당 클래스의 메소드로 진행된다.                            |

</div>

---

<div align = center>

  > Written by. 20163162 Cha, YoonSung

</div>