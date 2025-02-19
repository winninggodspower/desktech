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
        'custom-dark': '#202020',
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
        "float": "float 2s ease-in-out infinite"
      },
      keyframes: {
        'loop-scroll': {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        'float': {
          "0%": { transform: " translateY(0px)" },
          "50%": { transform: "translateY(-10px)" },
          "100%": { transform: "translateY(0px)" }
        }
      },
      backgroundImage: {
        'custom-gradient': 'linear-gradient(202.61deg, #B1F20E -39.15%, rgba(48,195,146,0.9) 65.17%)'
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

