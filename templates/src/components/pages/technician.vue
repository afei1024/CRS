<!-- templates/technician.html -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in repairTasks" :key="task.order_id">
          <td>{{ task.order_id }}</td>
          <td>{{ task.description }}</td>
          <td>{{ task.status }}</td>
          <td>
            <button @click="updateStatus(task.order_id)">Update Status</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      repairTasks: [],
    };
  },
  async created() {
    await this.fetchRepairTasks();
  },
  methods: {
    async fetchRepairTasks() {
      try {
        const response = await this.$axios.get("/api/repair/tasks", {
          params: { technician: "tech1" },
        });
        this.repairTasks = response.data;
      } catch (error) {
        console.error("Failed to fetch repair tasks", error);
      }
    },
    async updateStatus(orderId) {
      const status = prompt("Enter new status");
      if (status) {
        try {
          await this.$axios.post("/api/repair/update-task-status", { order_id: orderId, status });
          await this.fetchRepairTasks();
        } catch (error) {
          console.error("Failed to update task status", error);
        }
      }
    },
  },
};
</script>