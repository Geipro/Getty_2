<template>
  <div class="home">
    <Navbar/>
    <br>

    <div class="d-flex justify-content-center align-items-center">
      <MainPageCenter />
    </div>
    <!-- <MainPageBottom /> -->
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/MainPage/Navbar.vue'
import MainPageCenter from '@/components/MainPage/MainPageCenter.vue'
// import MainPageBottom from '@/components/MainPage/MainPageBottom.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    MainPageCenter,
    // MainPageBottom
  }
}
</script>
