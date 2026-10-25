/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,vue}'],
  theme: {
    extend: {
      colors: {
        neutral: {
          50: '#f8f5f0',
          100: '#f5f1ea',
          200: '#e0e2e6',
          300: '#bfc6d0',
          400: '#96a0b0',
          500: '#7d8798',
          600: '#566171',
          700: '#353e4d',
          800: '#252b36',
          900: '#181d26',
          950: '#0e1118',
        },
        hoa: {
          0: '#fff0eb',
          100: '#ffe6df',
          200: '#ffd7ce',
          300: '#ffc5b9',
          400: '#ffb0a1',
          500: '#ff9987',
          600: '#ff826c',
          700: '#ff6d58',
          800: '#ff5a4e',
          900: '#f65348',
          1000: '#ef4b42',
          1100: '#e5443e',
          1200: '#cf3c39',
          1300: '#b63132',
          1400: '#a3292e',
          1500: '#8d252a',
        },
      },
    },
  },
  darkMode: 'class',
}
