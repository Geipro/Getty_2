<template>
  <div>
    <Navbar />
    <div class="row">
      <div class="col-2">
        <MypageSide/>
      </div>
      <div class="col-10">
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
