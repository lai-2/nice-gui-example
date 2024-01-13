export default {
  template: `
    <label for="name">Enter your name:</label>
    <input
      type="text"
      id="name"
      v-model="name"
    />
    <button @click="submit">
      Submit
    </button>
  `,
  data() {
    return {
      name: "",
    };
  },
  methods: {
    submit() {
      this.$emit("change", this.name);
    },
    reset() {
      this.name = "";
    },
  },
  props: {
    title: String,
  },
};
