<template>
  <!-- login box start -->
    <div id="first">
        <div class="myform form">
            <div class="logo mb-3">
                <div class="col-md-12 text-center">
                    <h1>Change Password</h1>
                </div>
            </div>
            <form action="#" method="post" name="changePassword" class=" form-signin ">
                <div class="form-group">
                    <label for="exampleInputEmail1">Email</label>
                    <input type="email" name="email" v-validate="'required|email'" v-model="credential.email" data-vv-as="Email"
                        class="form-control" :class="{error: errors.has('email')}"  id="email" aria-describedby="emailHelp" placeholder="Enter email">
                    <span class="error" v-if="errors.has('email')">{{errors.first('email')}}</span>
                </div>
                <div class="col-md-12 text-center ">
                    <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm" @click.prevent="inputEmail">Send Code</button>
                </div>

                <br>

                <div class="form-group">
                    <label for="exampleInputVerificationCode">Verification Code</label>
                    <input type="code" name="code" v-validate="'required|min:8'" v-model="code.code" data-vv-as="Code"
                        class="form-control" :class="{error: errors.has('code')}"  id="code" aria-describedby="codeHelp" placeholder="Enter code">
                    <span class="error" v-if="errors.has('code')">{{errors.first('code')}}</span>
                </div>
                <div class="col-md-12 text-center ">
                    <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm" @click.prevent="inputCode">Verificate</button>
                </div>

                <div class="form-group">
                    <label for="">Password</label>
                    <input type="password" ref="password" name="password" v-validate="'required|min:6'" v-model="credential.password" data-vv-as="Password"
                        class="form-control" :class="{error: errors.has('password')}"  id="password" aria-describedby="password" placeholder="Enter Password">
                    <span class="error" v-if="errors.has('password')">{{errors.first('password')}}</span>
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail1">Password Confirmation</label>
                    <input type="password" name="passwordConfirmation" v-validate="'confirmed:password'" v-model="status.passwordConfirmation" data-vv-as="Password Confirmation"
                        class="form-control" :class="{error: errors.has('passwordConfirmation')}"  id="passwordConfirmation" aria-describedby="passwordConfirmationHelp" placeholder="Enter Password One More">
                    <span class="error" v-if="errors.has('passwordConfirmation')">{{errors.first('passwordConfirmation')}}</span>
                </div>
                <div class="col-md-12 text-center ">
                    <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm" @click.prevent="inputPw">Change Password</button>
                </div>
                <div class="col-md-12 ">
                    <div class="form-group">
                        <p class="text-center"><a href="#" @click="login">로그인</a></p>
                    </div>
                </div>
            </form>        
        </div>
    </div>
    <!-- login box end -->
</template>

<script>
import Vue from 'vue'
import axios from 'axios'

// const AUTH_SERVER_URL = process.env.VUE_APP_SERVER_URL

import * as VeeValidate from 'vee-validate';
import ko from 'vee-validate/dist/locale/ko.js'

ko.messages.email = (field) => `${field}은/는 올바른 이메일 형식이어야 합니다.`
ko.messages.required = (field) => `${field}이/가 필요합니다.`
ko.messages.code = (field) => `${field}은/는 8글자 입니다.`

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
    name: 'ChangePw',
    data: function () {
        return {
            credential: {
                email:'',
                password: '',
            },

            code:{
                code: '',
            },

            status:{
                passwordConfirmation: '',
                sendEmail: '',
                checkCode: '',
            }
        }
    },
    methods: {
        login(){
            this.$emit("login")
        },

        onSubmit() {
            this.$validator.validateAll()

            if (!this.errors.any()) {
                return true
            }
        },

        inputEmail(){
            if(this.credential.email != null){
                axios({
                    method: 'get',
                    url: `http://k5a405.p.ssafy.io:8000/api/emailAuth/send/${this.credential.email}`
                }).then((res) => {
                    console.log(res)
                    alert('이메일 전송이 완료되었습니다~!')
                    this.status.sendEmail = !this.status.sendEmail
                })
            }else{
                alert('이메일을 입력하세요!')
            }
        },

        inputCode(){
            if(this.code.code != null){
                axios({
                    method: 'post',
                    url: `http://k5a405.p.ssafy.io:8000/api/emailAuth/check/verifying`,
                    data: this.code
                }).then((res) => {
                    console.log(res)
                    console.log(res.data)
                    if(res.data == true){
                        alert('인증 확인되었습니다~!')
                        this.status.checkCode = !this.status.checkCode
                    }else
                        alert('인증번호가 틀렸습니다. 다시 확인해주세요!')
                    
                })
            }else{
                alert('인증번호를 입력하세요!')
            }
        },

        inputPw(){
            if(this.status.passwordConfirmation){
                if(this.status.checkCode){
                    if(this.status.sendEmail){
                        axios({
                            method: 'put',
                            url: `http://k5a405.p.ssafy.io:8000/api/auth/changePw`,
                            data: this.credential
                        }).then((res) => {
                            console.log(res)
                            alert('회원정보 수정이 완료되었습니다~!')
                            this.login()
                        })
                    }else{
                        alert('이메일을 적어 인증번호를 보내십시오.')
                    }
                }else{
                    alert('인증코드를 확인하세요.')
                }
            }else{
                alert('비밀번호가 일치하지 않습니다.')
            }
        }
    }
}
</script>
