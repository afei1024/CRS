<!-- templates/support.html -->
<template>
  <div>
    <h2>Support Status</h2>
    <p>{{ supportStatus.status }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      supportStatus: {},
    };
  },
  async created() {
    await this.fetchSupportStatus();
  },
  methods: {
    async fetchSupportStatus() {
      try {
        const response = await this.$axios.get("/api/support/status");
        this.supportStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch support status", error);
      }
    },
  },
};
</script>