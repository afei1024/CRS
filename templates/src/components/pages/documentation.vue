<!-- templates/documentation.html -->
<template>
  <div>
    <h2>Documentation</h2>
    <p>{{ documentationMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      documentationMessage: "",
    };
  },
  async created() {
    await this.fetchDocumentation();
  },
  methods: {
    async fetchDocumentation() {
      try {
        const response = await this.$axios.get("/api/documentation/docs");
        this.documentationMessage = response.data.message;
      } catch (error) {
        console.error("Failed to fetch documentation", error);
      }
    },
  },
};
</script>