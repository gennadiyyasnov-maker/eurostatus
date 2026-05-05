import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const distDir = path.join(__dirname, 'dist');

if (fs.existsSync(distDir)) {
  const files = fs.readdirSync(distDir);
  for (const file of files) {
    if (file.endsWith('.html') && file !== 'index.html' && !file.startsWith('yandex_') && !file.startsWith('google')) {
      const name = file.replace('.html', '');
      const folder = path.join(distDir, name);
      if (!fs.existsSync(folder)) {
        fs.mkdirSync(folder);
      }
      fs.renameSync(path.join(distDir, file), path.join(folder, 'index.html'));
      console.log(`Moved ${file} to ${name}/index.html for clean URLs`);
    }
  }
} else {
  console.log('dist directory not found!');
}
