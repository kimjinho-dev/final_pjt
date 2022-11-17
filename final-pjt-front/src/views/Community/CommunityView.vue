<template>
  <div>
    <h1>Community</h1>
    <hr/>
    <DummyList/>
    <DummyForm/>
  </div>
</template>

<script>
// import PageHeader from '@/components/community/PageHeader'
import DummyList from '@/components/community/DummyList'
import DummyForm from '@/components/community/DummyForm'

export default {
  name: 'CommunityView',
  components: {
    DummyList,
    DummyForm,
  }
}
</script>