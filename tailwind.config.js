/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'dark': '#3C3C3C',
        'lime': '#B1F20E',
        'custom-blue': '#30C392',
        'custom-white': {
          DEFAULT: '#FAFAFA',
          2: '#D9D9D9'
        }
      },
      fontFamily: {
        'LeagueSpantan': ['League Spartan', 'sans-serif']
      },
      animation: {
        'loop-scroll': 'loop-scroll 50s linear infinite',
      },
      keyframes: {
      'loop-scroll': {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

