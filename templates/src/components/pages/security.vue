<!-- templates/security.html -->
<template>
  <div>
    <h2>Security Status</h2>
    <p>{{ securityStatus.status }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      securityStatus: {},
    };
  },
  async created() {
    await this.fetchSecurityStatus();
  },
  methods: {
    async fetchSecurityStatus() {
      try {
        const response = await this.$axios.get("/api/security/status");
        this.securityStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch security status", error);
      }
    },
  },
};
</script>