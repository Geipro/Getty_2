<template>
  <div class="home" style="text-align: center;">
    <Navbar/>
    <br>

    <div class="d-flex justify-content-center align-items-center">
      <MainPageCenter />
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import MainPageCenter from '@/components/MainPage/MainPageCenter.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    MainPageCenter
  }
}
</script>
