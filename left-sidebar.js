export default {
  template: `
  <button>
  <strong>{{title}}: 0</strong>
</button>
    `,
  data() {
    return {
      // width: '100px',
    };
  },
  methods: {
    handle_click() {
      this.value += 1;
      this.$emit("change", this.value);
    },
    reset() {
      this.value = 0;
    },
  },
  props: {
    title: String,
  },
};
