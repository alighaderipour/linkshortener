<template>
  <div>
    <h2>Links List</h2>
    <ul>
      <li v-for="link in links" :key="link.id">
        {{ link.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return { links: [] }
  },
  mounted() {
    fetch('http://127.0.0.1:8000/links/list')
      .then(res => res.json())
      .then(data => { this.links = data })
  }
}
</script>
