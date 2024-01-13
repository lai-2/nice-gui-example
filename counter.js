export default {
  // template: `
  // <button @click="handle_click">
  //   <strong>{{title}}: {{value}}</strong>
  //   <strong>{{title2}}</strong>

  // </button>`,
  template: `
      <div class="sidebar relative">
        <h1>Left sidebar </h1>
        <strong>{{title}}</strong>
      </div>
      <div class="divider absolute right-0 top-0 h-screen
        bg-red-600 cursor-col-resize" style="width:2px;"
        @mousedown="mousedown"
        @mouseup="mouseup"
        @mouseenter="mouseenter"
        @mousemove="mousemove"
        >
      </div>
    `,
  style: {},
  methods: {
    mousedown(e) {
      console.log(`mouse down ${e.x}`);
    },
    mouseup(e){
      console.log(`mouse up ${e.x}`);
    },

    mouseenter(e){
      console.log(`mouse enter ${e.x}`);
    },

    mouseenter(e){
      console.log(`mouse move ${e.x}`);
    },
    handle_click() {
      this.width += 1;
      this.$emit("change", this.width);
    },
    // reset() {
    //   this.width = 0;
    // },
  },
  props: {
    title: String,
  },
};
