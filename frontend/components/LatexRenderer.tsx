'use client';

import React from 'react';
import katex from 'katex';

interface LatexRendererProps {
  text: string;
  diagramUrl?: string;
  diagramCaption?: string;
  className?: string;
}

export default function LatexRenderer({
  text,
  diagramUrl,
  diagramCaption,
  className = '',
}: LatexRendererProps) {
  if (!text) return null;

  // Normalize image URL for browser loading (e.g. data/diagrams/foo.svg -> /diagrams/foo.svg)
  const normalizeImageUrl = (raw: string) => {
    let u = raw.trim();
    if (u.startsWith('data/diagrams/')) {
      return '/' + u.replace('data/diagrams/', 'diagrams/');
    }
    if (u.startsWith('data/logos/')) {
      return '/' + u.replace('data/logos/', 'logos/');
    }
    return u;
  };

  // Render markdown text parts, supporting embedded ![alt](url) diagrams
  const renderTextWithImages = (content: string, partIndex: number) => {
    const imgRegex = /!\[(.*?)\]\((.*?)\)/g;
    const segments: React.ReactNode[] = [];
    let lastIndex = 0;
    let match: RegExpExecArray | null;

    while ((match = imgRegex.exec(content)) !== null) {
      if (match.index > lastIndex) {
        segments.push(
          <span key={`txt-${partIndex}-${lastIndex}`} className="whitespace-pre-line leading-relaxed">
            {content.slice(lastIndex, match.index)}
          </span>
        );
      }
      const alt = match[1] || 'Diagram';
      const url = normalizeImageUrl(match[2]);
      segments.push(
        <figure key={`img-${partIndex}-${match.index}`} className="my-3 text-center">
          <img
            src={url}
            alt={alt}
            className="mx-auto max-h-56 rounded-md border border-slate-200 bg-white p-2 shadow-sm object-contain"
          />
          <figcaption className="block text-xs text-slate-500 mt-1 italic">
            Figure: {alt}
          </figcaption>
        </figure>
      );
      lastIndex = imgRegex.lastIndex;
    }

    if (lastIndex < content.length) {
      segments.push(
        <span key={`txt-${partIndex}-${lastIndex}`} className="whitespace-pre-line leading-relaxed">
          {content.slice(lastIndex)}
        </span>
      );
    }

    return segments.length > 0 ? segments : <span key={`txt-${partIndex}`}>{content}</span>;
  };

  // Split string by $$...$$ and $...$
  const renderFormattedText = (input: string) => {
    const regex = /(\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$)/g;
    const parts = input.split(regex);

    return parts.map((part, index) => {
      if (part.startsWith('$$') && part.endsWith('$$')) {
        const math = part.slice(2, -2).trim();
        try {
          const html = katex.renderToString(math, {
            displayMode: true,
            throwOnError: false,
          });
          return (
            <div
              key={index}
              className="my-3 overflow-x-auto py-1 text-center"
              dangerouslySetInnerHTML={{ __html: html }}
            />
          );
        } catch (e) {
          return <span key={index} className="font-mono text-red-500">{part}</span>;
        }
      } else if (part.startsWith('$') && part.endsWith('$')) {
        const math = part.slice(1, -1).trim();
        try {
          const html = katex.renderToString(math, {
            displayMode: false,
            throwOnError: false,
          });
          return (
            <span
              key={index}
              className="inline-block px-0.5"
              dangerouslySetInnerHTML={{ __html: html }}
            />
          );
        } catch (e) {
          return <span key={index} className="font-mono text-red-500">{part}</span>;
        }
      }

      // Normal text which might contain ![alt](url)
      return renderTextWithImages(part, index);
    });
  };

  return (
    <div className={`text-slate-800 ${className}`}>
      {renderFormattedText(text)}
      {diagramUrl && (
        <figure className="my-3 text-center">
          <img
            src={normalizeImageUrl(diagramUrl)}
            alt={diagramCaption || 'Diagram'}
            className="mx-auto max-h-56 rounded-md border border-slate-200 bg-white p-2 shadow-sm object-contain"
          />
          {diagramCaption && (
            <figcaption className="block text-xs text-slate-500 mt-1 italic">
              Figure: {diagramCaption}
            </figcaption>
          )}
        </figure>
      )}
    </div>
  );
}
