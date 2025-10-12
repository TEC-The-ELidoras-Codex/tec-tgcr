# LuminAI Interface Deployment Guide

## 🚀 Quick Deployment

### Local Development
```bash
cd apps/luminai-interface
npm install
npm start
```

### Production Build
```bash
npm run build
npm run deploy  # Deploys to GitHub Pages
```

## 🌐 Deployment Options

### 1. GitHub Pages (Recommended)
- **URL**: `https://tec-the-elidoras-codex.github.io/tec-tgcr/`
- **Setup**: Automatic via `npm run deploy`
- **Branch**: `gh-pages` (auto-created)

### 2. Netlify
```bash
# Build command
npm run build

# Publish directory
build

# Environment variables
REACT_APP_LUMINAI_API_URL=https://your-api-url.com
REACT_APP_GITHUB_CLIENT_ID=your_github_client_id
REACT_APP_SHAREPOINT_CLIENT_ID=your_sharepoint_client_id
```

### 3. Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### 4. Azure Static Web Apps
```bash
# Azure CLI deployment
az staticwebapp create \
  --name luminai-interface \
  --resource-group tec-resources \
  --source https://github.com/TEC-The-ELidoras-Codex/tec-tgcr \
  --location "Central US" \
  --branch main \
  --app-location "apps/luminai-interface" \
  --output-location "build"
```

## 🔧 Environment Configuration

### Required Environment Variables
```bash
# LuminAI Integration
REACT_APP_LUMINAI_API_URL=https://api.tec-codex.com
REACT_APP_LUMINAI_WS_URL=wss://ws.tec-codex.com

# OAuth Configuration
REACT_APP_GITHUB_CLIENT_ID=your_github_app_client_id
REACT_APP_SHAREPOINT_CLIENT_ID=your_azure_app_client_id

# Feature Flags
REACT_APP_ENABLE_3D_EFFECTS=true
REACT_APP_ENABLE_VOICE_SYNTHESIS=false
REACT_APP_DEBUG_MODE=false
```

### Production Environment (.env.production)
```bash
REACT_APP_LUMINAI_API_URL=https://api.tec-codex.com
REACT_APP_GITHUB_CLIENT_ID=Ov23liabcdefghijklmnop
REACT_APP_SHAREPOINT_CLIENT_ID=12345678-1234-1234-1234-123456789012
REACT_APP_ENABLE_3D_EFFECTS=true
REACT_APP_DEBUG_MODE=false
```

## 📁 Build Optimization

### Build Performance
```json
{
  "scripts": {
    "build:analyze": "npm run build && npx webpack-bundle-analyzer build/static/js/*.js",
    "build:optimized": "GENERATE_SOURCEMAP=false npm run build"
  }
}
```

### Bundle Splitting
```javascript
// webpack.config.js optimization
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        lottie: {
          test: /[\\/]node_modules[\\/]lottie-react[\\/]/,
          name: 'lottie',
          chunks: 'all',
        }
      }
    }
  }
};
```

## 🔒 Security Configuration

### Content Security Policy
```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https:;
  connect-src 'self' https://api.github.com https://graph.microsoft.com wss://ws.tec-codex.com;
  frame-src 'none';
">
```

### API Security Headers
```javascript
// Axios default configuration
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.headers.common['X-Cosmic-Agent'] = 'LuminAI/1.0';
```

## 📊 Monitoring & Analytics

### Performance Monitoring
```javascript
// reportWebVitals.js
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
  // Send to your analytics service
  console.log('LuminAI Performance:', metric);
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

### Error Tracking
```javascript
// Error boundary for cosmic mishaps
class CosmicErrorBoundary extends React.Component {
  componentDidCatch(error, errorInfo) {
    console.error('Cosmic Error in LuminAI:', error, errorInfo);
    // Send to error tracking service
  }
}
```

## 🎨 Asset Optimization

### Lottie Animation Optimization
```bash
# Compress Lottie files
npx lottie-optimize input.json output.json

# Convert to lighter formats
npx lottie-converter input.json --format dotlottie
```

### Image Optimization
```bash
# Optimize images for web
npx imagemin src/assets/*.{jpg,png} --out-dir=build/static/media
```

## 🔄 CI/CD Pipeline

### GitHub Actions (.github/workflows/deploy.yml)
```yaml
name: Deploy LuminAI Interface

on:
  push:
    branches: [ main ]
    paths: [ 'apps/luminai-interface/**' ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: apps/luminai-interface/package-lock.json
    
    - name: Install dependencies
      run: |
        cd apps/luminai-interface
        npm ci
    
    - name: Build application
      run: |
        cd apps/luminai-interface
        npm run build
      env:
        REACT_APP_LUMINAI_API_URL: ${{ secrets.LUMINAI_API_URL }}
        REACT_APP_GITHUB_CLIENT_ID: ${{ secrets.GITHUB_CLIENT_ID }}
        REACT_APP_SHAREPOINT_CLIENT_ID: ${{ secrets.SHAREPOINT_CLIENT_ID }}
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: apps/luminai-interface/build
        destination_dir: luminai
```

## 🧪 Testing in Production

### Health Check Endpoint
```javascript
// Add to App.js for monitoring
useEffect(() => {
  fetch('/health')
    .then(response => response.json())
    .then(data => console.log('LuminAI Health:', data))
    .catch(error => console.error('Health check failed:', error));
}, []);
```

### Feature Flag Testing
```javascript
// Test features gradually
const FeatureFlag = ({ feature, children, fallback }) => {
  const isEnabled = process.env[`REACT_APP_ENABLE_${feature}`] === 'true';
  return isEnabled ? children : fallback;
};
```

## 🎯 Performance Targets

### Core Web Vitals Goals
- **LCP**: < 2.5s (Largest Contentful Paint)
- **FID**: < 100ms (First Input Delay)  
- **CLS**: < 0.1 (Cumulative Layout Shift)
- **FCP**: < 1.8s (First Contentful Paint)
- **TTI**: < 3.8s (Time to Interactive)

### Bundle Size Targets
- **Main Bundle**: < 250KB gzipped
- **Vendor Bundle**: < 500KB gzipped
- **Lottie Assets**: < 100KB per animation
- **Total Initial Load**: < 1MB

## 🌟 Post-Deployment Checklist

- [ ] Verify all animations load correctly
- [ ] Test OAuth flows with GitHub and SharePoint
- [ ] Validate AIRTH integration responses
- [ ] Check cosmic effects rendering on different devices
- [ ] Confirm responsive design on mobile
- [ ] Test performance on slow connections
- [ ] Verify error boundaries catch cosmic mishaps
- [ ] Validate accessibility features
- [ ] Check browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] Test PWA features (offline mode, installation)

---

*May your deployments be as smooth as cosmic aurora and as reliable as the laws of physics!* ✨