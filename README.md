# github-actions

**목차**
- [GitHub Actions](#github-actions)
- [워크플로우 예제](#workflow-예제)
- [다른 Action참조하기](#다른-action-참조하기)
- [Metadata syntax for GitHub Actions](#metadata-syntax-for-github-actions)

## GitHub Actions
Github Action은 빌드, 테스트, 배포 파이프라인을 자동화할 수 있는 지속적 통합 / 배포(CI/CD) 플랫폼이다. 레포지토리에 대한 모든 Pull Request를 빌드, 테스트하는 workflow를 생성하거나 merge된 Pull Request를 프로덕션에 배포할 수 있다. Github Action은 DevOps를 넘어 레포지토리에서 다른 이벤트가 발생할 때 workflow를 실행할 수 있다. 누가 저장소에 새 이슈를 만들 때마다 적절한 레이블을 자동 추가하는 workflow를 실행할 수 있다. 리눅스, 윈도우, MacOS 가상 머신을 제공해서 workflow를 실행하거나 자체 데이터 센터 또는 클라우드 인프라에서 자체 호스팅 러너를 호스팅할 수 있으며 GitHub Actions의구성 요소는 음과 같다.

- Workflows: 여러 개의 잡으로 구성되어 있는 자동화된 프로세스 단위로 YAML 파일로 설정된다. 워크플로는 `.github/workflows`라는 정해진 폴더 내에서 yaml파일로 정의되며 하나의 repository는 다수의 워크플로우를 가질 수 있다. 즉 다수의 워크플로우 yaml파일을 가질 수 있다.
- Events: 워크플로우를 실행시키는 특정 행동을 이벤트라고 한다. 예를 들어, PR, push 등이 워크플로우를 실행시키는 이벤트가 될 수 있다. [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)에서 모든 이벤트 항목을 확인 할 수 있다.
- Jobs: 스텝으로 구성되어 있는 실행 단위이다. 즉, 잡은 실제 실행을 정의하는 부분이며 다수의 스텝으로 구성될 수 있다.
- Actions: 사용자가 작성한 task를 지정할 수 도 있고 이미 만들어진 action을 지정할 수 도 있다. 이것은 반복적인 코드를 줄이고 재사용을 위해 사용될 수 있다. 본인의 action을 생성하기 위해서는 [Creating actions](https://docs.github.com/en/actions/creating-actions)를 참조한다.
- Runners: 워크플로우가 실행되는 서버를 의미한다. GitHub는 Ubuntu Linux, Microsoft Windows, 그리고 macOS VM을 제공한다. 기본으로 제공되는 runner를 사용하는 반면 사용자 정의 runner를 지정할수 도 있다.

## Workflow 예제
```yaml
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

|YAML|설명|
|---|---|
|name: learn-github-actions|GitHub Actions 탭에서 워크플로우 이름을 나타낸다. optional|
|run-name: ${{ github.actor }} is learning GitHub Actions|워크플로우의 run name을 나타낸다. optional|
|on: [push]|워크플로우를 trigger시키는 이벤트를 추가한다. push 이벤트 발생 시 해다 워크플로우가 동작된다.|
|jobs:|워크플로우에서 동작할 잡을 설정하는 부분이다.|
|check-bats-version:|해당 잡의 이름을 나타낸다.|
|runs-on: ubuntu-latest|해당 잡이 동작할 서버를 지정한다. [Github가 제공하는 runner](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#choosing-github-hosted-runners)를 참고한다.|
|steps:|잡에서 동작할 스텝을 나타낸다.|
|- uses: actions/checkout@v4|지정한 runner에 해당 repository를 checkout하는 action을 실행하는 부분이다.|
|- uses: actions/setup-node@v4|node.js를 설치하는 action을 실행하는 부분이다. 아래 14버전을 설치한다.|
|with:||
|node-version: '14'|설치할 노드의 버전을 명시한다.|
|- run: npm install -g bats|npm으로 bats를 설치한다.|
|- run: bats -v|batc command를 실행한다.|

## 다른 action 참조하기
**동일한 repository 내에 존재하는 action 추가하기**

예를 들어, 다음과 같은 폴더 구조로 되어 있는 경우에 `my-first-workflow.yml`가 `hello-world-action/action.yml`을 참조한다면 다음과 같다.
```bash
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

```yaml
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v4
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action
```

**다른 repository 내에 존재하는 action 추가하기**

만약 다른 repository 내에 존재하는 action을 추가한다면 `{owner}/{repo}@{ref}` 형식으로 지정한다. 

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/setup-node@v4
    steps:
      - uses: actions/javascript-action@v1.0.1
    steps:
      - uses: actions/javascript-action@main
```
## Metadata syntax for GitHub Actions

GitHub Actions에서 설정 가능한 [metadata](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)를 참고하여 action.yml 파일을 작성한다.

**Docker container**

[Dockerfile를 실행](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#runs-for-docker-container-actions)하기 위해 다음과 같이 설정할 수 있다.
```yaml
runs:
  using: 'docker'
  image: 'Dockerfile'
```

## Default environment 변수

**Default environment variables**

GitHub는 다양한 시스템 기본 변수를 제공한다. 자세한 정보는 [Default environment variabls](https://docs.github.com/ko/actions/learn-github-actions/variables#default-environment-variables)를 참고한다.

**Custom variables**

사용자는 `env`키를 사용하여 사용자 정의 변수를 설정할 수 있다. 자세한 사항은 [Define environment variables for a single workflow](https://docs.github.com/ko/actions/learn-github-actions/variables#defining-environment-variables-for-a-single-workflow)를 참조한다.

```yaml
name: Greeting on variable day

on:
  workflow_dispatch

env:
  DAY_OF_WEEK: Monday

jobs:
  greeting_job:
    runs-on: ubuntu-latest
    env:
      Greeting: Hello
    steps:
      - name: "Say Hello Mona it's Monday"
        run: echo "$Greeting $First_Name. Today is $DAY_OF_WEEK!"
        env:
          First_Name: Mona
```

`env` scope은 다음과 같이 정의될 수 있다.
- The entire workflow, by using env at the top level of the workflow file.
- The contents of a job within a workflow, by using jobs.<job_id>.env.
- A specific step within a job, by using jobs.<job_id>.steps[*].env.

## Runners
Runner는 gitHub Actions 워크플로에서 작업을 실행하는 머신을 의미한다. GitHub는 작업을 실행하는데 사용할 수 있는 runner를 제공하거나 사용자 고유의 runner를 사용할 수 도 있다. GitHub-hosted runner의 종류는 다음과 같다.

- [Standard GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources)
- [Larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners)
- [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners)

Standard GitHub-hosted VM의 리소스 정보는 [여기](https://docs.github.com/ko/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources)에서 확인 할 수 있다. public repository의 경우에는 VM을 무제한으로 무료로 사용이 가능하다. 하지만, private repository에서 사용하는 경우에는 무료 사용 가능 시간을 초과할 경우 요금이 청구된다. 자세한 사항은 [요금 청구 정보](https://docs.github.com/ko/billing/managing-billing-for-github-actions/about-billing-for-github-actions#github-actions-%EC%9A%94%EA%B8%88-%EC%B2%AD%EA%B5%AC-%EC%A0%95%EB%B3%B4)를 참고한다.




