<template>
  <div>
    <Navbar />
    <br>
    <br>

    <div class="row">
      <div class="col-2">
        <MypageSide/>
      </div>
      <div class="col-10">
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
