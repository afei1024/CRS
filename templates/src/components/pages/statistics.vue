<!-- templates/statistics.html -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Repair Type</th>
          <th>Count</th>
          <th>Average Duration (hours)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stat in repairStatistics" :key="stat.repair_type">
          <td>{{ stat.repair_type }}</td>
          <td>{{ stat.count }}</td>
          <td>{{ stat.average_duration }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      repairStatistics: [],
    };
  },
  async created() {
    await this.fetchRepairStatistics();
  },
  methods: {
    async fetchRepairStatistics() {
      try {
        const response = await this.$axios.get("/api/repair/statistics");
        this.repairStatistics = response.data;
      } catch (error) {
        console.error("Failed to fetch repair statistics", error);
      }
    },
  },
};
</script>