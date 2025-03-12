<!-- templates/logs.html -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Action</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="log in logs" :key="log.id">
          <td>{{ log.id }}</td>
          <td>{{ log.action }}</td>
          <td>{{ log.timestamp }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      logs: [],
    };
  },
  async created() {
    await this.fetchLogs();
  },
  methods: {
    async fetchLogs() {
      try {
        const response = await this.$axios.get("/api/logs/operations");
        this.logs = response.data;
      } catch (error) {
        console.error("Failed to fetch logs", error);
      }
    },
  },
};
</script>