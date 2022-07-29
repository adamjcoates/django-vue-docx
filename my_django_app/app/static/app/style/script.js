const app = Vue.createApp({
  data() {
    return {
      configuration : {}
    }
  },

  methods: {
    run(e) {
      //test data
      const config = {
        pageLimit: 9,
        marginSize: 1,
      };

      const fileInputField = document.getElementById("document");

      const formData = new FormData();
      formData.append("config", JSON.stringify(config, null, 2));
      formData.append("file", fileInputField.files[0]);

      fetch("http://localhost:8000/format/", {
        method: "POST",
        body: formData
      })
      .then(response => response.blob())
      .then(blob => {
        var a = document.createElement("a");
        a.href = window.URL.createObjectURL(blob);
        a.download = "word.docx";
        document.body.appendChild(a)
        a.click();
        a.remove();
      })
      .catch(error => {
        console.error("Error:", error);
      })
    }
  },
});

app.mount("#upload");
