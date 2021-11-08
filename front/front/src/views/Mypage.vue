<template>
  <div>
    <Navbar />
    <br>
    <br>
    <div class="row">
      <div class="col-2 d-flex justify-content-center align-items-center">
        <MypageSide/>
      </div>
      <!-- d-flex justify-content-center align-items-center 빼면 길어짐 -->
      <!-- api가 없는데 제외하고 페이지 변경해도 됨  -->
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
