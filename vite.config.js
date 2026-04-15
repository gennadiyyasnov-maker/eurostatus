import { defineConfig } from 'vite';
import { resolve } from 'path';

import fs from 'fs';

// Автоматически собираем все .html файлы в корне как точки входа
const htmlFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.html') && !file.startsWith('temp_') && !file.startsWith('recovered_') && file !== 'template.html');
const input = {};
htmlFiles.forEach(file => {
  const name = file.replace('.html', '');
  input[name] = resolve(__dirname, file);
});

export default defineConfig({
  build: {
    rollupOptions: {
      input: input
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
