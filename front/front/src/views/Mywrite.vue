<template>
  <div style="text-align: center;">
    <Navbar />
    <br>
    <br>
    <div class="row">
      <div class="col-2 d-flex justify-content-center align-items-center">
        <MypageSide/>
      </div>
      <div class="col-8">
        <WriteList/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import MypageSide from '@/components/Mypage/MypageSide.vue'
import WriteList from '@/components/Mypage/WriteList.vue'

export default {
  name: 'Mywrite',
  components: {
    Navbar,
    MypageSide,
    WriteList
  }
}
</script>

<style>

</style>
