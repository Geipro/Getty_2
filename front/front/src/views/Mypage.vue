<template>
  <div style="text-align: center;">
    <Navbar />
    <br>
    <br>
    <div class="row">
      <div class="col-2 d-flex justify-content-center align-items-center">
        <MypageSide/>
      </div>
      <div class="col-8 d-flex justify-content-center align-items-center">
        <UserInformationModify/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import MypageSide from '@/components/Mypage/MypageSide.vue'
import UserInformationModify from '@/components/Mypage/UserInformationModify.vue'

export default {
  name: 'Mypage',
  components: {
    Navbar,
    MypageSide,
    UserInformationModify
  }
}
</script>

<style>

</style>
