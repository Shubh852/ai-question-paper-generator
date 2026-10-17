import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AI Question Paper Generator | CBSE & Competitive Exam System',
  description: 'Autonomous AI question paper and marking scheme generator compiled via Typst for CBSE, IIT-JEE, and NEET.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
      </head>
      <body className="min-h-screen bg-slate-50 text-slate-900 antialiased selection:bg-brand-500 selection:text-white">
        {children}
      </body>
    </html>
  )
}
