export default {
  template: `
    <div class="sidebar relative">
      <label for="name">Enter your name:</label>
      <input
        type="text"
        id="name"
        v-model="name"
      />
      <button @click="submit">
        Submit
      </button>
    </div>
    <div class="divider absolute right-0 top-0 h-screen
      bg-red-600 cursor-ew-resize	" style="width:2px;"
      @mousedown="mousedown"
      >
    </div>
  `,
  data() {
    return {
      name: "",
    };
  },
  methods: {
    mousedown() {
      this.isDragging = true;
      console.log("enter mouse down");
      document.addEventListener("mousemove", this.drag);
      document.addEventListener("mouseup", this.stopDrag);
    },
    drag(e) {
      if (this.isDragging) {
        // console.log("enter mouse drag and in if");
        this.$emit("change", ['resize', e.clientX]);
      }
    },
    stopDrag() {
      this.isDragging = false;
      // console.log("enter stopDrag");
      document.removeEventListener("mousemove", this.drag);
      document.removeEventListener("mouseup", this.stopDrag);
    },

    submit() {
      this.$emit("change", this.name);
    },
    reset() {
      this.name = "";
      this.$emit("change", "");
    },
  },
  props: {
    title: String,
  },
};
