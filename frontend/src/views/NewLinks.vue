<template>
  <div class="new-link-form">
    <h2>Create New Link</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input id="name" v-model="form.name" type="text" required />
      </div>

      <div class="form-group">
        <label for="url">URL:</label>
        <input id="url" v-model="form.url" type="url" placeholder="https://example.com" required />
      </div>

      <button type="submit" class="button">Create Link</button>
    </form>

    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        url: ''
      },
      message: ''
    }
  },
  methods: {
    async submitForm() {
      try {
        const res = await fetch('http://127.0.0.1:8000/link/create/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        });
        if (!res.ok) {
          const errorData = await res.json();
          this.message = `Error: ${errorData.detail || res.statusText}`;
        } else {
          this.message = '🔥 Link created successfully!';
          this.form.name = '';
          this.form.url = '';
          this.$router.push('/list');
        }
      } catch (err) {
        console.error(err);
        this.message = 'Network or server error.';
      }
    }
  }
}
</script>

<style>
.new-link-form {
  width: 400px;
  margin: 30px auto;
  font-family: Arial, sans-serif;
}
.form-group {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
}
input {
  width: 100%;
  padding: 7px;
  box-sizing: border-box;
}
.button {
  background-color: #2ecc71;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.message {
  margin-top: 15px;
  color: green;
}
</style>
