// craco.config.js - Custom React App Configuration for LuminAI
// Extends Create React App without ejecting

const path = require('path');

module.exports = {
  webpack: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/components'),
      '@assets': path.resolve(__dirname, 'src/assets'),
      '@utils': path.resolve(__dirname, 'src/utils'),
      '@styles': path.resolve(__dirname, 'src/styles'),
    },
    configure: (webpackConfig, { env, paths }) => {
      // Optimize bundle for LuminAI cosmic performance
      if (env === 'production') {
        // Split chunks for better caching
        webpackConfig.optimization.splitChunks = {
          chunks: 'all',
          cacheGroups: {
            default: {
              minChunks: 2,
              priority: -20,
              reuseExistingChunk: true
            },
            vendor: {
              test: /[\\/]node_modules[\\/]/,
              name: 'vendors',
              priority: -10,
              chunks: 'all'
            },
            lottie: {
              test: /[\\/]node_modules[\\/]lottie-react[\\/]/,
              name: 'lottie',
              priority: 10,
              chunks: 'all'
            },
            xstate: {
              test: /[\\/]node_modules[\\/]@?xstate[\\/]/,
              name: 'xstate',
              priority: 10,
              chunks: 'all'
            },
            three: {
              test: /[\\/]node_modules[\\/]three[\\/]/,
              name: 'three',
              priority: 10,
              chunks: 'all'
            }
          }
        };

        // Optimize assets for cosmic efficiency
        webpackConfig.module.rules.push({
          test: /\.(json)$/,
          include: path.resolve(__dirname, 'public/animations'),
          type: 'asset/resource',
          generator: {
            filename: 'static/animations/[name].[contenthash][ext]'
          }
        });
      }

      return webpackConfig;
    }
  },
  style: {
    postcss: {
      plugins: [
        require('autoprefixer'),
        require('cssnano')({
          preset: 'default'
        })
      ]
    }
  },
  devServer: {
    port: 3000,
    hot: true,
    compress: true,
    historyApiFallback: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
    }
  }
};