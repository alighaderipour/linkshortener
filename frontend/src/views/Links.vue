<template>
  <div class="container">
    <h2>Links List</h2>

    <router-link to="/link/create" class="button">Create New Links</router-link>
    <ul>
      <li v-for="link in links" :key="link.id" class="link-item">
        <span class="name">{{ link.name }}</span>
        -

        <a :href="link.url" class="slug" @click.prevent="handleClick(link)">
          {{ link.slug }}
        </a>
        -
        <span class="clicks">{{ link.clicks }} clicks</span>
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
    fetch('http://127.0.0.1:8000/list')
      .then(res => res.json())
      .then(data => { this.links = data })
  },
  methods:{
    handleClick(link) {
      fetch(`http://127.0.0.1:8000/list/${link.slug}/`)
        .then(() => {
          // optional: update click count locally
          link.clicks += 1
          // then open the link
          window.open(link.url, '_blank')
        })
        .catch(err => console.error("Failed to track click", err))
    }

  }
}
</script>

<style>
.container {
  width: 600px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

h2 {
  text-align: center;
  color: #333;
}

ul {
  list-style: none;
  padding: 0;
}

.link-item {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.name {
  font-weight: bold;
}

.slug {
  color: blue;
  text-decoration: none;
}

.slug:hover {
  text-decoration: underline;
}

.clicks {
  color: #666;
  font-size: 0.9em;
}
.button{
color: green;
}
</style>
