import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        about_progress1: resolve(__dirname, 'about_progress1.html'),
        about_progress2: resolve(__dirname, 'about_progress2.html'),
        contact: resolve(__dirname, 'contact.html'),
        faq: resolve(__dirname, 'faq.html'),
        reviews: resolve(__dirname, 'reviews.html'),
        anketa: resolve(__dirname, 'anketa.html')
      }
    }
  },
  plugins: [
    {
      name: 'clean-urls',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          // Redirect visible .html to clean URLs
          if (req.url.endsWith('.html') && req.url !== '/index.html') {
            res.writeHead(301, { Location: req.url.replace(/\.html$/, '') });
            return res.end();
          }
          if (req.url === '/index.html') {
            res.writeHead(301, { Location: '/' });
            return res.end();
          }

          // Add default extension for clean URLs (e.g. /about -> /about.html)
          // Skip if it asks for an asset or explicit extension
          if (!req.url.includes('.') && !req.url.endsWith('/')) {
            req.url += '.html';
          } else if (req.url.endsWith('/')) {
            req.url += 'index.html';
          }
          next();
        });
      }
    }
  ]
});
