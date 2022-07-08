## 07/08(Service 실습)

### Creat & Read

```java
//데이터 저장 
courseRepository.save(new Course("test","product","code01",5,10,50));

//데이터 모두 조회
List<Course> courseList = courseRepository.findAll();
            for (int i=0; i<courseList.size(); i++) {
                Course course = courseList.get(i);
                System.out.println(course.getId());
                System.out.println(course.getCompany_name());
                System.out.println(course.getProduct_name());
                System.out.println(course.getProduct_code());
                System.out.println(course.getQuantity());
                System.out.println(course.getPrice());
                System.out.println(course.getSum());
            }

//데이터 하나만 조회
Course course = repository.findById(1L).orElseThrow(
        () -> new IllegalArgumentException("해당 아이디가 존재하지 않습니다.")
);
```

### Update

Course class에 update method 추가

```java
    public void update(Course course) {
        this.company_name = course.company_name;
        this.product_name = course.product_name;
        this.product_code = course.product_code;
        this.price = course.price;
        this.quantity = course.quantity;
        this.sum = course.sum;
        //this.oredr_date = course.oredr_date;
       // this.due_date = course.due_date;
    }
```

src > main > java > com.nk.ordermanagement > service package생성

CourseService.java 생성

CourseService.java

```java
@Service // 스프링에게 이 클래스는 서비스임을 명시
public class CourseService {

		// final: 서비스에게 꼭 필요한 녀석임을 명시
    private final CourseRepository courseRepository;

		// 생성자를 통해, Service 클래스를 만들 때 꼭 Repository를 넣어주도록
		// 스프링에게 알려줌
    public CourseService(CourseRepository courseRepository) {
        this.courseRepository = courseRepository;
    }

    @Transactional // SQL 쿼리가 일어나야 함을 스프링에게 알려줌
    public Long update(Long id, Course course) {
        Course course1 = courseRepository.findById(id).orElseThrow(
                () -> new IllegalArgumentException("해당 아이디가 존재하지 않습니다.")
        );
        course1.update(course);
        return course1.getId();
    }
}
```

### Update & Delete연습

OrderManagementApplication.java

```java
 @Bean
    public CommandLineRunner demo(CourseRepository courseRepository, CourseService courseService) {
        return (args) -> {
          //첫번째 데이터 저장
            courseRepository.save(new Course("test", "product","code01",5,10,50));

          //데이터 출력
            System.out.println("데이터 인쇄");
            List<Course> courseList = courseRepository.findAll();
            for (int i=0; i<courseList.size(); i++) {
                Course course = courseList.get(i);
                System.out.println(course.getId());
                System.out.println(course.getCompany_name());
                System.out.println(course.getProduct_name());
                System.out.println(course.getProduct_code());
                System.out.println(course.getQuantity());
                System.out.println(course.getPrice());
                System.out.println(course.getSum());
            }

          //데이터 수정
            Course new_course = new Course("test01", "product01","code02",15,20,300);
          //update 실행
            courseService.update(1L, new_course);
          //수정된 데이터 출력
            courseList = courseRepository.findAll();
            for (int i=0; i<courseList.size(); i++) {
                Course course = courseList.get(i);
                System.out.println(course.getId());
                System.out.println(course.getCompany_name());
                System.out.println(course.getProduct_name());
                System.out.println(course.getProduct_code());
                System.out.println(course.getQuantity());
                System.out.println(course.getPrice());
                System.out.println(course.getSum());
            }
          //데이터 삭제
            courseRepository.deleteAll();
        };
    }}
```

실행 결과

```
----------------------데이터 저장-----------------------
Hibernate: select course0_.id as id1_0_, course0_.created_at as created_2_0_, course0_.modified_at as modified3_0_, course0_.company_name as company_4_0_, course0_.due_date as due_date5_0_, course0_.oredr_date as oredr_da6_0_, course0_.price as price7_0_, course0_.product_code as product_8_0_, course0_.product_name as product_9_0_, course0_.quantity as quantit10_0_, course0_.sum as sum11_0_ from course course0_
1
test
product
code01
5
10
50
----------------------데이터 업데이트-----------------------
Hibernate: select course0_.id as id1_0_0_, course0_.created_at as created_2_0_0_, course0_.modified_at as modified3_0_0_, course0_.company_name as company_4_0_0_, course0_.due_date as due_date5_0_0_, course0_.oredr_date as oredr_da6_0_0_, course0_.price as price7_0_0_, course0_.product_code as product_8_0_0_, course0_.product_name as product_9_0_0_, course0_.quantity as quantit10_0_0_, course0_.sum as sum11_0_0_ from course course0_ where course0_.id=?
Hibernate: update course set created_at=?, modified_at=?, company_name=?, due_date=?, oredr_date=?, price=?, product_code=?, product_name=?, quantity=?, sum=? where id=?
Hibernate: select course0_.id as id1_0_, course0_.created_at as created_2_0_, course0_.modified_at as modified3_0_, course0_.company_name as company_4_0_, course0_.due_date as due_date5_0_, course0_.oredr_date as oredr_da6_0_, course0_.price as price7_0_, course0_.product_code as product_8_0_, course0_.product_name as product_9_0_, course0_.quantity as quantit10_0_, course0_.sum as sum11_0_ from course course0_
1
test01
product01
code02
15
20
300
-----------------------데이터 삭제-----------------------
Hibernate: select course0_.id as id1_0_, course0_.created_at as created_2_0_, course0_.modified_at as modified3_0_, course0_.company_name as company_4_0_, course0_.due_date as due_date5_0_, course0_.oredr_date as oredr_da6_0_, course0_.price as price7_0_, course0_.product_code as product_8_0_, course0_.product_name as product_9_0_, course0_.quantity as quantit10_0_, course0_.sum as sum11_0_ from course course0_
Hibernate: delete from course where id=?
```