<template>
  <div style="color: white" class="justify-content-center bg-dark">
    <router-link :to="{ name: 'Home' }">
      <img src="@/assets/logo.png" style="width:70px">
    </router-link>
    Getty
    <!-- 로고 옆으로 조정해보기 -->
    <!-- <div class="justify-content-end "> -->
      <!-- <router-link :to="{ name: 'About' }" class="nav-link">로그인</router-link> -->
    <!-- </div> -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</div>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    msg: String
  },
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('Token')
      localStorage.removeItem('ID')
      this.$router.go()
    },
  },
  created: function () {
    const token = localStorage.getItem('Token')
    if (token != null) {
      this.isLogin = true
    }
  }
}
</script>

<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */

/* #navbar {
  font-family: 'Noto Sans KR', sans-serif;
} */

</style>
