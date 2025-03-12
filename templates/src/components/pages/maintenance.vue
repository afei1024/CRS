<!-- templates/maintenance.html -->
<template>
  <div>
    <h2>Maintenance Status</h2>
    <p>{{ maintenanceStatus.status }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      maintenanceStatus: {},
    };
  },
  async created() {
    await this.fetchMaintenanceStatus();
  },
  methods: {
    async fetchMaintenanceStatus() {
      try {
        const response = await this.$axios.get("/api/maintenance/status");
        this.maintenanceStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch maintenance status", error);
      }
    },
  },
};
</script>