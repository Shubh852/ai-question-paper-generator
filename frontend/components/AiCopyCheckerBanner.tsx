'use client';

import React from 'react';
import {
  Sparkles,
  FileCheck2,
  Zap,
  ArrowRight,
  ShieldCheck,
  UploadCloud,
  CheckCircle2
} from 'lucide-react';

interface AiCopyCheckerBannerProps {
  onOpenModal: () => void;
  variant?: 'card' | 'compact' | 'hero';
  subject?: string;
  grade?: number;
}

export default function AiCopyCheckerBanner({
  onOpenModal,
  variant = 'card',
  subject,
  grade
}: AiCopyCheckerBannerProps) {
  if (variant === 'compact') {
    return (
      <div className="bg-gradient-to-r from-indigo-900 via-blue-900 to-purple-900 text-white rounded-2xl p-4 shadow-sm border border-indigo-700/50 flex flex-col sm:flex-row items-center justify-between gap-3">
        <div className="flex items-center space-x-3">
          <div className="h-9 w-9 rounded-xl bg-amber-400 text-amber-950 flex items-center justify-center font-black shrink-0 shadow-md">
            <Zap className="h-5 w-5 fill-current" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-black text-white">
                Auto-Check Student Copies with AI
              </span>
              <span className="bg-amber-400/20 text-amber-300 border border-amber-400/40 text-[10px] font-bold px-1.5 py-0.2 rounded-full">
                ₹500 / batch
              </span>
            </div>
            <p className="text-[11px] text-blue-200">
              Upload scanned PDF answer sheets • Automatic step-by-step CBSE rubric grading.
            </p>
          </div>
        </div>

        <button
          onClick={onOpenModal}
          className="shrink-0 px-4 py-2 rounded-xl bg-amber-400 hover:bg-amber-500 text-amber-950 font-black text-xs shadow-md transition-all flex items-center space-x-1.5"
        >
          <span>Try Copy Checker</span>
          <ArrowRight className="h-3.5 w-3.5" />
        </button>
      </div>
    );
  }

  return (
    <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-950 via-slate-900 to-blue-950 border border-indigo-500/30 p-5 sm:p-6 text-white shadow-xl">
      {/* Decorative background glow */}
      <div className="absolute -top-12 -right-12 w-48 h-48 bg-blue-500/20 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-12 -left-12 w-48 h-48 bg-purple-500/20 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
        {/* Left Side: Headline & Value Prop */}
        <div className="space-y-2 max-w-2xl">
          <div className="flex flex-wrap items-center gap-2">
            <span className="inline-flex items-center space-x-1 rounded-full bg-amber-400 text-amber-950 px-2.5 py-0.5 text-[10px] font-black uppercase tracking-wider shadow-xs">
              <Zap className="h-3 w-3 fill-current" />
              <span>New Feature Spotlight</span>
            </span>
            <span className="inline-flex items-center space-x-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 px-2.5 py-0.5 text-[10px] font-bold">
              <ShieldCheck className="h-3 w-3 text-blue-400" />
              <span>CBSE Step-Marking Compliant</span>
            </span>
          </div>

          <h3 className="text-lg sm:text-xl font-black text-white tracking-tight flex items-center gap-2">
            <span>Want AI to Grade Your Students&apos; Copies for this Paper?</span>
          </h3>

          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Done generating your test? Don&apos;t spend hours manually checking 40+ answer sheets. 
            Upload your student copies in PDF format — our AI checks every calculation and step against 
            the exact marking rubric of this paper, awarding step marks just like you do.
          </p>

          {/* Value Pills */}
          <div className="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-slate-300">
            <div className="flex items-center space-x-1 text-emerald-400">
              <CheckCircle2 className="h-3.5 w-3.5" />
              <span>Step-by-step marking rubrics</span>
            </div>
            <div className="flex items-center space-x-1 text-blue-400">
              <CheckCircle2 className="h-3.5 w-3.5" />
              <span>PDF red-pen annotations</span>
            </div>
            <div className="flex items-center space-x-1 text-purple-400">
              <CheckCircle2 className="h-3.5 w-3.5" />
              <span>Automated grade analytics</span>
            </div>
          </div>
        </div>

        {/* Right Side: Price Box & CTA */}
        <div className="w-full lg:w-auto shrink-0 flex flex-col sm:flex-row lg:flex-col items-center sm:items-stretch lg:items-center justify-between gap-3 bg-white/5 border border-white/10 rounded-2xl p-4 backdrop-blur-xs">
          <div className="text-center sm:text-left lg:text-center">
            <div className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">
              Introductory Price
            </div>
            <div className="flex items-baseline justify-center sm:justify-start lg:justify-center space-x-2">
              <span className="text-2xl font-black text-amber-400">₹500</span>
              <span className="text-xs text-slate-400 line-through">₹2,000</span>
              <span className="text-[10px] font-bold text-emerald-400">75% OFF</span>
            </div>
            <div className="text-[10px] text-slate-400">per batch (up to 40 copies)</div>
          </div>

          <button
            type="button"
            onClick={onOpenModal}
            className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 hover:from-amber-500 hover:to-orange-500 text-slate-950 font-black text-xs shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center space-x-2 group"
          >
            <span>Explore AI Copy Checker</span>
            <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
          </button>
        </div>
      </div>
    </div>
  );
}
