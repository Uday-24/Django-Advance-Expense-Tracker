module.exports = {
  content: [
    './mysite/myapp/templates/**/*.html', // Adjusted to target all HTML files in templates
    './mysite/myapp/static/myapp/**/*.css', // Including your CSS files with Tailwind directives
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
