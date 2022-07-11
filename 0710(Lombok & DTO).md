## 07/10 (Lombok & DTO)

### Lombok

Java의 라이브러리로 반복되는 메소드를 `Annotation`을 사용해서 자동으로 작성해주는 라이브러리다. 

보통 DTO나 Model, Entity의 경우 여러 속성이 존재하고 이들이 가지는 프로퍼티에 대해서 Getter나 Setter, 생성자 등을 매번 작성해줘야 하는 경우가 많은데 이러한 부분을 자동으로 만들어주는 라이브러리라고 할 수 있다.

Course.java

```java
  public String getCompany_name() {

        return this.company_name;
    }

    public String getProduct_name() 

        return this.product_name;
    }

    public String getProduct_code() {
        return this.product_code;
    }

    public int getQuantity() {
        return this.quantity;
    }

    public int getPrice() {

        return this.price;
    }

    public int getSum() {
        return this.sum;
    }
    public Date getOredr_date() {
        return this.oredr_date;
    }
    public Date getDue_date() {
        return this.due_date;
    }


```

Getter가 잔뜩 적혀 있는 Course파일을

```java
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
//@Getter와 @Setter를 클래스 이름 위에 적용시키면 모든 변수들에 적용이 가능하고, 변수 이름 위에 적용시키면 해당 변수들만 적용 가능하다.

@NoArgsConstructor
//@NoArgsConstructor는 어떠한 변수도 사용하지 않는 기본 생성자를 자동완성 시켜주는 어노테이션이다. @NoArgsConstructor를 활용한 예제는 아래와 같다

```

이렇게 추가하면 깔끔하게 사라진다.

또한 CourseService.java

```java
public CourseService(CourseRepository courseRepository) {
        this.courseRepository = courseRepository;
    }
```

CourseService가 시작할때마다 CourseRepository를 알아서 생성하도록해 맴버변수로 전달하도록 했다. 이것을

```java
import lombok.RequiredArgsConstructor;
@RequiredArgsConstructor
/*
@RequiredArgsConstructor는 특정 변수만을 활용하는 생성자를 자동완성 시켜주는 어노테이션이다. 
생성자의 인자로 추가할 변수에 @NonNull 어노테이션을 붙여서 해당 변수를 생성자의 인자로 추가할 수 있다. 아니면 해당 변수를 final로 선언해도 의존성을 주입받을 수 있다.
*/
```

를 추가해서 사용하지 않도록 했다

이렇게 Lombok을 사용해 코드를 효율적으로 단축해보았다.

### DTO

DTO(Data Transfer Object)란 계층간 데이터 교환을 위해 사용하는 객체(Java Beans)

+ 유저가 입력한 데이터를 DB에 넣는 과정
  + 유저가 자신의 브라우저에서 데이터를 입력하여 form에 있는 데이터를 DTO에 넣어서 전송한다.
  + 해당 DTO를 받은 서버가 DAO를 이용하여 데이터베이스로 데이터를 집어넣습니다.
+ 로직을 갖고 있지 않는 순수한 데이터 객체이며, getter/setter 메서드만을 갖는다.
+ 하지만 DB에서 꺼낸 값을 임의로 변경할 필요가 없기 때문에 DTO클래스에는 setter가 없다. (대신 생성자에서 값을 할당한다.)

src > main > java > com.nk.ordermanagement > domain > CourseRequestDto.java 생성

```java
package com.nk.ordermanagement.domain;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.Column;
import java.sql.Date;

@RequiredArgsConstructor
@Getter
@Setter
public class CourseRequestDto {
    private final String company_name;//회사명
    private final String product_name; //제품명
    private final String product_code;  //제품 코드
    private final int price ;  		//단가
    private final int quantity ;		//수량
    private final int sum ;			//총액
    private Date oredr_date ;	//수주일
    private Date due_date ;		//납기일
    }

```

이렇게 생성 후 코드를 변경해준다

CourseService.java

```java
    public Long update(Long id, Course course) {
        Course course1 = courseRepository.findById(id).orElseThrow(
                () -> new IllegalArgumentException("해당 아이디가 존재하지 않습니다.")
        );
        course1.update(course);
        return course1.getId();
    }
```



```java
    public Long update(Long id, CourseRequestDto requestDto) {
        Course course1 = courseRepository.findById(id).orElseThrow(
                () -> new IllegalArgumentException("해당 아이디가 존재하지 않습니다.")
        );
        course1.update(requestDto);
        return course1.getId();
    }
```

Course.java

```java
public void update(CourseRequestDto requestDto) {
        this.company_name = requestDto.getCompany_name();
        this.product_name = requestDto.getProduct_name();
        this.product_code = requestDto.getProduct_code();
        this.price = requestDto.getPrice();
        this.quantity = requestDto.getQuantity();
        this.sum = requestDto.getSum();
        //this.oredr_date = course.oredr_date;
       // this.due_date = course.due_date;
    }
```

OrderManagemnetApplicationTests.java

```java
CourseRequestDto requestDto = new CourseRequestDto("test01", "product01","code02",15,20,300);
            courseService.update(1L, requestDto);
```

코드가 상당히 줄었음에도 문제없이 잘 실행됨을 확인했다