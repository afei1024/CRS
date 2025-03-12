<!-- templates/deployment.html -->
<template>
  <div>
    <h2>Deployment Status</h2>
    <p>Status: {{ deploymentStatus.status }}</p>
    <p>Version: {{ deploymentStatus.version }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      deploymentStatus: {},
    };
  },
  async created() {
    await this.fetchDeploymentStatus();
  },
  methods: {
    async fetchDeploymentStatus() {
      try {
        const response = await this.$axios.get("/api/deployment/status");
        this.deploymentStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch deployment status", error);
      }
    },
  },
};
</script>