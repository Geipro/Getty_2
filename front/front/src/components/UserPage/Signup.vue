<template>
  <!-- signup box start -->
  <div id="second">
    <div class="myform form">
      <div class="logo mb-3">
        <div class="col-md-12 text-center">
          <h1 class="text-light" >회원가입</h1>
        </div>
      </div>
      <form 
        @submit.prevent="onSubmit" 
        name="registration"
      >
        <div class="text-left form-group justify-content-between mb-2 mt-2">
          <div class="d-flex justify-content-between">
            <label for="user_name">이름</label>
          </div>
          <input type="text"  name="user_name" v-validate="'required'" v-model="userinfo.user_name"
          class="form-control" id="user_name" aria-describedby="nameHelp" placeholder="이름을 입력하세요">
          <span class="error" v-if="errors.has('user_name')">{{errors.first('user_name')}}</span>
        </div>
        <div class="form-group mb-2 mt-2">
          <div class="d-flex justify-content-between">
            <label for="user_id">아이디</label>
          </div>
          <input type="id" name="user_id" v-validate="'required'" v-model="userinfo.user_id" data-vv-as="ID"
          class="form-control" :class="{error: errors.has('user_id')}"  id="id" aria-describedby="UserIdHelp" placeholder="ID를 입력하세요">
          <span class="error" v-if="errors.has('user_id')">{{errors.first('user_id')}}</span>
        </div>


        <!-- 생년월일 -->
        <div class="col-md-12">
          <div class="form-group mb-3 mb-2 mt-2">
            <div class="text-left justify-content-between">
              <div class="d-flex justify-content-between">
                <label for="exampleInputBirthday">출생연도</label>
              </div>
              <div class="row_fluid">
                <div class="float-left">
                  <span class="">
                    <select
                    id="yy"
                    class="form-control float-left"
                    v-model="userinfo.year"
                    @focus="checkFlag = false"
                    >
                      <option value="">년도</option>
                      <option
                      v-for="(yy, index) in yyyyList"
                      :key="index"
                      :value="yy.value"
                      >
                      {{ yy.text }}
                      </option>
                    </select>
                  </span>
                </div>
                <div class="float-left mr-3 ml-3">
                  <span class="form-select">
                    <select
                    id="mm"
                    class="form-control"
                    v-model="userinfo.month"
                    @focus="checkFlag = false"
                    >
                      <option value="">월</option>
                      <option
                      v-for="(mm, index) in mmlist"
                      :key="index"
                      :value="mm.value"
                      >
                      {{ mm.text }}
                      </option>
                    </select>
                  </span>
                </div>
                <div class="float-left mr-3">
                  <span class="form-select">
                    <select
                    id="dd"
                    class="form-control"
                    v-model="userinfo.day"
                    @focus="checkFlag = false"
                    >
                      <option value="">일</option>
                      <option
                      v-for="(dd, idx) in ddlist"
                      :key="idx"
                      :value="dd.value"
                      >
                        {{ dd.text }}
                      </option>
                    </select>
                  </span>
                </div>
              </div>
            </div>
          </div>
          </div>
          <div class="form-group text-left mb-2 mt-2">
            <div class="d-flex justify-content-between">
              <label class="mr-5" for="sex">성별</label>
            </div>
            <label class="radio is-inline" v-for="sex in sexs" :key="sex">
              <input type="radio" :value="sex.value" class="radio-input" v-validate="'required'" data-vv-as="성별" v-model="userinfo.sex" name="sex">
              <span class="radio-label ml-5 mr-3" style="margin-left:10px; margin-right:50px"> {{ sex.text }} </span>
            </label>
            <br>
            <span class="error" v-if="errors.has('sex')">{{errors.first('sex')}}</span>
          </div>
        <div class="form-group text-left mb-2 mt-2">
          <div class="d-flex justify-content-between">
            <label for="phone">전화번호</label>
          </div>
          <input type="tel" name="phone" v-validate="'required|digits:11'" v-model="userinfo.phone_number" data-vv-as="전화번호"
          class="form-control" :class="{error: errors.has('phone')}" id="phone" aria-describedby="phoneHelp" placeholder="01012345678">
          <span class="error" v-if="errors.has('phoneNumber')">{{errors.first('phoneNumber')}}</span>
        </div>
        <div class="form-group text-left mb-2 mt-2">
          <div class="d-flex justify-content-between">
            <label for="password">Password</label>
          </div>
          <input type="password" ref="password" name="password" v-validate="'required|min:4'" v-model="userinfo.user_pw" data-vv-as="Password"
          class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="비밀번호를 입력해주세요">
          <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
        </div>
        <div class="form-group text-left mb-2 mt-2">
          <div class="d-flex justify-content-between">
            <label for="passwordConfirmation">Password Confirmation</label>
          </div>
          <input type="password" name="passwordConfirmation" v-validate="'confirmed:password'" v-model="userinfo.passwordConfirmation" data-vv-as="Password Confirmation"
          class="form-control" :class="{error: errors.has('passwordConfirmation')}"  id="passwordConfirmation" aria-describedby="passwordConfirmationHelp" placeholder="비밀번호를 한번 더 입력해주세요">
          <span class="error" v-if="errors.has('passwordConfirmation')">{{errors.first('passwordConfirmation')}}</span>
        </div>
        <div class="text-center float-right mt-3 mb-3">
          <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm w-100" @click="signupCheck">
            <span>회원가입</span>
          </button>
        </div>
        <div class="col-md-12 ">
          <div class="form-group">
            <a href="#" class="mr-5 text-light" id="login" @click="login">로그인 페이지로 이동</a>
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

import VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'

ko.messages.required = (field) => `${field} 이/가 필요합니다.`

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
      sexs: [
        {
          value:0,
          text:"남성"
        },
        {
          value:1,
          text:"여성"
        }
      ],
      userinfo:{
        user_name:'',
        user_id:'',
        birth:'',
        year: "",
        month: "",
        day: "",
        sex:'',
        phone_number:'',
        user_pw:'',
        passwordConfirmation: null
      },
      sendData:{
        user_name:'',
        user_id:'',
        birth:'',
        sex:'',
        phone_number:'',
        user_pw:'',
      },
      yyyyList: [],
      mmlist: [],
      ddlist: [],
    };
  },
  created() {
    const nowYear = new Date().getFullYear();
    for (let i = 0; i <= 100; i++) {
      let date = nowYear - i;
      this.yyyyList.push({ value: date, text: date });
    }
    for (let i = 1; i < 13; i++) {
      if(i > 9){
        this.mmlist.push({
          value: i,
          text: i,
        });
      }else{
        this.mmlist.push({
          value: '0' + i,
          text: '0' + i,
        });
      }
    }
    for(let i = 1; i < 32; i++){
      if(i > 9){
        this.ddlist.push({
          value:i,
          text:i
        })
      }else{
        this.ddlist.push({
          value:'0' + i,
          text: '0' + i
        })
      }
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
      return false
    },
    signupCheck() {
      var sumDate = this.userinfo.year
      sumDate = String(sumDate) + String(this.userinfo.month) + String(this.userinfo.day)
      this.userinfo.birth = sumDate

      this.sendData.user_name = this.userinfo.user_name
      this.sendData.user_id = this.userinfo.user_id
      this.sendData.user_pw = this.userinfo.user_pw
      this.sendData.birth = this.userinfo.birth
      this.sendData.sex = this.userinfo.sex
      this.sendData.job = this.userinfo.job
      this.sendData.salary = this.userinfo.salary
      this.sendData.phone_number = this.userinfo.phone_number
      if (this.onSubmit()) {
        if (this.userinfo.passwordConfirmation) {
          axios({
            method: 'post',
            url: `https://k5a405.p.ssafy.io/backend/signup`,
            data: this.sendData
          }).then((res) => {
            //console.log(res)
            res
            alert('회원가입이 완료되었습니다~!')
            //this.login()
            this.$emit('login')
            this.login()
          }).catch((err) =>{
            //alert(err)
            err
          })
        }else {
          alert('비밀번호 확인하여주세요!')
        }
      }else{
        alert("항목을 전부 입력해주세요!")
      }
    }
  }
}
</script>