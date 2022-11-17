<template>
  <div>
    <h1>Foods</h1>
    <hr/>
    <DummyList/>
    <DummyForm/>
  </div>
</template>

<script>
import DummyList from '@/components/foods/DummyList'
import DummyForm from '@/components/foods/DummyForm'

export default {
  name: 'FoodsView',
  components: {
    DummyList,
    DummyForm
  }
}
</script>

<style>
</style>