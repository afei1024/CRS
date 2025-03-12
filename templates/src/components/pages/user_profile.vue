<!-- templates/user_profile.html -->
<template>
  <div>
    <form @submit.prevent="updateProfile">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="phone" type="tel" placeholder="Phone" required />
      <button type="submit">Update Profile</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      phone: "",
    };
  },
  async created() {
    await this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await this.$axios.get("/api/user/profile", {
          params: { username: "johndoe" },
        });
        this.email = response.data.email;
        this.phone = response.data.phone;
      } catch (error) {
        console.error("Failed to fetch user profile", error);
      }
    },
    async updateProfile() {
      try {
        await this.$axios.post("/api/user/update-profile", {
          username: "johndoe",
          email: this.email,
          phone: this.phone,
        });
        alert("Profile updated successfully");
      } catch (error) {
        console.error("Failed to update profile", error);
      }
    },
  },
};
</script>