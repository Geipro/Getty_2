<template>
  <div>
    <h2>전세자금대출</h2>
  </div>
</template>

<script>

export default {
  name: 'RentHouse',
  props: {
    msg: String
  },
  data: function () {
    return {
      isLogin: false,
    }
  }
}
</script>

<style scoped>
.ulist {
   list-style: none;
}
ul {
  padding: 0;
}
li {
  display: inline-block;
}
.nav-margin{
    padding-right: 6rem;
    padding-left: 6rem;
    /* padding-top: 1rem; */
    color: white;
}
.title-style {
  color: white;
  font-size: 2.5rem;
  background-color: #1f2325;
  /* background-color: #2c3e50; */
}

</style>
