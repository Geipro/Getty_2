<template>
  <!-- signup box start -->
  <div id="second">
    <div class="myform form">
      <div class="logo mb-3">
        <div class="col-md-12 text-center">
          <h1>Signup</h1>
        </div>
      </div>
      <form 
        @submit.prevent="onSubmit" 
        name="registration"
      >
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="exampleInputUsername text-left float-left">이름</label>
          </div>
          <input type="text"  name="username" v-model="credential.username"
          class="form-control" id="username" aria-describedby="emailHelp" placeholder="이름">
        </div>
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="exampleInputEmail1">닉네임</label> 
            
          </div>
          <input type="text"  name="nickname" v-model="credential.nickname"
          class="form-control" id="nickname" aria-describedby="nicknameHelp" placeholder="닉네임">
        </div>
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="exampleInputId">아이디</label>
            
          </div>
          <input type="id" name="id" v-validate="'required'" v-model="credential.id" data-vv-as="ID"
          class="form-control" :class="{error: errors.has('id')}"  id="id" aria-describedby="idHelp" placeholder="ID">
          <span class="error" v-if="errors.has('id')">{{errors.first('id')}}</span>
        </div>
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="exampleInputEmail1">전화번호</label> 
          </div>
          <input type="tel" name="phone" v-validate="'digits:11'" v-model="credential.phoneNum" data-vv-as="PhoneNumber"
          class="form-control" :class="{error: errors.has('phone')}" id="phone" aria-describedby="phoneHelp" placeholder="01012345678">
        </div>
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="">비밀번호</label>
          </div>
          <input type="password" ref="password" name="password" v-validate="'required|min:6'" v-model="credential.password" data-vv-as="Password"
          class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="Enter Password">
          <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
        </div>
        <div class="form-group mb-2">
          <div class="d-flex justify-content-between">
            <label for="exampleInputEmail1">비밀번호 확인</label>
          </div>
          <input type="password" name="passwordConfirmation" v-validate="'confirmed:password'" v-model="credential.passwordConfirmation" data-vv-as="Password Confirmation"
          class="form-control" :class="{error: errors.has('passwordConfirmation')}"  id="passwordConfirmation" aria-describedby="passwordConfirmationHelp" placeholder="Enter Password One More">
          <span class="error" v-if="errors.has('passwordConfirmation')">{{errors.first('passwordConfirmation')}}</span>
        </div>
        <div class="text-center mb-3 mt-3">
          <button type="submit" @click="signup" class=" btn btn-block mybtn btn-primary tx-tfm w-100">
            <span>회원가입</span>
          </button>
        </div>
        <div class="col-md-12 ">
          <div class="form-group">
              <p class="text-center"><a href="#" @click="login">로그인</a></p>
          </div>
        </div>
      </form>
    </div>
  </div>
  <!-- signup box end -->
</template>
<script>
import Vue from 'vue'
import axios from 'axios'

// const AUTH_SERVER_URL = process.env.VUE_APP_SERVER_URL

import * as VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'

ko.messages.email = (field) => `${field}은/는 올바른 이메일 형식이어야 합니다.`
ko.messages.required = (field) => `${field}이/가 필요합니다.`

ko.messages.password = (field) => `${field}는 최소 6글자 여야합니다.`
ko.messages.passwordConfirmation = (field) => `${field}는 최소 6글자 여야합니다.`


const config = {
  locale: 'ko',
  dictionary: {
    ko
  }
}

Vue.use(VeeValidate, config)

export default {
  name: 'Signup',

  data: function () {
    return {
      credential: {
        username: null,
        nickname: null,
        id: null,
        phoneNum: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },

  methods: {
    login:function(){
      this.$emit('login')
    },

    onSubmit() {
      this.$validator.validateAll()

      if (!this.errors.any()) {
          return true
        }
    },

    // nicknameDuplicateCheck() {
    //   axios({
    //     method: 'get',
    //     url: `http://k5a405.p.ssafy.io:8000/api/auth/checkNickname/${this.credential.nickname}`,
    //     data: this.credential.nickname
    //   })
    //     .then((res) => {
    //       if (!res.data) {
    //         this.duplicate.nicknameCheck = true
    //         alert('닉네임 중복체크 완료!')
    //       }
    //       else {
    //         alert('다른 닉네임을 입력해주세요!')
    //       }
    //     })
    // },
    
    // emailDuplicateCheck() {
    //   axios({
    //     method: 'get',
    //     url: `http://k5a405.p.ssafy.io:8000/api/auth/checkEmail/${this.credential.email}`,
    //   })
    //     .then((res) => {
    //       if (!res.data) {
    //         this.duplicate.emailCheck = true
    //         alert('이메일 중복체크 완료!')
    //       }
    //       else {
    //         alert('다른 이메일을 입력해주세요!')
    //       }
    //     })
    // },

    signup() {
      console.log(this.passwordConfirmation)
      if (this.onSubmit()) {
        if (this.credential.passwordConfirmation) {
          axios({
            method: 'post',
            url: `http://k5a405.p.ssafy.io:8000/api/auth/signup`,
            data: this.credential
          })
          .then((res) => {
            console.log(res)
            alert('회원가입이 완료되었습니다~!')
            this.login()
          })
        }
      } else {
        alert('비밀번호를 한번 더 입력해주세요!')
      }
    }
  }
}
</script>