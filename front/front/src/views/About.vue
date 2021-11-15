<template>
  <div class="about conatiner h-100" style="text-align: center;">
    <Navbar/>
    <div class="row justify-content-center align-items-center h-100">
      <div class="col-4 d-flex flex-column my-5">
        <login v-if="login"
        @signup="changeSignup"
        class=""></login>

        <signup v-if="signup"
        @login="changeLogin"
        class="" ></signup>
      </div>
    </div>
  </div>
</template>

<script>
import Login from '@/components/UserPage/Login.vue'
import Signup from '@/components/UserPage/Signup.vue'
import Navbar from '@/components/MainPage/Navbar.vue'

export default {
    name: 'About',
    components: {
        Login,
        Signup,
        Navbar,
    },
    data () {
        return {
          login: true,
          signup: false
        }
    },
    methods : {
        changeLogin(){
            this.login = true,
            this.signup = false
        },
        changeSignup(){
            this.login = false,
            this.signup = true
        }
    }
}
</script>
<style>

</style>
