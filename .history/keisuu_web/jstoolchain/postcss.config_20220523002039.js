module.exports = {
  plugins: [
      require('tailwindcss'),
      require('autoprefixer')
  ],
  purge: {
    enabled: true,
    content: ['~/keisuu_web/keisuu_web/templates/**/*.html'],
    content: ['~/keisuu_web/home/templates/**/*.html'],
  },
}