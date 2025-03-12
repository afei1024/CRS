<!-- templates/management.html -->
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
        <tr v-for="order in repairOrders" :key="order.order_id">
          <td>{{ order.order_id }}</td>
          <td>{{ order.description }}</td>
          <td>{{ order.status }}</td>
          <td>
            <button @click="viewDetails(order.order_id)">View Details</button>
            <button @click="assignTechnician(order.order_id)">Assign Technician</button>
            <button @click="updateStatus(order.order_id)">Update Status</button>
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
      repairOrders: [],
    };
  },
  async created() {
    await this.fetchRepairOrders();
  },
  methods: {
    async fetchRepairOrders() {
      try {
        const response = await this.$axios.get("/api/repair/list");
        this.repairOrders = response.data;
      } catch (error) {
        console.error("Failed to fetch repair orders", error);
      }
    },
    async viewDetails(orderId) {
      try {
        const response = await this.$axios.get(`/api/repair/detail/${orderId}`);
        alert(`Details: ${JSON.stringify(response.data)}`);
      } catch (error) {
        console.error("Failed to fetch order details", error);
      }
    },
    async assignTechnician(orderId) {
      const technician = prompt("Enter technician name");
      if (technician) {
        try {
          await this.$axios.post("/api/repair/assign", { order_id: orderId, technician });
          await this.fetchRepairOrders();
        } catch (error) {
          console.error("Failed to assign technician", error);
        }
      }
    },
    async updateStatus(orderId) {
      const status = prompt("Enter new status");
      if (status) {
        try {
          await this.$axios.post("/api/repair/update-status", { order_id: orderId, status });
          await this.fetchRepairOrders();
        } catch (error) {
          console.error("Failed to update status", error);
        }
      }
    },
  },
};
</script>