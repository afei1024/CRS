<!-- templates/testing.html -->
<template>
  <div>
    <h2>Testing Endpoint</h2>
    <button @click="testEndpoint">Test Endpoint</button>
    <p>{{ testMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      testMessage: "",
    };
  },
  methods: {
    async testEndpoint() {
      try {
        const response = await this.$axios.get("/api/testing/test");
        this.testMessage = response.data.message;
      } catch (error) {
        console.error("Failed to test endpoint", error);
      }
    },
  },
};
</script>