# github-actions

**목차**
- [GitHub Actions](#github-actions)

## GitHub Actions
Github Action은 빌드, 테스트, 배포 파이프라인을 자동화할 수 있는 지속적 통합 / 배포(CI/CD) 플랫폼이다. 레포지토리에 대한 모든 Pull Request를 빌드, 테스트하는 workflow를 생성하거나 merge된 Pull Request를 프로덕션에 배포할 수 있다. Github Action은 DevOps를 넘어 레포지토리에서 다른 이벤트가 발생할 때 workflow를 실행할 수 있다. 누가 저장소에 새 이슈를 만들 때마다 적절한 레이블을 자동 추가하는 workflow를 실행할 수 있다. 리눅스, 윈도우, MacOS 가상 머신을 제공해서 workflow를 실행하거나 자체 데이터 센터 또는 클라우드 인프라에서 자체 호스팅 러너를 호스팅할 수 있으며 GitHub Actions의구성 요소는 음과 같다.

- Workflows: 여러 개의 잡으로 구성되어 있는 자동화된 프로세스 단위로 YAML 파일로 설정된다. 워크플로는 `.github/workflows`라는 정해진 폴더 내에서 yaml파일로 정의되며 하나의 repository는 다수의 워크플로우를 가질 수 있다. 즉 다수의 워크플로우 yaml파일을 가질 수 있다.
- Events: 워크플로우를 실행시키는 특정 행동을 이벤트라고 한다. 예를 들어, PR, push 등이 워크플로우를 실행시키는 이벤트가 될 수 있다. [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)에서 모든 이벤트 항목을 확인 할 수 있다.
- Jobs: 스텝으로 구성되어 있는 실행 단위이다. 즉, 잡은 실제 실행을 정의하는 부분이며 다수의 스텝으로 구성될 수 있다.
- Actions: 사용자 작성한 task를 의미한다.
- Runners: 워크플로우가 실행되는 서버를 의미한다. GitHub는 Ubuntu Linux, Microsoft Windows, 그리고 macOS VM을 제공한다. 기본으로 제공되는 runner를 사용하는 반면 사용자 정의 runner를 지정할수 도 있다.




