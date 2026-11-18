import path from "node:path";
import { fileURLToPath } from "node:url";

import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Un seul .env, à la racine. Seules les variables VITE_ arrivent dans le navigateur.
const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

export default defineConfig({
  envDir: projectRoot,
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
    strictPort: true,
    watch: process.env.CHOKIDAR_USEPOLLING === "true" ? { usePolling: true } : undefined,
    proxy: {
      "/api": {
        target: process.env.PROXY_TARGET || "http://127.0.0.1:8001",
        changeOrigin: true,
      },
    },
  },
  preview: {
    host: true,
    port: 4173,
    strictPort: true,
  },
});
