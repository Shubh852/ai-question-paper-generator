/** @type {import('next').NextConfig} */
const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

const nextConfig = {
  reactStrictMode: false,
  cleanDistDir: false,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${backendUrl}/api/:path*`,
      },
      {
        source: '/diagrams/:path*',
        destination: `${backendUrl}/diagrams/:path*`,
      },
      {
        source: '/logos/:path*',
        destination: `${backendUrl}/logos/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
