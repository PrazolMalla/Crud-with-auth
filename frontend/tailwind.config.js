/** @type {import('tailwindcss').Config} */
export default {
  mode: 'jit',
  purge: {
    enabled: true
  },
  content: ['./public/**/*.html', './src/**/*.vue', './src/main.js'],
  theme: {
    extend: {
      colors: {
        'custom-border': '#709BFF',
        'purple-color': '#c09afe',
        'blue-color': '#88dcff'
      },
      fontFamily: {
        helvetica: ['helvetica']
      }
    }
  },
  plugins: []
}
