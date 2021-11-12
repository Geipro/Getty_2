<template>
  <div>
    <Navbar/>
    <ProductGroup />
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import ProductGroup from '@/components/FinanceProduct/ProductGroup.vue'

export default {
  name: 'Product',
  components: {
    Navbar,
    ProductGroup,
  }
}
</script>

<style>

</style>
