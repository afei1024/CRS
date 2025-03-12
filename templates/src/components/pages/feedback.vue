<!-- templates/feedback.html -->
<template>
  <div>
    <form @submit.prevent="submitFeedback">
      <textarea v-model="message" placeholder="Your feedback" required></textarea>
      <input v-model="user" type="text" placeholder="Your username" required />
      <button type="submit">Submit Feedback</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Message</th>
          <th>User</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="feedback in feedbackList" :key="feedback.id">
          <td>{{ feedback.id }}</td>
          <td>{{ feedback.message }}</td>
          <td>{{ feedback.user }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      user: "",
      feedbackList: [],
    };
  },
  async created() {
    await this.fetchFeedback();
  },
  methods: {
    async fetchFeedback() {
      try {
        const response = await this.$axios.get("/api/feedback/list");
        this.feedbackList = response.data;
      } catch (error) {
        console.error("Failed to fetch feedback", error);
      }
    },
    async submitFeedback() {
      try {
        await this.$axios.post("/api/feedback/submit", {
          message: this.message,
          user: this.user,
        });
        this.message = "";
        this.user = "";
        await this.fetchFeedback();
      } catch (error) {
        console.error("Failed to submit feedback", error);
      }
    },
  },
};
</script>