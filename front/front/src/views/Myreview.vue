<template>
  <div>
    <Navbar />
    <br>
    <br>
    <div class="row">
      <div class="col-2 d-flex justify-content-center align-items-center">
        <MypageSide/>
      </div>
      <div class="col-8">
        <ReviewList/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import MypageSide from '@/components/Mypage/MypageSide.vue'
import ReviewList from '@/components/Mypage/ReviewList.vue'

export default {
  name: 'Myreview',
  components: {
    Navbar,
    MypageSide,
    ReviewList
  }
}
</script>