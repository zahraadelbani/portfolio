module.exports = {
  darkMode: "class",   // ✅ REQUIRED
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/src/**/*.{html,js}",
    "./**/*.py"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0ea5a4",
        accent: "#7c3aed"
      }
    }
  },
  plugins: []
};
