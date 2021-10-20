## 자율 PJT를 위한 학습



## Vuex

- vuex는 vue.js를 위한 상태 관리 라이브러리.
  - 모든 컴포넌트들에서 접근 가능한 중앙 집중식 데이터 저장소
  - 모든 데이터 흐름을 중앙에서 관리함으로써 예측 가능한 애플리케이션을 구현할 수 있다.
- 다른 상태 관리 패턴이나 라이브러리와 비교했을 때 뷰의 반응성(Reactivity) 체계를 효율적으로 활용하여 화면을 업데이트 한다는 차이점이 있습니다.



## 상태 관리(State Management)가 왜 필요한가?

컴포넌트 기반 프레임워크에서는 작은 단위로 쪼개진 여러 개의 컴포넌트로 화면을 구성합니다. 예를 들면, header, button, list 등의 화면 요소가 각각 컴포넌트로 구성되어 한 화면에서 많은 컴포넌트를 사용합니다. 이에 따라 **컴포넌트 간의 통신이나 데이터 전달을 좀 더 유기적으로 관리할 필요성이 생깁니다.**



## 상태 관리란?

상태 관리란 여러 컴포넌트 간의 데이터 전달과 이벤트 통신을 한곳에서 관리하는 패턴을 의미합니다. 뷰와 성격이 비슷한 프레임워크인 리액트(React)에서는 Redux, Mobx와 같은 상태 관리 라이브러리를 사용하고 있고 뷰에서는 Vuex라는 상태 관리 라이브러리를 사용합니다.



## 상태 관리로 해결할 수 있는 문제점?

상태 관리는 중대형 규모의 웹 애플리케이션에서 컴포넌트 간에 데이터를 더 효율적으로 전달할 수 있습니다. 일반적으로 앱의 규모가 커지면서 생기는 문제점들은 다음과 같습니다.

1. 뷰의 컴포넌트 통신 방식인 props, event emit 때문에 **중간에 거쳐할 컴포넌트가 많아지거나**
2. 이를 피하기 위해 Event Bus를 사용하여 **컴포넌트 간 데이터 흐름을 파악하기 어려운 것**

이러한 문제점을 해결하기 위해 모든 데이터 통신을 한 곳에서 중앙 집중식으로 관리하는 것이 상태 관리입니다.



![img](https://joshua1988.github.io/images/posts/web/vuejs/vuex-1/vuex-diagram.png)

Vuex 전체 흐름도



## 상태 관리 패턴

상태 관리 구성요소는 크게 3가지가 있습니다.

- **state** : 컴포넌트 간에 공유할 **data**
- **view** : 데이터가 표현될 **template**
- **actions** : 사용자의 입력에 따라 반응할 **methods**

```js
new Vue({
  // state
  data() {
    return {
      counter: 0
    };
  },
  // view
  template: `
    <div>{{ counter }}</div>
  `,
  // actions
  methods: {
    increment() {
      this.counter++;
    }
  }
});
```





#### vuex 설치법

```
npm install vuex --save

npm install vuex
(이것도 가능)


npm install es6-promise --save 
```



### Vuex의 기본흐름과 핵심컨셉

- state: 
- mutations:
- actions:







## 캡틴판교 vuex 자료 참고하기

- https://joshua1988.github.io/web-development/vuejs/vuex-start/
- https://joshua1988.github.io/web-development/vuejs/vuex-getters-mutations/
- https://joshua1988.github.io/web-development/vuejs/vuex-actions-modules/

#### 기타 참고 사이트

- https://webruden.tistory.com/340

  
