<!-- templates/issue_report.html -->
<template>
  <div>
    <form @submit.prevent="submitRepair">
      <textarea v-model="description" placeholder="Describe the issue" required></textarea>
      <select v-model="repairType">
        <option value="plumbing">Plumbing</option>
        <option value="electrical">Electrical</option>
        <option value="carpentry">Carpentry</option>
      </select>
      <input type="file" multiple @change="handleFileUpload" />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      description: "",
      repairType: "",
      images: [],
    };
  },
  methods: {
    handleFileUpload(event) {
      this.images = event.target.files;
    },
    async submitRepair() {
      const formData = new FormData();
      formData.append("description", this.description);
      formData.append("repair_type", this.repairType);
      for (let i = 0; i < this.images.length; i++) {
        formData.append("images", this.images[i]);
      }
      try {
        const response = await this.$axios.post("/api/repair/submit", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        alert(`Repair order submitted with ID: ${response.data.order_id}`);
      } catch (error) {
        console.error("Failed to submit repair order", error);
      }
    },
  },
};
</script>