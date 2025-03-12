<!-- templates/notification.html -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Message</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="notification in notifications" :key="notification.id">
          <td>{{ notification.message }}</td>
          <td>{{ notification.is_read ? 'Read' : 'Unread' }}</td>
          <td>
            <button @click="markAsRead(notification.id)">Mark as Read</button>
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
      notifications: [],
    };
  },
  async created() {
    await this.fetchNotifications();
  },
  methods: {
    async fetchNotifications() {
      try {
        const response = await this.$axios.get("/api/notification/list");
        this.notifications = response.data;
      } catch (error) {
        console.error("Failed to fetch notifications", error);
      }
    },
    async markAsRead(notificationId) {
      try {
        await this.$axios.post("/api/notification/mark-as-read", { notification_id: notificationId });
        await this.fetchNotifications();
      } catch (error) {
        console.error("Failed to mark notification as read", error);
      }
    },
  },
};
</script>