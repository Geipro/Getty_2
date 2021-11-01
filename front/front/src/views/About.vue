<template>
  <div class="about conatiner h-100">
    <div class="row justify-content-center align-items-center h-100">
      <div class="col-4 d-flex flex-column my-5">
        <login v-if="login" 
        @signup="changeSignup"
        @pw="changePw"
        class=""></login>
        
        <signup v-if="signup" 
        @login="changeLogin"
        class="" ></signup>
        
        <change-pw v-if="pw" 
        @login="changeLogin"
        class=""></change-pw>
      </div>
    </div>
  </div>
</template>

<script>
import Login from '@/components/UserPage/Login.vue'
import Signup from '@/components/UserPage/Signup.vue'
import ChangePw from '@/components/UserPage/ChangePw.vue'

export default {
    name: 'About',
    components: {
        Login,
        Signup,
        ChangePw
    },
    data () {
        return {
          login: true,
          signup: false,
          pw : false
        }
    },
    methods : {
        changeLogin(){
            this.login = true,
            this.signup = false,
            this.pw = false
        },
        changeSignup(){
            this.login = false,
            this.signup = true,
            this.pw = false
        },
        changePw(){
            this.pw = true,
            this.login = false,
            this.signup = false
        }
    }
}
</script>
<style>

</style>