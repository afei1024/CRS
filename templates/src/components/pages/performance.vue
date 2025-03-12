<!-- templates/performance.html -->
<template>
  <div>
    <h2>Performance Status</h2>
    <p>{{ performanceStatus.status }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      performanceStatus: {},
    };
  },
  async created() {
    await this.fetchPerformanceStatus();
  },
  methods: {
    async fetchPerformanceStatus() {
      try {
        const response = await this.$axios.get("/api/performance/status");
        this.performanceStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch performance status", error);
      }
    },
  },
};
</script>