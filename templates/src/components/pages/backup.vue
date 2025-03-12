<!-- templates/backup.html -->
<template>
  <div>
    <h2>Backup Status</h2>
    <p>{{ backupStatus.status }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backupStatus: {},
    };
  },
  async created() {
    await this.fetchBackupStatus();
  },
  methods: {
    async fetchBackupStatus() {
      try {
        const response = await this.$axios.get("/api/backup/status");
        this.backupStatus = response.data;
      } catch (error) {
        console.error("Failed to fetch backup status", error);
      }
    },
  },
};
</script>