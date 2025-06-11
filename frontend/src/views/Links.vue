<template>
  <div class="links-container">
    <h2 class="title">Links List</h2>
    <ul class="links-list">
      <li v-for="link in links" :key="link.id" class="link-item">
        <div class="link-header">
          <span class="link-name">{{ link.name }}</span>
          <span class="link-clicks">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 16">
              <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
            </svg>
            {{ link.clicks }}
          </span>
        </div>
          <div class="link-body">
            <a :href="link.url" target="_blank" class="link-url">{{ link.url }}</a>
            <span class="link-slug">/{{ link.slug }}</span>
          </div>
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
    // Mock data for demonstration if the fetch fails
    const mockData = [
      { id: 1, name: 'Google Search', url: 'https://www.google.com', clicks: 1024, slug: 'google' },
      { id: 2, name: 'VueJS Documentation', url: 'https://vuejs.org', clicks: 876, slug: 'vue-docs' },
      { id: 3, name: 'Awesome Design Inspiration', url: 'https://dribbble.com', clicks: 1532, slug: 'design-insp' }
    ];

    fetch('http://127.0.0.1:8000/list')
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        this.links = data;
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        this.links = mockData; // Fallback to mock data
      });
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.links-container {
  max-width: 800px;
  margin: 40px auto;
  padding: 30px;
  font-family: 'Poppins', sans-serif;
  background-color: #f4f7f9;
}

.title {
  color: #2c3e50;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 30px;
  text-align: center;
}

.links-list {
  list-style: none;
  padding: 0;
}

.link-item {
  background: #ffffff;
  margin-bottom: 1rem;
  padding: 1.25rem 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  border-left: 5px solid #007bff;
}

.link-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  border-left-color: #0056b3;
}

.link-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.link-name {
  color: #34495e;
  font-size: 1.2rem;
  font-weight: 600;
}

.link-clicks {
  display: flex;
  align-items: center;
  background-color: #e9ecef;
  color: #495057;
  padding: 0.25rem 0.6rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

.link-clicks svg {
  margin-right: 0.4rem;
  color: #007bff;
}

.link-body {
  display: flex;
  flex-direction: column;
}

.link-url {
  color: #007bff;
  text-decoration: none;
  font-size: 0.9rem;
  margin-bottom: 0.25rem;
  word-break: break-all;
  transition: color 0.2s ease;
}

.link-url:hover {
  color: #0056b3;
  text-decoration: underline;
}

.link-slug {
  color: #6c757d;
  font-size: 0.85rem;
  font-style: italic;
}

@media (max-width: 768px) {
  .links-container {
    padding: 20px;
  }

  .title {
    font-size: 1.8rem;
  }

  .link-item {
    padding: 1rem;
  }

  .link-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .link-name {
    margin-bottom: 0.5rem;
  }
}
</style>