export default {
    // template: `
    // <button @click="handle_click">
    //   <strong>{{title}}: {{value}}</strong>
    // </button>`,
    template: `
    <div class="left__sidebar">
  <div class="sidebar">
    <h1>Left sidebar</h1>
  </div>
  <div class="divider"></div>
</div>

`,
    data() {
      return {
        value: 0,
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