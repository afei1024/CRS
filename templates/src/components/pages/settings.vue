<!-- templates/settings.html -->
<template>
  <div>
    <h2>Repair Types</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="repairType in repairTypes" :key="repairType.id">
          <td>{{ repairType.id }}</td>
          <td>{{ repairType.name }}</td>
        </tr>
      </tbody>
    </table>
    <form @submit.prevent="addRepairType">
      <input v-model="newRepairType" type="text" placeholder="New Repair Type" required />
      <button type="submit">Add Repair Type</button>
    </form>

    <h2>Users</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Role</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.role }}</td>
        </tr>
      </tbody>
    </table>
    <form @submit.prevent="addUser">
      <input v-model="newUsername" type="text" placeholder="Username" required />
      <input v-model="newRole" type="text" placeholder="Role" required />
      <button type="submit">Add User</button>
    </form>

    <h2>Roles</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="role in roles" :key="role.id">
          <td>{{ role.id }}</td>
          <td>{{ role.name }}</td>
        </tr>
      </tbody>
    </table>
    <form @submit.prevent="addRole">
      <input v-model="newRoleName" type="text" placeholder="New Role" required />
      <button type="submit">Add Role</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      repairTypes: [],
      newRepairType: "",
      users: [],
      newUsername: "",
      newRole: "",
      roles: [],
      newRoleName: "",
    };
  },
  async created() {
    await this.fetchRepairTypes();
    await this.fetchUsers();
    await this.fetchRoles();
  },
  methods: {
    async fetchRepairTypes() {
      try {
        const response = await this.$axios.get("/api/settings/repair-types");
        this.repairTypes = response.data;
      } catch (error) {
        console.error("Failed to fetch repair types", error);
      }
    },
    async addRepairType() {
      try {
        await this.$axios.post("/api/settings/repair-types", { name: this.newRepairType });
        this.newRepairType = "";
        await this.fetchRepairTypes();
      } catch (error) {
        console.error("Failed to add repair type", error);
      }
    },
    async fetchUsers() {
      try {
        const response = await this.$axios.get("/api/settings/users");
        this.users = response.data;
      } catch (error) {
        console.error("Failed to fetch users", error);
      }
    },
    async addUser() {
      try {
        await this.$axios.post("/api/settings/users", { username: this.newUsername, role: this.newRole });
        this.newUsername = "";
        this.newRole = "";
        await this.fetchUsers();
      } catch (error) {
        console.error("Failed to add user", error);
      }
    },
    async fetchRoles() {
      try {
        const response = await this.$axios.get("/api/settings/roles");
        this.roles = response.data;
      } catch (error) {
        console.error("Failed to fetch roles", error);
      }
    },
    async addRole() {
      try {
        await this.$axios.post("/api/settings/roles", { name: this.newRoleName });
        this.newRoleName = "";
        await this.fetchRoles();
      } catch (error) {
        console.error("Failed to add role", error);
      }
    },
  },
};
</script>