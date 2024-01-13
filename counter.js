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
        bg-red-600 cursor-ew-resize	" style="width:2px;"
        @mousedown="mousedown"
        >
      </div>
    `,
  style: {},
  methods: {
    mousedown() {
      this.isDragging = true;
      console.log("enter mouse down");
      document.addEventListener("mousemove", this.drag);
      document.addEventListener("mouseup", this.stopDrag);
    },
    drag(e) {
      if (this.isDragging) {
        console.log("enter mouse drag and in if");
        const newWidth = e.clientX;
        this.sidebarWidth = newWidth;
        this.$emit("change", newWidth);
      }
    },
    stopDrag() {
      this.isDragging = false;
      console.log("enter stopDrag");
      document.removeEventListener("mousemove", this.drag);
      document.removeEventListener("mouseup", this.stopDrag);
    },
  },
  props: {
    title: String,
  },
};
