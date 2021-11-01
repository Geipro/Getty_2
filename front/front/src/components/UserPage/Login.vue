<template>
  <!-- login box start -->
    <div id="first">
        <div class="myform form">
            <div class="logo mb-3">
                <div class="col-md-12 text-center">
                    <h1>Login</h1>
                </div>
            </div>
            <form action="#" method="post" name="login" class=" form-signin ">
                <div class="container">
                    <div class="float-left">
                        <div class="form-group">
                            <input type="id" name="id" v-validate="'required'" v-model="credential.id" data-vv-as="ID"
                            class="form-control" :class="{error: errors.has('ID')}"  id="ID" aria-describedby="idHelp" placeholder="Enter ID">
                            <span class="error" v-if="errors.has('ID')">{{errors.first('ID')}}</span>
                        </div>
                        <div class="form-group mt-3 mb-3">
                            <input type="password" ref="password" name="password" v-validate="'required|min:6'" v-model="credential.password" data-vv-as="Password"
                            class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="Enter Password">
                            <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
                        </div>
                    </div>
                    <div class="text-center float-right">
                        <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm w-100" @click.prevent="getJWT">
                            <span>로그인</span>
                        </button>
                    </div>
                </div>
                <div class="form-group mt-3">
                    <a href="#" class="mr-5" id="signup" @click="signup">회원가입</a>
                    <a class="ml-5 mr-5">           |            </a>
                    <a href="#" id="changePw" @click="changePw">비밀번호 찾기</a>
                </div>
            </form>        
        </div>
    </div>
    <!-- login box end -->
</template>

<script>
import Vue from 'vue'
//import VueRouter from 'vue-router'

import * as VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'
import axios from 'axios';

ko.messages.required = (field) => `${field}이/가 필요합니다.`

ko.messages.password = (field) => `${field}는 최소 6글자 여야합니다.`

const config = {
  locale: 'ko',
  dictionary: {
    ko
  }
}

Vue.use(VeeValidate, config)

export default {
  name: 'Login',
  data: function () {
    return {
      credential: {
        id: '',
        password: '',
      }
    }
  },
  methods: {
    change: function () {
      this.$emit('change')
    },
    signup: function(){
      this.$emit('signup')
    },
    changePw: function(){
      this.$emit('pw')
    },
    getJWT: function () {
      axios({
        method: 'put',
        url: `http://k5a405.p.ssafy.io:8000/api/auth/login`,
        data: this.credential
      })
        .then((res) => {
          // console.log(res)
          localStorage.setItem('nickname', res.data.message)
          localStorage.setItem('JWT_TOKEN', res.data.accessToken)
          alert(`${localStorage.getItem('nickname')} 님 반갑습니다!`)
          this.$router.push({ name: 'User' })
        })
        .catch((err) => {
          alert("탈퇴한 회원이거나 아이디 혹은 비밀번호가 일치하지 않습니다.")
          console.log(err.headers)
        })
    },

    onSubmit() {
      this.$validator.validateAll()

      if (!this.errors.any()) {
        alert('submit!')
      }
    }
  }
}
</script>